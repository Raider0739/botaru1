import discord
import random
import os
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure
from discord.ext.commands import Greedy
from discord import User
class Moderation(commands.Cog):

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
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        """Kicks the member you mention"""
        await member.kick(reason=reason)
        await ctx.send(f'{member.name} got kicked from server')

    @kick.error
    async def kick_error(self, ctx, error):

        if isinstance(error, commands.MissingPermissions):
            await ctx.send('Oops looks like you dont have the perm')
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to mention someone')

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

    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def roleall(self, ctx, role: discord.Role):
        await ctx.send('**Be patient when i am working on adding roles to everyone**')

        for member in ctx.guild.members:

            await member.add_roles(role)
        await ctx.send('**Role given to everyone successfully**')






def setup(client):
    client.add_cog(Moderation(client))

