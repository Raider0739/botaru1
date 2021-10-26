import discord
from discord.ext import commands
import json
import asyncio
import time
import datetime
import random

class Marriage(commands.Cog):
    def __init__(self, client):
        self.client = client

        self.client.loop.create_task(self.save_users())

        with open(f"cogs/waifus/waifu.json", 'r') as f:
            self.marriage = json.load(f)

    async def save_users(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            with open(r"cogs/waifus/waifu.json", 'w') as f:
                json.dump(self.marriage, f, indent=4)

            await asyncio.sleep(3)

    def check(self, author):
        def inner_check(message):
            if message.author != author:
                return False
            try:
                int(message.content)
                return True
            except ValueError:
                return False
        return inner_check

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return

        author_id = str(message.author.id)

        if not author_id in self.marriage:
            self.marriage[author_id] = {}
            self.marriage[author_id]['main'] = 'Nobody'
            self.marriage[author_id]['side_chick'] = ''
            self.marriage[author_id]['name'] = message.author.name

        else:
            return

    @commands.command(aliases=['propose'])
    async def marry(self, ctx, member: discord.Member):
        author_id = str(ctx.author.id)
        member_id = str(member.id)
        if member == ctx.author:
            await ctx.send("**It's actually sad that you tried marrying yourself**")
        else:
            if self.marriage[author_id]['main'] == 'Nobody':
                await ctx.send(f"{ctx.author.name} wants to marry {member.name}, do you accept?")
                response = await self.client.wait_for('message', check=lambda message: message.author == member, timeout=60)

                if response.content == 'yes':
                    marry = self.marriage[member_id]['name']
                    marry1 = self.marriage[author_id]['name']
                    self.marriage[author_id]['main'] = ''
                    self.marriage[member_id]['main'] = ''
                    self.marriage[author_id]['main'] += marry
                    self.marriage[member_id]['main'] += marry1
                    embed = discord.Embed(
                        description=f"{member.name} accepted {ctx.author.name}'s proposal now they are married!",
                        colour=discord.Colour.blue())
                    await ctx.send(embed=embed)

                else:
                    embe = discord.Embed(description="You just got denied better luck next time",
                                         colour=discord.Colour.blue())
                    await ctx.send(embed=embe)


            else:
                await ctx.send('You are already married to someone!')

    @marry.error
    async def marry_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("**Time is up**")

        raise error

    @commands.command(aliases=['div'])
    async def divorce(self, ctx, member: discord.Member):
        author_id = str(ctx.author.id)
        member_id = str(member.id)
        if self.marriage[author_id]['main'] == 'Nobody':
            await ctx.send("You aren't even married yet!")
        else:
            if self.marriage[author_id]['main'] == self.marriage[member_id]['name']:

                self.marriage[author_id]['main'] = 'Nobody'
                self.marriage[member_id]['main'] = 'Nobody'

                embed = discord.Embed(description="Congrats you are single now i will spread the word for you!", colour=discord.Colour.blue())
                await ctx.send(embed=embed)

            else:
                await ctx.send("You aren't married to this person!")

    @commands.command(aliases=['sc'])
    async def sidechick(self, ctx, member: discord.Member):
        author_id = str(ctx.author.id)
        member_id = str(member.id)
        if member == ctx.author:
            await ctx.send("**You can't be your own hoe**")

        elif self.marriage[member_id]['name'] in self.marriage[author_id]['side_chick']:
            await ctx.send("**You already have this hoe as your sidechick**")

        elif self.marriage[member_id]['name'] in self.marriage[author_id]['main']:
            await ctx.send("**That's your main chick bro what are you thinking**")

        else:
            await ctx.send(f"{ctx.author.name} wants to make {member.name} a sidechick")
            msg = await self.client.wait_for('message', check=lambda message: message.author == member, timeout=60)
            if msg.content == 'yes':
                hoe = self.marriage[member_id]['name']
                self.marriage[author_id]['side_chick'].append(f"{hoe}\n")

                embed = discord.Embed(description=f"{member.name} agreed to be {ctx.author.name}'s sidechick!", colour=discord.Colour.blue())
                await ctx.send(embed=embed)

            else:
                await ctx.send("**Guess you got rejected good luck finding another hoe**")

    @sidechick.error
    async def sidechick_error(self, ctx, error):
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("**Time is up**")

    @commands.command(aliases=['resc'])
    async def residechick(self, ctx, member: discord.Member):
        author_id = str(ctx.author.id)
        member_id = str(member.id)
        if self.marriage[member_id]['name'] in self.marriage[author_id]['side_chick']:
            hoe = self.marriage[member_id]['name']
            self.marriage[author_id]['side_chick'].remove(hoe)

            embed = discord.Embed(description=f"{ctx.author.name} gets rid of {member.name}", colour=discord.Colour.blue())
            await ctx.send(embed=embed)

        else:
            await ctx.send("**That's not your hoe bro**")

    @commands.command()
    async def showsc(self, ctx):
        author_id = str(ctx.author.id)

        embed = discord.Embed(description=f"{self.marriage[author_id]['side_chick']} ", colour=discord.Colour.blue())
        embed.set_author(name="Your Side chicks", icon_url=self.client.user.avatar_url)

        await ctx.send(embed=embed)

    @commands.command()
    async def waifu(self, ctx):
        author_id = str(ctx.author.id)

        embed = discord.Embed(description=f"{self.marriage[author_id]['main']}", colour=discord.Colour.blue())
        embed.set_author(name="Your waifu", icon_url=self.client.user.avatar_url)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Marriage(client))