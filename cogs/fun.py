import discord
import time
import random
from discord.ext import commands
from discord.ext.commands import Greedy
from discord import User
from discord.ext.commands import has_permissions, CheckFailure

class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client

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
    async def cuddle(self, ctx, member: discord.Member):
        """
            Cuddles the member you mention
            """
        author = ctx.message.author.name
        mention = member.name

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

        embed = discord.Embed(description=cuddle.format(author, mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await ctx.send(embed=embed)
    @cuddle.error
    async def cuddle_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to mention someone!')

        raise error

    @commands.command()
    async def kiss(self, ctx, member: discord.Member):
        """
            Kisses the member you mention
            """
        author = ctx.message.author.name
        mention = member.name

        kiss = '**{0} gave {1} a kiss!**'

        choices = ['https://media0.giphy.com/media/bGm9FuBCGg4SY/giphy.gif',
                   'http://giphygifs.s3.amazonaws.com/media/FqBTvSNjNzeZG/giphy.gif',
                   'https://media3.giphy.com/media/12VXIxKaIEarL2/giphy.gif',
                   'https://media.tenor.com/images/197df534507bd229ba790e8e1b5f63dc/tenor.gif',
                   'https://i1.wp.com/loveisaname.com/wp-content/uploads/2016/09/23.gif',
                   'http://33.media.tumblr.com/tumblr_m7x4176tyH1ro4cfco1_500.gif',
                   'https://wethehunted.files.wordpress.com/2015/11/katanagatari-kiss.gif',
                   'https://i0.wp.com/media2.giphy.com/media/ll5leTSPh4ocE/giphy.gif?resize=500%2C290&ssl=1']

        image = random.choice(choices)

        embed = discord.Embed(description=kiss.format(author, mention), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await ctx.send(embed=embed)
    @kiss.error
    async def kiss_error(self, ctx, error):
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
                   'https://media.tenor.com/images/0351b76e63a1b7d799936481f734477c/tenor.gif.']

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
            embed.set_image(url='https://media0.giphy.com/media/IUksUxlnc6P7i/giphy.gif?cid=790b7611475929a00079c589e4cd5f6e4651bcd33f6460de&rid=giphy.gif')

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
                       '**{1} dies from being so thirsty for girls**']

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
            group = '**hugs as a group**'
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

            embed = discord.Embed(description=list + group, colour=discord.Colour.blue())
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


def setup(client):
    client.add_cog(Fun(client))