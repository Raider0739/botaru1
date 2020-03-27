import discord
import time
import asyncio
import datetime
from discord.ext import commands


class Events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        if message.author.id in [408785106942164992, 557580985646972928,
                                 270904126974590976, 213466096718708737,
                                 365975655608745985, 292953664492929025]:
            return
        msg = message.content
        channel = message.channel
        try:
            with open("message.txt", "a") as f:
                f.write(f"Time: {str(datetime.datetime.utcnow())}, Message Owner: {message.author}\n Message: {msg}\n"
                        f" Server Name: {message.guild.name}, Channel Name: {channel.name}\n")

            await asyncio.sleep(10)
        except Exception as e:
            print(e)
            await asyncio.sleep(10)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, commands.CommandNotFound):
            await ctx.send('**This is not a command!**')
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**You need to mention someone**')

        raise error


def setup(client):
    client.add_cog(Events(client))
