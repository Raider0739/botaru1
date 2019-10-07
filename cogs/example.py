import discord
import time
import sys
import datetime
import asyncio
from discord.ext import commands


to_write_buffers = {}
write_buffer_to_file_interval = 60 #seconds



class Example(commands.Cog):

 def __init__(self, client):
    self.client = client

    """async def write_buffer_to_files(self):
        while True:
            for guild_id in to_write_buffers:
                file_path = f"{sys.path[0]}\\chatlogs\\{guild_id}.txt"
                with open(file_path, "a", encoding="utf8") as outfile:
                    outfile.write(to_write_buffers[guild_id])
                    to_write_buffers[guild_id] = ""
                    await asyncio.sleep(write_buffer_to_file_interval)  # seconds"""

    """@commands.Cog.listener()
    async def on_ready(self):
        change_status.start()
        print('Bot is online.')
        await write_buffer_to_files()

    @commands.Cog.listener()
    async def on_message(self, message):
        # log conversations in sex chat server to buffer dict (buffer will be written to file periodically)
        if message.guild.id == 517012845238681602 and not message.author.bot and message.channel.category_id != 624557743839117313:
           if message.guild.id not in to_write_buffers:
            to_write_buffers[message.guild.id] = f"On guild {message.guild.name} {message.guild.id}\n"
            to_write_buffers[message.guild.id] += f"On channel {message.channel.name} {message.channel.id}\n"
            to_write_buffers[message.guild.id] += f"At {datetime.datetime.now()}\n"
            to_write_buffers[message.guild.id] += f"MsgID {message.id}\n"
            to_write_buffers[message.guild.id] += f"By {message.author.id} {message.author.name}\n"
            to_write_buffers[message.guild.id] += f"{message.content}\n\n"
        else:
            to_write_buffers[message.guild.id] += f"On guild {message.guild.name} {message.guild.id}\n"
            to_write_buffers[message.guild.id] += f"On channel {message.channel.name} {message.channel.id}\n"
            to_write_buffers[message.guild.id] += f"At {datetime.datetime.now()}\n"
            to_write_buffers[message.guild.id] += f"MsgID {message.id}\n"
            to_write_buffers[message.guild.id] += f"By {message.author.id} {message.author.name}\n"
            to_write_buffers[message.guild.id] += f"{message.content}\n\n"

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
        # save deleted message to database for snipe command
        if before.author.bot:  # don't save messages from bots
            return

        # log conversations in sex chat server to buffer dict (buffer will be written to file periodically)
        if before.guild.id == 517012845238681602 and not before.author.bot:
            if before.guild.id not in to_write_buffers:
                to_write_buffers[before.guild.id] = f"On {before.guild.name} {before.guild.id}\n"
                to_write_buffers[before.guild.id] += f"At {datetime.datetime.now()}\n"
                to_write_buffers[before.guild.id] += f"MsgID {before.id}\n"
                to_write_buffers[before.guild.id] += f"By {before.author.id} {before.author.name}\n"
                to_write_buffers[before.guild.id] += f"Message edited:\n{before.content}\nto\n{after.content} \n\n"
            else:
                to_write_buffers[before.guild.id] += f"On {before.guild.name} {before.guild.id}\n"
                to_write_buffers[before.guild.id] += f"At {datetime.datetime.now()}\n"
                to_write_buffers[before.guild.id] += f"MsgID {before.id}\n"
                to_write_buffers[before.guild.id] += f"By {before.author.id} {before.author.name}\n"
                to_write_buffers[
                    before.guild.id] += f"Message edited from:\n{before.content}\nTo:\n{after.content} \n\n"
"""
@commands.command()
async def wow(self, ctx):
 await ctx.send('wow :flushed:')


def setup(client):
    client.add_cog(Example(client))