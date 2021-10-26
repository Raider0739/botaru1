import discord
import random
import os
import datetime
import asyncio
import time
from discord.ext import commands
from discord.ext.commands import Greedy
from discord import User

def getTime():
    currenttime = time.time()
    datetim = datetime.datetime.fromtimestamp(currenttime).strftime("%c")
    return datetim

class Moderation(commands.Cog):

    OK_SLOWMODE_ON = "Slowmode on :snail: ({} seconds)"
    OK_SLOWMODE_OFF = "Slowmode off"
    OK_SLOWMODE_CHANGED = "Slowmode set to :snail: ({} seconds)"
    ERROR_SLOWMODE_SECONDS = "Rate limit has to be between 0-120."

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['purge'])
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount: int):
        """
            Purge command deletes messages(Requires delete message permission)
                """
        channel = ctx.channel

        await channel.purge(limit=amount+1)

        msg = await ctx.send(f'{amount} messages deleted')

        await asyncio.sleep(10)
        await msg.delete()

    @clear.error
    async def clear_error(self, ctx, error):

        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Oops looks like you dont have the perm')
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to specify an amount')
        if isinstance(error, commands.BadArgument):
            await ctx.send('Please enter a number')

        raise error

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        """Bans the member you mention"""
        await member.ban(reason=reason)
        await ctx.send(f'{member.name} got banned from server')

    @ban.error
    async def ban_error(self, ctx, error):

        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Oops looks like you dont have the perm')
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to mention someone')

        raise error

    @commands.command(pass_context=True, aliases=['ar'])
    @commands.has_role('Verification Team')
    async def addrole(self, ctx, user: discord.Member, *, role: discord.Role):
            if role in user.roles:
                await user.remove_roles(role)
                emb = discord.Embed(description=f"**{ctx.author.name} has removed a role called: {role.name} from {user.name}**", colour=discord.Colour.blue())
                channel = self.client.get_channel(626876374497624089)
                embed = discord.Embed(colour=discord.Colour.blue(), timestamp=ctx.message.created_at)
                embed.set_author(name="Role removed", icon_url=user.avatar_url)
                embed.add_field(name="User Name", value=user.mention, inline=True)
                embed.add_field(name="Role Name", value=role.name, inline=True)
                embed.add_field(name="Removed by", value=ctx.author.mention, inline=False)
                await ctx.send(embed=emb)
                await channel.send(embed=embed)

            else:
                await user.add_roles(role)
                emb = discord.Embed(description=f"**Hey {ctx.author.name}, {user.name} has been given a role called: {role.name}**", colour=discord.Colour.blue())
                channel = self.client.get_channel(626876374497624089)
                embed = discord.Embed(colour=discord.Colour.blue(), timestamp=ctx.message.created_at)
                embed.set_author(name="Role added", icon_url=user.avatar_url)
                embed.add_field(name="User Name", value=user.mention, inline=True)
                embed.add_field(name="Role Name", value=role.name, inline=True)
                embed.add_field(name="Added by", value=ctx.author.mention, inline=False)
                await ctx.send(embed=emb)
                await channel.send(embed=embed)

    @addrole.error
    async def addrole_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send("**Make sure you got everything right**")

        if isinstance(error, commands.MissingRole):
            await ctx.send('**You aren\'t a staff member**')

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**You need to give user id or mention someone**')

        raise error

    @commands.command(aliases=['ra'])
    @commands.has_permissions(manage_roles=True)
    async def roleall(self, ctx, *, role: discord.Role):
        await ctx.send('**Be patient when i am working on adding roles to everyone**')

        for member in ctx.guild.members:

            await member.add_roles(role)
        await ctx.send('**Role given to everyone successfully**')

    @roleall.error
    async def roleall_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('**You don\'t have permission to do that!**')
        if isinstance(error, commands.BadArgument):
            await ctx.send('**Make sure you type it correctly!**')
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**You need to type in the role name**')

        raise error

    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    @commands.bot_has_permissions(manage_messages=True)
    @commands.command()
    async def slowmode(self, ctx, seconds: int):

        if seconds == 0:  # Turn Slow Mode off
            await ctx.channel.edit(slowmode_delay=seconds,
                                   reason="{} requested to turn off slowmode.".format(ctx.author))
            embed = discord.Embed(description=self.OK_SLOWMODE_OFF, colour=discord.Colour.blue())
            return await ctx.send(embed=embed)

        elif 0 < seconds <= 120 and ctx.channel.slowmode_delay == 0:  # Turn Slow Mode On
            await ctx.channel.edit(slowmode_delay=seconds,
                                   reason="{} requested slowmode with a timer of {}".format(ctx.author, seconds))
            embed = discord.Embed(description=self.OK_SLOWMODE_ON.format(seconds), colour=discord.Colour.blue())
            return await ctx.send(embed=embed)

        elif 0 < seconds <= 120 and ctx.channel.slowmode_delay > 0:  # Change value of Slow Mode timer
            await ctx.channel.edit(slowmode_delay=seconds,
                                   reason="{} requested slowmode timer be changed to {}".format(ctx.author, seconds))
            embed = discord.Embed(description=self.OK_SLOWMODE_CHANGED.format(seconds), colour=discord.Colour.blue())
            return await ctx.send(embed=embed)
        elif seconds < 0 or seconds > 120:
            raise commands.BadArgument(self.ERROR_SLOWMODE_SECONDS)

    @commands.command(pass_context=True)
    async def serverinfo(self, ctx):

        embed = discord.Embed(title="{}'s info".format(ctx.guild.name),
                              description="Information on the server", color=0xcc0000)
        embed.add_field(name="Server Name", value=ctx.guild.name, inline=True)
        embed.add_field(name="Server ID", value=ctx.guild.id, inline=True)
        embed.add_field(name="Members", value=str(ctx.guild.member_count))
        embed.add_field(name="Owner", value=ctx.guild.owner, inline=True)
        embed.add_field(name="Role Count", value=str(len(ctx.guild.roles)))
        embed.add_field(name="Region", value=ctx.guild.region, inline=True)
        servMade = ctx.guild.created_at
        servMade2 = servMade.strftime("%B %d, %Y %I:%M %p")
        embed.add_field(name="Created", value="{}".format(servMade2))

        embed.set_thumbnail(url=ctx.guild.icon_url)
        embed.set_footer(text="Requested by {}".format(ctx.author))
        await ctx.send(embed=embed)
        print("Server Info requested")

    @commands.command()
    @commands.is_owner()
    async def remind(self, ctx, *, args):
        getTime()
        msg = args.split(' ')
        reminder = ' '.join(map(str, msg[0:-1]))
        try:
            if 's' in msg[-1]:
                time = int(msg[-1].replace('s', ''))
                await ctx.send(f"Ok i will remind you in {str(msg[-1].replace('s', ''))} seconds to {reminder}")
                await asyncio.sleep(time)
                await ctx.author.send(
                    f"You asked me to remind you to {reminder} {str(time)} seconds from {str(getTime())}")

            if 'm' in msg[-1]:
                time = int(msg[-1].replace('m', '')) * 60
                await ctx.send(f"Ok i will remind you in {str(msg[-1].replace('m', ''))} minutes to {reminder}")
                await asyncio.sleep(time)
                await ctx.author.send(
                    f"You asked me to remind you to {reminder} {str(time // 60)} minutes from {str(getTime())}")

            if 'h' in msg[-1]:
                time = int(msg[-1].replace('h', '')) * 3600
                await ctx.send(f"Ok i will remind you in {str(args[-1].replace('h', ''))} hours to {reminder}")
                await asyncio.sleep(time)
                await ctx.author.send(
                    f"You asked me to remind you to {reminder} {str(time // 3600)} hours from {str(getTime())}")
        except:
            pass

def setup(client):
    client.add_cog(Moderation(client))