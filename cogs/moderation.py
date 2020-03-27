import discord
import random
import os
import datetime
from discord.ext import commands
from discord.ext.commands import Greedy
from discord import User


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

        await ctx.send(f'{amount} messages deleted')

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
            await ctx.send(f"**{ctx.author.name} has removed a role called: {role.name} from {user.name}**")

        else:
            await user.add_roles(role)
            await ctx.send(f"**Hey {ctx.author.name}, {user.name} has been given a role called: {role.name}**")

    @addrole.error
    async def addrole_error(self, ctx, error):

        if isinstance(error, commands.MissingRole):
            await ctx.send('**You aren\'t a staff member**')

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**You need to give user id or mention someone**')

        raise error

    @commands.command()
    async def testgroup(self, ctx, users: Greedy[User]):
        list = ''
        for user in users:
            list += f'{user.name}'

        await ctx.send(f'{list}')

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
        online = 0
        for i in ctx.guild.members:
            if str(i.status) == 'online' or str(i.status) == 'idle' or str(i.status) == 'dnd':
                online += 1

        embed = discord.Embed(title="{}'s info".format(ctx.guild.name),
                              description="Information on the server", color=0xcc0000)
        embed.add_field(name="Server Name", value=ctx.guild.name, inline=True)
        embed.add_field(name="Server ID", value=ctx.guild.id, inline=True)
        embed.add_field(name="Members", value=str(len(ctx.guild.members)))
        embed.add_field(name="Online Members", value=str(online))
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


def setup(client):
    client.add_cog(Moderation(client))