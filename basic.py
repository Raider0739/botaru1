import discord
import os
import asyncio
#import youtube_dl
from discord.utils import get
import shutil
import sys
import datetime
import sqlite3
import json
import traceback
import discord.utils
from discord.ext import commands, tasks
from itertools import cycle


def get_prefix(client, message):
    if not message.guild:
        return commands.when_mentioned_or('$')(client, message)

    with open('prefixes.json', 'r') as f:
        prefixes = json.load(f)

    if str(message.guild.id) not in prefixes:
        return commands.when_mentioned_or('$')(client, message)

    prefix = prefixes[str(message.guild.id)]
    return commands.when_mentioned_or(prefix)(client, message)


intents = discord.Intents.default()

intents.members = True
initial_extensions = ['cogs.actions', 'cogs.events', 'cogs.example', 'cogs.fun', 'cogs.moderation', 'cogs.nsfw', 'cogs.prefix']
client = commands.Bot(command_prefix=get_prefix)
status = cycle(['$help for commands', '$nsfw for nsfw commands', 'Still under Development'])
owner = client.is_owner(user='464802706930794496')
client.timer_manager = timers.TimerManager(client)

initial_extensions = ['cogs.character', 'cogs.help', 'cogs.marriage', 'cogs.levels', 'cogs.prefix', 'cogs.actions', 'cogs.events', 'cogs.fun', 'cogs.moderation', 'cogs.nsfw']
client = commands.Bot(command_prefix=get_prefix, case_insensitive=True, intents=intents)
status = cycle(['$help for commands', '$nsfw for nsfw commands', '$patreon to donate', '$invite to invite Botaru'])
owner = client.is_owner(user='464802706930794496')
client.remove_command('help')
queues = {}


@client.event
async def on_ready():
    change_status.start()
    print('Bot is online.')
    print('Owner : Raider')
    print('--------------')
    print(f"Currently in {str(len(client.guilds))} servers")


@client.event
async def on_member_join(member):
    if member.guild.id == 624151939504013322:
        role = discord.utils.get(member.guild.roles, name='.・。.・゜✭ Server ✭・゜・。.')
        role1 = discord.utils.get(member.guild.roles, name='.・。.・゜✭ Bio ✭・゜・。.')
        role2 = discord.utils.get(member.guild.roles, name='.・。.・゜✭ Traits ✭・゜・。.')
        role3 = discord.utils.get(member.guild.roles, name='.・。.・゜✭ Kinks ✭・゜・。.')
        await member.add_roles(role, role1, role2, role3)
    if member.guild.id == 693712195049226271:
        await client.get_channel(693712195049226274).send(f"Welcome {member.mention} to Cheeky 18+ please head to <#693714056720154656> accept them then get <#693714074852130857>, in order to start having fun! Enjoy your stay!")


@tasks.loop(seconds=30)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.command()
async def userinfo(ctx, member: discord.Member = None):
    """Shows the user info"""
    if not member:
        member = ctx.author

    roles = [role for role in member.roles]

    embed=discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

    embed.set_author(name=f'User Info - {member}')
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)

    embed.add_field(name= 'ID:', value=member.id)
    embed.add_field(name= 'Guild Name:', value=member.display_name)

    embed.add_field(name= 'Created at:', value=member.created_at.strftime('%a, %#d %B %Y %I:%M %p UTC'))
    embed.add_field(name= 'Joined at:', value=member.joined_at.strftime('%a, %#d %B %Y %I:%M %p UTC'))

    embed.add_field(name= f'Roles ({len(roles)}):', value=' '.join([role.mention for role in roles]))
    embed.add_field(name= 'Top role:', value=member.top_role.mention)

    embed.add_field(name= 'Bot?:', value=member.bot)

    await ctx.send(embed=embed)


@client.command(aliases=['av'])
async def avatar(ctx, *, member: discord.Member = None):
    """
    Shows a members avatar.
    """
    if not member:
        member = ctx.author


    embed= discord.Embed(description=member.name + 's avatar', colour=discord.Colour.blue(), timestamp=ctx.message.created_at)
    embed.set_image(url=member.avatar_url)
    embed.set_footer(text='ㅤㅤRequested by: ' + ctx.author.name, icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)
    #await ctx.send(f"The avatar of {member.name} is: {member.avatar_url_as(static_format='png')}")


@client.command()
@commands.is_owner()
async def servers(ctx):
    for guild in client.guilds:
        await ctx.send(guild.name)

@client.command()
@commands.is_owner()
async def reload(ctx, initial_extensions):
    """Bot Owner only command"""
    try:
        client.unload_extension(f'cogs.{initial_extensions}')
        client.load_extension(f'cogs.{initial_extensions}')
        embed = discord.Embed(description=f"**I reloaded {initial_extensions} daddy**", colour=discord.Colour.blue())
        embed.set_image(url='https://cdn.discordapp.com/attachments/798913238229188608/822550521273516042/tenor.gif')
        await ctx.send(embed=embed)
    except Exception as e:
        print(f'{initial_extensions} can not be loaded:')
        raise e


if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()

<<<<<<< HEAD
client.run('Token')
=======

client.run(os.environ['token'])
>>>>>>> ed4de21a87fd83201281390adb97ea4f098d7b65
