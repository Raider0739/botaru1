import discord
from discord.ext import commands

class Events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        msg = message.content
        print(f'{message.author} said {msg}')

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.send('You dont have the permission to do that!')
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('This is not a command!')

        raise error

def setup(client):
    client.add_cog(Events(client))