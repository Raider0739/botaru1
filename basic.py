import discord
import random
import os
import sys
import json
import traceback
import discord.utils
import logging
import time
import datetime
import asyncio
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


initial_extensions = ['cogs.prefix', 'cogs.actions', 'cogs.events', 'cogs.example', 'cogs.fun', 'cogs.moderation', 'cogs.nsfw']
client = commands.Bot(command_prefix=get_prefix)
status = cycle(['$help for commands', '$nsfw for nsfw commands', 'Still under Development'])
owner = client.is_owner(user='464802706930794496')
#to_write_buffers = {}
#write_buffer_to_file_interval = 60 #seconds

client.remove_command('help')


def determineGender(mention):
    """mention: one of: string, class discord.Mention"""
    gender = None
    if type(mention) == str:
        gender = None
    else:
        for role in mention.roles:
            if role.name.lower() in ["male", "trans m->f", "mtf", "m-f", "bi-curious male", "bi male", "gay male", "straight male", "straight guy", "pan & others male", "gay couple", "straight couple", "gentlemen", "guys", "guy", "gentleman", 'gentlemen']:
                gender = "male"
            elif role.name.lower() in ["female", "bi-curious girl", "straight girl", "bi girl", "straight woman", "bi woman", "woman" "lesbian", "pan & others female", "lesbian couple", "ladies", "lady"]:
                gender = "female"
            elif role.name.lower() in ["f-m","ftm", "trans f->m", "trans", "tran","transexual", "transsexual", "other", "others"+"otherg", "trap"]:
                gender = "trans"
    return gender

"""async def write_buffer_to_files():
    while True:
        for guild_id in to_write_buffers:
            file_path = f"{sys.path[0]}\\chatlogs\\{guild_id}.txt"
            with open(file_path, "a", encoding="utf8") as outfile:
                outfile.write(to_write_buffers[guild_id])
                to_write_buffers[guild_id] = ""
        await asyncio.sleep(write_buffer_to_file_interval) # seconds """


@client.event
async def on_ready():
        change_status.start()
        print('Bot is online.')
        print('Owner : Raider')
        print('--------------')
        #await write_buffer_to_files()


@client.event
async def on_member_join(member):
    if member.guild.id == 624151939504013322:
        role = discord.utils.get(member.guild.roles, name='.・。.・゜✭ Server ✭・゜・。.')
        role1 = discord.utils.get(member.guild.roles, name='.・。.・゜✭ Bio ✭・゜・。.')
        role2 = discord.utils.get(member.guild.roles, name='.・。.・゜✭ Traits ✭・゜・。.')
        role3 = discord.utils.get(member.guild.roles, name='.・。.・゜✭ Kinks ✭・゜・。.')
        await member.add_roles(role, role1, role2, role3)


@tasks.loop(seconds=30)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#this was a test command!!
""""@client.command()
async def testembed(ctx):
    embed = discord.Embed(title='Title', description='Description',colour=discord.Color.red(), url='https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif')
    embed.set_author(name=client.user.name, icon_url=client.user.avatar_url)
    embed.set_footer(text='Footer', icon_url=ctx.author.avatar_url)
    embed.set_image(url='https://media.giphy.com/media/26BRv0ThflsHCqDrG/giphy.gif')
    embed.set_thumbnail(url='https://pbs.twimg.com/profile_images/875749462957670400/T0lwiBK8.jpg')
    await ctx.send(embed=embed)"""

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
async def help(ctx, user: discord.User=None):
    if not user:
        user = ctx.author

    em = discord.Embed(colour=discord.Colour.blue())
    em.set_author(name='Help')
    em.add_field(name='avatar(av)', value='Shows a members avatar.', inline=False)
    em.add_field(name='userinfo', value='Shows the user info', inline=False)
    em.add_field(name='morning(gm)', value='Morning gifs', inline=False)
    em.add_field(name='goodnight(gn)', value='Goodnight gifs', inline=False)
    em.add_field(name='ping', value='Gives latency', inline=False)
    em.add_field(name='hug', value='Hugs the member you mention', inline=False)
    em.add_field(name='cuddle', value='Cuddles the member you mention', inline=False)
    em.add_field(name='kiss', value='Kisses the member you mention', inline=False)
    em.add_field(name='pat', value='Pats the member you mention', inline=False)
    em.add_field(name='smile', value='Smile gifs for happy moments', inline=False)
    em.add_field(name='kill', value='Kills the member you mention', inline=False)
    em.add_field(name='fistbump', value='Bumps fist with the member you mention', inline=False)
    em.add_field(name='bunny', value='Sends cute bunny gifs', inline=False)
    em.add_field(name='punch', value='Punches the member you mention', inline=False)
    emb = discord.Embed(colour=discord.Colour.blue())
    emb.set_author(name='Help 1')
    emb.add_field(name='gay', value='Calls the person you mention gay(only for fun purposes)', inline=False)
    emb.add_field(name='nap', value='Time to take a nap zzZ..', inline=False)
    emb.add_field(name='holdhand', value='Holds the hand of member you mention', inline=False)
    emb.add_field(name='spooky', value='Halloween special command', inline=False)
    emb.add_field(name='penis', value='Lets see how big are you', inline=False)
    emb.add_field(name='lewd', value='Calls people lewd', inline=False)
    emb.add_field(name='nom', value='NOMNOMNOM, basically its nomming', inline=False)
    emb.add_field(name='blowkiss', value='Blows a kiss to member you mention', inline=False)
    emb.add_field(name='slap', value='Slaps the member you mention', inline=False)
    emb.add_field(name='poke', value='Pokes the member you mention', inline=False)
    emb.add_field(name='fu', value='Says fuck you to member you mention', inline=False)
    emb.add_field(name='boop', value='Boops the member you mention', inline=False)
    emb.add_field(name='grouphug', value='Group hug command you can mention multiple members', inline=False)

    await user.send(embed=em)
    await user.send(embed=emb)
    await ctx.send('**Sending info in DMs...($nsfw for nsfw command list)**')


@client.command()
@commands.is_owner()
async def reload(ctx, initial_extensions):
    """Bot Owner only command"""
    try:
        client.unload_extension(f'cogs.{initial_extensions}')
        client.load_extension(f'cogs.{initial_extensions}')
        await ctx.send(f'{initial_extensions} reloaded')
    except Exception as e:
        print(f'{initial_extensions} can not be loaded:')
        raise e


"""for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')"""

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()


client.run('NDg5ODA4MDc0OTI5MDc4Mjcy.XZJKsg.jLjVHP6CRE1Gz7BIEsYhTiyqWEA')