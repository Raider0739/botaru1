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
from discord.ext import commands, tasks, timers
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
client.timer_manager = timers.TimerManager(client)

client.remove_command('help')
queues = {}

@client.event
async def on_ready():

        change_status.start()
        print('Bot is online.')
        print('Owner : Raider')
        print('--------------')


async def check_for_birthday(ctx):
    await client.wait_until_ready()
    now = datetime.datetime.now()
    curmonth = now.month
    curday = now.day

    while not client.is_closed():
        with open('birthday.json', 'r') as f:
            var = json.load(f)
            for member in var:
                if member['month'] == curmonth:
                    if member['day'] == curday:
                        try:
                            await client.get_user(member).send("Happy Birthday!")
                        except:
                            pass
                        success = False
                        index = 0
                        while not success:
                            try:
                                await ctx.guild.channels[index].send(f"Happy birtday to <@{member}>!")
                            except discord.Forbidden:
                                index += 1
                            except AttributeError:
                                index += 1
                            except IndexError:
                                pass
                            else:
                                success = True
        await asyncio.sleep(86400)


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
    em.set_author(name='Help 1')
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
    em.add_field(name='popcorn', value='Eating popcorn alone or with someone', inline=False)
    em.add_field(name='goodjob(gj)', value='Good job gifs', inline=False)
    emb = discord.Embed(colour=discord.Colour.blue())
    emb.set_author(name='Help 2')
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
    emb.add_field(name='feed', value='Feeds the member you mention', inline=False)
    emb.add_field(name='suplex', value='Suplex the member you mention', inline=False)
    emb.add_field(name='cat', value='Sends random cat pics', inline=False)
    await user.send(embed=em)
    await user.send(embed=emb)
    await ctx.send('**Sending info in DMs...($nsfw for nsfw command list)**')


@client.command()
async def setbirthday(ctx):
    member = ctx.message.author.id
    await ctx.send("What is your birthday? Please use MM/DD format.")

    def check(user):
        return user == ctx.message.author and user == ctx.message.channel
    msg = await client.wait_for('message', check=check)
    try:
        list = msg.split("/")
        if list[0] > 13 or list[0] < 1:
            await ctx.send("Invalid date.")
            await ctx.send("Aborting...")
            return
        else:
            pass

        if list[0] in (1, 3, 5, 7, 8, 10, 12):
            if list[1] > 31 or list[1] < 1:
                await ctx.send("Invalid date.")
                await ctx.send("Aborting...")
                return
            else:
                pass

        elif list[0] in (4, 6, 9, 11,):
            if list[1] > 30 or list[1] < 1:
                await ctx.send("Invalid date.")
                await ctx.send("Aborting...")
                return
            else:
                pass

        elif list[0] == 2:
            if list[1] > 29 or list[1] < 1:
                await ctx.send("Invalid date.")
                await ctx.send("Aborting...")
                return
            else:
                pass

        else:
            await ctx.send("Invalid date.")
            await ctx.send("Aborting...")
            return

    except:
        await ctx.send("Invalid date.")
        await ctx.send("Aborting...")
        return

    list = msg.split("/")
    month = list[0]
    day = list[1]

    with open(r'C:\Users\utku1utku\Desktop\Botaru Project\birthday.json', 'w') as f:
        var = json.load(f)
        var[member] = {'month': month, 'day': day}
        json.dump(var, f, indent=4)

@client.command()
async def remind(ctx, time, *, text):
    date = datetime.datetime(*map(int, time.split("/")))

    client.timer_manager.create_timer("reminder", date, args=(ctx.channel.id, ctx.author.id, text))

@client.event
async def on_reminder(channel_id, author_id, text):
    channel = client.get_channel(channel_id)

    await channel.send("Hey <@{0}>, remember to: {1}".format(author_id, text))



@client.command()
async def invite(ctx):
    await ctx.send('https://discordapp.com/api/oauth2/authorize?client_id=489808074929078272&permissions=8&scope=bot')


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


if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            client.load_extension(extension)
        except Exception as e:
            print(f'Failed to load extension {extension}.', file=sys.stderr)
            traceback.print_exc()


client.run('NDg5ODA4MDc0OTI5MDc4Mjcy.XdSLWQ.Fb9Gw3NBA2p5ovgwGs7FDHmd7uc')
