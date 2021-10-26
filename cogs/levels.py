import discord
from discord.ext import commands
import json
import asyncio
import time
import datetime
import random
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import io
import urllib.request


class Levels(commands.Cog):
    def __init__(self, client):
        self.client = client

        self.client.loop.create_task(self.save_users())

        with open(f"cogs/users.json", 'r') as f:
            self.users = json.load(f)

        with open(f"cogs/waifus/waifu.json", 'r') as af:
            self.marriage = json.load(af)

    async def save_users(self):
        await self.client.wait_until_ready()
        while not self.client.is_closed():
            with open(r"cogs/users.json", 'w') as f:
                json.dump(self.users, f, indent=4)

            await asyncio.sleep(5)


    def lvl_up(self, author_id):
        cur_xp = self.users[author_id]['exp']
        cur_lvl = self.users[author_id]['level']

        if cur_xp >= round(4 * (cur_lvl ** 3) / 5):
            self.users[author_id]['level'] += 1
            self.users[author_id]['exp'] = 1
            return True
        else:
            return False

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        if message.author.bot:
            return
        empty_array = []
        dm_channel = self.client.get_channel(485155567950626829)
        if not message.guild:
            if message.attachments != empty_array:
                files = message.attachments

                #await dm_channel.send(f"{message.content} by {message.author}")
                for file in files:
                    image = file.url
                embed = discord.Embed(description=f"{message.content}", colour=discord.Colour.blue())
                embed.set_footer(text=f"{message.author}")
                embed.set_image(url=image)
                await dm_channel.send(embed=embed)
            else:
                embed = discord.Embed(description=f"**{message.content}**", colour=discord.Colour.blue())
                embed.set_footer(text=f"{message.author}")
                await dm_channel.send(embed=embed)

        author_id = str(message.author.id)

        if not author_id in self.users:
            self.users[author_id] = {}
            self.users[author_id]['level'] = 1
            self.users[author_id]['exp'] = 0
            self.users[author_id]['last_message'] = 0
            self.users[author_id]['money'] = 0
            self.users[author_id]['reputation'] = 0
            self.users[author_id]['name'] = message.author.name
            self.users[author_id]['token'] = 0

        if time.time() - self.users[author_id]['last_message'] > 30:
            xp = random.randint(20, 50)
            self.users[author_id]['exp'] += xp
            self.users[author_id]['last_message'] = time.time()
        else:
            return

        if self.lvl_up(author_id):
            channel = self.client.get_channel(701199286074867763)
            embed = discord.Embed(description=f"{message.author.mention} is now level {self.users[author_id]['level']}" ,colour=discord.Colour.blue())
            await channel.send(embed=embed)
        
        


    @commands.command(aliases=['lb lvl', 'lb'])
    async def levels(self, ctx):
        high_score_list = sorted(self.users, key=lambda x: self.users[x].get('exp', 0), reverse=True)
        message = ''

        for number, user in enumerate(high_score_list):
            message += '{0}- {1} with {2}xp\n'.format(number + 1, self.users[user]['name'], self.users[user].get('exp', 0))
            if len(message) >= 500:
                break
            else:
                pass

        embed = discord.Embed(description=message, colour= discord.Colour.blue())
        embed.set_author(name="Leaderboard", icon_url=self.client.user.avatar_url)

        await ctx.send(embed=embed)

    """@commands.command(aliases=['bal'])
    async def balance(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        member_id = str(member.id)

        if not member_id in self.users:
            await ctx.send("**That's a broke hoe**")
        else:
            embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)
            emoji = self.client.get_emoji(702224468893761640)
            emo = self.client.get_emoji(702241850597179392)
            embed.set_author(name=f"Balance - {member}", icon_url=self.client.user.avatar_url)
            money = self.users[member_id]['money']
            token = self.users[member_id]['token']
            embed.add_field(name="Money", value=f"{money}{emoji}")
            embed.add_field(name='Token', value=f"{token}{emo}")

            await ctx.send(embed=embed)"""

    @commands.command(aliases=['level', 'lvl'])
    async def rank(self, ctx, user: discord.User = None):
        if user == None:
            user = ctx.author
        member_id = str(user.id)
        rank = Image.open("cogs/back1.jpg")
        asset = user.avatar_url_as(size=128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = pfp.resize((125, 125))
        circle_image = Image.new('L', (125, 125))
        circle_draw = ImageDraw.Draw(circle_image)
        circle_draw.ellipse((0, 0, 125, 125), fill=255)
        rank.paste(pfp, (26, 19), circle_image)

        font = ImageFont.truetype("cogs/OpenSans-Regular.ttf", 28)
        draw = ImageDraw.Draw(rank)
        text = f"{user.name}#{user.discriminator}"
        draw.text((200, 60), text, (137, 207, 240), font=font)
        font1 = ImageFont.truetype("cogs/OpenSans-Regular.ttf", 24)
        text1 = f"{self.users[member_id]['exp']}/ {round(4 * (self.users[member_id]['level'] ** 3) / 5)}xp"
        draw.text((400, 160), text1, (137, 207, 240), font=font1)
        text2 = f"Level {self.users[member_id]['level']}"
        draw.text((430, 110), text2, (137, 207, 240), font=font1)
        rectangle = Image.open("cogs/rankbar.png")
        percent = (self.users[member_id]['exp'] / round(4 * (self.users[member_id]['level'] ** 3) / 5))*100
        rectangle = rectangle.resize((round(rectangle.size[0] * percent / 100), rectangle.size[1]))
        rank.paste(rectangle, (47, 200))
        rank.save("rank.jpg")

        await ctx.send(file=discord.File("rank.jpg"))

    @commands.command(aliases=['w'])
    @commands.cooldown(1, 7200, commands.BucketType.user)
    async def work(self, ctx):
        author_id = str(ctx.author.id)

        money = random.randint(250, 750)
        self.users[author_id]['money'] += money
        emoji = self.client.get_emoji(702224468893761640)
        message = f"{ctx.author.name} earned {money}{emoji}!"
        embed = discord.Embed(description=message, colour=discord.Colour.blue())

        await ctx.send(embed=embed)

    @work.error
    async def work_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):

            msg = 'Try again in {:}'.format(str(datetime.timedelta(seconds=int(error.retry_after))))
            await ctx.send(msg)
        else:
            raise error


    @commands.command()
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def daily(self, ctx):
        author_id = str(ctx.author.id)
        daily = random.randint(500, 1000)
        self.users[author_id]['money'] += daily
        emoji = self.client.get_emoji(702227225205932153)
        message = f"{ctx.author.name} got {daily}{emoji} from daily claim!"

        embed = discord.Embed(description=message, colour=discord.Colour.blue())

        await ctx.send(embed=embed)

    @daily.error
    async def daily_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):

            msg = 'Try again in {:}'.format(str(datetime.timedelta(seconds=int(error.retry_after))))
            await ctx.send(msg)
        else:
            raise error

    @commands.command()
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def rep(self, ctx, member: discord.Member):
        author_id = str(member.id)

        if member == ctx.author:
            await ctx.send("**You can't rep yourself baka**")
            self.rep.reset_cooldown(ctx)
        else:

            self.users[author_id]['reputation'] += 1

            message = f"{ctx.author.name} gave 1 reputation to {member.display_name}"

            embed = discord.Embed(description=message, colour=discord.Colour.blue())
            await ctx.send(embed=embed)

    @rep.error
    async def rep_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):

            msg = 'Try again in {:}'.format(str(datetime.timedelta(seconds=int(error.retry_after))))
            await ctx.send(msg)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("**You have to mention someone baka!**")
            self.rep.reset_cooldown(ctx)
        if isinstance(error, commands.CommandInvokeError):
            await ctx.send("**This user isn't registered yet**")
            self.rep.reset_cooldown(ctx)
        else:
            raise error

    @commands.command()
    async def profile(self, ctx, member: discord.Member = None):
        member = ctx.author if not member else member
        author_id = str(member.id)
        if not author_id in self.users:
            await ctx.send("**Member doesn't have a Profile yet**")
        else:
            if self.marriage[author_id]['main'] == "Nobody":
                marry = "Nobody"
            else:
                marry = self.marriage[author_id]['main']
            if self.marriage[author_id]['side_chick'] == "":
                side = "You got no hoes yet"
            else:
                side = self.marriage[author_id]['side_chick']
            emoji = self.client.get_emoji(702224468893761640)
            emo = self.client.get_emoji(702241850597179392)
            embed = discord.Embed(color=member.color, timestamp=ctx.message.created_at)


            embed.set_author(name=f"Profile - {member.display_name}", icon_url=self.client.user.avatar_url)

            embed.add_field(name="Level", value=self.users[author_id]['level'], inline=True)
            embed.add_field(name="XP", value=self.users[author_id]['exp'], inline=True)
            embed.add_field(name="Reputation", value=self.users[author_id]['reputation'], inline=False)
            embed.add_field(name='Balance', value=f"{self.users[author_id]['money']} {emoji}", inline=True)
            embed.add_field(name="Tokens", value=f"{self.users[author_id]['token']} {emo}", inline=True)
            embed.add_field(name="Married to", value=marry, inline=False)
            embed.add_field(name="Sidechicks", value=side, inline=False)
            embed.set_thumbnail(url=member.avatar_url)
            await ctx.send(embed=embed)

    @commands.command(aliases=['r', 'ref'])
    async def refresh(self, ctx):
        author_id = str(ctx.author.id)
        self.users[author_id]['name'] = ctx.author.name

        await ctx.send("Refreshed your username successfully")

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def token(self, ctx):
        author_id = str(ctx.author.id)
        gain = random.randint(5, 50)
        self.users[author_id]['token'] += gain
        emoji = self.client.get_emoji(702227796013088795)

        msg = f"{ctx.author.name} just got {gain} panty token {emoji}"
        embed = discord.Embed(description=msg, colour=discord.Colour.blue())

        await ctx.send(embed=embed)

    @token.error
    async def token_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            msg = 'Try again in {:} seconds'.format(int(error.retry_after))
            await ctx.send(msg)
        else:
            raise error

    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def gamble(self, ctx, *, amount: int):
        author_id = str(ctx.author.id)
        if amount > self.users[author_id]['token']:
           await ctx.send('You dont have enough tokens')
        else:
            if self.users[author_id]['token'] == 0:
                await ctx.send("You need tokens to do this")
            else:
                gambler = random.randint(1, 6)
                if gambler == 1:
                    self.users[author_id]['token'] -= amount
                    gain = amount * 2
                    self.users[author_id]['money'] += gain
                    emoji = self.client.get_emoji(702227225205932153)
                    embed = discord.Embed(description=f"{ctx.author.name} won and earned {gain}{emoji} with gambling", colour=discord.Colour.blue())
                    await ctx.send(embed=embed)

                if gambler == 2:
                    self.users[author_id]['token'] -= amount
                    gain = 0
                    self.users[author_id]['money'] += gain
                    embed = discord.Embed(description=f"{ctx.author.name} lost everything, rip...", colour=discord.Colour.blue())
                    await ctx.send(embed=embed)

                if gambler == 3:
                    self.users[author_id]['token'] -= amount
                    gain = amount
                    self.users[author_id]['money'] += gain
                    emoji = self.client.get_emoji(702227225205932153)
                    embed = discord.Embed(description=f"{ctx.author.name} well you suck but i will be nice and convert your tokens {gain}{emoji} is what you get, loser...", colour=discord.Colour.blue())
                    await ctx.send(embed=embed)

                if gambler == 4:
                    self.users[author_id]['token'] -= amount
                    lose = amount * 2
                    gain = random.randint(0, lose)
                    self.users[author_id]['money'] -= gain
                    emoji = self.client.get_emoji(702227225205932153)
                    embed = discord.Embed(description=f"{ctx.author.name} damn bro you just lost {gain}{emoji}", colour=discord.Colour.blue())
                    await ctx.send(embed=embed)

                if gambler == 5:
                    self.users[author_id]['token'] -= amount
                    emoji = self.client.get_emoji(702227225205932153)
                    embed = discord.Embed(description=f"Woops my hands slipped and i forgot to put your bet on you lost {amount}{emoji}", colour=discord.Colour.blue())
                    await ctx.send(embed=embed)

                if gambler == 6:
                    self.users[author_id]['token'] -= amount
                    self.users[author_id]['money'] += 1
                    emoji = self.client.get_emoji(702227225205932153)
                    embed = discord.Embed(description=f"{ctx.author.name} just got 1{emoji}", colour=discord.Colour.blue())
                    await ctx.send(embed=embed)

    @gamble.error
    async def gamble_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            msg = "Try again in {:} second".format(int(error.retry_after))
            await ctx.send(msg)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You will need some panty tokens to gamble...")
            self.gamble.reset_cooldown(ctx)
        else:
            raise error

    @commands.command(aliases=['pb'])
    async def pantyboard(self, ctx):
        high_score_list = sorted(self.users, key=lambda x: self.users[x].get('money', 0), reverse=True)
        message = ''

        for number, user in enumerate(high_score_list):
            emoji = self.client.get_emoji(702224468893761640)
            message += '{0}- {1} with {2} {3}\n'.format(number + 1, self.users[user]['name'], self.users[user].get('money', 0), emoji)
            if len(message) >= 500:
                break
            else:
                pass
        embed = discord.Embed(description=message, colour=discord.Colour.blue())
        embed.set_author(name="Most Panties", icon_url=self.client.user.avatar_url)

        await ctx.send(embed=embed)

    @commands.command(aliases=['resetexp', 'resexp'])
    @commands.is_owner()
    async def reset_exp(self, ctx, member: discord.Member):
        member_id = str(member.id)
        self.users[member_id]['exp'] = 0
        self.users[member_id]['level'] = 1
        embed = discord.Embed(description=f"{member.mention} got exp reset", colour=discord.Colour.blue())

        await ctx.send(embed=embed)

    @reset_exp.error
    async def reset_exp_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send("You aren't my owner gtfo!")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You forgot to add something bro")

        raise error

    @commands.command()
    @commands.is_owner()
    async def addpanty(self, ctx, member: discord.Member, *, amount: int):
        member_id = str(member.id)

        self.users[member_id]['money'] += amount
        emoji = self.client.get_emoji(702224468893761640)
        embed = discord.Embed(description=f"{member.mention} got {amount}{emoji} added to balance", colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @addpanty.error
    async def add_panty_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send("You aren't my owner gtfo!")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You forgot to add something bro")

        raise error

    @commands.command(aliases=['removepanty'])
    @commands.is_owner()
    async def remove_panty(self, ctx, member: discord.Member, *, amount: int):
        member_id = str(member.id)

        self.users[member_id]['money'] -= amount
        emoji = self.client.get_emoji(702224468893761640)
        embed = discord.Embed(description=f"{member.mention} got {amount}{emoji} removed from balance",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @remove_panty.error
    async def _remove_panty_error(self, ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send("You aren't my owner gtfo!")
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You forgot to add something bro")

        raise error

    @commands.command(aliases=['cop'])
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def convertpanty(self, ctx, *, amount: int):
        author_id = str(ctx.author.id)
        if self.users[author_id]['money'] == 0:
            await ctx.send("Bitch you are broke!")
            self.convertpanty.reset_cooldown(ctx)
        else:
            if amount >= 250:
                emoji = self.client.get_emoji(702224468893761640)
                await ctx.send(f"You can't convert more than 250{emoji}")
                self.convertpanty.reset_cooldown(ctx)
            elif amount <= 249:
                emoji = self.client.get_emoji(702224468893761640)
                self.users[author_id]['money'] -= amount
                self.users[author_id]['token'] += amount
                embed = discord.Embed(description=f"{ctx.author.name} converted {amount}{emoji} to tokens", colour=discord.Colour.blue())
                await ctx.send(embed=embed)

    @convertpanty.error
    async def convertpanty_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            msg = "Try again in {:} second".format(int(error.retry_after))
            await ctx.send(msg)
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You forgot to add amount")
            self.convertpanty.reset_cooldown(ctx)

        raise error
    @commands.command()
    async def welcome(self, ctx, member: discord.Member=None):
       if ctx.guild.id == 693712195049226271:
            if member == None:
                await ctx.send(f"**Welcome Newbie to Cheeky 18+ please head to <#693714056720154656> accept them then get <#693714074852130857>, in order to start having fun! Enjoy your stay!**")
            else:
                await ctx.send(f"**Welcome {member.mention} to Cheeky 18+ please head to <#693714056720154656> accept them then get <#693714074852130857>, in order to start having fun! Enjoy your stay!**")
       else:
           await ctx.send("**This server doesnt have a welcome command assigned with Botaru please contact my owner if you wish to do so**")
def setup(client):
    client.add_cog(Levels(client))