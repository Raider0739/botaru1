import discord
import time
import json
import aiohttp
from discord.ext import commands
from discord.ext.commands import Greedy
from discord import User
from utils import http
import asyncio
import random
import asyncpraw

reddit = asyncpraw.Reddit(
                     client_id="HnSytsXOGAIQUQ",
                     client_secret="dOx5veQH6HuivOY-1Lrs731j1gryWg",
                     user_agent="botaru",
                     username="botarudev",
                     password="u1t2k3u4"
                     )
def determineGender(mention):
    """mention: one of: string, class discord.Mention"""
    gender = None
    if type(mention) == str:
        gender = None
    else:
        for role in mention.roles:
            if role.name.lower() in ["male", "trans m->f", "mtf", "m-f", "bi-curious male", "bi male", "gay male", "straight male", "straight guy", "pan & others male", "gay couple", "straight couple", "gentlemen", "guys", "guy", "gentleman", 'gentlemen',
                                     "pan + others male"]:
                gender = "male"
            elif role.name.lower() in ["female", "bi-curious girl", "straight girl", "bi girl", "straight woman",
                                       "straight female", "woman" "lesbian", "pan & others female", "lesbian couple",
                                       "ladies", "lady", "non-binary", "bi female", "alien", "intersex", "transgender",
                                       "pan + others female", "lesbian female", "bi - curious female", "bi woman", "genderqueer",
                                       "genderfluid", "gender-fluid"]:
                gender = "female"
            elif role.name.lower() in ["f-m","ftm", "trans f->m", "trans", "tran","transexual", "transsexual", "other", "others"+"otherg", "trap"]:
                gender = "trans"
    return gender

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    async def randomimageapi(self, ctx, url, endpoint):
            try:
                r = await http.get(url, res_method="json", no_cache=True)
            except json.JSONDecodeError:
                return await ctx.send("Couldn't find anything from the API")

            await ctx.send(r[endpoint])

    @commands.command()
    async def ping(self, ctx):
        """pseudo-ping time"""
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await ctx.trigger_typing()
        t2 = time.perf_counter()
        await ctx.send("Latency is: {}ms".format(round((t2 - t1) * 1000)))

    @commands.command()
    async def hug(self, ctx, member: discord.Member):
        """
           Hugs the member you mention
                    """
        author = ctx.message.author.name
        mention = member.name

        hug = '**{0} gave {1} a hug!**'

        choices = ['https://media1.tenor.com/images/b0de026a12e20137a654b5e2e65e2aed/tenor.gif?itemid=7552093',
                   'https://media1.tenor.com/images/49a21e182fcdfb3e96cc9d9421f8ee3f/tenor.gif?itemid=3532079',
                   'https://media3.giphy.com/media/od5H3PmEG5EVq/giphy.gif',
                   'http://37.media.tumblr.com/f2a878657add13aa09a5e089378ec43d/tumblr_n5uovjOi931tp7433o1_500.gif',
                   'http://25.media.tumblr.com/tumblr_ma7l17EWnk1rq65rlo1_500.gif',
                   'https://66.media.tumblr.com/291c8b98b219283f9e21927e7ef6c3f2/tumblr_mzscklfLYx1tptsy9o1_400.gif',
                   'http://25.media.tumblr.com/2a3ec53a742008eb61979af6b7148e8d/tumblr_mt1cllxlBr1s2tbc6o1_500.gif',
                   'https://media2.giphy.com/media/ddGxYkb7Fp2QRuTTGO/source.gif',
                   'https://i.pinimg.com/originals/ab/58/a8/ab58a8f3ad91fd62911f84bf3d54127c.gif',
                   'https://gifimage.net/wp-content/uploads/2017/09/anime-hugging-gif-6.gif',
                   'https://media1.tenor.com/images/ee95b90c9461219ff77136d6534d1f6b/tenor.gif?itemid=11050300',
                   'https://haningtonbrothers.com/image/195353-full_big-hug-gifs-get-the-best-gif-on-giphy.gif',
                   'https://media2.giphy.com/media/VGACXbkf0AeGs/giphy.gif']

        image = random.choice(choices)

        embed=discord.Embed(description=hug.format(author, mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await ctx.send(embed=embed)
    @hug.error
    async def hug_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to mention someone!')

        raise error

    @commands.command()
    async def cuddle(self, ctx, member:discord.Member=None):
        """
            Cuddles the member you mention
            """
        if ctx.invoked_subcommand is None:
            try:
                mentions = ctx.message.mentions[0]
            except:
                mentions = message
            author = ctx.author.name
            

            cuddle = '**{0} cuddles {1}! So cute~~ **'

            choices = ['https://media1.tenor.com/images/8f8ba3baeecdf28f3e0fa7d4ce1a8586/tenor.gif?itemid=12668750',
                    'https://media1.tenor.com/images/d16a9affe8915e6413b0c1f1d380b2ee/tenor.gif?itemid=12669052',
                    'https://thumbs.gfycat.com/DecisiveThankfulHermitcrab-small.gif',
                    'https://media.tenor.com/images/6c557a90736713c7183c1939cc8dd398/tenor.gif',
                    'https://media1.tenor.com/images/d0c2e7382742f1faf8fcb44db268615f/tenor.gif?itemid=5853736',
                    'https://media1.tenor.com/images/e07473d3cf372dbc24c760527740b85e/tenor.gif?itemid=12668884',
                    'https://i.pinimg.com/originals/21/45/25/214525ad2d99ee7de4de42b138ae9e2a.gif',
                    'https://gifimage.net/wp-content/uploads/2017/10/cuddle-anime-gif-13.gif',
                    'https://media1.tenor.com/images/13be52a4a4a26b0c9e479df6644d6de5/tenor.gif?itemid=12668752',
                    'https://cdn140.picsart.com/247171032013202.gif?r240x240',
                    'https://media1.giphy.com/media/LVXJQat47MwQU/giphy.gif',
                    'https://media.giphy.com/media/ohiWzVWGkAOCA/giphy.gif',
                    'https://media.tenor.com/images/2b821a1dc983cacc20d721cf2e5f2190/tenor.gif']

            image = random.choice(choices)

            embed = discord.Embed(description=cuddle.format(author, mentions.name), colour=discord.Colour.blue())
            embed.set_image(url=image)

            await ctx.send(embed=embed)


    @cuddle.error
    async def cuddle_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to mention someone!')

        raise error


    @commands.command()
    async def pat(self, ctx, member: discord.Member):
        """
            Pats the person you mention
        """
        author= ctx.message.author.name
        mention= member.name

        pat= '**{0} pats {1}~~**'

        choices= ['https://media.tenor.com/images/ad8357e58d35c1d63b570ab7e587f212/tenor.gif',
                  'https://media.tenor.com/images/1d37a873edfeb81a1f5403f4a3bfa185/tenor.gif',
                  'https://media.giphy.com/media/ARSp9T7wwxNcs/giphy.gif',
                  'https://66.media.tumblr.com/f94eb1143883554a0c7825f75d593756/tumblr_pjr04jWu3x1tm1dgio2_400.gif',
                  'https://media1.tenor.com/images/c0bcaeaa785a6bdf1fae82ecac65d0cc/tenor.gif?itemid=7453915',
                  'https://thumbs.gfycat.com/AgileHeavyGecko-max-1mb.gif',
                  'https://thumbs.gfycat.com/FlimsyDeafeningGrassspider-size_restricted.gif',
                  'https://66.media.tumblr.com/6289c42ea805f475698f02207da0a377/tumblr_p14hcsxPsb1tm1dgio1_400.gif',
                  'https://i.pinimg.com/originals/c0/c1/c5/c0c1c5d15f8ad65a9f0aaf6c91a3811e.gif',
                  'https://media1.tenor.com/images/68d981347bf6ee8c7d6b78f8a7fe3ccb/tenor.gif?itemid=5155410',
                  'https://media0.giphy.com/media/L2z7dnOduqEow/giphy.gif',
                  'https://i.pinimg.com/originals/c2/34/cd/c234cdcb3af7bed21ccbba2293470b8c.gif',
                  'https://media1.tenor.com/images/1e92c03121c0bd6688d17eef8d275ea7/tenor.gif?itemid=9920853',
                  'https://data.whicdn.com/images/295195659/original.gif',
                  'https://thumbs.gfycat.com/DecisiveVioletBass-small.gif',
                  'https://media0.giphy.com/media/ye7OTQgwmVuVy/giphy.gif',
                  'https://gifimage.net/wp-content/uploads/2017/09/anime-pat-gif-4.gif',
                  'http://store.donanimhaber.com/04/76/d4/0476d4b7110a577859db0d448f97ee0f.gif',
                  'https://i.redd.it/bsce3x89zi911.gif',
                  'https://media1.tenor.com/images/098a45951c569edc25ea744135f97ccf/tenor.gif?itemid=10895868',
                  'https://i.kym-cdn.com/photos/images/newsfeed/001/286/811/7c7.gif',
                  'https://data.whicdn.com/images/125164822/original.gif',
                  'https://data.whicdn.com/images/217039329/original.gif']

        image = random.choice(choices)

        embed = discord.Embed(description=pat.format(author,mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await ctx.send(embed=embed)
    @pat.error
    async def pat_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to mention someone!')

        raise error

    @commands.command()
    async def smile(self,ctx):
        """
        Sends a smile gif
        """

        author = ctx.message.author.name

        smile = '**{0} smiles happily!**'

        choices=['http://giphygifs.s3.amazonaws.com/media/ree8xCap5nHi/giphy.gif',
                 'http://giphygifs.s3.amazonaws.com/media/bqSkJ4IwNcoZG/giphy.gif',
                 'https://media.giphy.com/media/ellxlkgbPTiM0/giphy.gif',
                 'https://media.tenor.com/images/5303cc9edb959b0bebd188e5d326ee20/tenor.gif',
                 'https://media0.giphy.com/media/w9j3Zf0yVNIJy/source.gif',
                 'https://i.pinimg.com/originals/63/ca/58/63ca58fb23c0901176abf1787fa3bfce.gif',
                 'https://media.tenor.com/images/769fede93ec2f2293dadca1e0449eb50/tenor.gif',
                 'https://i.pinimg.com/originals/b3/d5/16/b3d516636dcb886d3606a0ad88f86ffd.gif']

        image = random.choice(choices)

        embed = discord.Embed(description=smile.format(author), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await ctx.send(embed=embed)

    @commands.command()
    async def gay(self, ctx, member: discord.Member):
        """
        Calls the person you mention gay(only fun purposes)
        """

        author = ctx.message.author.name
        mention = member.name

        gay = '**{0} says that {1} got the big gay!**'

        choices= ['http://giphygifs.s3.amazonaws.com/media/8fxad4tvqIzwk/giphy.gif',
                  'https://thumbs.gfycat.com/ForthrightPopularAustralianfreshwatercrocodile-size_restricted.gif',
                  'https://thumbs.gfycat.com/AliveBitesizedHylaeosaurus-size_restricted.gif',
                  'https://media1.tenor.com/images/331401baf3b9a004b3956af6ce7eca22/tenor.gif?itemid=9808231',
                  'http://1.bp.blogspot.com/-xHCd4Igtal8/UZR_Qp2g8TI/AAAAAAAAAN8/ts8IKbvICc0/s640/Gay.gif',
                  'https://media.tenor.com/images/34013a2f15f4d310c5694c730bc6a669/tenor.gif',
                  'https://media.giphy.com/media/gNHbqod07bC4o/giphy.gif']

        image = random.choice(choices)

        embed = discord.Embed(description=gay.format(author,mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await ctx.send(embed=embed)
    @gay.error
    async def gay_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to mention someone!')

        raise error

    @commands.command()
    async def nap(self, ctx):
        """
        Nap command mention someone to use
        """
        author = ctx.message.author.name

        nap = '{0} takes a nap!'

        choices = ['https://s0.gifyu.com/images/giphy-1640d61907817d4017.gif',
                   'https://s0.gifyu.com/images/giphy-8b763df74503b9c00.gif',
                   'https://s0.gifyu.com/images/sourcee02abceabde776af.gif',
                   'https://s0.gifyu.com/images/original198a05be130f7114.gif',
                   'https://s0.gifyu.com/images/ijuhygvhc8f8f2ecbf9157b0.gif',
                   'https://s0.gifyu.com/images/giphy-1556a84497edbb11f9.gif',
                   'https://s0.gifyu.com/images/giphy-105123fa6d374666e8.gif',
                   'https://s0.gifyu.com/images/giphy21f052aa0830d8b6.gif',
                   'https://s0.gifyu.com/images/giphy-2db8f775ca2c2ad9e.gif',
                   'https://s0.gifyu.com/images/giphy-14a42b45b8bb13b6d9.gif',
                   'https://s0.gifyu.com/images/giphy-13b2f1ca21100c5e18.gif',
                   'https://s0.gifyu.com/images/giphy-112bf409ba9b76f655.md.gif',
                   'https://s0.gifyu.com/images/giphy-123a4efd156fb3cbcd.gif',
                   'https://s0.gifyu.com/images/giphy-6d89ff78f1626549c.gif',
                   'https://s0.gifyu.com/images/giphy-972d8cab2f950ae0b.gif',
                   'https://s0.gifyu.com/images/giphy-77ab07e3a275bcfb7.gif',
                   'https://s0.gifyu.com/images/downloada378fa01d0e833ea.gif',
                   'https://s0.gifyu.com/images/giphy-3987743e3d91490d3.gif',
                   'https://s0.gifyu.com/images/giphy-46caa04523e269068.gif',
                   'https://s0.gifyu.com/images/giphy-517adfc723fb26926.gif',
                   'https://s0.gifyu.com/images/_3fYL8i6Q-n-155t3dn_4oa8joxN4d65hmFMp22bNTIUW3ufQExKZv-GKL4AdqgU8dfee158fa7560a6.gif']
        image = random.choice(choices)

        embed = discord.Embed(description=nap.format(author), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await ctx.send(embed=embed)

    @commands.command()
    async def holdhand(self, ctx, member: discord.Member):
        """
        Holds the hand of the person you mention
        """

        author = ctx.message.author.name
        mention = member.name

        holdhand = '**{0} holds hands of {1} >.<**'

        choices = ['https://media1.giphy.com/media/8InZ7jthZUVCU/giphy.gif?cid=790b7611f86f40597db7e029401fd45d9079fcab1c448a19&rid=giphy.gif',
                   'https://media2.giphy.com/media/1P4gWVC7n4BRC/giphy.gif?cid=790b7611cca290ad1040f8e7f3db7ef22e8a86ab34743794&rid=giphy.gif',
                   'https://media0.giphy.com/media/NAUtEs7cbhRAc/giphy.gif?cid=790b7611a160fb80bd1cd8b76779f9f2d7e00a257bf33f5f&rid=giphy.gif',
                   'https://media1.giphy.com/media/11DxcyjrKPAuVG/giphy.gif?cid=790b76119c51ed7af7acb0adbd384c49cdbbb8798af32585&rid=giphy.gif',
                   'https://66.media.tumblr.com/2089f3da5e98836d8333c2c961591b8d/tumblr_oukurrIWDD1re8kj6o1_500.gifv',
                   'https://66.media.tumblr.com/074b75c0bb8398f489adeaf99631d615/tumblr_pizbenW4rW1vikcwho1_400.gifv',
                   'https://66.media.tumblr.com/eb7cd825cd1a21d6ebaa6b9a20f83096/tumblr_orst3izDMh1u7esouo1_500.gifv',
                   'https://66.media.tumblr.com/8edd76058bd0fe049c11405286a4131a/tumblr_ozc5imGu1s1sy5k7wo1_500.gif',
                   'https://66.media.tumblr.com/3e59c2d808b15afa3d8bd48662e02412/tumblr_owjyw655O71vtjg2eo1_500.gif',
                   'https://66.media.tumblr.com/fa6a056c1e24ef0db0a146b52959efd4/tumblr_otvi8iLTvs1rmawi3o1_500.gif',
                   'https://66.media.tumblr.com/555d05a26273a5447db752fb736e17ec/tumblr_p13w27ZrEl1w22g9to1_500.gif',
                   'https://66.media.tumblr.com/17079aa75c95564ee56c38b010d967aa/tumblr_p4qivjppT11wayez7o1_500.gif',
                   'https://66.media.tumblr.com/2b29c66fba1630b73629d0d1cb28044f/tumblr_o0a467iac81u7esouo1_500.gif',
                   'https://66.media.tumblr.com/929a93a2237f518b1d872e3f0d8f3cec/tumblr_pxesib759D1ytpntyo1_540.gif',
                   'https://media1.tenor.com/images/6001ce02c96c53f319486b279a0eee94/tenor.gif?itemid=5298896',
                   'https://media.tenor.com/images/0351b76e63a1b7d799936481f734477c/tenor.gif.',
                   'https://media.tenor.com/images/87aa9335fc36112d5c5d29241b146126/tenor.gif',
                   'https://media.tenor.com/images/fb1f35ea5f583474b3502cf5cd035aa9/tenor.gif',
                   'https://media.tenor.com/images/ac2f7085820a706077d80e093b98615d/tenor.gif',
                   'https://media.giphy.com/media/11HyAcbfWAOH2E/giphy.gif',
                   'https://media.giphy.com/media/l3q2vScRNubmJGSUo/giphy.gif',
                   'https://media.giphy.com/media/82ijKtxghtq8MrWRv6/giphy.gif',
                   'https://media.giphy.com/media/KGw8FDgFPZhZAxYkZI/giphy.gif']

        image = random.choice(choices)

        embed = discord.Embed(description=holdhand.format(author, mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await ctx.send(embed=embed)
    @holdhand.error
    async def holdhand_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to mention someone!')

        raise error

    @commands.command(aliases=['scare'])
    async def spooky(self, ctx, member: discord.Member = None):
        """Halloween special command"""
        if not member:
            member = ctx.author
            if member == ctx.author:
                author = ctx.message.author.name

                spooky = '{0} spooks everyone :scream:'

                choices = ['http://media.tumblr.com/tumblr_ma0378yigX1qbhmtm.gif',
                           'https://cdn.discordapp.com/attachments/624659074943942656/628562387137593365/scary-halloween-gifs-19gif.gif',
                           'https://cdn.discordapp.com/attachments/628563534451834900/628565257035710464/242364-full_i-cannot-wait-for-halloween-gif-on-imgur.gif',
                           'https://cdn.discordapp.com/attachments/628563534451834900/628565276459270171/evildead.gif',
                           'https://cdn.discordapp.com/attachments/628563534451834900/628565860142809108/spooky.gif',
                           'https://cdn.discordapp.com/attachments/628563534451834900/628566043899461632/giphy.gif',
                           'https://media.giphy.com/media/Kg8e4SqpQ8zT4vrdol/giphy.gif',
                           'https://media.giphy.com/media/SwUdyMD24R8sY1FFDQ/giphy.gif',
                           'https://media.giphy.com/media/LnKekagItmp1C3UE04/giphy.gif',
                           'https://media.giphy.com/media/VbWJsjMlhlx0e3gmeH/giphy.gif',
                           'https://media.giphy.com/media/U5OxQaY3x6QRXSHp5Z/giphy.gif',
                           'https://media.giphy.com/media/W5aHlOsx5qr2OiDGvh/giphy.gif',
                           'https://media.giphy.com/media/IcvVgaqjxVa4es8t94/giphy.gif',
                           'https://media.giphy.com/media/j6lDH1oFBZU5gtyTh2/giphy.gif',
                           'https://media.giphy.com/media/WO6b30i6ZYfFv29Dau/giphy.gif',
                           'https://media.giphy.com/media/VgTqS0ZyOn3xHixIeK/giphy.gif',
                           'https://media.giphy.com/media/m9jzNfxCG15ighOCLC/giphy.gif',
                           'https://media.giphy.com/media/kHOeNP7avOoh1kdMWw/giphy.gif',
                           'https://media.giphy.com/media/Kecf5UZS70OBFSvB5I/giphy.gif',
                           'https://media.giphy.com/media/h8rjDIZadAUl8wFSLX/giphy.gif',
                           'https://media.giphy.com/media/LqV361fpJInnQj6Erv/giphy.gif',
                           'https://media.giphy.com/media/Std7DDAvwoYYMw03cY/giphy.gif',
                           'https://media.giphy.com/media/mCmCKqvoQ1Te29t2Vk/giphy.gif',
                           'https://media.giphy.com/media/H5BbdYyk1r0uafHuSA/giphy.gif',
                           'https://media.giphy.com/media/UttnVhTBQie5dTpMKJ/giphy.gif',
                           'https://media.giphy.com/media/XyOI8BsRDOUYPLO8ff/giphy.gif',
                           'https://media.giphy.com/media/XfasHOmQK9X8JdFPTk/giphy.gif',
                           'https://media.giphy.com/media/RGdlQI7wFDfATTN8Xu/giphy.gif',
                           'https://media.giphy.com/media/ghCZwLemzqkAqZ3UmF/giphy.gif',
                           'https://media.giphy.com/media/joZgGbZff1bjiXwwkV/giphy.gif',
                           'https://media.giphy.com/media/ThplIyPkehu6PRpLnR/giphy.gif',
                           'https://media.giphy.com/media/QuDFRDkF8IBL4Vcxdt/giphy.gif',
                           'https://media.giphy.com/media/SXqxRKozHp3jfh3qvG/giphy.gif',
                           'https://media.giphy.com/media/VhFKCvjLxgC1roNg9L/giphy.gif',
                           'https://media.giphy.com/media/LpKq28EjXVs5Fyr47W/giphy.gif',
                           'https://media.giphy.com/media/KcQ4YmuLKFjmpTNOGF/giphy.gif',
                           'https://media.giphy.com/media/U6ehLQyt3tkxMo3ZHF/giphy.gif',
                           'https://media.giphy.com/media/PjIdIfKnTKmgtsTCTY/giphy.gif',
                           'https://media.giphy.com/media/Wpg3XlIo6NpgMHAEy1/giphy.gif',
                           'https://media.giphy.com/media/j6TPdXWWn5jfEV0bIp/giphy.gif',
                           'https://media.giphy.com/media/Ti6tBrptSkkHkVUpyI/giphy.gif',
                           'https://media.giphy.com/media/hS49Tl580HZHrw4rlc/giphy.gif',
                           'https://cdn.discordapp.com/attachments/628563534451834900/629343692695797770/lightsout.gif',
                           'https://cdn.discordapp.com/attachments/628563534451834900/629343766540714006/anigif_sub-buzz-2656-1521228491-3.gif',
                           'https://cdn.discordapp.com/attachments/628563534451834900/629343796810874881/mbbSa1d.gif',
                           'https://cdn.discordapp.com/attachments/628563534451834900/629343666451775498/tenor_1.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=spooky.format(author), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif member:
                author = ctx.message.author.name
                mention = member.name

                spooky = '**{0} spooks {1}**'

                choices = ['http://media.tumblr.com/tumblr_ma0378yigX1qbhmtm.gif',
                           'https://cdn.discordapp.com/attachments/624659074943942656/628562387137593365/scary-halloween-gifs-19gif.gif',
                           'https://cdn.discordapp.com/attachments/628563534451834900/628565257035710464/242364-full_i-cannot-wait-for-halloween-gif-on-imgur.gif',
                           'https://cdn.discordapp.com/attachments/628563534451834900/628565276459270171/evildead.gif',
                           'https://cdn.discordapp.com/attachments/628563534451834900/628565860142809108/spooky.gif',
                           'https://cdn.discordapp.com/attachments/628563534451834900/628566043899461632/giphy.gif',
                           'https://media.giphy.com/media/Kg8e4SqpQ8zT4vrdol/giphy.gif',
                           'https://media.giphy.com/media/SwUdyMD24R8sY1FFDQ/giphy.gif',
                           'https://media.giphy.com/media/LnKekagItmp1C3UE04/giphy.gif',
                           'https://media.giphy.com/media/VbWJsjMlhlx0e3gmeH/giphy.gif',
                           'https://media.giphy.com/media/U5OxQaY3x6QRXSHp5Z/giphy.gif',
                           'https://media.giphy.com/media/W5aHlOsx5qr2OiDGvh/giphy.gif',
                           'https://media.giphy.com/media/IcvVgaqjxVa4es8t94/giphy.gif',
                           'https://media.giphy.com/media/j6lDH1oFBZU5gtyTh2/giphy.gif',
                           'https://media.giphy.com/media/WO6b30i6ZYfFv29Dau/giphy.gif',
                           'https://media.giphy.com/media/VgTqS0ZyOn3xHixIeK/giphy.gif',
                           'https://media.giphy.com/media/m9jzNfxCG15ighOCLC/giphy.gif',
                           'https://media.giphy.com/media/kHOeNP7avOoh1kdMWw/giphy.gif',
                           'https://media.giphy.com/media/Kecf5UZS70OBFSvB5I/giphy.gif',
                           'https://media.giphy.com/media/h8rjDIZadAUl8wFSLX/giphy.gif',
                           'https://media.giphy.com/media/LqV361fpJInnQj6Erv/giphy.gif',
                           'https://media.giphy.com/media/Std7DDAvwoYYMw03cY/giphy.gif',
                           'https://media.giphy.com/media/mCmCKqvoQ1Te29t2Vk/giphy.gif',
                           'https://media.giphy.com/media/H5BbdYyk1r0uafHuSA/giphy.gif',
                           'https://media.giphy.com/media/UttnVhTBQie5dTpMKJ/giphy.gif',
                           'https://media.giphy.com/media/XyOI8BsRDOUYPLO8ff/giphy.gif',
                           'https://media.giphy.com/media/XfasHOmQK9X8JdFPTk/giphy.gif',
                           'https://media.giphy.com/media/RGdlQI7wFDfATTN8Xu/giphy.gif',
                           'https://media.giphy.com/media/ghCZwLemzqkAqZ3UmF/giphy.gif',
                           'https://media.giphy.com/media/joZgGbZff1bjiXwwkV/giphy.gif',
                           'https://media.giphy.com/media/ThplIyPkehu6PRpLnR/giphy.gif',
                           'https://media.giphy.com/media/QuDFRDkF8IBL4Vcxdt/giphy.gif',
                           'https://media.giphy.com/media/SXqxRKozHp3jfh3qvG/giphy.gif',
                           'https://media.giphy.com/media/VhFKCvjLxgC1roNg9L/giphy.gif',
                           'https://media.giphy.com/media/LpKq28EjXVs5Fyr47W/giphy.gif',
                           'https://media.giphy.com/media/KcQ4YmuLKFjmpTNOGF/giphy.gif',
                           'https://media.giphy.com/media/U6ehLQyt3tkxMo3ZHF/giphy.gif',
                           'https://media.giphy.com/media/PjIdIfKnTKmgtsTCTY/giphy.gif',
                           'https://media.giphy.com/media/Wpg3XlIo6NpgMHAEy1/giphy.gif',
                           'https://media.giphy.com/media/j6TPdXWWn5jfEV0bIp/giphy.gif',
                           'https://media.giphy.com/media/Ti6tBrptSkkHkVUpyI/giphy.gif',
                           'https://media.giphy.com/media/hS49Tl580HZHrw4rlc/giphy.gif',
                           'https://cdn.discordapp.com/attachments/628563534451834900/629343692695797770/lightsout.gif',
                           'https://cdn.discordapp.com/attachments/628563534451834900/629343766540714006/anigif_sub-buzz-2656-1521228491-3.gif',
                           'https://cdn.discordapp.com/attachments/628563534451834900/629343796810874881/mbbSa1d.gif',
                           'https://cdn.discordapp.com/attachments/628563534451834900/629343666451775498/tenor_1.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=spooky.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)


    @commands.command(hidden=True)
    async def tea(self, ctx):
        if ctx.message.author.id in [453429259789402112]:

            embed = discord.Embed(description='It\'s tea time', colour=discord.Colour.blue())
            embed.set_image(url='https://media3.giphy.com/media/3o85xGocUH8RYoDKKs/giphy.gif?cid=790b76116dadddf067c6202eabb573b4761c26942dc8391f&rid=giphy.gif')

            await ctx.send(embed=embed)

        else:

            embed = discord.Embed(description='You\'re not mia gtfo!', colour=discord.Colour.blue())
            embed.set_image(url='https://media1.tenor.com/images/d004741ef8203dba11dd77991f997357/tenor.gif?itemid=5100592')

            await ctx.send(embed=embed)

    @commands.command()
    async def penis(self, ctx, member: discord.Member = None):
        """How big are you?"""
        if not member:
            member = ctx.author
            if member == ctx.author:
                embed = discord.Embed(description=member.name + '\'s Size: 8{}D'.format(random.randint(1, 20) * '='),
                                      colour=discord.Colour.blue())
                await ctx.send(embed=embed)

        elif member:
            embed = discord.Embed(description=member.name + '\'s Size: 8{}D'.format(random.randint(1, 20) * '='),
                                  colour=discord.Colour.blue())
            await ctx.send(embed=embed)

    @commands.command(hidden=True)
    async def kronos(self, ctx):
        if ctx.message.author.id in [343596224542146560]:

            embed = discord.Embed(description='Vivvy says Kronos is her property!', colour=discord.Colour.blue())
            embed.set_image(url='https://media3.giphy.com/media/l0K4c5WBW2DRzvQsg/giphy.gif?cid=790b7611ab35edccb5b4e6c51d2ad6a3a0ab3882ade714d4&rid=giphy.gif')

            await ctx.send(embed=embed)
        else:
            await ctx.send('You arent vivvy!!')

    @commands.command()
    async def lewd(self, ctx):
        """You lewdiess >.<"""
        author = ctx.message.author.name

        lewd = '**{0} says this is so lewd >.<**'

        choices = ['https://media1.tenor.com/images/bc2810fc980244dfe6b3f0993eb70486/tenor.gif?itemid=13984951',
                   'https://i.kym-cdn.com/photos/images/newsfeed/001/030/317/a0f.gif',
                   'https://i.kym-cdn.com/photos/images/newsfeed/000/794/434/6e7.gif',
                   'https://vignette.wikia.nocookie.net/joke-battles/images/a/ac/Lewd_Gif.gif/revision/latest?cb=20190205032704',
                   'https://cdn.4archive.org/img/PtZJmjO.gif',
                   'https://i.kym-cdn.com/photos/images/newsfeed/000/957/307/ee1.gif',
                   'https://ci.memecdn.com/2590357.gif',
                   'https://thumbs.gfycat.com/VillainousGlaringGazelle-size_restricted.gif',
                   'https://i.kym-cdn.com/photos/images/original/000/949/652/7fe.gif',
                   'https://media.tenor.com/images/f45f5c5fd72dd7c9ff50976e2bc7133c/tenor.gif',
                   'https://i.pinimg.com/originals/83/8b/b2/838bb2bb4cb288410fd5578e30cd851c.gif']
        image = random.choice(choices)

        embed = discord.Embed(description=lewd.format(author), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await ctx.send(embed=embed)

    @commands.command()
    async def nom(self, ctx, member: discord.Member=None):
        """NOMNOMNOMNOM"""
        if not member:
            member = ctx.author
            if member == ctx.author:
                author = ctx.message.author.name

                nom = '**{0} noms happily!**'

                choices = ['https://i.imgur.com/FxKrt2G.gif',
                            'https://i.imgur.com/iemsupP.gif',
                            'https://i.imgur.com/EKB2m.gif',
                            'https://i.imgur.com/Pa4Hlkq.gif',
                            'https://i.imgur.com/BZ2C2uI.gif',
                            'https://i.imgur.com/BleS1K0.gif',
                            'https://i.imgur.com/5uZyuhy.gif',
                            'https://i.imgur.com/b6eyg1x.gif',
                            'https://i.imgur.com/WqUk4yS.gif?1',
                            'https://i.imgur.com/ONu9WZ1.gif',
                            'https://i.imgur.com/4xcZHuJ.gif',
                           'https://tenor.com/view/cats-ear-bite-gif-10614631']
                image = random.choice(choices)

                embed = discord.Embed(description=nom.format(author), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif member:
            author = ctx.message.author.name
            mention = member.name
            nom = '**{0} noms on {1}**'

            choices = ['https://i.imgur.com/FxKrt2G.gif',
                       'https://i.imgur.com/iemsupP.gif',
                       'https://i.imgur.com/EKB2m.gif',
                       'https://i.imgur.com/Pa4Hlkq.gif',
                       'https://i.imgur.com/BZ2C2uI.gif',
                       'https://i.imgur.com/BleS1K0.gif',
                       'https://i.imgur.com/5uZyuhy.gif',
                       'https://i.imgur.com/b6eyg1x.gif',
                       'https://i.imgur.com/WqUk4yS.gif?1',
                       'https://i.imgur.com/ONu9WZ1.gif',
                       'https://i.imgur.com/4xcZHuJ.gif',
                       'https://tenor.com/view/cats-ear-bite-gif-10614631']
            image = random.choice(choices)

            embed = discord.Embed(description=nom.format(author, mention), colour=discord.Colour.blue())
            embed.set_image(url=image)

            await ctx.send(embed=embed)

    @commands.command(hidden=True)
    async def test(self, ctx, member: discord.Member = None):
        if not member:

            member = ctx.message.author
        author = ctx.message.author.name
        mention = member.name

        test = 'test {0} {1}'

        embed = discord.Embed(description=test.format(author,mention), colour=discord.Colour.blue())
        embed.set_image(url='https://imgur.com/FxKrt2G.gif')

        await ctx.send(embed=embed)




    @commands.command()
    async def blowkiss(self, ctx, member: discord.Member):
        """Blows a kiss to person you mention"""
        author = ctx.message.author.name
        mention = member.name

        blowkiss = '**{0} blows a kiss to {1}**'

        choices = ['https://media.giphy.com/media/hmiydBazzyW5y/giphy.gif',
                   'https://media.giphy.com/media/4UcraRMTbNpfO/giphy.gif',
                   'http://giphygifs.s3.amazonaws.com/media/NKmXVFgwd8HKw/giphy.gif',
                   'https://media.giphy.com/media/39isVWEe9yBwK8hzcj/giphy.gif',
                   'https://media.giphy.com/media/QAsBwSjx9zVKoGp9nr/giphy.gif',
                   'http://giphygifs.s3.amazonaws.com/media/10c9BEZyo8szo4/giphy.gif',
                   'https://media.giphy.com/media/xag8xIt7P4fGE/giphy.gif',
                   'https://media.giphy.com/media/m4OgFoffdQSti/giphy.gif',
                   'https://media.giphy.com/media/3o8doTunsmrY7j9h96/giphy.gif',
                   'https://media.giphy.com/media/2lZBbmkLX6FPPF30NR/giphy.gif']
        image = random.choice(choices)

        embed = discord.Embed(description=blowkiss.format(author, mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await ctx.send(embed=embed)

    @blowkiss.error
    async def blowkiss_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to mention someone!')

        raise error

    @commands.command()
    async def slap(self, ctx, member: discord.Member):
        """Slaps the person you mention"""
        author = ctx.message.author.name
        mention = member.name

        slap = '**{0} slaps the fuck out of {1}**'

        choices = ['https://media0.giphy.com/media/jLeyZWgtwgr2U/source.gif',
                   'https://media1.tenor.com/images/b6d8a83eb652a30b95e87cf96a21e007/tenor.gif?itemid=10426943',
                   'https://media3.giphy.com/media/LB1kIoSRFTC2Q/source.gif',
                   'https://media1.tenor.com/images/1cf84bf514d2abd2810588caf7d9fd08/tenor.gif?itemid=7679403',
                   'https://media1.tenor.com/images/85722c3e51d390e11a0493696f32fb69/tenor.gif?itemid=5463215',
                   'https://media3.giphy.com/media/Zau0yrl17uzdK/giphy.gif',
                   'https://thumbs.gfycat.com/PersonalUnlinedAsiaticwildass-size_restricted.gif',
                   'https://i.pinimg.com/originals/46/b0/a2/46b0a213e3ea1a9c6fcc060af6843a0e.gif',
                   'https://i.kym-cdn.com/photos/images/newsfeed/000/940/326/086.gif',
                   'https://i.pinimg.com/originals/1c/8f/0f/1c8f0f43c75c11bf504b25340ddd912d.gif',
                   'https://media1.tenor.com/images/fb17a25b86d80e55ceb5153f08e79385/tenor.gif?itemid=7919028',
                   'https://thumbs.gfycat.com/CompetentIncredibleInganue-small.gif',
                   'https://media.giphy.com/media/VEmm8ngZxwJ9K/giphy.gif',
                   'https://media1.tenor.com/images/4eed54377433c396ce2d9ad9ee5d22ef/tenor.gif?itemid=11234788',
                   'https://i.pinimg.com/originals/bf/ef/b4/bfefb401ed8f1f7a3fee62d76a2856a4.gif',
                   'http://pa1.narvii.com/5728/7b796b9cd6a6f44ef6b0aabee0d28d1351fdc7be_hq.gif',
                   'https://media3.giphy.com/media/iREUC7qrjN4vC/source.gif',
                   'https://media1.tenor.com/images/f619012e2ec268d73ecfb89af5a8fb51/tenor.gif?itemid=8562186']
        image = random.choice(choices)

        embed = discord.Embed(description=slap.format(author, mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await ctx.send(embed=embed)

    @slap.error
    async def slap_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to mention someone!')

        raise error

    @commands.command()
    async def poke(self, ctx, member: discord.Member):
        """Pokes the user you mention"""
        author = ctx.message.author.name
        mention = member.name

        poke = '**{0} pokes {1}**'

        choices = ['https://media1.giphy.com/media/WvVzZ9mCyMjsc/source.gif',
                   'https://media1.tenor.com/images/1236e0d70c6ee3ea91d414bcaf9f3aa4/tenor.gif?itemid=5015314',
                   'https://media1.tenor.com/images/01b264dc057eff2d0ee6869e9ed514c1/tenor.gif?itemid=14346763',
                   'https://media1.tenor.com/images/3b9cffb5b30236f678fdccf442006a43/tenor.gif?itemid=7739077',
                   'https://media1.tenor.com/images/fd46d903c4a20a7e82519a78f15b2750/tenor.gif?itemid=8562185',
                   'https://thumbs.gfycat.com/ConventionalIlliterateFattaileddunnart-size_restricted.gif',
                   'https://thumbs.gfycat.com/EnlightenedInferiorAfricanaugurbuzzard-size_restricted.gif',
                   'https://i.pinimg.com/originals/9d/25/23/9d25235a88f0fb52c3b72bf9404d2b7e.gif',
                   'https://data.whicdn.com/images/113023956/original.gif',
                   'https://media.giphy.com/media/ovbDDmY4Kphtu/giphy.gif',
                   'https://media1.tenor.com/images/e8b25e7d069c203ea7f01989f2a0af59/tenor.gif?itemid=12011027',
                   'https://media.indiedb.com/images/groups/1/1/84/rxsyBWA.gif',
                   'https://i.kym-cdn.com/photos/images/original/001/011/011/065.gif',
                   'https://media0.giphy.com/media/FdinyvXRa8zekBkcdK/giphy.gif',
                   'https://i.gifer.com/JTSO.gif',
                   'https://gifimage.net/wp-content/uploads/2017/09/anime-poke-gif-9.gif']
        image = random.choice(choices)

        embed = discord.Embed(description=poke.format(author, mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await ctx.send(embed=embed)

    @poke.error
    async def poke_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to mention someone!')

        raise error

    @commands.command()
    async def fu(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.author
            if member == ctx.author:
                author = ctx.message.author.name

                fu = '**{0} says fuck you to everyone**'

                choices = ['https://media.giphy.com/media/44Eq3Ab5LPYn6/giphy.gif',
                           'https://media.giphy.com/media/NBN2nFCVQDCDe/giphy.gif',
                           'https://media.giphy.com/media/I7p8K5EY9w9dC/giphy.gif',
                           'https://media.giphy.com/media/13UeVnBP6x05P2/giphy.gif',
                           'https://media.giphy.com/media/YFJ2iCW2FSnbpz0NKp/giphy.gif',
                           'https://media.giphy.com/media/3o7WIvmR2b3nNomGTm/giphy.gif',
                           'https://media.giphy.com/media/YAZziWPL9DBXQRp6Hw/giphy.gif',
                           'https://media.giphy.com/media/l4Fsly71gEOtGvLQA/giphy.gif',
                           'https://media.giphy.com/media/1ztjFS0ST5zZC/giphy.gif',
                           'https://media.giphy.com/media/3og0IGYNjIBiI20EjC/giphy.gif',
                           'https://media.giphy.com/media/l4pTp6rh1J8RjqtX2/giphy.gif',
                           'https://i.gifer.com/3Nx3W.gif',
                           'https://i.gifer.com/3Nx3V.gif',
                           'https://i.gifer.com/3Nx3R.gif',
                           'https://i.gifer.com/3Nx3O.gif',
                           'https://i.gifer.com/3Nx3U.gif',
                           'https://i.gifer.com/3Nx3N.gif',
                           'https://i.gifer.com/3Nx3Q.gif',
                           'https://i.gifer.com/3Nx3T.gif',
                           'https://i.gifer.com/3Nx3M.gif',
                           'https://i.gifer.com/3Nx3I.gif',
                           'https://i.gifer.com/3Nx3G.gif',
                           'https://i.gifer.com/3Nx3J.gif',
                           'https://i.gifer.com/3Nx3F.gif',
                           'https://i.gifer.com/3Nx3K.gif',
                           'https://i.gifer.com/3Nx3H.gif',
                           'https://i.gifer.com/3Nx3E.gif',
                           'https://i.gifer.com/3Nx39.gif',
                           'https://i.gifer.com/3Nx3A.gif',
                           'https://i.gifer.com/3Nx36.gif',
                           'https://i.gifer.com/3Nx34.gif',
                           'https://i.gifer.com/3Nx33.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=fu.format(author), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif member:
            author = ctx.message.author.name
            mention = member.name

            fu = '**{0} says fuck you to {1}**'

            choices = ['https://media.giphy.com/media/44Eq3Ab5LPYn6/giphy.gif',
                       'https://media.giphy.com/media/NBN2nFCVQDCDe/giphy.gif',
                       'https://media.giphy.com/media/I7p8K5EY9w9dC/giphy.gif',
                       'https://media.giphy.com/media/13UeVnBP6x05P2/giphy.gif',
                       'https://media.giphy.com/media/YFJ2iCW2FSnbpz0NKp/giphy.gif',
                       'https://media.giphy.com/media/3o7WIvmR2b3nNomGTm/giphy.gif',
                       'https://media.giphy.com/media/YAZziWPL9DBXQRp6Hw/giphy.gif',
                       'https://media.giphy.com/media/l4Fsly71gEOtGvLQA/giphy.gif',
                       'https://media.giphy.com/media/1ztjFS0ST5zZC/giphy.gif',
                       'https://media.giphy.com/media/3og0IGYNjIBiI20EjC/giphy.gif',
                       'https://media.giphy.com/media/l4pTp6rh1J8RjqtX2/giphy.gif',
                       'https://i.gifer.com/3Nx3W.gif',
                       'https://i.gifer.com/3Nx3V.gif',
                       'https://i.gifer.com/3Nx3R.gif',
                       'https://i.gifer.com/3Nx3O.gif',
                       'https://i.gifer.com/3Nx3U.gif',
                       'https://i.gifer.com/3Nx3N.gif',
                       'https://i.gifer.com/3Nx3Q.gif',
                       'https://i.gifer.com/3Nx3T.gif',
                       'https://i.gifer.com/3Nx3M.gif',
                       'https://i.gifer.com/3Nx3I.gif',
                       'https://i.gifer.com/3Nx3G.gif',
                       'https://i.gifer.com/3Nx3J.gif',
                       'https://i.gifer.com/3Nx3F.gif',
                       'https://i.gifer.com/3Nx3K.gif',
                       'https://i.gifer.com/3Nx3H.gif',
                       'https://i.gifer.com/3Nx3E.gif',
                       'https://i.gifer.com/3Nx39.gif',
                       'https://i.gifer.com/3Nx3A.gif',
                       'https://i.gifer.com/3Nx36.gif',
                       'https://i.gifer.com/3Nx34.gif',
                       'https://i.gifer.com/3Nx33.gif']
            image = random.choice(choices)

            embed = discord.Embed(description=fu.format(author, mention), colour=discord.Colour.blue())
            embed.set_image(url=image)

            await ctx.send(embed=embed)

    @commands.command()
    async def kill(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.author
            if member == ctx.author:
                author = ctx.message.author.name
                kill = '**{0} ok you are dead now pick someone else**'

                embed = discord.Embed(description=kill.format(author), colour=discord.Colour.blue())

                await ctx.send(embed=embed)

        elif member:
            author = ctx.message.author.name
            mention = member.name

            choices = ['**{1} takes an arrow to the knee. And everywhere else.**',
                       '**{0} murders {1} with an axe.**',
                       '**{1} gets struck by lightning.**',
                       '**{0} brutally murders {1} with a dildo**',
                       '**{1} dies in a car accident**',
                       '**{1} forgot the stove open and house blew up**',
                       '**{0} calls {1} fat till he/she dies from sadness**',
                       '**{1} dies from not having any friends**',
                       '**{1} trips over his own shoe laces and dies.**',
                       '**{1} dies from watching the emoji movie and enjoying it.**',
                       '**{1} dies from watching too much gay porn and fapping to it**',
                       '**{1} dies from masturbating too much**',
                       '**{1} tries to fight with a tiger and cant make it out alive**',
                       '**{1} dies from getting too many nudes in dms**',
                       '**{1} dies from being so thirsty for girls**',
                       '**{1} dies from dabbing too much**',
                       '**{0} attempts to kill {1} but fails horribly and dies**']

            kill = random.choice(choices)

            embed = discord.Embed(description=kill.format(author,mention), colour=discord.Colour.blue())

            await ctx.send(embed=embed)

    @commands.command()
    async def boop(self, ctx, member: discord.Member):
        author = ctx.message.author.name
        mention = member.name

        boop = '**{0} boops {1}**'

        choices = ['https://media1.tenor.com/images/cbf38a2e97a348a621207c967a77628a/tenor.gif?itemid=6287077',
                   'https://media2.giphy.com/media/11VhGVByJvvdTy/source.gif',
                   'https://media.tenor.com/images/9945480efe5179c227558769613ee275/tenor.gif',
                   'https://media1.tenor.com/images/afcc29ea455ac515670e51136b64143e/tenor.gif?itemid=12960345',
                   'https://media.tenor.com/images/f6f87118730878c578e0f188da5270fc/tenor.gif',
                   'https://media.giphy.com/media/nf4MjcggGyF7q/giphy.gif',
                   'https://media1.tenor.com/images/30e9924acf59a1f9dedfc25c14d4b12c/tenor.gif?itemid=5488652',
                   'https://media2.giphy.com/media/3o6ZtngdoBCLIdFWX6/giphy.gif',
                   'https://media0.giphy.com/media/10MSCF1viNV7zy/giphy.gif',
                   'https://media1.giphy.com/media/3rYxjO5uI5XKWfekns/giphy.gif',
                   'https://media.giphy.com/media/btKJis06RCYUw/giphy.gif',
                   'https://thumbs.gfycat.com/DigitalAdeptHarborporpoise-size_restricted.gif',
                   'https://i.chzbgr.com/full/8762736384/h8A112B3C/',
                   'http://31.media.tumblr.com/feec13efee561d51a1c36eb11d2c4be5/tumblr_muhdb0sOjh1svecmko1_250.gif']
        image = random.choice(choices)

        embed = discord.Embed(description=boop.format(author, mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await ctx.send(embed=embed)

    @commands.command()
    async def fistbump(self, ctx, member:discord.Member):
        author = ctx.message.author.name
        mention = member.name

        fistbump = '**{0} bumps fist with {1}**'

        choices = ['https://media3.giphy.com/media/UjCXeFnYcI2R2/giphy.gif',
                   'https://media3.giphy.com/media/Dnt2VnWFknFNm/giphy.gif',
                   'https://media.tenor.com/images/d9e0decca877f6a42143f4b3c5b62cc0/tenor.gif',
                   'https://media1.tenor.com/images/1f281a73477489a8b53ff85c13999714/tenor.gif?itemid=7529741',
                   'https://media.giphy.com/media/5nsfhEOCgU1Av5lNNb/giphy.gif',
                   'https://media0.giphy.com/media/l0NwIRQKlO1a9cdDG/giphy.gif',
                   'https://www.reactiongifs.us/wp-content/uploads/2014/10/obama_letterman_fist_bump.gif',
                   'https://68.media.tumblr.com/31abe1bdf2fedbc5ae53328dd125f7e7/tumblr_on1h4zgxIZ1urajweo4_1280.gif',
                   'http://gif-free.com/uploads/posts/2017-12/1512403816_community-fist-bump.gif',
                   'https://i.gifer.com/1Oxo.gif',
                   'http://38.media.tumblr.com/5eb7cb4cbcbc40130584e47da41372b2/tumblr_n8da54GYKp1rnjfjfo1_r1_400.gif',
                   'https://media0.giphy.com/media/8SocBAFka3VMQ/giphy.gif',
                   'https://66.media.tumblr.com/174ebb799428415c95e781790bf2a3c0/tumblr_o5e3vcDwyd1tf76g1o1_400.gifv',
                   'http://mrwgifs.com/wp-content/uploads/2013/11/Boosh-Fist-Bump-In-Gif-Hot-Rod.gif',
                   'https://thumbs.gfycat.com/HiddenPlainButterfly-size_restricted.gif',
                   'https://66.media.tumblr.com/c259ea5799788d06a5fbb8eaf689c04d/tumblr_o4rh6jsvZW1udh5n8o1_500.gifv',
                   'http://24.media.tumblr.com/f6a0eb44dfedbf6cf5142f7e6610115d/tumblr_mrvpwfUedD1sp64f5o1_500.gif',
                   'http://www.reactiongifs.us/wp-content/uploads/2013/02/fist_bump_shawn_gus_psych.gif',
                   'https://fansided.com/wp-content/blogs.dir/229/files/2013/12/camnewtonfistbump.gif']
        image = random.choice(choices)

        embed = discord.Embed(description=fistbump.format(author, mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await ctx.send(embed=embed)

    @commands.command(aliases=['grouphug'])
    async def hug1(self, ctx, users: Greedy[User]):
        list = ''
        for user in users:
            list += f'**{user.name},** '

        if list == '':
            await ctx.send('**You need to mention someone!**')

        else:
            group = '**and {0} hugs as a group**'
            choices = ['https://media3.giphy.com/media/Y0wDVs0JGCUA560hi8/giphy.gif',
                       'https://media.tenor.com/images/99d04f40d780cf6cbaeab95ceee8a79e/tenor.gif',
                       'https://media0.giphy.com/media/l396BZVg6Jn0hDj2w/giphy.gif',
                       'https://thumbs.gfycat.com/ShimmeringInexperiencedAfricanwildcat-size_restricted.gif',
                       'https://media.tenor.com/images/ce8aef6d7403cd119867cbbdbc78ffd4/tenor.gif',
                       'https://33.media.tumblr.com/b3e7b9c638f0ed4daa6341df21e0a127/tumblr_n7d49aREpx1smcbm7o1_250.gif',
                       'https://media0.giphy.com/media/3o6fJ1AfB0y1ajHQXe/giphy.gif',
                       'https://static.gofugyourself.com/uploads/2018/06/600_GroupHug_0-1528485848.gif',
                       'http://media.tumblr.com/tumblr_m834b76K5Z1r3vs6r.gif',
                       'https://media0.giphy.com/media/l0Iyd0ZNRWBENPhgA/source.gif',
                       'https://thumbs.gfycat.com/HollowFrenchHoneyeater-size_restricted.gif',
                       'https://i.gifer.com/2vSv.gif',
                       'https://thumbs.gfycat.com/EminentMediocreCoyote-size_restricted.gif',
                       'https://media.giphy.com/media/3og0IGaRAPqKLi6Hw4/giphy.gif',
                       'https://gifimage.net/wp-content/uploads/2017/07/group-hug-gif-13.gif',
                       'https://thumbs.gfycat.com/BlackandwhiteFeistyKronosaurus-size_restricted.gif']
            image = random.choice(choices)

            embed = discord.Embed(description=list + group.format(ctx.author.name), colour=discord.Colour.blue())
            embed.set_image(url=image)

            await ctx.send(embed=embed)

    @commands.command()
    async def bunny(self, ctx):
        author = ctx.message.author.name
        bunny = '**{0} demands some cute bunnies**'

        choices = ['https://cdn.discordapp.com/attachments/613870605489537097/630573014639181824/image1.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/630573015310139421/image0.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/630573026529771531/image1.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/630573027180150784/image0.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/630573041981849631/image1.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/630573043676086301/image0.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/630573044800159744/image1.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/630573045626699776/image0.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/630573056095420449/image1.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/630573056703856660/image0.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/630573072595943448/image0.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/630573072608657409/image1.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/630573072608657411/image0.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/630573090421604383/image1.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/630573091742941235/image0.gif']
        image = random.choice(choices)

        embed = discord.Embed(description=bunny.format(author), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await ctx.send(embed=embed)

    @commands.command()
    async def punch(self, ctx, member: discord.Member):
        author = ctx.message.author.name
        mention = member.name

        punch = '**{0} punches {1}**'
        choices = ['https://media1.tenor.com/images/c22ccca9bccec97234cfa3f0147c32a9/tenor.gif?itemid=5234627',
                   'https://thumbs.gfycat.com/SecondFeminineDuckbillcat-size_restricted.gif',
                   'https://media1.tenor.com/images/92f4595d3f6ac39b6c175eb3d454fec2/tenor.gif?itemid=10460715',
                   'https://thumbs.gfycat.com/ImperfectFrightenedFoal-size_restricted.gif',
                   'https://i.pinimg.com/originals/bc/96/17/bc9617a2460e4640fcd9cf474bea2c10.gif',
                   'https://media2.giphy.com/media/YjHx1taZwpfd6/source.gif',
                   'https://thumbs.gfycat.com/IllinformedRipeFlounder-size_restricted.gif',
                   'https://3.bp.blogspot.com/-k8BL9FEo_YI/Vx01PlromnI/AAAAAAAAAEo/vVEBwcQ1WHspWeDsuUdfFQp47YUj7HEBgCLcB/s1600/Punch%2B5.gif',
                   'https://media.tenor.com/images/9000aca94295d6438ea941069e402e77/tenor.gif',
                   'https://thumbs.gfycat.com/TeemingMeekGrouse-size_restricted.gif',
                   'https://image.myanimelist.net/ui/Z-1YCGdu5bHV02CityXmcU9OsIUZ3cArNJm65_eebXwHpLByYvLQV4ProdsQ4Iuoks76IHKSX6xqEsTYgpAyaSV7_VFhUXly5LFcPRgFLvE',
                   'https://pa1.narvii.com/5897/323ecb6c1ce55337a0e3c3a45be7cba0e77d222b_hq.gif',
                   'https://static.fjcdn.com/gifs/Turning+anime+into+manga+with+one+punch_78b39f_5520149.gif']
        image = random.choice(choices)

        embed = discord.Embed(description=punch.format(author, mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await ctx.send(embed=embed)

    @commands.command()
    async def feed(self, ctx, member: discord.Member):
        author = ctx.message.author.name
        mention = member.name

        feed = '**{0} feeds {1}**'

        choices = ['https://media1.tenor.com/images/4b48975ec500f8326c5db6b178a91a3a/tenor.gif?itemid=12593977',
                   'https://media1.tenor.com/images/571da4da1ad526afe744423f7581a452/tenor.gif?itemid=11658244',
                   'https://media3.giphy.com/media/xYy3O2fGTfflS/giphy.gif',
                   'https://thumbs.gfycat.com/EagerSpectacularHoverfly-size_restricted.gif',
                   'https://thumbs.gfycat.com/ScarceSlimyApatosaur-size_restricted.gif',
                   'https://media.tenor.com/images/577a40a2d18527b30f2b43aab9d619fe/tenor.gif',
                   'https://data.whicdn.com/images/27164350/original.gif',
                   'https://thumbs.gfycat.com/RawLightInvisiblerail-size_restricted.gif',
                   'https://media1.tenor.com/images/39ec9d3b1385467ed566f3a0b0a04e2d/tenor.gif?itemid=13451637',
                   'https://media.tenor.com/images/54112765b2c1b359ffc5f55bd0661b93/tenor.gif',
                   'http://24.media.tumblr.com/c7ae2bd6dccbf1cf07692103d850c975/tumblr_mwbflsTQoI1rkeknyo2_500.gif',
                   'https://media0.giphy.com/media/oIOjBqO1STizS/source.gif',
                   'https://i.gifer.com/7pDW.gif',
                   'https://media.tenor.com/images/b53f617f8d0ecce4f0a6d92dc613bac7/tenor.gif',
                   'https://i.pinimg.com/originals/79/d6/54/79d65474b84e0b1fbf8ac49d57634dfd.gif',
                   'https://thumbs.gfycat.com/ConventionalEntireEsok-size_restricted.gif',
                   'https://media1.giphy.com/media/Kg0dUKqs6RtjW/source.gif',
                   'https://data.whicdn.com/images/237892709/original.gif',
                   'https://31.media.tumblr.com/e70e0f9c84a247e7cfe61a7fdca47cac/tumblr_nnsewixbjT1r1zvalo1_500.gif',
                   'https://media1.tenor.com/images/8efff4185dfb404532d6132023775bcd/tenor.gif?itemid=6004308',
                   'https://i.kym-cdn.com/photos/images/newsfeed/001/071/689/b55.gif',
                   'https://pa1.narvii.com/6123/5ab70369db4a8971bdea24b09039ff3c5a3a244f_hq.gif',
                   'https://media1.tenor.com/images/6a69689b0b485b01b6395193f1490ceb/tenor.gif?itemid=15085210',
                   'https://66.media.tumblr.com/a9da103f86d9cb2f7d5e148981b0aef4/tumblr_pgm5qubdox1th206io1_400.gif',
                   'http://pa1.narvii.com/6104/71c25f7f7b223d94ba8a857214663f795ce6116f_00.gif',
                   'https://thumbs.gfycat.com/EachMajesticBuffalo-size_restricted.gif',
                   'https://static.wixstatic.com/media/c1299e_20abefa4f17748b9a87360f1a91941fa.gif',
                   'https://data.whicdn.com/images/89107524/original.gif',
                   'https://78.media.tumblr.com/870763f03b4f4feba3f0bf7a44b8d9f7/tumblr_njt4s7BxpX1unbsixo1_500.gif',
                   'https://i.imgur.com/cDONf0I.gif']
        image = random.choice(choices)

        embed = discord.Embed(description=feed.format(author, mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await ctx.send(embed=embed)

    @commands.command()
    async def fight(self, ctx, member: discord.Member):
        author = ctx.message.author.name
        mention = member.name

        fight = '**{0} picks up a fight with {1}**'

        choices = ['https://media2.giphy.com/media/eR7OEDQDyA7Cg/giphy.gif',
                   'https://media0.giphy.com/media/gFYt7JTzRp22k/giphy.gif',
                   'https://media0.giphy.com/media/FL2VUieM4YNKU/giphy.gif',
                   'https://media1.giphy.com/media/116VjFrTZdYMjm/giphy.gif',
                   'https://media1.giphy.com/media/6CJT5B0JwxCY8/giphy.gif',
                   'https://thumbs.gfycat.com/UnconsciousHandmadeFrilledlizard-small.gif',
                   'https://i.pinimg.com/originals/ff/a8/46/ffa84602baa92aa93c5d896e69494484.gif',
                   'https://media0.giphy.com/media/iqkCNZIzSSXSM/giphy.gif',
                   'https://media3.giphy.com/media/1mpAmSVQNOzxS/source.gif']
        image = random.choice(choices)
        embed = discord.Embed(description=fight.format(author, mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await ctx.send(embed=embed)

    @commands.command()
    async def suplex(self, ctx, member: discord.Member):
        author = ctx.message.author.name
        mention = member.name

        suplex = '**{0} suplex {1}**'
        choices = ['https://media2.giphy.com/media/65HMPg8Ta0nsefxubm/giphy.gif',
                   'https://media1.giphy.com/media/EV7JPgLez5frO/giphy.gif',
                   'https://media1.tenor.com/images/d3f671f6b9efcbd9663272efcdf22155/tenor.gif?itemid=10361194',
                   'https://media0.giphy.com/media/2ipdGA1xlWb2nfjvAh/giphy.gif',
                   'https://media1.giphy.com/media/RI4LPCRD0jIyXraX7S/giphy.gif',
                   'https://thumbs.gfycat.com/MemorableRepulsiveHoneybadger-size_restricted.gif',
                   'https://media1.tenor.com/images/679224d311edd36a8c396508bcd16127/tenor.gif?itemid=9720582',
                   'https://media.giphy.com/media/cjyxGK1CjUhlNehbfm/giphy.gif',
                   'https://media.giphy.com/media/S5254dkkQRPg9qRQyT/giphy.gif',
                   'https://media.giphy.com/media/MZjezuai3ePphFEzwc/giphy.gif',
                   'https://media.giphy.com/media/L3oMzP9U1Q7zC8MDiu/giphy.gif',
                   'https://media.giphy.com/media/RNQG9i7RDalXpaSqEo/giphy.gif',
                   'https://media.giphy.com/media/S5ErgGr5TtPFhujpAC/giphy.gif',
                   'https://media.giphy.com/media/f9N93ITGG55XjRB2f4/giphy.gif',
                   'https://media.giphy.com/media/f6EIhpOxVVmSIeX6FF/giphy.gif',
                   'https://media.giphy.com/media/VzlJMzxcQ0qVcDacTT/giphy.gif',
                   'https://media.giphy.com/media/UqGXOfTfsE6DkZnLWn/giphy.gif',
                   'https://media.giphy.com/media/L0H8mgd5rstTsA4WjS/giphy.gif',
                   'https://media.giphy.com/media/H4DPJNLYe1Qfq1Cahv/giphy.gif',
                   'https://media.giphy.com/media/MdFJTaM2lqvQWVUPBj/giphy.gif',
                   'https://media.giphy.com/media/llILopI9TcGJ71m4TT/giphy.gif',
                   'https://media.giphy.com/media/SXBLhZGYVUXZqMv2GD/giphy.gif',
                   'https://media.giphy.com/media/LNezPh8P7Xz48Fvxy4/giphy.gif',
                   'https://media.giphy.com/media/M9a96ELb4F7PkSvhxh/giphy.gif',
                   'https://media.giphy.com/media/izbiRljkNdoj6feqj5/giphy.gif',
                   'https://media.giphy.com/media/eLWwLb9y3Be9fMfCoS/giphy.gif',
                   'https://thumbs.gfycat.com/CookedMiserlyGrizzlybear.webp']
        image = random.choice(choices)

        embed = discord.Embed(description=suplex.format(author, mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await ctx.send(embed=embed)

    @suplex.error
    async def suplex_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**You need to mention someone**')

        raise error

    @commands.command()
    async def popcorn(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.author
            if member == ctx.author:
                author = ctx.message.author.name
                popcorn = '**{0} eats some popcorn**'

                choices = ['https://media.giphy.com/media/XQq8UMo254P16/giphy.gif',
                           'https://media.giphy.com/media/13WQCUCrviZrPy/giphy.gif',
                           'http://giphygifs.s3.amazonaws.com/media/edho4s1lWEawo/giphy.gif',
                           'http://giphygifs.s3.amazonaws.com/media/gl0mkIZOW6Nwc/giphy.gif',
                           'http://giphygifs.s3.amazonaws.com/media/8cdZit2ZcjTri/giphy.gif',
                           'https://media.giphy.com/media/tyqcJoNjNv0Fq/giphy.gif',
                           'https://media.giphy.com/media/UlqLDtI8Qc0j6/giphy.gif',
                           'https://media.giphy.com/media/SM68qhJl96Bgc/giphy.gif',
                           'https://media.giphy.com/media/l0HlPystfePnAI3G8/giphy.gif',
                           'https://media.giphy.com/media/dZylOH8HYZ6KOed8N6/giphy.gif',
                           'https://media.giphy.com/media/l0HluKLonblTf8ili/giphy.gif',
                           'https://media.giphy.com/media/9RcIx27XA7qhi/giphy.gif',
                           'https://media.giphy.com/media/d3YQCPcckxQiYibe/giphy.gif',
                           'http://giphygifs.s3.amazonaws.com/media/ri3DONNgpGW4w/giphy.gif',
                           'http://giphygifs.s3.amazonaws.com/media/2yp39L1OH092M/giphy.gif',
                           'https://media.giphy.com/media/3o7TKUa74eWvYkW7hm/giphy.gif',
                           'https://media.giphy.com/media/l0IsIZw8doJm3ysRq/giphy.gif',
                           'https://media.giphy.com/media/TaNiLOpQhqhA4/giphy.gif',
                           'http://giphygifs.s3.amazonaws.com/media/Pq31kHa0MDWuc/giphy.gif',
                           'https://media.giphy.com/media/3o7rc0qU6m5hneMsuc/giphy.gif'
                           ]
                image = random.choice(choices)

                embed = discord.Embed(description=popcorn.format(author), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif member:
            author = ctx.message.author.name
            mention = member.name
            popcorn = '**{0} eats some popcorn with {1}**'

            choices = ['https://media.giphy.com/media/XQq8UMo254P16/giphy.gif',
                       'https://media.giphy.com/media/13WQCUCrviZrPy/giphy.gif',
                       'http://giphygifs.s3.amazonaws.com/media/edho4s1lWEawo/giphy.gif',
                       'http://giphygifs.s3.amazonaws.com/media/gl0mkIZOW6Nwc/giphy.gif',
                       'http://giphygifs.s3.amazonaws.com/media/8cdZit2ZcjTri/giphy.gif',
                       'https://media.giphy.com/media/tyqcJoNjNv0Fq/giphy.gif',
                       'https://media.giphy.com/media/UlqLDtI8Qc0j6/giphy.gif',
                       'https://media.giphy.com/media/SM68qhJl96Bgc/giphy.gif',
                       'https://media.giphy.com/media/l0HlPystfePnAI3G8/giphy.gif',
                       'https://media.giphy.com/media/dZylOH8HYZ6KOed8N6/giphy.gif',
                       'https://media.giphy.com/media/l0HluKLonblTf8ili/giphy.gif',
                       'https://media.giphy.com/media/9RcIx27XA7qhi/giphy.gif',
                       'https://media.giphy.com/media/d3YQCPcckxQiYibe/giphy.gif',
                       'http://giphygifs.s3.amazonaws.com/media/ri3DONNgpGW4w/giphy.gif',
                       'http://giphygifs.s3.amazonaws.com/media/2yp39L1OH092M/giphy.gif',
                       'https://media.giphy.com/media/3o7TKUa74eWvYkW7hm/giphy.gif',
                       'https://media.giphy.com/media/l0IsIZw8doJm3ysRq/giphy.gif',
                       'https://media.giphy.com/media/TaNiLOpQhqhA4/giphy.gif',
                       'http://giphygifs.s3.amazonaws.com/media/Pq31kHa0MDWuc/giphy.gif',
                       'https://media.giphy.com/media/3o7rc0qU6m5hneMsuc/giphy.gif'
                       ]
            image = random.choice(choices)

            embed = discord.Embed(description=popcorn.format(author, mention), colour=discord.Colour.blue())
            embed.set_image(url=image)

            await ctx.send(embed=embed)

    @commands.command(aliases=['gj'])
    async def goodjob(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
            if member == ctx.author:
                author = ctx.message.author.name
                popcorn = '**{0} says good job**'

                choices = ['https://media.giphy.com/media/cEODGfeOYMRxK/giphy.gif',
                           'https://media.giphy.com/media/3ofT5ISstLshYolhSg/giphy.gif',
                           'https://media.giphy.com/media/d2Z9QYzA2aidiWn6/giphy.gif',
                           'https://media.giphy.com/media/3o7abGQa0aRJUurpII/giphy.gif',
                           'https://media.giphy.com/media/fs6jSAbosLAVp5KhH0/giphy.gif',
                           'http://giphygifs.s3.amazonaws.com/media/diUKszNTUghVe/giphy.gif',
                           'https://media.giphy.com/media/111ebonMs90YLu/giphy.gif',
                           'https://media.giphy.com/media/3o72FcJmLzIdYJdmDe/giphy.gif',
                           'https://media.giphy.com/media/x8apGmpYGeFyM/giphy.gif',
                           'https://media.giphy.com/media/9xt1MUZqkneFiWrAAD/giphy.gif',
                           'https://media.giphy.com/media/tIeCLkB8geYtW/giphy.gif',
                           'https://media.giphy.com/media/oGO1MPNUVbbk4/giphy.gif',
                           'https://media.giphy.com/media/3ohs4xsq0oEhqC4why/giphy.gif',
                           'https://media.giphy.com/media/l0HlyiU60rxnEWady/giphy.gif',
                           'http://giphygifs.s3.amazonaws.com/media/gVjt2fYDi7EIM/giphy.gif',
                           'http://giphygifs.s3.amazonaws.com/media/CvZuv5m5cKl8c/giphy.gif',
                           'https://media.tenor.com/images/8bfff93dfe3bb2b5a4c2cbcad7d2130e/tenor.gif'

                           ]
                image = random.choice(choices)

                embed = discord.Embed(description=popcorn.format(author), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif member:
            author = ctx.message.author.name
            mention = member.name
            popcorn = '**{0} says good job to {1}**'

            choices = ['https://media.giphy.com/media/cEODGfeOYMRxK/giphy.gif',
                       'https://media.giphy.com/media/3ofT5ISstLshYolhSg/giphy.gif',
                       'https://media.giphy.com/media/d2Z9QYzA2aidiWn6/giphy.gif',
                       'https://media.giphy.com/media/3o7abGQa0aRJUurpII/giphy.gif',
                       'https://media.giphy.com/media/fs6jSAbosLAVp5KhH0/giphy.gif',
                       'http://giphygifs.s3.amazonaws.com/media/diUKszNTUghVe/giphy.gif',
                       'https://media.giphy.com/media/111ebonMs90YLu/giphy.gif',
                       'https://media.giphy.com/media/3o72FcJmLzIdYJdmDe/giphy.gif',
                       'https://media.giphy.com/media/x8apGmpYGeFyM/giphy.gif',
                       'https://media.giphy.com/media/9xt1MUZqkneFiWrAAD/giphy.gif',
                       'https://media.giphy.com/media/tIeCLkB8geYtW/giphy.gif',
                       'https://media.giphy.com/media/oGO1MPNUVbbk4/giphy.gif',
                       'https://media.giphy.com/media/3ohs4xsq0oEhqC4why/giphy.gif',
                       'https://media.giphy.com/media/l0HlyiU60rxnEWady/giphy.gif',
                       'http://giphygifs.s3.amazonaws.com/media/gVjt2fYDi7EIM/giphy.gif',
                       'http://giphygifs.s3.amazonaws.com/media/CvZuv5m5cKl8c/giphy.gif',
                       'https://media.tenor.com/images/8bfff93dfe3bb2b5a4c2cbcad7d2130e/tenor.gif'

                       ]
            image = random.choice(choices)

            embed = discord.Embed(description=popcorn.format(author, mention), colour=discord.Colour.blue())
            embed.set_image(url=image)

            await ctx.send(embed=embed)

    @commands.command()
    async def burn(self, ctx, member: discord.Member):
        author = ctx.message.author.name
        mention = member.name
        burn = '**{0} burns {1} down, burn them witches**'

        choices = ['https://media2.giphy.com/media/WWamd7I3OP852/source.gif',
                   'https://media.giphy.com/media/xVmYUIXOc3Ucg/giphy.gif',
                   'https://media1.tenor.com/images/bef5d72766b6a85ca183476946a7c04b/tenor.gif?itemid=11687404',
                   'https://thumbs.gfycat.com/KindNegativeKangaroo-small.gif',
                   'https://media1.giphy.com/media/l2JdWwSCbpvEQuBbO/source.gif',
                   'https://media2.giphy.com/media/AdXMjoQHXgXhC/source.gif',
                   'https://media1.giphy.com/media/H55l0bcEOOqWqlrNbt/giphy.gif',
                   'https://i.pinimg.com/originals/f1/45/45/f14545883fee05736142fe3365233450.gif']
        image = random.choice(choices)

        embed = discord.Embed(description=burn.format(author, mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await ctx.send(embed=embed)

    @burn.error
    async def burn_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("**You need to mention someone**")

        raise error

    @commands.command()
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://aws.random.cat/meow") as r:
                data = await r.json()

                embed = discord.Embed(title="Meow", colour=discord.Colour.blue())
                embed.set_image(url=data['file'])
                await ctx.send(embed=embed)


    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def dog(self, ctx):
        """ Posts a random dog """
        await self.randomimageapi(ctx, 'https://random.dog/woof.json', 'url')

    @commands.command()
    async def kick(self, ctx, member: discord.Member):
        author = ctx.message.author.name
        mention = member.name

        kick = '**{0} kicks {1} hard**'

        choices = ['https://media0.giphy.com/media/wOly8pa4s4W88/source.gif',
                   'https://media.giphy.com/media/u2LJ0n4lx6jF6/giphy.gif',
                   'https://media1.tenor.com/images/8b879c6cfa40fb8cbf14252c36ae97cb/tenor.gif?itemid=4798017',
                   'https://media1.tenor.com/images/d54f63dd2f5f807f6de4eedb48ca949b/tenor.gif?itemid=7782627',
                   'https://media1.tenor.com/images/0ef933cc7febed3edd0476cd8040f142/tenor.gif?itemid=5634605',
                   'https://media1.tenor.com/images/e3347537e6cf0a5d0fcceed619a5ea9f/tenor.gif?itemid=8618459',
                   'https://media1.tenor.com/images/fb2a19c9b689123e6254ad9ac6719e96/tenor.gif?itemid=4922649',
                   'https://media0.giphy.com/media/5IPhXGZWeRk64/source.gif',
                   'http://38.media.tumblr.com/ccfb562515974aafd5e879b75439ff18/tumblr_nece2jUD3p1tsd042o1_500.gif',
                   'https://i.kym-cdn.com/photos/images/newsfeed/001/054/543/c22.gif',
                   'https://media.giphy.com/media/VgR9ky7IYjc9W/giphy.gif',
                   'https://i.pinimg.com/originals/c1/96/3f/c1963f1a6e0f4252adf09ee467571853.gif',
                   'https://media1.tenor.com/images/d4bd24c980e46c66f67077aff59f0565/tenor.gif?itemid=13098645',
                   'https://i.chzbgr.com/full/6771336960/hA8C6465D/',
                   'http://24.media.tumblr.com/dfa5b815c6e587c2f1581d85c7c85442/tumblr_mw4irwOMjK1solyeco1_500.gif',
                   'https://media.giphy.com/media/PrxP7r6hgFqx2/giphy.gif',
                   'https://thumbs.gfycat.com/UnnaturalInfiniteKitten-size_restricted.gif',
                   'https://i.pinimg.com/originals/a4/91/52/a49152c33bd633d8a4f0616d9725421a.gif',
                   'https://pa1.narvii.com/5755/83da2064c1b4ecbb60794d200366575818da4524_hq.gif',
                   'https://media1.tenor.com/images/3f212a46e353c61c839a107d755048cd/tenor.gif?itemid=4934443',
                   'https://data.whicdn.com/images/269297930/original.gif',
                   'https://media1.tenor.com/images/ab39f67a357bdf6723cdfbc515498175/tenor.gif?itemid=12822445',
                   'https://i.gifer.com/1ACj.gif',
                   'https://data.whicdn.com/images/121010715/original.gif',
                   'https://media1.tenor.com/images/f6157452e70e127fca276c6981d9e387/tenor.gif?itemid=13610775',
                   'https://i.chzbgr.com/full/6659985408/hE643943B/',
                   'https://gifimage.net/wp-content/uploads/2018/10/anime-kicks-gif-6.gif',
                   'https://media.tenor.com/images/c830621119234f54eaa14b75d39b0409/tenor.gif',
                   'https://thumbs.gfycat.com/VeneratedOblongAfghanhound-size_restricted.gif',
                   'https://i.makeagif.com/media/7-13-2015/zt2uD7.gif',
                   'http://31.media.tumblr.com/ceb700b9939c52a73a4566791811d1be/tumblr_n8ietuNUQq1tg3a8ao1_500.gif',
                   'https://thumbs.gfycat.com/DampTangibleAldabratortoise-size_restricted.gif',
                   'https://media1.tenor.com/images/35f3b7b00c08aa3aeee76d7cac4b796c/tenor.gif?itemid=15220008']
        image = random.choice(choices)

        embed = discord.Embed(description=kick.format(author, mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await ctx.send(embed=embed)

    @commands.command()
    @commands.cooldown(rate=1, per=1.5, type=commands.BucketType.user)
    async def birb(self, ctx):
        """ Posts a random birb """
        await self.randomimageapi(ctx, 'https://api.alexflipnote.dev/birb', 'file')

    @commands.command()
    async def nitro(self, ctx):

        if ctx.channel.id == 484747799083221013:
            role = discord.utils.get(ctx.guild.roles, name="Nitro")
            if role in ctx.author.roles:
                await ctx.send('It works!')

            else:
                await ctx.send('You need to boost the server!')

        else:
            await ctx.send('It works!')

    @commands.command()
    async def yeet(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
            if member == ctx.author:
                author = ctx.message.author.name
                yeet = "**{0} yeets out of here!**"
                choices = ['https://media.giphy.com/media/KzoZUrq40MaazLgHsg/giphy.gif',
                           'https://media2.giphy.com/media/5PhDdJQd2yG1MvHzJ6/giphy.gif',
                           'https://media.giphy.com/media/YnBthdanxDqhB99BGU/giphy.gif',
                           'https://media1.tenor.com/images/b7cded2e6c866a147425f525eeb1e56e/tenor.gif?itemid=12559094',
                           'https://media.giphy.com/media/J1ABRhlfvQNwIOiAas/giphy.gif',
                           'https://media.giphy.com/media/4EEIsDmNJCiNcvAERe/giphy.gif',
                           'https://media1.tenor.com/images/016ac4e4ec3bfd9edb26a6e9007cf087/tenor.gif?itemid=15298225',
                           'https://media.tenor.com/images/8017b6a99c813cbd96421505ec093251/tenor.gif',
                           'https://media.tenor.com/images/016e3e651e3c9382c3376832d2d5acd7/tenor.gif',
                           'https://media.tenor.com/images/b753f87f998e57c0aa3e70b36251cfda/tenor.gif',
                           'https://s0.gifyu.com/images/KwArmIT.gif',
                           'https://s0.gifyu.com/images/0126a483e737d3adf9f1d8a006349c9f.gif',
                           'https://s0.gifyu.com/images/tenor-1abe30c119a8b57e5.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=yeet.format(author), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif member:
            author = ctx.message.author.name
            member = member.name
            yeet = "**{0} yeets {1} out of here!**"
            choices = ['https://media.giphy.com/media/KzoZUrq40MaazLgHsg/giphy.gif',
                       'https://media2.giphy.com/media/5PhDdJQd2yG1MvHzJ6/giphy.gif',
                       'https://media.giphy.com/media/YnBthdanxDqhB99BGU/giphy.gif',
                       'https://media1.tenor.com/images/b7cded2e6c866a147425f525eeb1e56e/tenor.gif?itemid=12559094',
                       'https://media.giphy.com/media/J1ABRhlfvQNwIOiAas/giphy.gif',
                       'https://media.giphy.com/media/4EEIsDmNJCiNcvAERe/giphy.gif',
                       'https://media1.tenor.com/images/016ac4e4ec3bfd9edb26a6e9007cf087/tenor.gif?itemid=15298225',
                       'https://media.tenor.com/images/8017b6a99c813cbd96421505ec093251/tenor.gif',
                       'https://media.tenor.com/images/016e3e651e3c9382c3376832d2d5acd7/tenor.gif',
                       'https://media.tenor.com/images/b753f87f998e57c0aa3e70b36251cfda/tenor.gif',
                       'https://s0.gifyu.com/images/KwArmIT.gif',
                       'https://s0.gifyu.com/images/0126a483e737d3adf9f1d8a006349c9f.gif',
                       'https://s0.gifyu.com/images/tenor-1abe30c119a8b57e5.gif']
            image = random.choice(choices)

            embed = discord.Embed(description=yeet.format(author, member), colour=discord.Colour.blue())
            embed.set_image(url=image)

            await ctx.send(embed=embed)

    @commands.command()
    async def weed(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
            if member == ctx.author:
                author = ctx.author.name
                weed = '**{0} smokes weed all alone**'

                choices = ['https://media.giphy.com/media/KpAPQVW9lWnWU/giphy.gif',
                           'https://media.giphy.com/media/jy4kfeF7Taw48/giphy.gif',
                           'https://media.giphy.com/media/ftdUGIeXOlE290OHjc/giphy.gif',
                           'https://media.giphy.com/media/mBHNZRnjvIVMc/giphy.gif',
                           'https://media.giphy.com/media/Kj6ADcuUnpn68/giphy.gif',
                           'https://media.giphy.com/media/26gJAaPZKuQutL1mg/giphy.gif',
                           'https://media.giphy.com/media/12Etpv4q5ZmXxm/giphy.gif',
                           'https://media.giphy.com/media/2Y8Iq3xe121Ba3hUAM/giphy.gif',
                           'https://media.giphy.com/media/s5CJw8UPITK6I/giphy.gif',
                           'https://media.giphy.com/media/hrWuupb0FAcWk/giphy.gif',
                           'https://media.giphy.com/media/xTiTnkCSkEeBijjq00/giphy.gif',
                           'https://media.giphy.com/media/ghiI1d2FT12E0/giphy.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=weed.format(author), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif member:
            author = ctx.author.name
            mention = member.name

            weed = '**{0} smokes weed with {1}**'
            choices = ['https://media.giphy.com/media/KpAPQVW9lWnWU/giphy.gif',
                       'https://media.giphy.com/media/jy4kfeF7Taw48/giphy.gif',
                       'https://media.giphy.com/media/ftdUGIeXOlE290OHjc/giphy.gif',
                       'https://media.giphy.com/media/mBHNZRnjvIVMc/giphy.gif',
                       'https://media.giphy.com/media/Kj6ADcuUnpn68/giphy.gif',
                       'https://media.giphy.com/media/26gJAaPZKuQutL1mg/giphy.gif',
                       'https://media.giphy.com/media/12Etpv4q5ZmXxm/giphy.gif',
                       'https://media.giphy.com/media/2Y8Iq3xe121Ba3hUAM/giphy.gif',
                       'https://media.giphy.com/media/s5CJw8UPITK6I/giphy.gif',
                       'https://media.giphy.com/media/hrWuupb0FAcWk/giphy.gif',
                       'https://media.giphy.com/media/xTiTnkCSkEeBijjq00/giphy.gif',
                       'https://media.giphy.com/media/ghiI1d2FT12E0/giphy.gif']
            image = random.choice(choices)

            embed = discord.Embed(description=weed.format(author, mention), colour=discord.Colour.blue())
            embed.set_image(url=image)

            await ctx.send(embed=embed)

    @commands.command()
    async def cake(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
            if member == ctx.author:
                author = ctx.author.name
                cake = '**{0} takes a cake to eat**'

                choices = ['https://media.giphy.com/media/9u8GF7MuhdvS8/giphy.gif',
                           'https://media.giphy.com/media/He4wudo59enf2/giphy.gif',
                           'https://media.giphy.com/media/jbKaOGsQyBgRgi83t3/giphy.gif',
                           'https://media.giphy.com/media/E5jCN5tsN21Ec/giphy.gif',
                           'https://media.giphy.com/media/TEkr9oBZ57KFmMWScZ/giphy.gif',
                           'https://media.giphy.com/media/hNahVvxcVA9Og/giphy.gif',
                           'https://media.giphy.com/media/26FmPC0waZwmJoGY0/giphy.gif']

                image = random.choice(choices)

                embed = discord.Embed(description=cake.format(author), colour=discord.Colour.blue())
                embed.set_image(url=image)
                await ctx.send(embed=embed)

        elif member:
            author = ctx.author.name
            mention = member.name
            cake = '**{0} takes a cake to eat with {1}**'

            choices = ['https://media.giphy.com/media/9u8GF7MuhdvS8/giphy.gif',
                       'https://media.giphy.com/media/He4wudo59enf2/giphy.gif',
                       'https://media.giphy.com/media/jbKaOGsQyBgRgi83t3/giphy.gif',
                       'https://media.giphy.com/media/E5jCN5tsN21Ec/giphy.gif',
                       'https://media.giphy.com/media/TEkr9oBZ57KFmMWScZ/giphy.gif',
                       'https://media.giphy.com/media/hNahVvxcVA9Og/giphy.gif',
                       'https://media.giphy.com/media/26FmPC0waZwmJoGY0/giphy.gif']

            image = random.choice(choices)

            embed = discord.Embed(description=cake.format(author, mention), colour=discord.Colour.blue())
            embed.set_image(url=image)
            await ctx.send(embed=embed)

    @commands.command()
    async def pout(self, ctx):
        author = ctx.author.name
        pout = '**{0} pouts!!**'
        choices = ['https://media1.tenor.com/images/b7e132fd3f4e110ea54ef8aa8f4eebbe/tenor.gif?itemid=15650605',
                   'https://media.tenor.com/images/3e0c7be0cb8e24c389f5e1f78a8f69a5/tenor.gif',
                   'https://media1.tenor.com/images/2aedb9ff34aa111c5789004d22d05a78/tenor.gif?itemid=12144903',
                   'https://media1.tenor.com/images/834176874a04f82c10b6f0ea6180212c/tenor.gif?itemid=7302800',
                   'https://media1.tenor.com/images/d52117b1bbec0fa89baa8095e2c0fe87/tenor.gif?itemid=11686117',
                   'https://media.tenor.com/images/4217a276896fa6b73099cf84f136e795/tenor.gif',
                   'https://media1.tenor.com/images/760ec8be1ccf4e9ca49f976b34cdc6e9/tenor.gif?itemid=5478780',
                   'https://media.tenor.com/images/011ec2a67e69cd48570bf530ce84016b/tenor.gif',
                   'https://media1.tenor.com/images/a2cde795512dffb7ed89448a14d7e68e/tenor.gif?itemid=12007445']
        image = random.choice(choices)

        embed = discord.Embed(description=pout.format(author), colour=discord.Colour.blue())
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command()
    async def aesthetic(self, ctx):
        if ctx.message.author.id == 264613923490234368:
            choices = ['https://www.wykop.pl/cdn/c3201142/comment_EK77chp6pkcJ5Y4qxMJT32YCW8zHDqwA.gif',
                       'https://thumbs.gfycat.com/ValidWearyDipper-small.gif',
                       'https://thumbs.gfycat.com/LikelyWearyDartfrog-small.gif',
                       'https://thumbs.gfycat.com/ShamefulGeneralDairycow-small.gif',
                       'https://thumbs.gfycat.com/LimpBestFritillarybutterfly-small.gif',
                       'https://thumbs.gfycat.com/BountifulLikableBellfrog-small.gif']
            image = random.choice(choices)

            embed = discord.Embed(colour=discord.Colour.blue())
            embed.set_image(url=image)
            await ctx.send(embed=embed)

        else:
            await ctx.send("You don't have access to this command")

    @commands.command()
    async def howgay(self, ctx, member:discord.Member = None):
        if not member:
            member = ctx.author
            number = random.randint(0, 100)
            emoji = self.client.get_emoji(704452881616732251)
            embed = discord.Embed(description=f"{member.name} is {number}% {emoji}", colour=discord.Colour.blue())
            await ctx.send(embed=embed)

        else:
            number = random.randint(0, 100)
            emoji = self.client.get_emoji(704452881616732251)
            embed = discord.Embed(description=f"{member.name} is {number}% {emoji}", colour=discord.Colour.blue())
            await ctx.send(embed=embed)

    @commands.command()
    async def coffee(self, ctx, member:discord.Member = None):
        if not member:
            member = ctx.author
            if member == ctx.author:
                author = ctx.author.name
                cake = '**{0} takes a coffee to drink**'

                choices = ['https://media3.giphy.com/media/3oriO04qxVReM5rJEA/200.gif',
                           'https://media2.giphy.com/media/PkFHBnpzHZTCBX1ZwU/giphy.gif',
                           'https://media.giphy.com/media/u9QoHec9uGfq8/giphy.gif',
                           'https://media.giphy.com/media/xT5LMT6SSx83oZz464/giphy.gif',
                           'https://akns-images.eonline.com/eol_images/Entire_Site/2015829/rs_500x200-150929111657-635645773709041928-948364329_LeslieKnope_coffee.gif?fit=inside|900:auto&output-quality=90',
                           'https://gif-free.com/uploads/posts/2017-07/1500311393_jim-carrey-coffee.gif',
                           'https://media1.giphy.com/media/HVhofxmUXMyGs/giphy.gif']

                image = random.choice(choices)

                embed = discord.Embed(description=cake.format(author), colour=discord.Colour.blue())
                embed.set_image(url=image)
                await ctx.send(embed=embed)

        elif member:
                author = ctx.author.name
                mention = member.name
                cake = '**{0} drinks a coffee with {1}**'

                choices = ['https://media3.giphy.com/media/3oriO04qxVReM5rJEA/200.gif',
                           'https://media2.giphy.com/media/PkFHBnpzHZTCBX1ZwU/giphy.gif',
                           'https://media.giphy.com/media/u9QoHec9uGfq8/giphy.gif',
                           'https://media.giphy.com/media/xT5LMT6SSx83oZz464/giphy.gif',
                           'https://akns-images.eonline.com/eol_images/Entire_Site/2015829/rs_500x200-150929111657-635645773709041928-948364329_LeslieKnope_coffee.gif?fit=inside|900:auto&output-quality=90',
                           'https://gif-free.com/uploads/posts/2017-07/1500311393_jim-carrey-coffee.gif',
                           'https://media1.giphy.com/media/HVhofxmUXMyGs/giphy.gif']

                image = random.choice(choices)

                embed = discord.Embed(description=cake.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)
                await ctx.send(embed=embed)

    @commands.command()
    async def dab(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
            if member == ctx.author:
                author = ctx.author.name
                randomize = ['**{0} dabs furiously**',
                             '**{0} dabs on them haters**',
                             '**{0} dabs so hard everyone notices it**',
                             '**{0} is on a dabbing spree**',
                             '**{0} dabs nonstop**']
                dab = random.choice(randomize)

                choices = ['https://media.giphy.com/media/A4R8sdUG7G9TG/giphy.gif',
                           'https://media.giphy.com/media/SoshjAcfNsOsw/giphy.gif',
                           'https://media.giphy.com/media/lae7QSMFxEkkE/giphy.gif',
                           'https://media.giphy.com/media/5zKGCHBd8x5GE/giphy.gif',
                           'https://media.giphy.com/media/l0Iy0re0QAYULZvPy/giphy.gif',
                           'https://media.giphy.com/media/3oKIP6AYztSrFZ0AoM/giphy.gif',
                           'https://media.giphy.com/media/oqJrPBk7UzhIc/giphy.gif',
                           'https://media.giphy.com/media/26BRI6cTc6tUzeYNO/giphy.gif',
                           'https://media.giphy.com/media/l0JMeYqiwKDkZsEOk/giphy.gif']

                image = random.choice(choices)

                embed = discord.Embed(description=dab.format(author), colour=discord.Colour.blue())
                embed.set_image(url=image)
                await ctx.send(embed=embed)

        elif member:
            author = ctx.author.name
            mention = member.name
            randomize = ['**{0} dabs on {1}**',
                         '**{0} dabs furiously on {1}**',
                         '**{0} can\'t stop dabbing on {1}**',
                         '**{0} keeps dabbing on {1}**']
            dab = random.choice(randomize)

            choices = ['https://media.giphy.com/media/A4R8sdUG7G9TG/giphy.gif',
                       'https://media.giphy.com/media/SoshjAcfNsOsw/giphy.gif',
                       'https://media.giphy.com/media/lae7QSMFxEkkE/giphy.gif',
                       'https://media.giphy.com/media/5zKGCHBd8x5GE/giphy.gif',
                       'https://media.giphy.com/media/l0Iy0re0QAYULZvPy/giphy.gif',
                       'https://media.giphy.com/media/3oKIP6AYztSrFZ0AoM/giphy.gif',
                       'https://media.giphy.com/media/oqJrPBk7UzhIc/giphy.gif',
                       'https://media.giphy.com/media/26BRI6cTc6tUzeYNO/giphy.gif',
                       'https://media.giphy.com/media/l0JMeYqiwKDkZsEOk/giphy.gif']

            image = random.choice(choices)

            embed = discord.Embed(description=dab.format(author, mention), colour=discord.Colour.blue())
            embed.set_image(url=image)
            await ctx.send(embed=embed)

    @commands.command(aliases=['donate'])
    async def patreon(self, ctx):
        embed = discord.Embed(title="Click this to go to Patreon page to Support me and my owner~~", url="https://www.patreon.com/botarubot",
                              colour=discord.Colour.blue())
        embed.set_image(url="https://cdn.discordapp.com/attachments/819952464127459338/821746131825721344/botarupat.png")
        await ctx.send(embed=embed)

    @commands.command()
    async def meme(self, ctx):
        subreddit = await reddit.subreddit("memes", fetch=True)

        all_subs = []
        async for submission in subreddit.hot(limit=100):
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        em = discord.Embed(title=name, colour=discord.Colour.blue())
        em.set_image(url=url)

        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(1, 540, commands.BucketType.user)
    async def respond(self, ctx):
        if ctx.author.id == 193419820660686848:
            user_id = await self.client.fetch_user(464802706930794496)
            i = 0
            
            await ctx.send("I'll go annoy <@464802706930794496> till he responds to you")
            while i < 45:
                choices = ["**Raider what's taking you so long bitch**",
                        "**Stop Jerking off and reply to me you hoe**",
                        "**I'M HORNY BE QUICK**",
                        "**Check Your DMs Bitch**",
                        "**COME ON RAIDER CONTINUE THE RP**",
                        ":woman_with_probing_cane:",
                        ":woman_standing:"]
                ran = random.choice(choices)
                await user_id.send(ran)
                await asyncio.sleep(10)
                i += 1
            
        else:
            self.respond.reset_cooldown(ctx)
            choices = [
                'https://cdn.discordapp.com/attachments/798913238229188608/822156703285379119/giphy_1.gif',
                'https://cdn.discordapp.com/attachments/798913238229188608/822156709862178846/067025659eb25f9b74605738d1b2a7a7.gif',
                'https://cdn.discordapp.com/attachments/798913238229188608/822155216287039509/IcyCookedCoot-small.gif',
                'https://cdn.discordapp.com/attachments/798913238229188608/822156711674118174/200.gif',
                'https://cdn.discordapp.com/attachments/798913238229188608/822156717138772048/giphy.gif',
                'https://media1.tenor.com/images/d004741ef8203dba11dd77991f997357/tenor.gif?itemid=5100592']
            img = random.choice(choices)
            embed = discord.Embed(title="This is a Custom Command", colour=discord.Colour.blue())
            embed.set_image(url=img)
            embed.set_footer(text="$patreon to buy a custom command!")
            await ctx.send(embed=embed)        
    
    @respond.error
    async def respond_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            em = discord.Embed(title=f"Slow it down Mandy!",description=f"Try again in {error.retry_after:.2f}s.", colour=discord.Colour.blue())
            await ctx.send(embed=em)

    @commands.command(aliases=["tacos"])
    async def taco(self, ctx, message=None):
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author = ctx.author.name
        
        if mentions == message:
            if message == None:
                    txt = ["{0} says its taco time bitches",
                            "{0} wants to stuff everyone with tacos",
                            "{0} loves them tacos",
                            "{0} wants to be the hot sauce on your tacos",
                            "{0} wishes she/he was full of tacos instead of emotions"]
                    
                    choices = ["https://cdn.discordapp.com/attachments/827259361399013386/827259706762068009/giphy.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259709731897384/taco-tuesday-icegif-6.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259720628174898/tenor_1.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259728379248661/tenor_2.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259728585162762/tenor.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259738050920468/tenor_1.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259751644528640/5675e7e773bde91de2e54f088e88c5b1.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259754493116480/200_d.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259791586885672/SimpleSpitefulChinchilla-small.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259798403285002/giphy_6.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259830976381009/giphy_2.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259838757208125/en4HK93.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259859215974400/200.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259861535817748/FastInbornFlyingfox-size_restricted.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259870243061851/giphy_7.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259875364438026/79db514f-9b1e-450f-812b-73f0e6f5253f_text.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259891265437746/giphy_1.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259898714390629/bc53f3ffcb2f4775-.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259922986827856/0QzK050.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259928803934258/taco-party-1.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259954729713744/giphy_3.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259977655517184/giphy_4.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259986869485568/d70730aba0c133bc6d1f84fe5d50a336.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259987842695198/giphy_5.gif"
                            ]
                    img = random.choice(choices)
                    text = random.choice(txt)
                    embed = discord.Embed(title=text.format(author), colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
            else:
                    txt = ["{0} says its taco time bitches to {1}",
                            "{0} wants to stuff {1} with tacos",
                            "{0} loves them tacos with {1}",
                            "{0} wants to be the hot sauce on your tacos {1}",
                            "{0} says shut up and take this taco to {1}"]
                    
                    choices = ["https://cdn.discordapp.com/attachments/827259361399013386/827259706762068009/giphy.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259709731897384/taco-tuesday-icegif-6.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259720628174898/tenor_1.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259728379248661/tenor_2.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259728585162762/tenor.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259738050920468/tenor_1.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259751644528640/5675e7e773bde91de2e54f088e88c5b1.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259754493116480/200_d.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259791586885672/SimpleSpitefulChinchilla-small.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259798403285002/giphy_6.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259830976381009/giphy_2.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259838757208125/en4HK93.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259859215974400/200.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259861535817748/FastInbornFlyingfox-size_restricted.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259870243061851/giphy_7.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259875364438026/79db514f-9b1e-450f-812b-73f0e6f5253f_text.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259891265437746/giphy_1.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259898714390629/bc53f3ffcb2f4775-.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259922986827856/0QzK050.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259928803934258/taco-party-1.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259954729713744/giphy_3.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259977655517184/giphy_4.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259986869485568/d70730aba0c133bc6d1f84fe5d50a336.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259987842695198/giphy_5.gif"
                            ]
                    img = random.choice(choices)
                    text = random.choice(txt)
                    embed = discord.Embed(title=text.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
        else:
                txt = ["{0} says its taco time bitches to {1}",
                            "{0} wants to stuff {1} with tacos",
                            "{0} loves them tacos with {1}",
                            "{0} wants to be the hot sauce on your tacos {1}",
                            "{0} says shut up and take this taco to {1}"]
                text = random.choice(txt)
                choices = ["https://cdn.discordapp.com/attachments/827259361399013386/827259706762068009/giphy.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259709731897384/taco-tuesday-icegif-6.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259720628174898/tenor_1.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259728379248661/tenor_2.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259728585162762/tenor.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259738050920468/tenor_1.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259751644528640/5675e7e773bde91de2e54f088e88c5b1.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259754493116480/200_d.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259791586885672/SimpleSpitefulChinchilla-small.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259798403285002/giphy_6.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259808268288070/200_1.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259830976381009/giphy_2.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259838757208125/en4HK93.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259861535817748/FastInbornFlyingfox-size_restricted.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259870243061851/giphy_7.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259875364438026/79db514f-9b1e-450f-812b-73f0e6f5253f_text.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259891265437746/giphy_1.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259898714390629/bc53f3ffcb2f4775-.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259922986827856/0QzK050.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259928803934258/taco-party-1.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259954729713744/giphy_3.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259977655517184/giphy_4.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259986869485568/d70730aba0c133bc6d1f84fe5d50a336.gif",
                            "https://cdn.discordapp.com/attachments/827259361399013386/827259987842695198/giphy_5.gif"
                            ]
                img = random.choice(choices)
                embed = discord.Embed(title=text.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=img)
                await ctx.send(embed=embed)
        

def setup(client):
    client.add_cog(Fun(client))