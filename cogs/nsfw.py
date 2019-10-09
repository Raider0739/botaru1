import discord
import random
from discord.ext import commands
from discord.ext.commands import Greedy
from discord import User
import helper


def determineGender(mention):
    """mention: one of: string, class discord.Mention"""
    gender = None
    if type(mention) == str:
        gender = None
    else:
        for role in mention.roles:
            if role.name.lower() in ["male", "trans m->f", "mtf", "m-f", "bi-curious male", "bi male", "gay male", "straight male", "straight guy", "pan & others male", "gay couple", "straight couple", "gentlemen", "guys", "guy", "gentleman", 'gentlemen', 'non-binary']:
                gender = "male"
            elif role.name.lower() in ["female", "bi-curious girl", "straight girl", "bi girl", "straight woman", "bi woman", "woman" "lesbian", "pan & others female", "lesbian couple", "ladies", "lady", 'non-binary']:
                gender = "female"
            elif role.name.lower() in ["f-m","ftm", "trans f->m", "trans", "tran","transexual", "transsexual", "other", "others"+"otherg", "trap"]:
                gender = "trans"
    return gender

class Nsfw(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def nsfw(self, ctx, user: discord.User = None):
        if not user:
            user = ctx.author

        em = discord.Embed(colour=discord.Colour.blue())
        em.set_author(name='Nsfw Command List')
        em.add_field(name='fuck', value='Fucks the member you mention', inline=False)
        em.add_field(name='spank', value='Spanks the member you mention', inline=False)
        em.add_field(name='suck', value='Sucks the member you mention', inline=False)
        em.add_field(name='anal', value='Anal with the member you mention', inline=False)
        em.add_field(name='dom', value='Dominates the member you mention', inline=False)
        em.add_field(name='69', value='69 with the member you mention', inline=False)
        em.add_field(name='creampie', value='Creampies the member you mention', inline=False)
        em.add_field(name='lick', value='Licks the member you mention', inline=False)
        em.add_field(name='tits(tiddy,tiddies)', value='Sends some tits in chat', inline=False)
        em.add_field(name='tease', value='Teases the member you mention', inline=False)
        em.add_field(name='finger', value='Fingers the member you mention', inline=False)
        em.set_footer(text='Channel must be NSFW to use the commands!')
        await user.send(embed=em)
        await ctx.send('**Sending a list of NSFW commands in your DMs**')

    @commands.command(aliases=['fucks'])
    @commands.is_nsfw()
    async def fuck(self, ctx, member: discord.Member):
        """Fucks the user you mention"""

        author_gender = determineGender(ctx.author)
        mention_gender = determineGender(member)

        if author_gender == 'male':
            if mention_gender == 'male':
                author = ctx.message.author.name
                mention = member.name

                fuck = '**{0} fucks {1}**'

                choices = [
                    'https://38.media.tumblr.com/fc562fa7a892467d622844f85068fff0/tumblr_not6bvD3Pe1rpbjogo3_500.gif',
                    'https://images.sex.com/images/pinporn/2013/07/13/300/3177244.gif',
                    'https://18gayteen.com/wp-content/uploads/2019/02/Twink_anal_02.gif',
                    'http://18gayteen.com/wp-content/uploads/2017/09/gay_fuck.gif',
                    'http://megapornx.com/xxx/close-up-anal-gay-gifs.gif',
                    'https://18gayteen.com/wp-content/uploads/2019/08/twinks_anal_08.gif',
                    'https://ii.yuki.la/b/93/c1d369936011b14a31fdbafb1b5a2d24d99bbe977a221da960b78f015879a93b.gif',
                    'http://101hotguys.com/wp-content/uploads/2017/12/Jack_Harrer_01.gif',
                    'http://gaygifs.net/albums/2016/08/30/17/1/vftpx1472568433-international-playboys-jack-harrer-and-darius-ferdynand-1.gif']

                image = random.choice(choices)

                embed = discord.Embed(description=fuck.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

            else:
                author = ctx.message.author.name
                mention = member.name

                fuck = '**{0} fucks {1}**'

                choices = ['https://i.imgur.com/7GNPWmt.gif',
                           'https://i.imgur.com/c35C8jE.gif',
                           'https://i.imgur.com/oLJeFvA.gif',
                           'https://i.imgur.com/mt8Ftyw.gif',
                           'https://i.imgur.com/g5oR261.gif',
                           'https://i.imgur.com/2OZak8m.gif',
                           'https://i.imgur.com/2vc1lSv.gif',
                           'https://i.imgur.com/2GEnjiS.gif',
                           'https://i.imgur.com/FvR7Lj5.gif',
                           'https://i.imgur.com/eUli4xM.gif',
                           'https://i.imgur.com/PDgtutn.gif',
                           'https://i.imgur.com/dfZ0qbJ.gif',
                           'https://i.imgur.com/4prPeMJ.gif',
                           'https://i.imgur.com/NvPHLrO.gif',
                           'https://i.imgur.com/jSRRz5k.gif',
                           'https://i.imgur.com/XkXDBfd.gif',
                           'https://i.imgur.com/phdoII5.gif',
                           'https://i.imgur.com/MTu8wBT.gif',
                           'https://i.imgur.com/aKjJRKt.gif',
                           'https://i.imgur.com/zpcZ3TS.gif',
                           'https://i.imgur.com/Kcf2GdI.gif',
                           'https://i.imgur.com/KkVO095.gif',
                           'https://i.imgur.com/ZYGTQlX.gif'
                           'https://www.youpeg.com/wp-content/uploads/2019/02/gallery-the-worlds-hottest-gianna-dior-xxx-porn-gif-gallery-syber-pussy-xxx-forums-porn-videos-x-1550160633c8p4l.gif',
                           'https://hotporngifs.eu/wp-content/uploads/2018/07/tumblr_ovlpmn6KtD1tduf00o1_400.gif',
                           'https://hotporngifs.eu/wp-content/uploads/2018/05/tumblr_otj1dxn4yq1sg1lgao1_500.gif',
                           'https://hotporngifs.eu/wp-content/uploads/2018/12/tumblr_pgk4v0rSGC1rat4opo1_500-450x635.gif',
                           'http://i.imgur.com/DDso5m8.gif'
                           'http://www.reuni.eu/image/417862.gif',
                           'https://24.media.tumblr.com/073577e9b34d44bc2a13bf534ebcca38/tumblr_mipo08ImUU1qbh1xjo1_500.gif',
                           'https://sluterest.com/wp-content/uploads/2015/06/juicy-fuck-office.gif',
                           'http://www.coaching-et-formation-coaching.eu/image/269c5c7998a9443f1310cd063783b55c.gif',
                           'http://huntingdonshirecricket.com/images/223199.gif']


            image = random.choice(choices)

            embed = discord.Embed(description=fuck.format(author, mention), colour=discord.Colour.blue())
            embed.set_image(url=image)

            await ctx.send(embed=embed)

        elif author_gender == 'female':

            if mention_gender == 'female':
                author = ctx.message.author.name
                mention = member.name

                fuck = '**{0} fucks {1}**'

                choices = ['http://www.porngif.org/wp-content/uploads/2014/08/Evil-Angel-Anal-Corruption.gif',
                           'https://www.pornosexgif.org/wp-content/uploads/2015/11/Brazzers-Lesbian-porn-gif1.gif',
                           'http://www.reuni.eu/image/nude-hot-naked-lesbians-gif-scissors-2.gif',
                           'https://fb05.manworldmediacdn.com/data/images/straight/006/010/390/ezgif.com-resize_web.gif?1437052318',
                           'http://www.daporngifs.com/gif/lesbian-bdsm.gif',
                           'https://www.eroticaingif.com/upload/2019/06/17/20190617013319-b0f987c7.gif',
                           'http://porngif.org/wp-content/uploads/2013/10/1380279930887.gif',
                           'http://revlt.be/wp-content/uploads/lesbian-strapon-gif-9.jpg',
                           'http://24.media.tumblr.com/tumblr_meo9s2EmYh1rt4xvro1_500.gif'
                           'https://i.imgur.com/udgBDoL.gif',
                           'https://i.imgur.com/talPIg8.gif',
                           'https://i.imgur.com/9cwrtjk.gif',
                           'https://i.imgur.com/QaelNEU.gif',
                           'https://i.imgur.com/4NUnIV2.gif',
                           'https://i.imgur.com/VHsGpZs.gif',
                           'https://i.imgur.com/GWDtFww.gif',
                           'https://i.imgur.com/GaS62Di.gif',
                           'https://i.imgur.com/IicsbaR.gif',
                           'https://i.imgur.com/X77kSlX.gif']

                image = random.choice(choices)

                embed = discord.Embed(description=fuck.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name
                mention = member.name

                fuck = '**{0} fucks {1}**'

                choices = ['https://i.imgur.com/rzcjHMc.gif',
                           'https://i.imgur.com/wtasCyb.gif',
                           'https://i.imgur.com/M1rC7p3.gif',
                           'https://i.imgur.com/omP7sd3.gif',
                           'https://i.imgur.com/ySEaQhY.gif',
                           'https://i.imgur.com/eaf3VL2.gif',
                           'https://i.imgur.com/G9486LC.gif',
                           'https://i.imgur.com/IBiN77S.gif',
                           'https://i.imgur.com/5QPB8Am.gif',
                           'https://i.imgur.com/aNftLC1.gif',
                           'https://i.imgur.com/DiiDNPQ.gif',
                           'https://i.imgur.com/euRINPh.gif',
                           'https://i.imgur.com/QiibV2g.gif',
                           'https://i.imgur.com/c1OwdSh.gif',
                           'https://i.imgur.com/bgIMqLT.gif',
                           'https://i.imgur.com/n4PzUcO.gif',
                           'https://i.imgur.com/JdJjVw2.gif',
                           'https://i.imgur.com/62CgFoM.gif',
                           'https://i.imgur.com/zbiCI2n.gif',
                           'https://i.imgur.com/TFFTXLA.gif']

                image = random.choice(choices)

                embed = discord.Embed(description=fuck.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

    @fuck.error
    async def fuck_error (self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to mention someone!')

            raise error

    @commands.command(aliases=['spanks'])
    @commands.is_nsfw()
    async def spank(self, ctx, member: discord.Member):
        """Spanks the user you mention"""
        author_gender = determineGender(ctx.author)
        mention_gender = determineGender(member)

        if author_gender == 'male':
            if mention_gender == 'male':

                author = ctx.message.author.name
                mention = member.name

                spank = '**{0} spanks {1}s booty**'

                choices = ['https://66.media.tumblr.com/3c847409a303f9e532143d3f3c5d048a/tumblr_pg8g29z9Nu1xqr2fio1_500.gif',
                           'https://66.media.tumblr.com/fc70714c4908c1dd184a34027a2f3a9f/tumblr_p8981eux6T1xqr2fio1_540.gif',
                           'https://i1.wp.com/gayspankingclips.com/wp-content/uploads/2014/11/nicholas-rym-spanked.gif?zoom=2.625&resize=396%2C222',
                           'http://spankgifs.com/wp-content/uploads/2015/12/m-m-spanlking.gif',
                           'https://57.media.tumblr.com/0782af14546e3f9d7b7eb23a3751339b/tumblr_mtj4kpi5XB1rcf0aqo1_400.gif',
                           'https://gaygifs.net/albums/2016/08/30/18/1/he-wants-him.gif',
                           'http://3.bp.blogspot.com/-nrsjmFKbuY8/US7wShcGqVI/AAAAAAAAdAc/MhleGSPE9Xs/s1600/tumblr_mfehy7B06R1qanl9mo1_500.gif',
                           'https://33.media.tumblr.com/e982e2e2aa267d728844dbee8fac2034/tumblr_nnfpi6UZMn1tk5yaho1_500.gif']

                image = random.choice(choices)

                embed = discord.Embed(description=spank.format(author,mention), colour=discord.Colour.blue())
                embed.set_image(url=image)
                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name
                mention = member.name

                spank = '**{0} spanks {1}s booty**'

                choices = ['https://images.sex.com/images/pinporn/2018/12/06/300/20313530.gif',
                           'https://78.media.tumblr.com/0cd26d3ab04e6cfbaa91f2c8c47bd1bd/tumblr_oxre9dg03m1w48g7zo1_500.gif',
                           'https://images.sex.com/images/pinporn/2016/06/20/620/15967749.gif',
                           'http://spankgifs.com/wp-content/uploads/2015/06/spanked.gif',
                           'https://images.sex.com/images/pinporn/2015/05/20/300/12005830.gif',
                           'https://i.pinimg.com/originals/e6/8d/7c/e68d7c7efa0e06b580b24ffaece80777.gif',
                           'https://images.sex.com/images/pinporn/2018/03/19/300/19265241.gif',
                           'https://3.bp.blogspot.com/-Jyfs29ETpAE/W-DSLBKXklI/AAAAAAAAwVs/75JH6OWJU_4hcRpGLzwBa-0Q_J0RJjeiQCLcBGAs/s640/000000.gif',
                           'http://spankgifs.com/wp-content/uploads/2019/07/Cunt-pain-reminds-you-of-your-place.gif',
                           'http://cutiepiessexyspankings.com/wp-content/uploads/2019/06/SPANKING-GIF-3.gif']

                image = random.choice(choices)

                embed = discord.Embed(description=spank.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)
                await ctx.send(embed=embed)

        elif author_gender == 'female':
            if mention_gender == 'female':
                author = ctx.message.author.name
                mention = member.name

                spank = '**{0} spanks {1}s booty**'

                choices = ['https://images.sex.com/images/pinporn/2018/01/15/300/18950853.gif',
                           'https://images.sex.com/images/pinporn/2015/07/25/300/13064053.gif',
                           'https://images.sex.com/images/pinporn/2019/02/08/300/20661173.gif',
                           'https://images.sex.com/images/pinporn/2015/09/10/300/13752941.gif',
                           'https://images.sex.com/images/pinporn/2017/11/15/300/18657851.gif',
                           'http://spankgifs.com/wp-content/uploads/2017/03/lesbian-couple-enjoy-spanking-over-the-couch.gif',
                           'http://spankgifs.com/wp-content/uploads/2018/01/lesbian-spanking-games.gif',
                           'http://24.media.tumblr.com/6e14e875fd593012eb2b9828bbad382c/tumblr_mk07urmcXQ1rjhn1to1_500.gif',
                           'https://images.sex.com/images/pinporn/2019/06/15/300/21326686.gif',
                           'http://spankgifs.com/wp-content/uploads/2016/08/fem-to-fem-hairbrush-spanking.gif',
                           'https://juicygif.com/albums/userpics/2017y/12/16/1/1/small_8516-hot-lesbian-spanking-action-d.gif',
                           'http://www.akceleratorbiznesu.eu/image/c6898511e364d53a4fbb5fbf815fa5dc.gif']

                image = random.choice(choices)

                embed = discord.Embed(description=spank.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)
                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name
                mention = member.name

                spank = '**{0} spanks {1}s booty**'

                choices = ['http://24.media.tumblr.com/tumblr_m4ceroZAmE1qmg17xo1_500.gif',
                           'http://78.media.tumblr.com/9c7b45eec99dfd3488ebe99426b1a320/tumblr_p5lquoqCGx1sg5ymbo1_500.gif',
                           'http://kesmifmonline.com/wp-content/pics/fm-spanking-tumblr-4.gif',
                           'https://78.media.tumblr.com/4c8f382f1c3d1e5fa3410ffc966dcea5/tumblr_ms8so93jcN1scehjfo1_400.gif',
                           'https://thespankingzone.files.wordpress.com/2016/05/n455ct.gif?w=700',
                           'https://2.bp.blogspot.com/--ncijD0BNdo/WbruViog93I/AAAAAAAAp7M/GOzgUH9W540vYZ2tIRwZ7giO8cJoGJvKACLcBGAs/s640/0000000000000000000000.gif',
                           'https://66.media.tumblr.com/69c36f129aaa85a9ad8f7f42b4665c42/tumblr_inline_p32b1px9Dj1s81k16_250.gif',
                           'http://strictwives.com/wp-content/uploads/2017/05/Christine-Justice-Spanks.gif',
                           'https://ourbottomsburn.files.wordpress.com/2018/10/70a72-fme032252bcopy.gif',
                           'https://s.smutty.com/media_smutty_2/s/h/a/m/b/shame85-wir6s-410bb1.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=spank.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)
                await ctx.send(embed=embed)

    @spank.error
    async def spank_error(self, ctx, error):

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to mention someone!')

            raise error

    @commands.command(aliases=['sucks'])
    @commands.is_nsfw()
    async def suck(self, ctx, member: discord.Member):
        """Sucks the person you mention"""
        author_gender = determineGender(ctx.author)
        mention_gender= determineGender(member)

        if author_gender == 'male':
            if mention_gender == 'male':

                author = ctx.message.author.name
                mention = member.name

                suck = '**{0} sucks {1} off!**'

                choices = ['https://i.gifer.com/3NwwL.gif',
                           'https://i.gifer.com/3NwwK.gif',
                           'https://i.gifer.com/3NwwJ.gif',
                           'https://i.gifer.com/3NwwI.gif',
                           'https://i.gifer.com/3NwwF.gif',
                           'https://i.gifer.com/3NwwG.gif',
                           'https://i.gifer.com/3NwwH.gif',
                           'https://i.gifer.com/3NwwT.gif',
                           'https://i.gifer.com/3NwwS.gif',
                           'https://i.gifer.com/3NwwR.gif',
                           'https://i.gifer.com/3NwwP.gif',
                           'https://i.gifer.com/3NwwM.gif',
                           'https://i.gifer.com/3NwwN.gif',
                           'https://i.gifer.com/3NwwH.gif']

                image = random.choice(choices)

                embed = discord.Embed(description=suck.format(author,mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name
                mention = member.name

                suck = '**{0} sucks on {1}!**'

                choices = ['http://juicygif.com/albums/userpics/2014y/05/17/3/1/5970-sucking-on-her-tits.gif',
                           'https://i1.wp.com/25.media.tumblr.com/tumblr_m4mklyBOVG1rqom82o1_500.gif',
                           'https://dl.phncdn.com/gif/4774841.gif',
                           'https://tse1.mm.bing.net/th?id=OGC.760f969d982748c34cfd79747531288b&',
                           'http://4.bp.blogspot.com/-I9A03UjGuTo/VmBgZYRb02I/AAAAAAAAI7E/0Dy7te817Nw/s1600/hot%2Bnipples%2Bsucking%2Bgif%2Bimages-4.gif',
                           'https://erogifs.net/upload/20150101231124uid.gif',
                           'https://marawaresearch.com/img/495812.gif',
                           'https://marawaresearch.com/img/fuck-suck-boobs-gif-5.jpg',
                           'https://s.smutty.com/media_smutty_2/m/o/o/n/b/moonspell-2j1ur-d69c0c.gif']

                image = random.choice(choices)

                embed = discord.Embed(description=suck.format(author,mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif author_gender == 'female':
            if mention_gender == 'male':
                author = ctx.message.author.name
                mention = member.name

                suck = '**{0} sucks {1} off**'

                choices = ['http://www.ict-peces.eu/image/a03e9dead09d04acc2483aa169ce0bb6.gif',
                           'https://hiqqu.com/files/www.hiqqu.xxx-3cdbae9a828883eff9db2d84bfd6bdd7150909c2.gif',
                           'http://www.reuni.eu/image/7109be8e2fc20c273166efeea87806d7.gif',
                           'http://teen-sex-photos.eu/wp-content/uploads/2014/06/tumblr_n6nlm2wPC01sqkolro1_400.gif',
                           'http://blowjobgif.net/albums/2016/04/22/12/1/beaublowjobtiful-women-does.gif',
                           'http://blowjobgif.net/albums/2018/06/21/1/1/porn-gifs-teen-sex-gifs-hot-teen-sex-gifs-1614.gif',
                           'http://blowjobgif.net/albums/2017/05/28/11/1/sex-541-hot-teen-porn-gifs.gif',
                           'http://blowjobgif.net/albums/2018/06/10/1/1/brunette-giving-a-great-blowjob-and-cumshots.gif',
                           'http://blowjobgif.net/albums/2018/05/20/3/1/pov-blowjob-cumshot-porn-gif.gif',
                           'http://blowjobgif.net/albums/2017/08/31/15/1/blowjob-brunette.gif',
                           'http://blowjobgif.net/albums/2015/08/31/9/1/blonde-teen-with-big-tits-giving-head.gif',
                           'http://blowjobgif.net/albums/2015/06/14/12/1/big-tits-blond-blowjob.gif',
                           'http://blowjobgif.net/albums/2015/11/04/22/1/german-with-big-tits-giving-blowjob.gif',
                           'http://blowjobgif.net/albums/2018/11/23/5/1/big-tits-blowjob.gif']

                image = random.choice(choices)

                embed = discord.Embed(description=suck.format(author,mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name
                mention = member.name

                suck = '**{0} sucks on {1}!**'

                choices = ['https://i.gifer.com/3NwwD.gif',
                           'https://i.gifer.com/3NwwC.gif',
                           'https://i.gifer.com/3NwwB.gif',
                           'https://i.gifer.com/3NwwA.gif',
                           'https://i.gifer.com/3Nww7.gif',
                           'https://i.gifer.com/3Nww8.gif',
                           'https://i.gifer.com/3Nww9.gif',
                           'https://i.gifer.com/3Nww6.gif',
                           'https://i.gifer.com/3Nww5.gif',
                           'https://i.gifer.com/3Nww0.gif',
                           'https://i.gifer.com/3Nww2.gif',
                           'https://i.gifer.com/3Nww4.gif',
                           'https://i.gifer.com/3Nww3.gif',
                           'https://i.gifer.com/3Nww1.gif',
                           'https://i.gifer.com/3Nwvz.gif']


                image = random.choice(choices)

                embed = discord.Embed(description=suck.format(author,mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

    @suck.error
    async def suck_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to mention someone!')

            raise error

    @commands.command()
    @commands.is_nsfw()
    async def anal(self, ctx, member: discord.Member):
        """Anal with the person you mention"""
        author_gender = determineGender(ctx.author)
        mention_gender = determineGender(member)

        if author_gender == 'male':
            if mention_gender == 'female':
                author = ctx.message.author.name
                mention = member.name

                anal = '**{0} fucks {1} in the ass**'

                choices = ['https://mediav-img.porn.com/secure/9d5f1db85ddfcc17f145d9fe9670d11c/sc/4/4362/4362279/source/001.gif',
                           'http://gifsgonewild.com/wp-content/uploads/2019/07/ezgif-4-cca09b249c06.gif',
                           'http://bestsexgif.com/wp-content/uploads/2016/08/Big-ass-lingerie-anal-fuck-hardcore.gif',
                           'https://geoprevi.xyz/img/215168.gif',
                           'http://www.daporngifs.com/gif/standing-anal.gif',
                           'https://i0.wp.com/morefunforyou.com/wp-content/uploads/2014/07/Blonde-White-Girl-Gets-Anal-withBlack-Cock-Mr-Anal.gif?resize=480%2C270',
                           'https://www.pornosexgif.org/wp-content/uploads/2015/12/kalite-anal-gif.gif',
                           'https://www.malina.xxx/wp-content/uploads/2018/12/Leah-Gotti-And-Her-Boss.2018-11-21-13_28_51.gif',
                           'https://www.x-zine.de/wp-content/uploads/2019/06/Anal28.gif',
                           'https://www.x-zine.de/wp-content/uploads/2019/06/anal3.gif',
                           'http://nudebabes.realnakedgirls.net/wp-content/uploads/2018/06/15280762618c4pl.gif',
                           'http://holyasshole.com/content/2018/09/anal-only_001-2.gif',
                           'https://www.tudelicias.net/wp-content/uploads/2017/03/gifs-de-sexo-anal-cacete-grande-e-grosso-02.gif',
                           'http://bestsexgif.com/wp-content/uploads/2015/02/Mischa-Brooks-anal-sex-gif.gif',
                           'https://www.pornosexgif.org/wp-content/uploads/2015/12/anal-720p-gif.gif',
                           'http://amateurhomeporn.net/wp-content/uploads/2012/08/photo-Amateur-Anal-Gif-871075187.gif']

                image = random.choice(choices)

                embed = discord.Embed(description=anal.format(author,mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name
                mention = member.name

                anal = '**{0} fucks {1} in the ass**'

                choices = ['http://gaygifs.net/albums/2016/08/30/22/1/going-deep.gif',
                           'http://gaygifs.net/albums/2016/08/31/0/1/getting-fucked-by-a-big-dick.gif',
                           'http://gaygifs.net/albums/2016/08/30/17/1/gay-hardcore-gay-sex.gif',
                           'http://gaygifs.net/albums/2016/08/30/18/1/hardcore-gay-sex-.gif',
                           'http://gaygifs.net/albums/2016/08/31/13/1/this-one-was-fun-to-do.gif',
                           'http://gaygifs.net/albums/2016/08/30/18/1/hard-dick-gay-sex-.gif',
                           'http://gaygifs.net/albums/2016/08/30/18/1/hard-gay-fuc.gif',
                           'http://gaygifs.net/albums/2016/08/31/4/1/ass-pounding.gif',
                           'http://gaygifs.net/albums/2016/08/30/17/1/tempimagetumblrpage-57c59dd23dc5e.gif',
                           'http://mendujour.net/wp-content/uploads/2019/04/Gay-anal-sex.gif',
                           'http://mendujour.net/wp-content/uploads/2019/06/Gay-anal-sex-1.gif',
                           'https://gifs.iloopit.net/resources/623dceae-9984-429c-a4fa-b4fea3a3ff26/converted.gif']

                image = random.choice(choices)

                embed = discord.Embed(description=anal.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif author_gender == 'female':
            if mention_gender == 'female':
                author = ctx.message.author.name
                mention = member.name

                anal = '**{0} fucks {1} in the ass**'

                choices = ['https://thumb-p7.xhcdn.com/a/Cg6tNTVPSGtP4g_5WkRClQ/000/123/736/257_1000.gif',
                           'http://vintage-calc.info/img/lesbian-nude-anal-sex-gif.gif',
                           'https://cdn1.hothag.com/media/gifs/1/1/lesbian-ass-fingering-1034-lesbian.gif',
                           'https://cdn1.hothag.com/media/gifs/1/1/anal-lesbian-with-hot-girls-4073-lesbian.gif',
                           'https://www.youpeg.com/wp-content/uploads/2019/06/Angelica-Ebbi-Krystal-Boyd-has-her-pussy-and-ass-played-with-by-a-girl.gif',
                           'https://i2.wp.com/morefunforyou.com/wp-content/uploads/2014/06/ashley-fires-strap-on-anal-lesbian-sex.gif?fit=480%2C270&ssl=1',
                           'http://vintage-calc.info/img/lesbian-nude-anal-sex-gif-2.jpg',
                           'http://gapemaster.com/wp-content/uploads/anal-strapon-lesbians-linda-samantha-gaping-1.gif',
                           'https://thumb-p4.xhcdn.com/a/Dd6_vcOLwt3uaaVTa8XCtA/000/132/330/174_1000.gif',
                           'http://megapornx.com/xxx/beautiful-lesbian-in-incredible-anal-toys-gif-photo.gif',
                           'https://49.media.tumblr.com/2726135f41cf5339a76d8adf64211521/tumblr_nexod3lJzG1semc6ko9_500.gif',
                           'https://cdn1.hothag.com/media/gifs/1/1/slut-fucks-her-ass-with-big-thick-dildo-3596-anal.gif',
                           'http://www.anima2011.eu/image/477962.gif']


                image = random.choice(choices)

                embed = discord.Embed(description=anal.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name
                mention = member.name

                anal = '**{0} gets fucked in the ass by {1}**'

                choices = ['https://www.niceandquite.com/wp-content/uploads/2015/06/RigidFluidHornshark.gif',
                           'https://i.imgur.com/2yZ6HnD.gif',
                           'http://www.daporngifs.com/gif/blonde-anal-ride.gif',
                           'https://static-ca-cdn.eporner.com/photos/145779.gif',
                           'https://25.media.tumblr.com/tumblr_mb3sgk4Hvj1rfgm3ro1_500.gif',
                           'https://fat.gfycat.com/HideousRichArmedcrab.gif',
                           'https://www.niceandquite.com/wp-content/uploads/2014/09/Sexy-ebony-Kiki-Minaj-gets-anal-peasure-by-white-cock.gif',
                           'https://juicygif.com/albums/userpics/2014y/05/21/23/1/9386-anal-riding.gif',
                           'https://i.imgur.com/zVSiu0b.gif',
                           'https://cdn5-images.motherlessmedia.com/images/C0B93B5.gif',
                           'https://i2.wp.com/171gifs.com/wp-content/uploads/2013/11/Bara-Brass-Riding-Big-Cock-Anal.gif',
                           'http://erogifs.net/upload/20160110210051uid.gif',
                           'http://www.daporngifs.com/gif/fast-anal-ride.gif',
                           'https://static-ca-cdn.eporner.com/photos/276566.gif',
                           'https://bestsexgif.com/wp-content/uploads/2015/02/Anal-dick-riding.gif',
                           'http://bestsexgif.com/wp-content/uploads/2015/03/anal-cock-riding-brazilian-ass.gif',
                           'https://www.niceandquite.com/wp-content/uploads/2015/05/ZanyDishonestArmednylonshrimp.gif',
                           'https://morefunforyou.com/wp-content/uploads/2014/12/isabella-de-santos-enter-her-exit-scene-02-anal-ass-riding.gif',
                           'https://juicygif.com/albums/userpics/2017y/08/11/16/1/small_4913-anal-riding.gif',
                           'http://sokol-tabor.info/pictures/shyla-stylez-anal-riding-gif-3.gif',
                           'http://fat.gfycat.com/GregariousAdoredBlacklemur.gif',
                           'http://www.daporngifs.com/gif/little-anal-ride.gif',
                           'https://cdn1.hothag.com/media/gifs/1/1/tori-riding-a-black-pole-2009-anal.gif',
                           'https://static-ca-cdn.eporner.com/photos/108154.gif',
                           'https://cdnio.luscious.net/166/lusciousnet_rfaptogifs_anal_riding__1935374002.gif']


                image = random.choice(choices)

                embed = discord.Embed(description=anal.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)
    @anal.error
    async def anal_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to mention someone!')

            raise error

    @commands.command(aliases=['doms', 'dominate', 'dominates'])
    @commands.is_nsfw()
    async def dom(self, ctx, member: discord.Member):
        """Dominates the person you mention"""
        author_gender = determineGender(ctx.author)
        mention_gender = determineGender(member)

        if author_gender == 'male':
            if mention_gender == 'female':
                author = ctx.message.author.name
                mention = member.name

                dom = '**{0} dominates {1}**'

                choices = ['https://i.gifer.com/3Nwy3.gif',
                           'https://i.gifer.com/3Nwy5.gif',
                           'https://i.gifer.com/3Nwy9.gif',
                           'https://i.gifer.com/3Nwy8.gif',
                           'https://i.gifer.com/3Nwy6.gif',
                           'https://i.gifer.com/3Nwy7.gif',
                           'https://i.gifer.com/3Nwy4.gif',
                           'https://i.gifer.com/3Nwy1.gif',
                           'https://i.gifer.com/3Nwy2.gif',
                           'https://i.gifer.com/3Nwxz.gif',
                           'https://i.gifer.com/3Nwxo.gif',
                           'https://i.gifer.com/3Nwy0.gif',
                           'https://i.gifer.com/3NwyA.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=dom.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name
                mention = member.name

                dom = '**{0} dominates {1}**'

                choices = ['https://i.gifer.com/3Nwxy.gif',
                           'https://i.gifer.com/3Nwxx.gif',
                           'https://i.gifer.com/3Nwxw.gif',
                           'https://i.gifer.com/3Nwxv.gif',
                           'https://i.gifer.com/3Nwxt.gif',
                           'https://i.gifer.com/3Nwxr.gif',
                           'https://i.gifer.com/3Nwxs.gif',
                           'https://i.gifer.com/3Nwxu.gif',
                           'https://i.gifer.com/3Nwxq.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=dom.format(author,mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif author_gender == 'female':
            if mention_gender == 'male':
                author = ctx.message.author.name
                mention = member.name

                dom = '**{0} dominates {1}**'

                choices = ['https://i.gifer.com/3NwyM.gif',
                           'https://i.gifer.com/3NwyL.gif',
                           'https://i.gifer.com/3NwyK.gif',
                           'https://i.gifer.com/3NwyJ.gif',
                           'https://i.gifer.com/3NwyI.gif',
                           'https://i.gifer.com/3NwyH.gif',
                           'https://i.gifer.com/3NwyG.gif',
                           'https://i.gifer.com/3NwyD.gif',
                           'https://i.gifer.com/3NwyE.gif',
                           'https://i.gifer.com/3NwyF.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=dom.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name
                mention = member.name

                dom = '**{0} dominates {1}**'

                choices = ['https://i.gifer.com/3Nwxm.gif',
                           'https://i.gifer.com/3Nwxn.gif',
                           'https://i.gifer.com/3Nwxp.gif',
                           'https://i.gifer.com/3Nwxj.gif',
                           'https://i.gifer.com/3Nwxl.gif',
                           'https://i.gifer.com/3Nwxk.gif',
                           'https://i.gifer.com/3Nwxf.gif',
                           'https://i.gifer.com/3Nwxg.gif',
                           'https://i.gifer.com/3Nwxh.gif',
                           'https://i.gifer.com/3Nwxi.gif',
                           'https://i.gifer.com/3Nwxc.gif',
                           'https://i.gifer.com/3Nwxd.gif',
                           'https://i.gifer.com/3Nwxe.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=dom.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)
    @dom.error
    async def dom_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to mention someone!')

            raise error

    @commands.command(aliases=['69'])
    @commands.is_nsfw()
    async def sixtynine(self, ctx, member: discord.Member):
        """69 command"""
        author_gender = determineGender(ctx.author)
        mention_gender = determineGender(member)

        if author_gender == 'male':
            if mention_gender == 'female':
                author = ctx.message.author.name
                mention = member.name

                sixtynine = '**{0} 69 with {1}**'

                choices = ['https://i.imgur.com/SA2tI0O.gif',
                           'https://i.imgur.com/b0m755A.gif',
                           'https://i.imgur.com/2NDCDPd.gif',
                           'https://i.imgur.com/FjCqFxb.gif',
                           'https://i.imgur.com/G65qszB.gif',
                           'https://i.imgur.com/ekACRB9.gif',
                           'https://i.imgur.com/DHuzCO8.gif',
                           'https://i.imgur.com/xrCy1no.gif',
                           'https://i.imgur.com/SEbsqa5.gif',
                           'https://i.imgur.com/taBIfnF.gif',
                           'https://i.imgur.com/tHQnHbN.gif',
                           'https://i.imgur.com/LSIwPRd.gif',
                           'https://i.imgur.com/YBeJcFF.gif',
                           'https://i.imgur.com/SFWBZb5.gif',
                           'https://i.imgur.com/U3LDNCF.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=sixtynine.format(author,mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name
                mention = member.name

                sixtynine = '**{0} 69 with {1}**'

                choices = ['https://i.imgur.com/dZ8KivV.gif',
                           'https://i.imgur.com/ezM4WDa.gif',
                           'https://i.imgur.com/BFsIQAB.gif',
                           'https://i.imgur.com/ejA8v59.gif',
                           'https://i.imgur.com/YPoJTU4.gif',
                           'https://i.imgur.com/yLl6EYe.gif',
                           'https://i.imgur.com/mHvGlKE.gif',
                           'https://i.imgur.com/rUfo3rN.gif',
                           'https://i.imgur.com/lznLqdb.gif',
                           'https://i.imgur.com/cVL44v9.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=sixtynine.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif author_gender == 'female':
            if mention_gender == 'male':
                author = ctx.message.author.name
                mention = member.name

                sixtynine = '**{0} 69 with {1}**'

                choices = ['https://i.imgur.com/SA2tI0O.gif',
                           'https://i.imgur.com/b0m755A.gif',
                           'https://i.imgur.com/2NDCDPd.gif',
                           'https://i.imgur.com/FjCqFxb.gif',
                           'https://i.imgur.com/G65qszB.gif',
                           'https://i.imgur.com/ekACRB9.gif',
                           'https://i.imgur.com/DHuzCO8.gif',
                           'https://i.imgur.com/xrCy1no.gif',
                           'https://i.imgur.com/SEbsqa5.gif',
                           'https://i.imgur.com/taBIfnF.gif',
                           'https://i.imgur.com/tHQnHbN.gif',
                           'https://i.imgur.com/LSIwPRd.gif',
                           'https://i.imgur.com/YBeJcFF.gif',
                           'https://i.imgur.com/SFWBZb5.gif',
                           'https://i.imgur.com/U3LDNCF.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=sixtynine.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name
                mention = member.name

                sixtynine = '**{0} 69 with {1}**'

                choices = ['https://i.imgur.com/ThKCcX1.gif',
                           'https://i.imgur.com/1KiRsHc.gif',
                           'https://i.imgur.com/RlSAxWJ.gif',
                           'https://i.imgur.com/qmke8BM.gif',
                           'https://i.imgur.com/rdoOJc1.gif',
                           'https://i.imgur.com/NdSak4f.gif',
                           'https://i.imgur.com/Qd561oS.gif',
                           'https://i.imgur.com/S37Lck6.gif',
                           'https://i.imgur.com/jCt6gam.gif',
                           'https://i.imgur.com/ByjjDAy.gif',
                           'https://i.imgur.com/YEcn9bs.gif',
                           'https://i.imgur.com/aLTv6uB.gif',
                           'https://i.imgur.com/NTyoNKv.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=sixtynine.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

    @sixtynine.error
    async def sixtynine_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to mention someone!')

            raise error

    @commands.command(aliases=['cream'])
    @commands.is_nsfw()
    async def creampie(self, ctx, member: discord.Member):
        """Creampie command"""
        author_gender = determineGender(ctx.author)
        mention_gender = determineGender(member)

        if author_gender == 'male':
            if mention_gender == 'female':
                author = ctx.message.author.name
                mention = member.name

                sixtynine = '**{0} creampies {1}**'

                choices = ['https://i.imgur.com/f92tc1G.gif',
                           'https://i.imgur.com/wNOz1Kq.gif',
                           'https://i.imgur.com/zCht4bl.gif',
                           'https://i.imgur.com/4Fu1tBC.gif',
                           'https://i.imgur.com/3pqyJ83.gif',
                           'https://i.imgur.com/JjSbfio.gif',
                           'https://i.imgur.com/JODYD5A.gif',
                           'https://i.imgur.com/V9bfKyJ.gif',
                           'https://i.imgur.com/ML2ZNkp.gif',
                           'https://i.imgur.com/KL5Kzz5.gif',
                           'https://i.imgur.com/eJFjund.gif',
                           'https://i.imgur.com/rUSkgYw.gif',
                           'https://i.imgur.com/6UrAIhC.gif',
                           'https://i.imgur.com/CgKpQz7.gif',
                           'https://i.imgur.com/Lmr3cv2.gif',
                           'https://i.imgur.com/SsBqRLT.gif',
                           'https://i.imgur.com/F8YuNs4.gif',
                           'https://i.imgur.com/L2TtXFU.gif',
                           'https://i.imgur.com/Nnahwh2.gif',
                           'https://i.imgur.com/Hh3sAA0.gif',
                           'https://i.imgur.com/u4yxCmx.gif',
                           'https://i.imgur.com/oB9Swdh.gif',
                           'https://i.imgur.com/SsNBok3.gif',
                           'https://i.imgur.com/cH14eNJ.gif',
                           'https://i.imgur.com/2osxNjV.gif',
                           'https://i.imgur.com/Zu48qr9.gif',
                           'https://i.imgur.com/hzQK4DT.gif',
                           'https://i.imgur.com/4hIs3lV.gif',
                           'https://i.imgur.com/DLCQZ1t.gif',
                           'https://i.imgur.com/WStdajj.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=sixtynine.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name
                mention = member.name

                sixtynine = '**{0} creampies {1}**'

                choices = ['https://i.imgur.com/QzVs0zA.gif',
                           'https://i.imgur.com/b6uSmBw.gif',
                           'https://i.imgur.com/P1jJL5Z.gif',
                           'https://i.imgur.com/vgS6Guw.gif',
                           'https://i.imgur.com/iBSXKjT.gif',
                           'https://i.imgur.com/qqReaY3.gif',
                           'https://i.imgur.com/GOwpKBc.gif',
                           'https://i.imgur.com/JsBYwLP.gif',
                           'https://i.imgur.com/xcrOGQC.gif',
                           'https://i.imgur.com/BazoUno.gif',
                           'https://i.imgur.com/vhASHVp.gif',
                           'https://i.imgur.com/Zphc2Yn.gif',
                           'https://i.imgur.com/hC1bfXm.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=sixtynine.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif author_gender == 'female':
            if mention_gender == 'male':
                author = ctx.message.author.name
                mention = member.name

                sixtynine = '**{0} gets creampie from {1}**'

                choices = ['https://i.imgur.com/f92tc1G.gif',
                           'https://i.imgur.com/wNOz1Kq.gif',
                           'https://i.imgur.com/zCht4bl.gif',
                           'https://i.imgur.com/4Fu1tBC.gif',
                           'https://i.imgur.com/3pqyJ83.gif',
                           'https://i.imgur.com/JjSbfio.gif',
                           'https://i.imgur.com/JODYD5A.gif',
                           'https://i.imgur.com/V9bfKyJ.gif',
                           'https://i.imgur.com/ML2ZNkp.gif',
                           'https://i.imgur.com/KL5Kzz5.gif',
                           'https://i.imgur.com/eJFjund.gif',
                           'https://i.imgur.com/rUSkgYw.gif',
                           'https://i.imgur.com/6UrAIhC.gif',
                           'https://i.imgur.com/CgKpQz7.gif',
                           'https://i.imgur.com/Lmr3cv2.gif',
                           'https://i.imgur.com/SsBqRLT.gif',
                           'https://i.imgur.com/F8YuNs4.gif',
                           'https://i.imgur.com/L2TtXFU.gif',
                           'https://i.imgur.com/Nnahwh2.gif',
                           'https://i.imgur.com/Hh3sAA0.gif',
                           'https://i.imgur.com/u4yxCmx.gif',
                           'https://i.imgur.com/oB9Swdh.gif',
                           'https://i.imgur.com/SsNBok3.gif',
                           'https://i.imgur.com/cH14eNJ.gif',
                           'https://i.imgur.com/2osxNjV.gif',
                           'https://i.imgur.com/Zu48qr9.gif',
                           'https://i.imgur.com/hzQK4DT.gif',
                           'https://i.imgur.com/4hIs3lV.gif',
                           'https://i.imgur.com/DLCQZ1t.gif',
                           'https://i.imgur.com/WStdajj.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=sixtynine.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name
                mention = member.name

                sixtynine = '**{0} creampies {1}**'

                choices = ['http://porngifmag.com/content/2016/08/agnes-strapon-creampie-after-the-breakfast_008.gif',
                           'https://barris4congress.com/img/lick-cum-from-ass-3.gif',
                           'https://i.imgur.com/7NMAMrk.gif',
                           'https://i.imgur.com/4zAQA6c.gif',
                           'https://i.imgur.com/xHFX1vQ.gif',
                           'https://i.imgur.com/JZO7n1B.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=sixtynine.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

    @creampie.error
    async def creampie_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to mention someone!')

            raise error

    @commands.command(aliases=['licks'])
    @commands.is_nsfw()
    async def lick(self, ctx, member: discord.Member):
        """Licks the member you mention"""
        author_gender = determineGender(ctx.author)
        mention_gender = determineGender(member)

        if author_gender == 'male':
            if mention_gender == 'female':
                author = ctx.message.author.name
                mention = member.name

                lick = '**{0} licks {1}**'

                choices = ['https://i.imgur.com/zuq4KwY.gif',
                           'https://i.imgur.com/7AVVv97.gif',
                           'https://i.imgur.com/1qBKwHW.gif',
                           'https://i.imgur.com/VJbL6Pn.gif',
                           'https://i.imgur.com/kKQnLYi.gif',
                           'https://i.imgur.com/KuxDdoW.gif',
                           'https://i.imgur.com/lOS3CbK.gif',
                           'https://i.imgur.com/hjnPBhs.gif',
                           'https://i.imgur.com/5eTWPzP.gif',
                           'https://i.imgur.com/TbekPiB.gif',
                           'https://i.imgur.com/sw40J09.gif',
                           'https://i.imgur.com/de81nde.gif',
                           'https://i.imgur.com/F2afwUW.gif',
                           'https://i.imgur.com/6WIXSdz.gif',
                           'https://i.imgur.com/OWmCCk5.gif',
                           'https://i.imgur.com/mP8oY8W.gif',
                           'https://i.imgur.com/ccyWRxg.gif',
                           'https://i.imgur.com/OsBrrtI.gif',
                           'https://i.imgur.com/6MZRwBY.gif',
                           'https://i.imgur.com/KncvJ93.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=lick.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name
                mention = member.name

                lick = '**{0} licks {1}**'

                choices = ['https://i.imgur.com/Zreq0I9.gif',
                           'https://i.imgur.com/9EY5kmX.gif',
                           'https://i.imgur.com/xqXBsrz.gif',
                           'https://i.imgur.com/RKeKOg4.gif',
                           'https://i.imgur.com/BnAdCRr.gif',
                           'https://i.imgur.com/r3vxz3u.gif',
                           'https://i.imgur.com/ufTQoDy.gif',
                           'https://i.imgur.com/lGicNRW.gif',
                           'https://i.imgur.com/R9MPbh8.gif',
                           'https://i.imgur.com/PbhSohm.gif',
                           'https://i.imgur.com/sC0tEKN.gif',
                           'https://i.imgur.com/8VuBuM5.gif',
                           'https://i.imgur.com/x9H3MAT.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=lick.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif author_gender == 'female':
            if mention_gender == 'male':
                author = ctx.message.author.name
                mention = member.name

                lick = '**{0} licks {1}**'

                choices = ['https://i.imgur.com/XQv9mMi.gif',
                           'https://i.imgur.com/R721Cu9.gif',
                           'https://i.imgur.com/lnLfDjr.gif',
                           'https://i.imgur.com/wmsmjZN.gif',
                           'https://i.imgur.com/sDWd4sG.gif',
                           'https://i.imgur.com/2vbdUIb.gif',
                           'https://i.imgur.com/cMLgK7Q.gif',
                           'https://i.imgur.com/twhdqlX.gif',
                           'https://i.imgur.com/EuHVEHT.gif',
                           'https://i.imgur.com/VyniV0V.gif',
                           'https://i.imgur.com/cuL1Bmo.gif',
                           'https://i.imgur.com/cNTCt2f.gif',
                           'https://i.imgur.com/gtMQV5K.gif',
                           'https://i.imgur.com/h1LwM7H.gif',
                           'https://i.imgur.com/AZg0Lkj.gif',
                           'https://i.imgur.com/LSJCxQO.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=lick.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name
                mention = member.name

                lick = '**{0} licks {1}**'

                choices = ['https://i.imgur.com/F0oEUW0.gif',
                           'https://i.imgur.com/djXaJ30.gif',
                           'https://i.imgur.com/nG2T3dE.gif',
                           'https://i.imgur.com/RHS2b4k.gif',
                           'https://i.imgur.com/beaW8yE.gif',
                           'https://i.imgur.com/57hUfQJ.gif',
                           'https://i.imgur.com/FeTKvd3.gif',
                           'https://i.imgur.com/3KfOTdI.gif',
                           'https://i.imgur.com/FNFK7Cn.gif',
                           'https://i.imgur.com/L6vM23M.gif',
                           'https://i.imgur.com/DWuCgGY.gif',
                           'https://i.imgur.com/pXiIiKr.gif',
                           'https://i.imgur.com/FV5SUTW.gif',
                           'https://i.imgur.com/SFcuA3e.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=lick.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

    @lick.error
    async def lick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need to mention someone!')

            raise error

    @commands.command(aliases=['tiddies', 'tiddy'])
    @commands.is_nsfw()
    async def tits(self, ctx):
        tits = '**Here is some tiddies for ya**'

        choices = ['https://cdn.discordapp.com/attachments/613870605489537097/629860411155677204/image0.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/629860257698414603/image1.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/629860259225272328/image0.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/629860273905467392/image1.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/629860274446401537/image0.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/629860300132450314/image1.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/629860301935869952/image0.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/629860304137748501/image1.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/629860306683953152/image0.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/629860314569244692/image1.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/629860315080818722/image0.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/629860339902578717/image1.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/629860341052080128/image0.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/629860359125204993/image1.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/629860359661944863/image0.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/629860367560081438/image1.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/629860368696606740/image0.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/629860393648390194/image1.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/629860394663673866/image0.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/629860402330730506/image1.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/629860403169460224/image0.gif',
                   'https://cdn.discordapp.com/attachments/613870605489537097/629860410207502364/image1.gif',
                   'https://i.imgur.com/rpt4TE8.gif',
                   'https://cdn.discordapp.com/attachments/522571237357125633/560628775080034314/image0.gif',
                   'https://cdn.boob.bot/boobs/8000E578.gif',
                   'https://cl.phncdn.com/gif/921691.gif',
                   'https://dl.phncdn.com/gif/963111.gif',
                   'https://cl.phncdn.com/gif/6805451.gif',
                   'https://i.imgur.com/UBlOpTZ.gif',
                   'https://i.imgur.com/Ok24HpH.gif',
                   'https://i.imgur.com/MJFl8GR.gif',
                   'https://i.imgur.com/MCYfXpP.gif']
        image = random.choice(choices)

        embed = discord.Embed(description=tits, colour=discord.Colour.blue())
        embed.set_image(url=image)

        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_nsfw()
    async def tease(self, ctx, member: discord.Member):
        author_gender = determineGender(ctx.author)
        mention_gender = determineGender(member)
        if author_gender == 'male':
            if mention_gender == 'female':
                author = ctx.message.author.name
                mention = member.name

                tease = '**{0} teases {1}**'

                choices = ['http://www.juicygif.com/albums/userpics/2014y/12/27/14/1/6210-kiss-me-while-i-tease-your-little-clit.gif',
                           'http://www.juicygif.com/albums/userpics/2014y/12/27/14/1/6210-kiss-me-while-i-tease-your-little-clit.gif',
                           'https://media1.tenor.com/images/ca3abfde78278629f47d47af05b92585/tenor.gif?itemid=14561607',
                           'https://media1.tenor.com/images/f7ce15bea841b01faa1b308e63fd7d1f/tenor.gif?itemid=14337427',
                           'https://media1.tenor.com/images/44edd082323148592a0e0adede012c9b/tenor.gif?itemid=9380810',
                           'https://i.imgur.com/QEbc16D.gif',
                           'https://i.imgur.com/9OSqOlR.gif',
                           'https://i.imgur.com/YjqKCOL.gif',
                           'https://i.imgur.com/CuTlsxw.gif',
                           'https://i.imgur.com/4wlSPUG.gif',
                           'https://i.imgur.com/DSuWEda.gif',
                           'https://i.imgur.com/RmBBf3N.gif',
                           'https://i.imgur.com/I6QxD4n.gif'
                           ]
                image = random.choice(choices)
                embed = discord.Embed(description=tease.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name
                mention = member.name

                tease = '**{0} teases {1}**'

                choices = ['https://i.imgur.com/C55RcTh.gif',
                           'https://i.imgur.com/WCCkb1A.gif',
                           'https://i.imgur.com/yk2vw25.gif',
                           'https://i.imgur.com/UynKWEG.gif',
                           'https://i.imgur.com/boWzYIQ.gif',
                           'https://i.imgur.com/psYq6ph.gif',
                           'https://i.imgur.com/j5JuOcO.gif',
                           'https://i.imgur.com/isFZwiP.gif']
                image = random.choice(choices)
                embed = discord.Embed(description=tease.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif author_gender == 'female':
            if mention_gender == 'male':
                author = ctx.message.author.name
                mention = member.name

                tease = '**{0} teases {1}**'

                choices = ['https://i.imgur.com/45JZIpI.gif',
                           'https://i.imgur.com/1FTmuEY.gif',
                           'https://i.imgur.com/myMO6EE.gif',
                           'https://i.imgur.com/88hBTTa.gif',
                           'https://i.imgur.com/I5VAheR.gif',
                           'https://i.imgur.com/eDohWaM.gif',
                           'https://i.imgur.com/Ti6U7cj.gif',
                           'https://i.imgur.com/xe57XN4.gif',
                           'https://i.imgur.com/DvxURsE.gif',
                           'https://i.imgur.com/VPTdWcS.gif',
                           'https://i.imgur.com/4PJGH5E.gif',
                           'https://i.imgur.com/Est3gYi.gif',
                           'https://i.imgur.com/mf3i1ob.gif',
                           'https://i.imgur.com/mLSTiFj.gif',
                           'https://i.imgur.com/w1t7WYG.gif',
                           'https://i.imgur.com/GNvMTFs.gif'
                           ]
                image = random.choice(choices)
                embed = discord.Embed(description=tease.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name
                mention = member.name

                tease = '**{0} teases {1}**'

                choices = ['https://i.imgur.com/lVKVncQ.gif',
                           'https://i.imgur.com/8yzOzWL.gif',
                           'https://i.imgur.com/KZozR4a.gif',
                           'https://i.imgur.com/F24pQb4.gif',
                           'https://i.imgur.com/9NlzPrW.gif',
                           'https://i.imgur.com/ZuMTpK5.gif',
                           'https://i.imgur.com/TLISVwP.gif',
                           'https://i.imgur.com/IhC9GwT.gif',
                           'https://i.imgur.com/KR8S224.gif',
                           'https://i.imgur.com/r3JBtIL.gif',
                           'https://i.imgur.com/Ez8eDIS.gif',
                           'https://i.imgur.com/EsSGLqt.gif',
                           'https://i.imgur.com/YWVJHZw.gif',
                           'https://i.imgur.com/S5VnLid.gif',
                           'https://i.imgur.com/LW4WGbo.gif']
                image = random.choice(choices)
                embed = discord.Embed(description=tease.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)


    @commands.command()
    @commands.is_nsfw()
    async def finger(self, ctx, member: discord.Member):
        author_gender = determineGender(ctx.author)
        mention_gender = determineGender(member)

        if author_gender == 'male':
            if mention_gender == 'female':
                author = ctx.message.author.name
                mention = member.name

                finger = '**{0} fingers {1}**'
                choices = ['http://gifsgonewild.com/wp-content/uploads/2019/06/ezgif-2-af51b7354c33.gif',
                           'https://i.imgur.com/9CgmNzD.gif',
                           'https://i.imgur.com/prL0gJV.gif',
                           'https://i.imgur.com/A1n75nE.gif',
                           'https://i.imgur.com/jazK311.gif',
                           'https://i.imgur.com/SYjPFIo.gif',
                           'https://i.imgur.com/8bg9DDt.gif',
                           'https://i.imgur.com/PsqRVv4.gif',
                           'https://i.imgur.com/9bIzccy.gif',
                           'https://i.imgur.com/44i8wIA.gif',
                           'https://i.imgur.com/svsazqV.gif',
                           'https://i.imgur.com/iIid4yg.gif',
                           'https://i.imgur.com/66qAGGL.gif',
                           'https://i.imgur.com/YhQu4Vj.gif',
                           'https://i.imgur.com/e0rz2pk.gif',
                           'https://i.imgur.com/Oz4g5BW.gif',
                           'https://i.imgur.com/7Fr6oFs.gif',
                           'https://i.imgur.com/CuerZUT.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=finger.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name
                mention = member.name

                finger = '**{0} fingers {1}**'
                choices = ['https://66.media.tumblr.com/3fc5e5aede749fe34fcbb07ba5ee19b8/tumblr_mxj5iizgpG1qf2a5vo1_r2_540.gif',
                           'https://i.imgur.com/cXABGgS.gif',
                           'https://i.imgur.com/cG2zv3f.gif',
                           'https://i.imgur.com/EDSDtnr.gif',
                           'https://i.imgur.com/4AroUSl.gif',
                           'https://i.imgur.com/nhowCRo.gif',
                           'https://i.imgur.com/qRx6mpa.gif',
                           'https://i.imgur.com/bXf4NYh.gif',
                           'https://i.imgur.com/wDSGz9v.gif',
                           'https://i.imgur.com/RWAA8m5.gif',
                           'https://i.imgur.com/3RnteI6.gif'
                           ]
                image = random.choice(choices)

                embed = discord.Embed(description=finger.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif author_gender == 'female':
            if mention_gender == 'male':
                author = ctx.message.author.name
                mention = member.name

                finger = '**{0} fingers {1}**'
                choices = ['https://49.media.tumblr.com/280ce1aa102df8a42d87175d8388f9bc/tumblr_nqx7t1nKF81snzlxso1_400.gif',
                           'https://i.imgur.com/cEl2pBq.gif',
                           'https://i.imgur.com/nAsqe56.gif',
                           'https://i.imgur.com/vMOGT97.gif',
                           'https://i.imgur.com/kxYKtnw.gif',
                           'https://i.imgur.com/jCT58Kt.gif',
                           'https://i.imgur.com/LLMUip4.gif',
                           'https://i.imgur.com/XtwtZ5L.gif',
                           'https://i.imgur.com/9Rkbd0D.gif',
                           'https://i.imgur.com/Uyw9r9I.gif',
                           'https://i.imgur.com/FiR7uEW.gif',
                           'https://i.imgur.com/0MRK2LJ.gif',
                           'https://i.imgur.com/RNJYpvX.gif',
                           'https://i.imgur.com/8xBX1Nj.gif'
                           ]
                image = random.choice(choices)

                embed = discord.Embed(description=finger.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name
                mention = member.name

                finger = '**{0} fingers {1}**'
                choices = ['http://porngif.org/wp-content/uploads/2014/01/4579.gif',
                           'https://i.imgur.com/mRDonle.gif',
                           'https://i.imgur.com/NUwxaYj.gif',
                           'https://i.imgur.com/vW0dr4m.gif',
                           'https://i.imgur.com/ExKBNf8.gif',
                           'https://i.imgur.com/gWW6Gbe.gif',
                           'https://i.imgur.com/RxhB9LS.gif',
                           'https://i.imgur.com/cjbsw51.gif',
                           'https://i.imgur.com/B9Rv80L.gif',
                           'https://i.imgur.com/Ijjw6Wd.gif',
                           'https://i.imgur.com/6Dl63Go.gif',
                           'https://i.imgur.com/soZBtKJ.gif',
                           'https://i.imgur.com/BaE48IN.gif',
                           'https://i.imgur.com/n1VsPZR.gif',
                           'https://i.imgur.com/G32krR2.gif'
                           ]
                image = random.choice(choices)

                embed = discord.Embed(description=finger.format(author, mention), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

    @finger.error
    async def finger_error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send('**Oops you did something wrong**')

        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('**You gotta mention someone!**')

        raise error


def setup(client):
    client.add_cog(Nsfw(client))


