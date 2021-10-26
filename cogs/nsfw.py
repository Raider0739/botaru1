import discord
import random
import asyncio
from discord.ext import commands
from discord.ext.commands import Greedy
from discord import Member
import asyncpraw

reddit = asyncpraw.Reddit(client_id="MmkzYn1FZ7AKHA",
                     client_secret="7lkbJd3zwE77zwypLjdzIZZatbCMww",
                     user_agent="botarunsfw",
                     username="botarudev",
                     password="u1t2k3u4")

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

class Nsfw(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group()
    async def nsfw(self, ctx):

        user = ctx.author

        if ctx.invoked_subcommand is None:
            em = discord.Embed(colour=discord.Colour.blue())
            em.set_author(name='Nsfw Command List')
            em.add_field(name='Commands',
                         value="""**fuck, spank, suck, anal, dom, 69, creampie, lick, tits, tease, finger, booty, 
                               bite, massage, cum, collar, twerk, thicc, choke, sub, ride, threesome,
                                deepthroat, doggy, facial, brat, porn, hentai, missionary, public, ropeplay(bondage), petplay, whip, punish, swallow, masturbate, titfuck, shower sex, 
                                cuddlefuck**""", inline=False)

            em.set_footer(text='Channel must be NSFW to use the commands!')
            emb = discord.Embed(colour=discord.Colour.blue())
            emb.set_author(name='Nsfw Command List')
            emb.add_field(name='Commands',
                         value="""**fuck, spank, suck, anal, dom, 69, creampie, lick, tits, tease, finger, booty, 
                               bite, massage, cum, collar, twerk, thicc, choke, sub, ride, threesome,
                                deepthroat, doggy, facial, brat, porn, hentai, missionary, public, ropeplay(bondage), petplay, whip, punish, swallow, masturbate, titfuck, shower sex,
                                cuddlefuck**""", inline=False)

            emb.set_footer(text='Channel must be NSFW to use the commands!, Your dms are closed...')
            try:
                await ctx.send('**Trying to send a list of NSFW commands in your DMs**')
                await user.send(embed=em)
            except Exception:
                await ctx.send(embed=emb)
    
    @nsfw.command(name="masturbate")
    async def _masturbate(self, ctx):
        embed = discord.Embed(description=f"**Example use: $masturbate @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name="swallow")
    async def _swallow(self, ctx):
        embed = discord.Embed(description=f"**Example use: $swallow @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name="punish")
    async def _punish(self, ctx):
        embed = discord.Embed(description=f"**Example use: $punish @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name="whip")
    async def _whip(self, ctx):
        embed = discord.Embed(description=f"**Example use: $whip @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='bondage')
    async def _bondage(self, ctx):
        embed = discord.Embed(description=f"**Example use: $bondage @User#6969 or $ropeplay @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='petplay')
    async def _petplay(self, ctx):
        embed = discord.Embed(description=f"**Example use: $petplay @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='fuck')
    async def _fuck(self, ctx):
        embed = discord.Embed(description=f"**Example use: $fuck @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='spank')
    async def _spank(self, ctx):
        embed = discord.Embed(description=f"**Example use: $spank @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='suck')
    async def _suck(self, ctx):
        embed = discord.Embed(description=f"**Example use: $suck @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='anal')
    async def _anal(self, ctx):
        embed = discord.Embed(description=f"**Example use: $anal @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='dom')
    async def _dom(self, ctx):
        embed = discord.Embed(description=f"**Example use: $dom @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='69')
    async def _69(self, ctx):
        embed = discord.Embed(description=f"**Example use: $69 @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='creampie')
    async def _creampie(self, ctx):
        embed = discord.Embed(description=f"**Example use: $creampie @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='lick')
    async def _lick(self, ctx):
        embed = discord.Embed(description=f"**Example use: $lick @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='tits')
    async def _tits(self, ctx):
        embed = discord.Embed(description=f"**Example use: $tits**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='tease')
    async def _tease(self, ctx):
        embed = discord.Embed(description=f"**Example use: $tease @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='finger')
    async def _finger(self, ctx):
        embed = discord.Embed(description=f"**Example use: $finger @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='booty')
    async def _booty(self, ctx):
        embed = discord.Embed(description=f"**Example use: $booty**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='bite')
    async def _bite(self, ctx):
        embed = discord.Embed(description=f"**Example use: $bite @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='massage')
    async def _massage(self, ctx):
        embed = discord.Embed(description=f"**Example use: $massage @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='cum')
    async def _cum(self, ctx):
        embed = discord.Embed(description=f"**Example use: $cum @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='collar')
    async def _collar(self, ctx):
        embed = discord.Embed(description=f"**Example use: $collar @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='twerk')
    async def _twerk(self,ctx):
        embed = discord.Embed(description=f"**Example use: $twerk @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='thicc')
    async def _thicc(self, ctx):
        embed = discord.Embed(description=f"**Example use: $thicc**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='choke')
    async def _choke(self, ctx):
        embed = discord.Embed(description=f"**Example use: $choke @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='sub')
    async def _sub(self, ctx):
        embed = discord.Embed(description=f"**Example use: $sub @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='ride')
    async def _ride(self, ctx):
        embed = discord.Embed(description=f"**Example use: $ride @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='threesome')
    async def _threesome(self, ctx):
        embed = discord.Embed(description=f"**Example use: $threesome @User#6969 @User#0420**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='deepthroat')
    async def _deepthroat(self, ctx):
        embed = discord.Embed(description=f"**Example use: $deepthroat @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='doggy')
    async def _doggy(self, ctx):
        embed = discord.Embed(description=f"**Example use: $doggy @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='facial')
    async def _facial(self, ctx):
        embed = discord.Embed(description=f"**This is a custom command to buy your own check $patreon\nExample use: $facial @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='brat')
    async def _brat(self, ctx):
        embed = discord.Embed(
            description=f"**This is a custom command to buy your own check $patreon\nExample use: $brat @User#6969 or $brat**",
            colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='porn')
    async def _porn(self, ctx):
        embed = discord.Embed(
            description=f"**Example use: $porn**",
            colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='hentai')
    async def _hentai(self, ctx):
        embed = discord.Embed(
            description=f"**Example use: $hentai**",
            colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='missionary')
    async def _missionary(self, ctx):
        embed = discord.Embed(
            description=f"**Example use: $missionary @User#6969**",
            colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @nsfw.command(name='public')
    async def _public(self, ctx):
        embed = discord.Embed(
            description=f"**Example use: $public @User#6969 or $public**",
            colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @commands.command(aliases=['fucks', 'bang', 'root'])
    @commands.is_nsfw()
    async def fuck(self, ctx, message=None):
        """Fucks the user you mention"""
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author_gender = determineGender(ctx.author)
        if mentions == message:
            if message == None:
                embed = discord.Embed(description=f"**You can't fuck nothing you horni dumbo\nExample use: $fuck @User#6969**", colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                if author_gender == 'male':
                    author = ctx.message.author.name

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
                           'https://i.imgur.com/ZYGTQlX.gif',
                           'https://www.youpeg.com/wp-content/uploads/2019/02/gallery-the-worlds-hottest-gianna-dior-xxx-porn-gif-gallery-syber-pussy-xxx-forums-porn-videos-x-1550160633c8p4l.gif',
                           'https://hotporngifs.eu/wp-content/uploads/2018/07/tumblr_ovlpmn6KtD1tduf00o1_400.gif',
                           'https://hotporngifs.eu/wp-content/uploads/2018/05/tumblr_otj1dxn4yq1sg1lgao1_500.gif',
                           'https://hotporngifs.eu/wp-content/uploads/2018/12/tumblr_pgk4v0rSGC1rat4opo1_500-450x635.gif',
                           'http://i.imgur.com/DDso5m8.gif',
                           'http://www.reuni.eu/image/417862.gif',
                           'https://24.media.tumblr.com/073577e9b34d44bc2a13bf534ebcca38/tumblr_mipo08ImUU1qbh1xjo1_500.gif',
                           'https://sluterest.com/wp-content/uploads/2015/06/juicy-fuck-office.gif',
                           'http://www.coaching-et-formation-coaching.eu/image/269c5c7998a9443f1310cd063783b55c.gif',
                           'http://huntingdonshirecricket.com/images/223199.gif',
                           'https://i.imgur.com/B2HlgWs.gif',
                           'https://i.imgur.com/9FkZsAD.gif',
                           'https://i.imgur.com/pEts2Qq.gif',
                           'https://i.imgur.com/gFLjKK5.gif',
                           'https://i.imgur.com/0NfK8UE.gif',
                           'https://i.imgur.com/1L6Cbmt.gif',
                           'https://i.imgur.com/2xaMyW3.gif',
                           'https://i.imgur.com/x0anhio.gif',
                           'https://i.imgur.com/e2KWlA5.gif',
                           'https://i.imgur.com/NfXSD3F.gif',
                           'https://i.imgur.com/Ldsdjld.gif',
                           'https://i.imgur.com/oRYeQ3h.gif',
                           'https://i.imgur.com/0rbmTGv.gif',
                           'https://i.imgur.com/KRHMCLZ.gif',
                           'https://i.imgur.com/w57Ankv.gif',
                           'https://i.imgur.com/jh288pa.gif',
                           'https://i.imgur.com/aCwm2n1.gif',
                           'https://i.imgur.com/g5CpZqq.gif',
                           'https://i.imgur.com/RhcqXDC.gif',
                           'https://i.imgur.com/N2kpuPJ.gif',
                           'https://i.imgur.com/bHmgAxS.gif',
                           'https://i.imgur.com/tZMorlV.gif',
                           'https://i.imgur.com/wLS5PBn.gif',
                           'https://i.imgur.com/ROObS6Z.gif',
                           'https://i.imgur.com/8mLdoxE.gif',
                           'https://i.imgur.com/UyaZx3z.gif',
                           'https://i.imgur.com/wvuAZEy.gif',
                           'https://i.imgur.com/MbtJv11.gif',
                           'https://i.imgur.com/doys7zJ.gif',
                           'https://i.imgur.com/iDy5bUZ.gif',
                           'https://i.imgur.com/DdnOMmu.gif',
                           'https://i.imgur.com/YBn9YiI.gif',
                           'https://i.imgur.com/5BSLpXh.gif',
                           'https://i.imgur.com/rzcjHMc.gif',
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
                           'https://i.imgur.com/TFFTXLA.gif',
                           'https://i.imgur.com/z1CDDXw.gif',
                           'https://i.imgur.com/QEr59Mw.gif',
                           'https://i.imgur.com/nYrqMsT.gif',
                           'https://i.imgur.com/B7mOdCh.gif',
                           'https://i.imgur.com/f0EXhkt.gif',
                           'https://i.imgur.com/K75Tb10.gif',
                           'https://i.imgur.com/9VtZHXQ.gif',
                           'https://i.imgur.com/jNv4kjC.gif',
                           'https://i.imgur.com/JrT7W2n.gif',
                           'https://i.imgur.com/XbnjSq5.gif',
                           'https://i.imgur.com/B4SpAa0.gif',
                           'https://media.discordapp.net/attachments/530484675613949973/819838063823552522/image0.gif',
                           'https://media.discordapp.net/attachments/530484675613949973/819837890174779422/image0.gif',
                           'https://media.discordapp.net/attachments/530484675613949973/819837930528702465/image0.gif',
                           'https://media.discordapp.net/attachments/530484675613949973/819838239593463818/image0.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820225012945387530/7b2177798996a8fc8494bfd96d847378.gif'
                           ]
                    image = random.choice(choices)

                    embed = discord.Embed(description=fuck.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)
                elif author_gender == 'female':
                    author = ctx.message.author.name

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
                           'https://i.imgur.com/ZYGTQlX.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820225012945387530/7b2177798996a8fc8494bfd96d847378.gif',
                           'https://www.youpeg.com/wp-content/uploads/2019/02/gallery-the-worlds-hottest-gianna-dior-xxx-porn-gif-gallery-syber-pussy-xxx-forums-porn-videos-x-1550160633c8p4l.gif',
                           'https://hotporngifs.eu/wp-content/uploads/2018/07/tumblr_ovlpmn6KtD1tduf00o1_400.gif',
                           'https://hotporngifs.eu/wp-content/uploads/2018/05/tumblr_otj1dxn4yq1sg1lgao1_500.gif',
                           'https://hotporngifs.eu/wp-content/uploads/2018/12/tumblr_pgk4v0rSGC1rat4opo1_500-450x635.gif',
                           'http://i.imgur.com/DDso5m8.gif',
                           'http://www.reuni.eu/image/417862.gif',
                           'https://24.media.tumblr.com/073577e9b34d44bc2a13bf534ebcca38/tumblr_mipo08ImUU1qbh1xjo1_500.gif',
                           'https://sluterest.com/wp-content/uploads/2015/06/juicy-fuck-office.gif',
                           'http://www.coaching-et-formation-coaching.eu/image/269c5c7998a9443f1310cd063783b55c.gif',
                           'http://huntingdonshirecricket.com/images/223199.gif',
                           'https://i.imgur.com/B2HlgWs.gif',
                           'https://i.imgur.com/9FkZsAD.gif',
                           'https://i.imgur.com/pEts2Qq.gif',
                           'https://i.imgur.com/gFLjKK5.gif',
                           'https://i.imgur.com/0NfK8UE.gif',
                           'https://i.imgur.com/1L6Cbmt.gif',
                           'https://i.imgur.com/2xaMyW3.gif',
                           'https://i.imgur.com/x0anhio.gif',
                           'https://i.imgur.com/e2KWlA5.gif',
                           'https://i.imgur.com/NfXSD3F.gif',
                           'https://i.imgur.com/Ldsdjld.gif',
                           'https://i.imgur.com/oRYeQ3h.gif',
                           'https://i.imgur.com/0rbmTGv.gif',
                           'https://i.imgur.com/KRHMCLZ.gif',
                           'https://i.imgur.com/w57Ankv.gif',
                           'https://i.imgur.com/jh288pa.gif',
                           'https://i.imgur.com/aCwm2n1.gif',
                           'https://i.imgur.com/g5CpZqq.gif',
                           'https://i.imgur.com/RhcqXDC.gif',
                           'https://i.imgur.com/N2kpuPJ.gif',
                           'https://i.imgur.com/bHmgAxS.gif',
                           'https://i.imgur.com/tZMorlV.gif',
                           'https://i.imgur.com/wLS5PBn.gif',
                           'https://i.imgur.com/ROObS6Z.gif',
                           'https://i.imgur.com/8mLdoxE.gif',
                           'https://i.imgur.com/UyaZx3z.gif',
                           'https://i.imgur.com/wvuAZEy.gif',
                           'https://i.imgur.com/MbtJv11.gif',
                           'https://i.imgur.com/doys7zJ.gif',
                           'https://i.imgur.com/iDy5bUZ.gif',
                           'https://i.imgur.com/DdnOMmu.gif',
                           'https://i.imgur.com/YBn9YiI.gif',
                           'https://i.imgur.com/5BSLpXh.gif',
                           'https://i.imgur.com/rzcjHMc.gif',
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
                           'https://i.imgur.com/TFFTXLA.gif',
                           'https://i.imgur.com/z1CDDXw.gif',
                           'https://i.imgur.com/QEr59Mw.gif',
                           'https://i.imgur.com/nYrqMsT.gif',
                           'https://i.imgur.com/B7mOdCh.gif',
                           'https://i.imgur.com/f0EXhkt.gif',
                           'https://i.imgur.com/K75Tb10.gif',
                           'https://i.imgur.com/9VtZHXQ.gif',
                           'https://i.imgur.com/jNv4kjC.gif',
                           'https://i.imgur.com/JrT7W2n.gif',
                           'https://i.imgur.com/XbnjSq5.gif',
                           'https://i.imgur.com/B4SpAa0.gif',
                           'https://media.discordapp.net/attachments/530484675613949973/819838063823552522/image0.gif',
                           'https://media.discordapp.net/attachments/530484675613949973/819837890174779422/image0.gif',
                           'https://media.discordapp.net/attachments/530484675613949973/819837930528702465/image0.gif',
                           'https://media.discordapp.net/attachments/530484675613949973/819838239593463818/image0.gif'
                           ]
                    image = random.choice(choices)

                    embed = discord.Embed(description=fuck.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

        mention_gender = determineGender(ctx.message.mentions[0])

        if author_gender == 'male':
            if mention_gender == 'male':
                author = ctx.message.author.name


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
                    'http://gaygifs.net/albums/2016/08/30/17/1/vftpx1472568433-international-playboys-jack-harrer-and-darius-ferdynand-1.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/820041916661760030/mm_anal1.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/820041933115097098/mm_anal2.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/820041953747140638/mm_anal3.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/820041970743246929/mm_anal4.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/820041978892124160/mm_anal5.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/820041987120955462/mm_anal6.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/820041992233943110/mm_anal7.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/820042006541238347/mm_anal8.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/820042017773453352/mm_anal9.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/820042031232974896/mm_anal10.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/820042039483564042/mm_anal11.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/820042048865828884/mm_anal12.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/820042053529370644/mm_anal13.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/820042070861152360/mm_anal14.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/820042078061985852/mm_anal15.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/820042082667986975/mm_anal16.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/820042086375882823/mm_anal17.gif'
                ]

                image = random.choice(choices)

                embed = discord.Embed(description=fuck.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

            else:
                author = ctx.message.author.name


                fuck = '**{0} fucks {1}**'

                choices = ['https://i.imgur.com/7GNPWmt.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820225012945387530/7b2177798996a8fc8494bfd96d847378.gif',
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
                           'https://i.imgur.com/ZYGTQlX.gif',
                           'https://www.youpeg.com/wp-content/uploads/2019/02/gallery-the-worlds-hottest-gianna-dior-xxx-porn-gif-gallery-syber-pussy-xxx-forums-porn-videos-x-1550160633c8p4l.gif',
                           'https://hotporngifs.eu/wp-content/uploads/2018/07/tumblr_ovlpmn6KtD1tduf00o1_400.gif',
                           'https://hotporngifs.eu/wp-content/uploads/2018/05/tumblr_otj1dxn4yq1sg1lgao1_500.gif',
                           'https://hotporngifs.eu/wp-content/uploads/2018/12/tumblr_pgk4v0rSGC1rat4opo1_500-450x635.gif',
                           'http://i.imgur.com/DDso5m8.gif',
                           'http://www.reuni.eu/image/417862.gif',
                           'https://24.media.tumblr.com/073577e9b34d44bc2a13bf534ebcca38/tumblr_mipo08ImUU1qbh1xjo1_500.gif',
                           'https://sluterest.com/wp-content/uploads/2015/06/juicy-fuck-office.gif',
                           'http://www.coaching-et-formation-coaching.eu/image/269c5c7998a9443f1310cd063783b55c.gif',
                           'http://huntingdonshirecricket.com/images/223199.gif',
                           'https://i.imgur.com/B2HlgWs.gif',
                           'https://i.imgur.com/9FkZsAD.gif',
                           'https://i.imgur.com/pEts2Qq.gif',
                           'https://i.imgur.com/gFLjKK5.gif',
                           'https://i.imgur.com/0NfK8UE.gif',
                           'https://i.imgur.com/1L6Cbmt.gif',
                           'https://i.imgur.com/2xaMyW3.gif',
                           'https://i.imgur.com/x0anhio.gif',
                           'https://i.imgur.com/e2KWlA5.gif',
                           'https://i.imgur.com/NfXSD3F.gif',
                           'https://i.imgur.com/Ldsdjld.gif',
                           'https://i.imgur.com/oRYeQ3h.gif',
                           'https://i.imgur.com/0rbmTGv.gif',
                           'https://i.imgur.com/KRHMCLZ.gif',
                           'https://i.imgur.com/w57Ankv.gif',
                           'https://i.imgur.com/jh288pa.gif',
                           'https://i.imgur.com/aCwm2n1.gif',
                           'https://i.imgur.com/g5CpZqq.gif',
                           'https://i.imgur.com/RhcqXDC.gif',
                           'https://i.imgur.com/N2kpuPJ.gif',
                           'https://i.imgur.com/bHmgAxS.gif',
                           'https://i.imgur.com/tZMorlV.gif',
                           'https://i.imgur.com/wLS5PBn.gif',
                           'https://i.imgur.com/ROObS6Z.gif',
                           'https://i.imgur.com/8mLdoxE.gif',
                           'https://i.imgur.com/UyaZx3z.gif',
                           'https://i.imgur.com/wvuAZEy.gif',
                           'https://i.imgur.com/MbtJv11.gif',
                           'https://i.imgur.com/doys7zJ.gif',
                           'https://i.imgur.com/iDy5bUZ.gif',
                           'https://i.imgur.com/DdnOMmu.gif',
                           'https://i.imgur.com/YBn9YiI.gif',
                           'https://i.imgur.com/5BSLpXh.gif',
                           'https://i.imgur.com/rzcjHMc.gif',
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
                           'https://i.imgur.com/TFFTXLA.gif',
                           'https://i.imgur.com/z1CDDXw.gif',
                           'https://i.imgur.com/QEr59Mw.gif',
                           'https://i.imgur.com/nYrqMsT.gif',
                           'https://i.imgur.com/B7mOdCh.gif',
                           'https://i.imgur.com/f0EXhkt.gif',
                           'https://i.imgur.com/K75Tb10.gif',
                           'https://i.imgur.com/9VtZHXQ.gif',
                           'https://i.imgur.com/jNv4kjC.gif',
                           'https://i.imgur.com/JrT7W2n.gif',
                           'https://i.imgur.com/XbnjSq5.gif',
                           'https://i.imgur.com/B4SpAa0.gif',
                           'https://media.discordapp.net/attachments/530484675613949973/819838063823552522/image0.gif',
                           'https://media.discordapp.net/attachments/530484675613949973/819837890174779422/image0.gif',
                           'https://media.discordapp.net/attachments/530484675613949973/819837930528702465/image0.gif',
                           'https://media.discordapp.net/attachments/530484675613949973/819838239593463818/image0.gif'
                           ]


            image = random.choice(choices)

            embed = discord.Embed(description=fuck.format(author, mentions.name), colour=discord.Colour.blue())
            embed.set_image(url=image)

            await ctx.send(embed=embed)

        elif author_gender == 'female':

            if mention_gender == 'female':
                author = ctx.message.author.name


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
                           'https://i.imgur.com/X77kSlX.gif',
                           'https://media.discordapp.net/attachments/530484675613949973/819838151669055498/image0.gif',
                           'https://media.discordapp.net/attachments/530484675613949973/819838104046796800/image0.gif']

                image = random.choice(choices)

                embed = discord.Embed(description=fuck.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name


                fuck = '**{0} fucks {1}**'

                choices = ['https://i.imgur.com/7GNPWmt.gif',
                           'https://i.imgur.com/c35C8jE.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820225012945387530/7b2177798996a8fc8494bfd96d847378.gif',
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
                           'https://i.imgur.com/ZYGTQlX.gif',
                           'https://www.youpeg.com/wp-content/uploads/2019/02/gallery-the-worlds-hottest-gianna-dior-xxx-porn-gif-gallery-syber-pussy-xxx-forums-porn-videos-x-1550160633c8p4l.gif',
                           'https://hotporngifs.eu/wp-content/uploads/2018/07/tumblr_ovlpmn6KtD1tduf00o1_400.gif',
                           'https://hotporngifs.eu/wp-content/uploads/2018/05/tumblr_otj1dxn4yq1sg1lgao1_500.gif',
                           'https://hotporngifs.eu/wp-content/uploads/2018/12/tumblr_pgk4v0rSGC1rat4opo1_500-450x635.gif',
                           'http://i.imgur.com/DDso5m8.gif',
                           'http://www.reuni.eu/image/417862.gif',
                           'https://24.media.tumblr.com/073577e9b34d44bc2a13bf534ebcca38/tumblr_mipo08ImUU1qbh1xjo1_500.gif',
                           'https://sluterest.com/wp-content/uploads/2015/06/juicy-fuck-office.gif',
                           'http://www.coaching-et-formation-coaching.eu/image/269c5c7998a9443f1310cd063783b55c.gif',
                           'http://huntingdonshirecricket.com/images/223199.gif',
                           'https://i.imgur.com/B2HlgWs.gif',
                           'https://i.imgur.com/9FkZsAD.gif',
                           'https://i.imgur.com/pEts2Qq.gif',
                           'https://i.imgur.com/gFLjKK5.gif',
                           'https://i.imgur.com/0NfK8UE.gif',
                           'https://i.imgur.com/1L6Cbmt.gif',
                           'https://i.imgur.com/2xaMyW3.gif',
                           'https://i.imgur.com/x0anhio.gif',
                           'https://i.imgur.com/e2KWlA5.gif',
                           'https://i.imgur.com/NfXSD3F.gif',
                           'https://i.imgur.com/Ldsdjld.gif',
                           'https://i.imgur.com/oRYeQ3h.gif',
                           'https://i.imgur.com/0rbmTGv.gif',
                           'https://i.imgur.com/KRHMCLZ.gif',
                           'https://i.imgur.com/w57Ankv.gif',
                           'https://i.imgur.com/jh288pa.gif',
                           'https://i.imgur.com/aCwm2n1.gif',
                           'https://i.imgur.com/g5CpZqq.gif',
                           'https://i.imgur.com/RhcqXDC.gif',
                           'https://i.imgur.com/N2kpuPJ.gif',
                           'https://i.imgur.com/bHmgAxS.gif',
                           'https://i.imgur.com/tZMorlV.gif',
                           'https://i.imgur.com/wLS5PBn.gif',
                           'https://i.imgur.com/ROObS6Z.gif',
                           'https://i.imgur.com/8mLdoxE.gif',
                           'https://i.imgur.com/UyaZx3z.gif',
                           'https://i.imgur.com/wvuAZEy.gif',
                           'https://i.imgur.com/MbtJv11.gif',
                           'https://i.imgur.com/doys7zJ.gif',
                           'https://i.imgur.com/iDy5bUZ.gif',
                           'https://i.imgur.com/DdnOMmu.gif',
                           'https://i.imgur.com/YBn9YiI.gif',
                           'https://i.imgur.com/5BSLpXh.gif',
                           'https://i.imgur.com/rzcjHMc.gif',
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
                           'https://i.imgur.com/TFFTXLA.gif',
                           'https://i.imgur.com/z1CDDXw.gif',
                           'https://i.imgur.com/QEr59Mw.gif',
                           'https://i.imgur.com/nYrqMsT.gif',
                           'https://i.imgur.com/B7mOdCh.gif',
                           'https://i.imgur.com/f0EXhkt.gif',
                           'https://i.imgur.com/K75Tb10.gif',
                           'https://i.imgur.com/9VtZHXQ.gif',
                           'https://i.imgur.com/jNv4kjC.gif',
                           'https://i.imgur.com/JrT7W2n.gif',
                           'https://i.imgur.com/XbnjSq5.gif',
                           'https://i.imgur.com/B4SpAa0.gif',
                           'https://media.discordapp.net/attachments/530484675613949973/819838063823552522/image0.gif',
                           'https://media.discordapp.net/attachments/530484675613949973/819837890174779422/image0.gif',
                           'https://media.discordapp.net/attachments/530484675613949973/819837930528702465/image0.gif',
                           'https://media.discordapp.net/attachments/530484675613949973/819838239593463818/image0.gif'
                           ]

                image = random.choice(choices)

                embed = discord.Embed(description=fuck.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

    @fuck.error
    async def fuck_error (self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()

        raise error

    @commands.command(aliases=['spanks'])
    @commands.is_nsfw()
    async def spank(self, ctx, message=None):
        """Spanks the user you mention"""
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message

        author_gender = determineGender(ctx.author)
        if mentions == message:
            if message == None:
                embed = discord.Embed(description=f"**You can't spank nothing you horni dumbo\nExample use: $spank @User#6969**", colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                if author_gender == 'male':
                    author = ctx.message.author.name

                    spank = "**{0} spanks {1}'s booty**"

                    choices = ['https://i.imgur.com/rLSCY75.gif',
                                'https://i.imgur.com/pTtxvfK.gif',
                                'https://i.imgur.com/sHZFIgH.gif',
                                'https://i.imgur.com/jNTHiJs.gif',
                                'https://i.imgur.com/drzE8fi.gif',
                                'https://i.imgur.com/NbXKhlI.gif',
                                'https://i.imgur.com/ijPhdcp.gif',
                                'https://i.imgur.com/Ukck5NT.gif',
                                'https://i.imgur.com/wSfmq1k.gif',
                                'https://i.imgur.com/fQfIAFw.gif',
                                'https://i.imgur.com/Xgvjcea.gif',
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046665849569350/ezgif.com-gif-maker_48.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046648539545630/ezgif.com-gif-maker_60.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046644739113020/ezgif.com-gif-maker_45.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046642603950130/ezgif.com-gif-maker_24.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046638024425502/ezgif.com-gif-maker_31.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046634048487434/ezgif.com-gif-maker_61.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046625616887838/ezgif.com-gif-maker_32.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046619317829702/ezgif.com-gif-maker_74.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046619191214110/ezgif.com-gif-maker_26.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046617941835776/ezgif.com-gif-maker_39.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046617207308328/ezgif.com-gif-maker_49.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046608127557692/ezgif.com-gif-maker_43.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046608068575281/ezgif.com-gif-maker_35.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046603430068224/ezgif.com-gif-maker_27.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046600820555786/ezgif.com-gif-maker_34.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046578075238430/ezgif.com-gif-maker_66.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046572307939329/ezgif.com-gif-maker_71.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046573071040522/ezgif.com-gif-maker_51.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046553382715402/ezgif.com-gif-maker_70.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046552842174494/ezgif.com-gif-maker_59.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046540360056832/ezgif.com-gif-maker_40.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046535774765056/ezgif.com-gif-maker_64.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046530281013258/ezgif.com-gif-maker_69.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046520181260308/ezgif.com-gif-maker_33.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046518536830976/ezgif.com-gif-maker_30.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046505245081670/ezgif.com-gif-maker_29.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046502824574997/ezgif.com-gif-maker_23.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046498332999721/ezgif.com-gif-maker_65.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046491080261682/ezgif.com-gif-maker_36.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046490510753842/ezgif.com-gif-maker_76.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046488056299562/ezgif.com-gif-maker_25.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046479995371580/ezgif.com-gif-maker_52.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046473556983838/ezgif.com-gif-maker_38.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046471048527882/ezgif.com-gif-maker_72.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046432486883338/ezgif.com-gif-maker_57.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046427411251230/ezgif.com-gif-maker_78.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046417013178448/ezgif.com-gif-maker_56.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046410001350686/ezgif.com-gif-maker_58.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046315985109003/ezgif.com-gif-maker_28.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046314957635614/ezgif.com-gif-maker_41.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046314635329686/ezgif.com-gif-maker_63.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046306468102194/ezgif.com-gif-maker_55.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046274663350302/ezgif.com-gif-maker_37.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046250491314216/ezgif.com-gif-maker_42.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046249929670716/ezgif.com-gif-maker_62.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046239096045608/ezgif.com-gif-maker_54.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046199971053598/ezgif.com-gif-maker_73.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046187426414632/ezgif.com-gif-maker_77.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046110842617877/ezgif.com-gif-maker_46.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046097625317376/ezgif.com-gif-maker_50.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834046041174441994/ezgif.com-gif-maker_53.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834045986719531079/ezgif.com-gif-maker_44.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834045928351727646/ezgif.com-gif-maker_67.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834045891765207100/ezgif.com-gif-maker_68.gif"]

                    image = random.choice(choices)

                    embed = discord.Embed(description=spank.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=image)
                    await ctx.send(embed=embed)
                elif author_gender == 'female':
                    author = ctx.message.author.name

                    spank = "**{0} spanks {1}'s booty**"

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

                    embed = discord.Embed(description=spank.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=image)
                    await ctx.send(embed=embed)
        mention_gender = determineGender(ctx.message.mentions[0])

        if author_gender == 'male':
            if mention_gender == 'male':

                author = ctx.message.author.name

                spank = "**{0} spanks {1}'s booty**"

                choices = ['https://66.media.tumblr.com/3c847409a303f9e532143d3f3c5d048a/tumblr_pg8g29z9Nu1xqr2fio1_500.gif',
                           'https://66.media.tumblr.com/fc70714c4908c1dd184a34027a2f3a9f/tumblr_p8981eux6T1xqr2fio1_540.gif',
                           'https://i1.wp.com/gayspankingclips.com/wp-content/uploads/2014/11/nicholas-rym-spanked.gif?zoom=2.625&resize=396%2C222',
                           'http://spankgifs.com/wp-content/uploads/2015/12/m-m-spanlking.gif',
                           'https://57.media.tumblr.com/0782af14546e3f9d7b7eb23a3751339b/tumblr_mtj4kpi5XB1rcf0aqo1_400.gif',
                           'https://gaygifs.net/albums/2016/08/30/18/1/he-wants-him.gif',
                           'http://3.bp.blogspot.com/-nrsjmFKbuY8/US7wShcGqVI/AAAAAAAAdAc/MhleGSPE9Xs/s1600/tumblr_mfehy7B06R1qanl9mo1_500.gif',
                           'https://33.media.tumblr.com/e982e2e2aa267d728844dbee8fac2034/tumblr_nnfpi6UZMn1tk5yaho1_500.gif']

                image = random.choice(choices)

                embed = discord.Embed(description=spank.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)
                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name


                spank = "**{0} spanks {1}'s booty**"

                choices = ['https://i.imgur.com/rLSCY75.gif',
                           'https://i.imgur.com/pTtxvfK.gif',
                           'https://i.imgur.com/sHZFIgH.gif',
                           'https://i.imgur.com/jNTHiJs.gif',
                           'https://i.imgur.com/drzE8fi.gif',
                           'https://i.imgur.com/NbXKhlI.gif',
                           'https://i.imgur.com/ijPhdcp.gif',
                           'https://i.imgur.com/Ukck5NT.gif',
                           'https://i.imgur.com/wSfmq1k.gif',
                            'https://i.imgur.com/fQfIAFw.gif',
                            'https://i.imgur.com/Xgvjcea.gif',
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046665849569350/ezgif.com-gif-maker_48.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046648539545630/ezgif.com-gif-maker_60.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046644739113020/ezgif.com-gif-maker_45.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046642603950130/ezgif.com-gif-maker_24.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046638024425502/ezgif.com-gif-maker_31.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046634048487434/ezgif.com-gif-maker_61.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046625616887838/ezgif.com-gif-maker_32.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046619317829702/ezgif.com-gif-maker_74.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046619191214110/ezgif.com-gif-maker_26.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046617941835776/ezgif.com-gif-maker_39.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046617207308328/ezgif.com-gif-maker_49.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046608127557692/ezgif.com-gif-maker_43.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046608068575281/ezgif.com-gif-maker_35.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046603430068224/ezgif.com-gif-maker_27.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046600820555786/ezgif.com-gif-maker_34.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046578075238430/ezgif.com-gif-maker_66.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046572307939329/ezgif.com-gif-maker_71.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046573071040522/ezgif.com-gif-maker_51.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046553382715402/ezgif.com-gif-maker_70.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046552842174494/ezgif.com-gif-maker_59.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046540360056832/ezgif.com-gif-maker_40.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046535774765056/ezgif.com-gif-maker_64.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046530281013258/ezgif.com-gif-maker_69.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046520181260308/ezgif.com-gif-maker_33.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046518536830976/ezgif.com-gif-maker_30.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046505245081670/ezgif.com-gif-maker_29.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046502824574997/ezgif.com-gif-maker_23.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046498332999721/ezgif.com-gif-maker_65.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046491080261682/ezgif.com-gif-maker_36.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046490510753842/ezgif.com-gif-maker_76.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046488056299562/ezgif.com-gif-maker_25.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046479995371580/ezgif.com-gif-maker_52.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046473556983838/ezgif.com-gif-maker_38.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046471048527882/ezgif.com-gif-maker_72.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046432486883338/ezgif.com-gif-maker_57.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046427411251230/ezgif.com-gif-maker_78.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046417013178448/ezgif.com-gif-maker_56.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046410001350686/ezgif.com-gif-maker_58.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046315985109003/ezgif.com-gif-maker_28.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046314957635614/ezgif.com-gif-maker_41.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046314635329686/ezgif.com-gif-maker_63.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046306468102194/ezgif.com-gif-maker_55.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046274663350302/ezgif.com-gif-maker_37.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046250491314216/ezgif.com-gif-maker_42.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046249929670716/ezgif.com-gif-maker_62.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046239096045608/ezgif.com-gif-maker_54.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046199971053598/ezgif.com-gif-maker_73.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046187426414632/ezgif.com-gif-maker_77.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046110842617877/ezgif.com-gif-maker_46.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046097625317376/ezgif.com-gif-maker_50.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046041174441994/ezgif.com-gif-maker_53.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834045986719531079/ezgif.com-gif-maker_44.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834045928351727646/ezgif.com-gif-maker_67.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834045891765207100/ezgif.com-gif-maker_68.gif"]

                image = random.choice(choices)

                embed = discord.Embed(description=spank.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)
                await ctx.send(embed=embed)

        elif author_gender == 'female':
            if mention_gender == 'female':
                author = ctx.message.author.name

                spank = "**{0} spanks {1}'s booty**"

                choices = ['http://spankgifs.com/wp-content/uploads/2017/03/lesbian-couple-enjoy-spanking-over-the-couch.gif',
                           'http://spankgifs.com/wp-content/uploads/2018/01/lesbian-spanking-games.gif',
                           'http://24.media.tumblr.com/6e14e875fd593012eb2b9828bbad382c/tumblr_mk07urmcXQ1rjhn1to1_500.gif',
                           'http://spankgifs.com/wp-content/uploads/2016/08/fem-to-fem-hairbrush-spanking.gif',
                           'https://juicygif.com/albums/userpics/2017y/12/16/1/1/small_8516-hot-lesbian-spanking-action-d.gif',
                           'http://www.akceleratorbiznesu.eu/image/c6898511e364d53a4fbb5fbf815fa5dc.gif']

                image = random.choice(choices)

                embed = discord.Embed(description=spank.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)
                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name


                spank = "**{0} spanks {1}'s booty**"

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

                embed = discord.Embed(description=spank.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)
                await ctx.send(embed=embed)

    @spank.error
    async def spank_error(self, ctx, error):

        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()

        raise error

    @commands.command(aliases=['sucks'])
    @commands.is_nsfw()
    async def suck(self, ctx, message=None):
        """Sucks the person you mention"""
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author_gender = determineGender(ctx.author)
        if mentions == message:
            if message == None:
                embed = discord.Embed(description=f"**You can't suck nothing you horni dumbo\nExample use: $suck @User#6969**", colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                if author_gender == 'male':
                    author = ctx.message.author.name

                    suck = '**{0} sucks on {1}!**'

                    choices = [
                        'https://cdn.discordapp.com/attachments/819857033489940481/821440688684138556/ezgif.com-resize_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821440730039189515/ezgif.com-gif-maker_6.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821440733688758292/ezgif.com-gif-maker_4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821440735693897788/ezgif.com-gif-maker_7.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821440741800673360/ezgif.com-gif-maker_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821440744254210148/ezgif.com-gif-maker_10.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821440746229334036/ezgif.com-resize.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821440747826970704/ezgif.com-gif-maker_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821440749941948416/ezgif.com-gif-maker_9.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821440750675689472/ezgif.com-gif-maker_11.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821440751770271744/ezgif.com-gif-maker.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821441066107404288/ezgif.com-gif-maker_3.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821441050568425503/ezgif.com-gif-maker_5.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821441066107404288/ezgif.com-gif-maker_3.gif']

                    image = random.choice(choices)

                    embed = discord.Embed(description=suck.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)
                elif author_gender == 'female':
                    author = ctx.message.author.name

                    suck = '**{0} sucks {1} off**'

                    choices = [
                        'https://cdn.discordapp.com/attachments/819857033489940481/821391408157687828/ezgif.com-resize11.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821391462091456552/ezgif.com-gif-maker.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821391497831383070/ezgif.com-gif-maker_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821391507654967316/ezgif.com-gif-maker_13.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821391507998113832/ezgif.com-gif-maker_4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821391514042105856/ezgif.com-gif-maker_7.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821391527766392832/ezgif.com-resize_7.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821391534507294800/ezgif.com-gif-maker_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821391534972076132/ezgif.com-gif-maker_12.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821391547848196176/ezgif.com-gif-maker_3.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821391547605057546/ezgif.com-gif-maker_8.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821391548515745822/ezgif.com-gif-maker_10.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821391550138679316/ezgif.com-gif-maker_6.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821391550885658634/ezgif.com-gif-maker_5.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821391557197824050/ezgif.com-resize_4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821391558053855232/ezgif.com-gif-maker_14.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821391558913556480/ezgif.com-resize_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821391560490745876/ezgif.com-resize_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821391561107439636/ezgif.com-resize.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821391562805870612/ezgif.com-crop.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821391562906533888/ezgif.com-resize_3.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821391563195940884/ezgif.com-resize_6.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821391563326357564/ezgif.com-gif-maker_17.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821391919884140584/ezgif.com-gif-maker_9.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821392056730517504/ezgif.com-resize_5.gif']

                    image = random.choice(choices)

                    embed = discord.Embed(description=suck.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

        mention_gender = determineGender(ctx.message.mentions[0])

        if author_gender == 'male':
            if mention_gender == 'male':

                author = ctx.message.author.name


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
                           'https://i.gifer.com/3NwwH.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821444160350322728/ezgif.com-gif-maker.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821444162049015878/ezgif.com-gif-maker_17.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821444168525676564/ezgif.com-resize_1.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821444179384860737/ezgif.com-resize.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821444181456191574/ezgif.com-gif-maker_1.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821444183403397210/ezgif.com-gif-maker_2.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821444190361747466/ezgif.com-gif-maker_3.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821444198573539369/ezgif.com-gif-maker_4.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821444201140977684/ezgif.com-gif-maker_5.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821444205707657316/ezgif.com-gif-maker_6.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821444218538819645/ezgif.com-gif-maker_7.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821444220673589328/ezgif.com-gif-maker_8.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821444224230096946/ezgif.com-gif-maker_10.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821444229649268776/ezgif.com-gif-maker_11.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821444230613696582/ezgif.com-gif-maker_12.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821444238524809297/ezgif.com-gif-maker_9.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821444241325686885/ezgif.com-gif-maker_13.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821444250427195493/ezgif.com-gif-maker_14.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821444251068923914/ezgif.com-gif-maker_15.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821444252952559616/ezgif.com-gif-maker_16.gif']

                image = random.choice(choices)

                embed = discord.Embed(description=suck.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name


                suck = '**{0} sucks on {1}!**'

                choices = ['https://cdn.discordapp.com/attachments/819857033489940481/821440688684138556/ezgif.com-resize_1.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821440730039189515/ezgif.com-gif-maker_6.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821440733688758292/ezgif.com-gif-maker_4.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821440735693897788/ezgif.com-gif-maker_7.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821440741800673360/ezgif.com-gif-maker_1.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821440744254210148/ezgif.com-gif-maker_10.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821440746229334036/ezgif.com-resize.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821440747826970704/ezgif.com-gif-maker_2.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821440749941948416/ezgif.com-gif-maker_9.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821440750675689472/ezgif.com-gif-maker_11.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821440751770271744/ezgif.com-gif-maker.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821441066107404288/ezgif.com-gif-maker_3.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821441050568425503/ezgif.com-gif-maker_5.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821441066107404288/ezgif.com-gif-maker_3.gif']

                image = random.choice(choices)

                embed = discord.Embed(description=suck.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif author_gender == 'female':
            if mention_gender == 'male':
                author = ctx.message.author.name


                suck = '**{0} sucks {1} off**'

                choices = ['https://cdn.discordapp.com/attachments/819857033489940481/821391408157687828/ezgif.com-resize11.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821391462091456552/ezgif.com-gif-maker.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821391497831383070/ezgif.com-gif-maker_2.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821391507654967316/ezgif.com-gif-maker_13.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821391507998113832/ezgif.com-gif-maker_4.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821391514042105856/ezgif.com-gif-maker_7.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821391527766392832/ezgif.com-resize_7.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821391534507294800/ezgif.com-gif-maker_1.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821391534972076132/ezgif.com-gif-maker_12.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821391547848196176/ezgif.com-gif-maker_3.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821391547605057546/ezgif.com-gif-maker_8.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821391548515745822/ezgif.com-gif-maker_10.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821391550138679316/ezgif.com-gif-maker_6.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821391550885658634/ezgif.com-gif-maker_5.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821391557197824050/ezgif.com-resize_4.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821391558053855232/ezgif.com-gif-maker_14.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821391558913556480/ezgif.com-resize_1.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821391560490745876/ezgif.com-resize_2.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821391561107439636/ezgif.com-resize.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821391562805870612/ezgif.com-crop.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821391562906533888/ezgif.com-resize_3.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821391563195940884/ezgif.com-resize_6.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821391563326357564/ezgif.com-gif-maker_17.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821391919884140584/ezgif.com-gif-maker_9.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821392056730517504/ezgif.com-resize_5.gif']

                image = random.choice(choices)

                embed = discord.Embed(description=suck.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name


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
                           'https://i.gifer.com/3Nwvz.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821380913367482398/ezgif.com-gif-maker_7.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821380927343034438/ezgif.com-gif-maker_4.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821380936661991484/ezgif.com-gif-maker_1.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821380937357983794/ezgif.com-gif-maker_3.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821380937362571294/ezgif.com-gif-maker_9.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821380938935435335/ezgif.com-gif-maker_2.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821380938595565599/ezgif.com-gif-maker_6.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821380939062050856/ezgif.com-gif-maker_5.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821380939808505856/ezgif.com-gif-maker.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821380941385433118/ezgif.com-gif-maker_11.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/821381299461423124/ezgif.com-gif-maker_10.gif'
                           ]


                image = random.choice(choices)

                embed = discord.Embed(description=suck.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

    @suck.error
    async def suck_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()

        raise error

    @commands.command()
    @commands.is_nsfw()
    async def anal(self, ctx, message=None):
        """Anal with the person you mention"""
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author_gender = determineGender(ctx.author)
        if mentions == message:
            if message == None:
                embed = discord.Embed(description=f"**You can't fuck nothing you horni dumbo\nExample use: $anal @User#6969**", colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                if author_gender == 'male':
                    author = ctx.message.author.name

                    anal = '**{0} fucks {1} in the ass**'

                    choices = [
                        'https://mediav-img.porn.com/secure/9d5f1db85ddfcc17f145d9fe9670d11c/sc/4/4362/4362279/source/001.gif',
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
                        'http://amateurhomeporn.net/wp-content/uploads/2012/08/photo-Amateur-Anal-Gif-871075187.gif',
                        'https://cdn.discordapp.com/attachments/632301566438932498/632819515419394050/image0-1.gif',
                        'https://media.discordapp.net/attachments/819857033489940481/820043063921344512/mf_anal8.gif',
                        'https://media.discordapp.net/attachments/819857033489940481/820043069810016276/mf_anal9.gif',
                        'https://media.discordapp.net/attachments/819857033489940481/820043074377220116/mf_anal10.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/820043079649722398/mf_anal11.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/820043085718356008/mf_anal12.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/820043090705907712/mf_anal13.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/820043098385809509/mf_anal17.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/820043102701223946/mf_anal16.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/820043113035989052/mf_anal15.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/820043115712217199/mf_anal21.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/820043116907855892/mf_anal19.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/820043139586457660/mf_anal2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/820043141456330772/mf_anal4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/820043142530203668/mf_anal3.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/820043147937316874/mf_anal5.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/820043149354598430/mf_anal7.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/820043162080116786/mf_anal20.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/820043166237458502/mf_anal22.gif']

                    image = random.choice(choices)

                    embed = discord.Embed(description=anal.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=image)
                    await ctx.send(embed=embed)

                elif author_gender == 'female':
                    author = ctx.message.author.name

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
                               'https://cdnio.luscious.net/166/lusciousnet_rfaptogifs_anal_riding__1935374002.gif',
                               'https://media.discordapp.net/attachments/819857033489940481/820043063921344512/mf_anal8.gif',
                               'https://media.discordapp.net/attachments/819857033489940481/820043069810016276/mf_anal9.gif',
                               'https://media.discordapp.net/attachments/819857033489940481/820043074377220116/mf_anal10.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/820043079649722398/mf_anal11.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/820043085718356008/mf_anal12.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/820043090705907712/mf_anal13.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/820043098385809509/mf_anal17.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/820043102701223946/mf_anal16.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/820043113035989052/mf_anal15.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/820043115712217199/mf_anal21.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/820043116907855892/mf_anal19.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/820043139586457660/mf_anal2.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/820043141456330772/mf_anal4.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/820043142530203668/mf_anal3.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/820043147937316874/mf_anal5.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/820043149354598430/mf_anal7.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/820043162080116786/mf_anal20.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/820043166237458502/mf_anal22.gif'
                               ]

                    image = random.choice(choices)

                    embed = discord.Embed(description=anal.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

        mention_gender = determineGender(ctx.message.mentions[0])

        if author_gender == 'male':
            if mention_gender == 'female':
                author = ctx.message.author.name

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
                           'http://amateurhomeporn.net/wp-content/uploads/2012/08/photo-Amateur-Anal-Gif-871075187.gif',
                           'https://cdn.discordapp.com/attachments/632301566438932498/632819515419394050/image0-1.gif',
                           'https://media.discordapp.net/attachments/819857033489940481/820043063921344512/mf_anal8.gif',
                           'https://media.discordapp.net/attachments/819857033489940481/820043069810016276/mf_anal9.gif',
                           'https://media.discordapp.net/attachments/819857033489940481/820043074377220116/mf_anal10.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043079649722398/mf_anal11.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043085718356008/mf_anal12.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043090705907712/mf_anal13.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043098385809509/mf_anal17.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043102701223946/mf_anal16.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043113035989052/mf_anal15.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043115712217199/mf_anal21.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043116907855892/mf_anal19.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043139586457660/mf_anal2.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043141456330772/mf_anal4.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043142530203668/mf_anal3.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043147937316874/mf_anal5.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043149354598430/mf_anal7.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043162080116786/mf_anal20.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043166237458502/mf_anal22.gif']

                image = random.choice(choices)

                embed = discord.Embed(description=anal.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name

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
                           'https://gifs.iloopit.net/resources/623dceae-9984-429c-a4fa-b4fea3a3ff26/converted.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820041916661760030/mm_anal1.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820041933115097098/mm_anal2.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820041953747140638/mm_anal3.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820041970743246929/mm_anal4.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820041978892124160/mm_anal5.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820041987120955462/mm_anal6.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820041992233943110/mm_anal7.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820042006541238347/mm_anal8.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820042017773453352/mm_anal9.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820042031232974896/mm_anal10.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820042039483564042/mm_anal11.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820042048865828884/mm_anal12.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820042053529370644/mm_anal13.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820042070861152360/mm_anal14.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820042078061985852/mm_anal15.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820042082667986975/mm_anal16.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820042086375882823/mm_anal17.gif']

                image = random.choice(choices)

                embed = discord.Embed(description=anal.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif author_gender == 'female':
            if mention_gender == 'female':
                author = ctx.message.author.name

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
                           'http://www.anima2011.eu/image/477962.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820050638472740934/ezgif.com-gif-maker.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043517065429032/ff_anal10.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043515978973215/ff_anal15.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043510057140294/ff_anal11.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043506100994058/ff_anal9.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043505232773140/ff_anal14.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043496030208030/ff_anal12.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043484202795008/ff_anal16.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043473256054835/ff_anal13.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043452854960158/ff_anal6.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043442948014141/ff_anal8.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043434697162792/ff_anal7.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043424388087828/ff_anal5.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043416154931200/ff_anal4.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043412862271528/ff_anal3.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043397683085332/ff_anal2.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043396130406410/ff_anal1.gif']

                image = random.choice(choices)

                embed = discord.Embed(description=anal.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name

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
                           'https://cdnio.luscious.net/166/lusciousnet_rfaptogifs_anal_riding__1935374002.gif',
                           'https://media.discordapp.net/attachments/819857033489940481/820043063921344512/mf_anal8.gif',
                           'https://media.discordapp.net/attachments/819857033489940481/820043069810016276/mf_anal9.gif',
                           'https://media.discordapp.net/attachments/819857033489940481/820043074377220116/mf_anal10.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043079649722398/mf_anal11.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043085718356008/mf_anal12.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043090705907712/mf_anal13.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043098385809509/mf_anal17.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043102701223946/mf_anal16.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043113035989052/mf_anal15.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043115712217199/mf_anal21.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043116907855892/mf_anal19.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043139586457660/mf_anal2.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043141456330772/mf_anal4.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043142530203668/mf_anal3.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043147937316874/mf_anal5.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043149354598430/mf_anal7.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043162080116786/mf_anal20.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820043166237458502/mf_anal22.gif'
                           ]

                image = random.choice(choices)

                embed = discord.Embed(description=anal.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)
    @anal.error
    async def anal_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()

        raise error

    @commands.command(aliases=['doms', 'dominate', 'dominates'])
    @commands.is_nsfw()
    async def dom(self, ctx, message=None):
        """Dominates the person you mention"""
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author_gender = determineGender(ctx.author)
        if mentions == message:
            if message == None:
                embed = discord.Embed(description=f"**You can't dom nothing you horni dumbo\nExample use: $dom @User#6969**", colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                if author_gender == 'male':
                    author = ctx.message.author.name

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
                               'https://i.gifer.com/3NwyA.gif',
                               "https://cdn.discordapp.com/attachments/798913238229188608/834128714345611345/ezgif.com-gif-maker_1.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834128745551626320/ezgif.com-gif-maker_9.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834128784071983134/ezgif.com-gif-maker_20.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834128786467454986/ezgif.com-gif-maker_6.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834128789935489034/ezgif.com-gif-maker_13.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834128835787489310/ezgif.com-gif-maker_25.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834128897619525743/ezgif.com-gif-maker_4.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834128902460801024/ezgif.com-gif-maker_17.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834128906348134430/ezgif.com-gif-maker.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834128911905849364/ezgif.com-gif-maker_2.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834128914644205628/ezgif.com-gif-maker_5.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834128917924544522/ezgif.com-gif-maker_10.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834128929815527454/ezgif.com-gif-maker_15.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834128939252842516/ezgif.com-gif-maker_14.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834128953823330404/ezgif.com-gif-maker_18.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834128963939860520/ezgif.com-gif-maker_22.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834128965128028210/ezgif.com-gif-maker_16.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834128977613946890/ezgif.com-gif-maker_21.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834128993678262332/ezgif.com-gif-maker_8.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834128993698840647/ezgif.com-gif-maker_24.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834129014779543622/ezgif.com-gif-maker_3.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834129015216406538/ezgif.com-gif-maker_7.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834129022321295380/ezgif.com-gif-maker_11.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/834129024216334367/ezgif.com-gif-maker_23.gif"]
                    image = random.choice(choices)

                    embed = discord.Embed(description=dom.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

                elif author_gender == 'female':
                    author = ctx.message.author.name

                    dom = '**{0} dominates {1}**'

                    choices = ['https://cdn.discordapp.com/attachments/798913238229188608/902643142426247199/ezgif.com-gif-maker_-_2021-10-26T223710.267.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/902643134486442004/ezgif.com-gif-maker_97.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/902643133651779606/ezgif.com-gif-maker_-_2021-10-26T223733.116.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/902643131776892968/ezgif.com-gif-maker_-_2021-10-26T223722.586.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/902643130619273327/ezgif.com-gif-maker_100.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/902643128199159848/ezgif.com-gif-maker_98.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/902643116593520711/ezgif.com-gif-maker_99.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/902643104442630154/ezgif.com-gif-maker_-_2021-10-26T223741.764.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/902643094393090108/ezgif.com-gif-maker_-_2021-10-26T223750.127.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/902643087426342953/ezgif.com-gif-maker_96.gif']
                    image = random.choice(choices)

                    embed = discord.Embed(description=dom.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

        mention_gender = determineGender(ctx.message.mentions[0])

        if author_gender == 'male':
            if mention_gender == 'female':
                author = ctx.message.author.name


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
                           'https://i.gifer.com/3NwyA.gif',
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128714345611345/ezgif.com-gif-maker_1.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128745551626320/ezgif.com-gif-maker_9.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128784071983134/ezgif.com-gif-maker_20.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128786467454986/ezgif.com-gif-maker_6.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128789935489034/ezgif.com-gif-maker_13.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128835787489310/ezgif.com-gif-maker_25.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128897619525743/ezgif.com-gif-maker_4.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128902460801024/ezgif.com-gif-maker_17.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128906348134430/ezgif.com-gif-maker.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128911905849364/ezgif.com-gif-maker_2.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128914644205628/ezgif.com-gif-maker_5.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128917924544522/ezgif.com-gif-maker_10.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128929815527454/ezgif.com-gif-maker_15.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128939252842516/ezgif.com-gif-maker_14.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128953823330404/ezgif.com-gif-maker_18.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128963939860520/ezgif.com-gif-maker_22.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128965128028210/ezgif.com-gif-maker_16.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128977613946890/ezgif.com-gif-maker_21.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128993678262332/ezgif.com-gif-maker_8.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128993698840647/ezgif.com-gif-maker_24.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834129014779543622/ezgif.com-gif-maker_3.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834129015216406538/ezgif.com-gif-maker_7.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834129022321295380/ezgif.com-gif-maker_11.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834129024216334367/ezgif.com-gif-maker_23.gif"
                           ]
                image = random.choice(choices)

                embed = discord.Embed(description=dom.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name


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

                embed = discord.Embed(description=dom.format(author,mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif author_gender == 'female':
            if mention_gender == 'male':
                author = ctx.message.author.name


                dom = '**{0} dominates {1}**'

                choices = ['https://cdn.discordapp.com/attachments/798913238229188608/902643142426247199/ezgif.com-gif-maker_-_2021-10-26T223710.267.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/902643134486442004/ezgif.com-gif-maker_97.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/902643133651779606/ezgif.com-gif-maker_-_2021-10-26T223733.116.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/902643131776892968/ezgif.com-gif-maker_-_2021-10-26T223722.586.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/902643130619273327/ezgif.com-gif-maker_100.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/902643128199159848/ezgif.com-gif-maker_98.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/902643116593520711/ezgif.com-gif-maker_99.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/902643104442630154/ezgif.com-gif-maker_-_2021-10-26T223741.764.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/902643094393090108/ezgif.com-gif-maker_-_2021-10-26T223750.127.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/902643087426342953/ezgif.com-gif-maker_96.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=dom.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name


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

                embed = discord.Embed(description=dom.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)
    @dom.error
    async def dom_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()

        raise error

    @commands.command(aliases=['69'])
    @commands.is_nsfw()
    async def sixtynine(self, ctx, message=None):
        """69 command"""
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author_gender = determineGender(ctx.author)
        if mentions == message:
            if message == None:
                embed = discord.Embed(description=f"**You can't 69 nothing you horni dumbo\nExample use: $69 @User#6969**", colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                if author_gender == 'male':
                    author = ctx.message.author.name
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
                               'https://i.imgur.com/U3LDNCF.gif',
                               'https://media.discordapp.net/attachments/530484675613949973/819838016972390420/image0.gif']
                    image = random.choice(choices)

                    embed = discord.Embed(description=sixtynine.format(author, mentions),
                                          colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

                elif author_gender == 'female':
                    author = ctx.message.author.name

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
                               'https://i.imgur.com/U3LDNCF.gif',
                               'https://media.discordapp.net/attachments/530484675613949973/819838016972390420/image0.gif']
                    image = random.choice(choices)

                    embed = discord.Embed(description=sixtynine.format(author, mentions),
                                          colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

        mention_gender = determineGender(ctx.message.mentions[0])

        if author_gender == 'male':
            if mention_gender == 'female':
                author = ctx.message.author.name


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
                           'https://i.imgur.com/U3LDNCF.gif',
                           'https://media.discordapp.net/attachments/530484675613949973/819838016972390420/image0.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=sixtynine.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name


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

                embed = discord.Embed(description=sixtynine.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif author_gender == 'female':
            if mention_gender == 'male':
                author = ctx.message.author.name


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
                           'https://i.imgur.com/U3LDNCF.gif',
                           'https://media.discordapp.net/attachments/530484675613949973/819838016972390420/image0.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=sixtynine.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name


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

                embed = discord.Embed(description=sixtynine.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

    @sixtynine.error
    async def sixtynine_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()

        raise error

    @commands.command(aliases=['cream'])
    @commands.is_nsfw()
    async def creampie(self, ctx, message=None):
        """Creampie command"""
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author_gender = determineGender(ctx.author)
        if mentions == message:
            if message == None:
                embed = discord.Embed(description=f"**You can't creampie nothing you horni dumbo\nExample use: $creampie @User#6969**", colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                if author_gender == 'male':
                    author = ctx.message.author.name

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

                    embed = discord.Embed(description=sixtynine.format(author, mentions),
                                          colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)
                elif author_gender == 'female':
                    author = ctx.message.author.name

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

                    embed = discord.Embed(description=sixtynine.format(author, mentions),
                                          colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

        mention_gender = determineGender(ctx.message.mentions[0])

        if author_gender == 'male':
                if mention_gender == 'female':
                    author = ctx.message.author.name


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

                    embed = discord.Embed(description=sixtynine.format(author, mentions.name), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

                else:
                    author = ctx.message.author.name


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

                    embed = discord.Embed(description=sixtynine.format(author, mentions.name), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

        elif author_gender == 'female':
                if mention_gender == 'male':
                    author = ctx.message.author.name


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

                    embed = discord.Embed(description=sixtynine.format(author, mentions.name), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

                else:
                    author = ctx.message.author.name


                    sixtynine = '**{0} creampies {1}**'

                    choices = [
                        'http://porngifmag.com/content/2016/08/agnes-strapon-creampie-after-the-breakfast_008.gif',
                        'https://barris4congress.com/img/lick-cum-from-ass-3.gif',
                        'https://i.imgur.com/7NMAMrk.gif',
                        'https://i.imgur.com/4zAQA6c.gif',
                        'https://i.imgur.com/xHFX1vQ.gif',
                        'https://i.imgur.com/JZO7n1B.gif']
                    image = random.choice(choices)

                    embed = discord.Embed(description=sixtynine.format(author, mentions.name), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

    @creampie.error
    async def creampie_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()

        raise error

    @commands.command(aliases=['licks'])
    @commands.is_nsfw()
    async def lick(self, ctx, message=None):
        """Licks the member you mention"""
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author_gender = determineGender(ctx.author)
        if mentions == message:
            if message == None:
                embed = discord.Embed(description=f"**You can't lick nothing you horni dumbo\nExample use: $lick @User#6969**", colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                if author_gender == 'male':
                    author = ctx.message.author.name

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
                               'https://i.imgur.com/KncvJ93.gif',
                               'https://media.discordapp.net/attachments/530484675613949973/819837973390295080/image0.gif',
                               'https://media.discordapp.net/attachments/530484675613949973/819838369637990481/image0.gif',
                               'https://cdn.discordapp.com/attachments/530484675613949973/819838615533780992/image0.gif']
                    image = random.choice(choices)

                    embed = discord.Embed(description=lick.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)
                elif author_gender == 'female':
                    author = ctx.message.author.name

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
                               'https://i.imgur.com/LSJCxQO.gif'
                               ]
                    image = random.choice(choices)

                    embed = discord.Embed(description=lick.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)


        mention_gender = determineGender(ctx.message.mentions[0])

        if author_gender == 'male':
            if mention_gender == 'female':
                author = ctx.message.author.name

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
                           'https://i.imgur.com/KncvJ93.gif',
                           'https://media.discordapp.net/attachments/530484675613949973/819837973390295080/image0.gif',
                           'https://media.discordapp.net/attachments/530484675613949973/819838369637990481/image0.gif',
                           'https://cdn.discordapp.com/attachments/530484675613949973/819838615533780992/image0.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=lick.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name


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

                embed = discord.Embed(description=lick.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif author_gender == 'female':
            if mention_gender == 'male':
                author = ctx.message.author.name

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
                           'https://i.imgur.com/LSJCxQO.gif'
                           ]
                image = random.choice(choices)

                embed = discord.Embed(description=lick.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name


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
                           'https://i.imgur.com/SFcuA3e.gif',
                           'https://media.discordapp.net/attachments/530484675613949973/819838306883338280/image0.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=lick.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

    @lick.error
    async def lick_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()
        raise error

    @commands.command(aliases=['tiddies', 'tiddy'])
    @commands.is_nsfw()
    async def tits(self, ctx):
        tits = '**Here are some tiddies for ya**'

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
                   'https://i.imgur.com/MCYfXpP.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697495051625955438/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697495066284916877/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697495080243560518/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697495115588960316/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697495124455849994/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697495128021008424/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697495137860976810/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697495185961123961/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697495193468928000/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697495214633254912/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697495218408259674/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697495225626787910/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697495227606499478/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697495228549955654/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697495228571189268/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697495230215094392/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697507003924480089/3ce54ecf141689410ebb2d8f52b5499f.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697507039592841276/4a711e518e3f4b419c4b737a6be2061f.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697507065270239372/92Pp9qT.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697507096505221200/787d4bbec15247e68778396818f98840.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697507142919258152/992_450.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697507265627947099/6248-college-hottie-flashing-her-titties.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697507334204686356/yXh8CHH.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697507671485579264/59173361.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697507817384443964/f1726a7d63af741ea9cee246c0634d78.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697507901287432292/gif-titties-5.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697507945155395785/niceboobreveal-15621730278c4pl.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697508473461538876/tumblr_ntqyoikezu1s6jgbco1_400_01D4XFGNR94SEJ2Q2939K4GM38.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697508509268312105/tumblr_oqls87Q8Av1vbfdllo2_500.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697509564425175100/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697518602290593873/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697527102198513664/1ny2hj.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697527139225829396/4-1.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697527173166137405/8df3a56a-2635-4056-b9da-7b3be9af3f07.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697527212575817758/21db1d9dcc683042288d9e93b36d7320.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697527264635781260/72fc5cd5b5c379d5c3a6a83792f46573.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697527301457576047/75fe6c971f2fcc8b234f6ea9b50ee31e.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697527337834774618/115e0bb85e2c9b00dc4f847d1ebc488a.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697527406436679690/836_1000.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697527465178038403/8430-beautiful-small-perky-tits-teen-in-skin-tight-blue-dress.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697527495250936230/102109.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697527534895759503/124620.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697528112161882182/15218241628c4pl.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697528162065842222/a5cf23a06ba6b1439dde60ac3ab2028f.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697528261562859600/bc74a8750de91577fc5c5e7645aa990e.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697528414428725334/fc3f54aeaa1417cfa9aae1a8914e1c83.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697528458481500181/Horny-asian-teen-really-loves-big-cock.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697528509110943834/hotboobsdropreveal-15823135158c4pl.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697528566316924938/hugemelontitreveala-1568511943lp4c8.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697528617458073693/MissyMae-fucking-bigtits-porn-teensex.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697528686274150500/perfecttittiesgif-1546541579p48lc.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697528756977402028/realnakedgirls_0025.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697528814997209128/realnakedgirlsueiwj-1526143622c84lp.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697528952268390470/tumblr_np5kkvBhMq1qzb8n8o9_500.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697528991409504296/unnamed.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697529033302474822/vkvlrj-1525411351p4l8c.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697529070690500629/YearlyEnormousAlaskajingle-size_restricted.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697529214122852452/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697529306813038632/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697529422542143564/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697529522152800307/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697529612506366053/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697529626943029398/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697529692319776778/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697529709331742790/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697534320696623124/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697534325545107470/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697534337780023386/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697534343085817916/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697534351524626442/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697534364661186670/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697534368025018500/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697534384529604638/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697534392557633646/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697534400878870538/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697534466402549780/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697534489555107950/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697534510916435978/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697534524766027857/image0.gif',
                   'https://cdn.discordapp.com/attachments/694996260851286048/697534541249904760/image0.gif',
                   ]
        image = random.choice(choices)

        embed = discord.Embed(description=tits, colour=discord.Colour.blue())
        embed.set_image(url=image)

        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_nsfw()
    async def tease(self, ctx, message=None):
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author_gender = determineGender(ctx.author)
        if mentions == message:
            if message == None:
                embed = discord.Embed(description=f"**You can't tease nothing you horni dumbo\nExample use: $tease @User#6969**", colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                if author_gender == 'male':
                    author = ctx.message.author.name

                    tease = '**{0} teases {1}**'

                    choices = [
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
                    embed = discord.Embed(description=tease.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)
                elif author_gender == 'female':
                    author = ctx.message.author.name

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
                    embed = discord.Embed(description=tease.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

        mention_gender = determineGender(ctx.message.mentions[0])
        if author_gender == 'male':
            if mention_gender == 'female':
                author = ctx.message.author.name

                tease = '**{0} teases {1}**'

                choices = [
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
                embed = discord.Embed(description=tease.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name


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
                embed = discord.Embed(description=tease.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif author_gender == 'female':
            if mention_gender == 'male':
                author = ctx.message.author.name

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
                embed = discord.Embed(description=tease.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name


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
                embed = discord.Embed(description=tease.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)
        
    @tease.error
    async def tease_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()
        raise error

    @commands.command()
    @commands.is_nsfw()
    async def finger(self, ctx, message=None):
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author_gender = determineGender(ctx.author)
        if mentions == message:
            if message == None:
                embed = discord.Embed(description=f"**You can't finger nothing you horni dumbo\nExample use: $finger @User#6969**", colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                if author_gender == 'male':
                    author = ctx.message.author.name

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

                    embed = discord.Embed(description=finger.format(author, mentions),
                                          colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)
                elif author_gender == 'female':
                    author = ctx.message.author.name

                    finger = '**{0} fingers {1}**'
                    choices = [
                        'https://49.media.tumblr.com/280ce1aa102df8a42d87175d8388f9bc/tumblr_nqx7t1nKF81snzlxso1_400.gif',
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

                    embed = discord.Embed(description=finger.format(author, mentions),
                                          colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

        mention_gender = determineGender(ctx.message.mentions[0])

        if author_gender == 'male':
            if mention_gender == 'female':
                author = ctx.message.author.name

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

                embed = discord.Embed(description=finger.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name

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

                embed = discord.Embed(description=finger.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif author_gender == 'female':
            if mention_gender == 'male':
                author = ctx.message.author.name

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

                embed = discord.Embed(description=finger.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name

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

                embed = discord.Embed(description=finger.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)
            
    @finger.error
    async def finger_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()
        raise error

    @commands.command(aliases=['ass'])
    @commands.is_nsfw()
    async def booty(self, ctx):
        ass = '**Here is some booty for you**'

        choices = ['https://i.imgur.com/RqpvXVg.gif',
                    'https://i.imgur.com/ZJ5RMrm.gif',
                    'https://i.imgur.com/QrFimJF.gif',
                    'https://i.imgur.com/O3l8RaU.gif',
                    'https://i.imgur.com/TF6NJl4.gif',
                    'https://i.imgur.com/15xXYVZ.gif',
                    'https://i.imgur.com/cex2lVO.gif',
                    'https://i.imgur.com/PqM7kpy.gif',
                    'https://i.imgur.com/1lg0Xuv.gif',
                    'https://i.imgur.com/kRTBnEp.gif',
                    'https://i.imgur.com/9lYd8Q4.gif',
                    'https://i.imgur.com/AnojR9N.gif',
                    'https://i.imgur.com/0Xv27fj.gif',
                    'https://i.imgur.com/I0lZk8K.gif',
                    'https://i.imgur.com/1ay2m64.gif',
                    'https://i.imgur.com/sWb0SDl.gif',
                    'https://i.imgur.com/aOlf9Am.gif',
                    'https://i.imgur.com/2G9KEaw.gif',
                    'https://i.imgur.com/yxFn4if.gif',
                    'https://i.imgur.com/lUTdexl.gif',
                    'https://i.imgur.com/ahEayLe.gif',
                    'https://i.imgur.com/IpFoDQw.gif',
                    'https://i.imgur.com/h0l8BZL.gif',
                    'https://i.imgur.com/xG99n90.gif',
                    'https://i.imgur.com/rZ6YQil.gif',
                    'https://i.imgur.com/VX4fItZ.gif',
                    'https://i.imgur.com/DMpBUY0.gif',
                    'https://i.imgur.com/Uk5VruT.gif',
                    'https://i.imgur.com/8E2OOUN.gif',
                    'https://i.imgur.com/cHjwQkx.gif',
                    'https://i.imgur.com/Q5MV7nF.gif',
                    'https://i.imgur.com/cM2LON7.gif',
                    'https://i.imgur.com/f5ETI0P.gif',
                    'https://i.imgur.com/1UoCL9w.gif',
                    'https://i.imgur.com/jelRIkR.gif',
                    'https://i.imgur.com/GZXLL0v.gif',
                    'https://i.imgur.com/9m7wxB1.gif',
                    'https://i.imgur.com/QqxcfA7.gif',
                    'https://i.imgur.com/xZyQJgW.gif',
                    'https://i.imgur.com/oX8nOKs.gif',
                    'https://i.imgur.com/po2sPQ2.gif',
                    'https://i.imgur.com/bNXcYMD.gif',
                    'https://i.imgur.com/ijbotYC.gif',
                    'https://i.imgur.com/9kU4HOy.gif',
                    'https://i.imgur.com/AFrKcw0.gif',
                    'https://i.imgur.com/27XwR11.gif',
                    'https://i.imgur.com/eSgpK6y.gif',
                    'https://i.imgur.com/x3brY8U.gif',
                    'https://i.imgur.com/RWkkKpc.gif',
                    'https://i.imgur.com/AlN9oai.gif',
                    'https://i.imgur.com/8J65Ljh.gif',
                    'https://i.imgur.com/yaExBqv.gif',
                    'https://i.imgur.com/2oSjj7k.gif',
                    'https://i.imgur.com/YPpXkJZ.gif',
                    'https://i.imgur.com/d8WRYmX.gif',
                    'https://i.imgur.com/YpZSrGt.gif',
                    'https://i.imgur.com/cDhKCEw.gif',
                    'https://i.imgur.com/lAdyqoZ.gif',
                    'https://i.imgur.com/XFXdg0m.gif',
                    'https://i.imgur.com/GUqr6XX.gif',
                    'https://i.imgur.com/SslIMxT.gif',
                    'https://i.imgur.com/pw5LcHN.gif',
                    'https://i.imgur.com/IuC6PJ0.gif',
                    'https://i.imgur.com/Juksvnt.gif',
                    'https://i.imgur.com/eFalTcj.gif',
                    'https://i.imgur.com/SgPoB7b.gif',
                    'https://i.imgur.com/rKubRE6.gif',
                    'https://i.imgur.com/OzWE3Wp.gif',
                    'https://i.imgur.com/rzpNJdg.gif',
                    'https://i.imgur.com/IfXlpiY.gif',
                    'https://i.imgur.com/21N5Taz.gif',
                    'https://i.imgur.com/5zr1Zz9.gif',
                    'https://i.imgur.com/p0EtHbo.gif',
                    'https://i.imgur.com/ULx9QZR.gif',
                    'https://i.imgur.com/f0l9Whm.gif',
                    'https://i.imgur.com/DN94dGk.gif',
                    'https://i.imgur.com/AIWY35J.gif',
                    'https://i.imgur.com/XVj11LY.gif',
                    'https://i.imgur.com/Y0dzbJN.gif',
                    'https://i.imgur.com/LMCTtXx.gif',
                    'https://i.imgur.com/BQfSPDw.gif',
                    'https://i.imgur.com/tVX6DDF.gif',
                    'https://i.imgur.com/HMHex1V.gif',
                    'https://i.imgur.com/GK4LWTW.gif',
                    'https://i.imgur.com/0w070Jd.gif',
                    'https://i.imgur.com/IyC82z1.gif',
                    'https://i.imgur.com/Y1aQwrp.gif',
                    'https://i.imgur.com/IpmcMZx.gif',
                    'https://i.imgur.com/RGnIdQW.gif',
                    'https://i.imgur.com/F8okcfZ.gif',
                    'https://i.imgur.com/k3aev3V.gif',
                    'https://i.imgur.com/B6KHSwe.gif',
                    'https://i.imgur.com/NoE19KV.gif',
                    'https://i.imgur.com/FcoYbHL.gif',
                    'https://i.imgur.com/ausaQti.gif',
                    'https://i.imgur.com/dWcbj2t.gif',
                    'https://i.imgur.com/Mmc5YLm.gif',
                    'https://i.imgur.com/kolWaYQ.gif',
                    'https://i.imgur.com/698Fzws.gif',
                    'https://i.imgur.com/JCYCGWq.gif',
                    'https://i.imgur.com/BTeEFAH.gif',
                    'https://i.imgur.com/jGN811o.gif',
                    'https://i.imgur.com/OnDKlen.gif',
                    'https://i.imgur.com/EvnmuRy.gif',
                    'https://i.imgur.com/pBLHewF.gif',
                    'https://i.imgur.com/Nev3fHT.gif',
                    'https://i.imgur.com/Q59geBY.gif',
                    'https://i.imgur.com/KiSv9Gf.gif',
                    'https://i.imgur.com/SEYP2EN.gif',
                    'https://i.imgur.com/XpOHDvS.gif',
                    'https://i.imgur.com/IlX4mur.gif',
                    'https://i.imgur.com/CC6gFnd.gif',
                    'https://i.imgur.com/Lq5k9Ax.gif',
                    'https://i.imgur.com/H7svqbJ.gif',
                    'https://i.imgur.com/SqIr4xK.gif',
                    'https://i.imgur.com/A5kpsmV.gif',
                    'https://i.imgur.com/bYk5svg.gif',
                    'https://i.imgur.com/ews5Q2l.gif',
                    'https://i.imgur.com/zz6idf7.gif',
                    'https://i.imgur.com/Y0vrDbd.gif',
                    'https://i.imgur.com/AuwOHFW.gif',
                    'https://i.imgur.com/iaIwVgW.gif',
                    'https://i.imgur.com/uv2dN8f.gif',
                    'https://i.imgur.com/JvKMawF.gif',
                    'https://i.imgur.com/kuLn5o2.gif',
                    'https://i.imgur.com/TUAOhbK.gif',
                    'https://i.imgur.com/xyRUtdP.gif',
                    'https://i.imgur.com/qnlohKW.gif',
                    'https://i.imgur.com/4egZ3A4.gif',
                    'https://i.imgur.com/9xd0dDz.gif',
                    'https://i.imgur.com/sSQbWxG.gif',
                    'https://i.imgur.com/fAInxmN.gif']

        image = random.choice(choices)

        embed = discord.Embed(description=ass, colour=discord.Colour.blue())
        embed.set_image(url=image)

        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_nsfw()
    async def bite(self, ctx, message=None):
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author_gender = determineGender(ctx.author)
        if mentions == message:
            if message == None:
                embed = discord.Embed(description=f"**You can't bite nothing you horni dumbo\nExample use: $bite @User#6969**", colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                if author_gender == 'male':
                    author = ctx.message.author.name

                    bite = '**{0} bites {1}**'

                    choices = ['https://i.imgur.com/DfXChod.gif',
                               'https://i.imgur.com/8EmxUDt.gif',
                               'https://i.imgur.com/twkzbeS.gif',
                               'https://i.imgur.com/RdFmVr4.gif',
                               'https://i.imgur.com/wfDATY6.gif',
                               'https://i.imgur.com/QcRC7aP.gif',
                               'https://i.imgur.com/5kKyidf.gif',
                               'https://i.imgur.com/kia6vXA.gif',
                               'https://i.imgur.com/vWxiGkN.gif',
                               'https://i.imgur.com/rbKfRJu.gif'
                               ]
                    image = random.choice(choices)

                    embed = discord.Embed(description=bite.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

                elif author_gender == 'female':
                    author = ctx.message.author.name

                    bite = '**{0} bites {1}**'

                    choices = ['https://i.imgur.com/8wQK85v.gif',
                               'https://i.imgur.com/bZUlaSX.gif',
                               'https://i.imgur.com/KsQn9Nl.gif',
                               'https://i.imgur.com/qzCS7Fb.gif',
                               'https://i.imgur.com/H5bLbez.gif',
                               'https://i.imgur.com/TloqNAr.gif',
                               'https://i.imgur.com/I0eBNt1.gif',
                               'https://i.imgur.com/g68opeU.gif',
                               'https://i.imgur.com/IWEZeU4.gif'
                               ]
                    image = random.choice(choices)

                    embed = discord.Embed(description=bite.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

        mention_gender = determineGender(ctx.message.mentions[0])
        if author_gender == 'male':
            if mention_gender == 'female':
                    author = ctx.message.author.name

                    bite = '**{0} bites {1}**'

                    choices = ['https://i.imgur.com/DfXChod.gif',
                               'https://i.imgur.com/8EmxUDt.gif',
                               'https://i.imgur.com/twkzbeS.gif',
                               'https://i.imgur.com/RdFmVr4.gif',
                               'https://i.imgur.com/wfDATY6.gif',
                               'https://i.imgur.com/QcRC7aP.gif',
                               'https://i.imgur.com/5kKyidf.gif',
                               'https://i.imgur.com/kia6vXA.gif',
                               'https://i.imgur.com/vWxiGkN.gif',
                               'https://i.imgur.com/rbKfRJu.gif'
                               ]
                    image = random.choice(choices)

                    embed = discord.Embed(description=bite.format(author, mentions.name), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

            else:
                    author = ctx.message.author.name


                    bite = '**{0} bites {1}**'

                    choices = ['https://i.imgur.com/qknbidS.gif',
                               'https://i.imgur.com/AM0zDqp.gif',
                               'https://i.imgur.com/VsPzuep.gif',
                               'https://i.imgur.com/Ch75jYN.gif',
                               'https://i.imgur.com/Ch75jYN.gif',
                               'https://i.imgur.com/PyJBbVi.gif',
                               'https://i.imgur.com/PtKsG9O.gif',
                               'https://i.imgur.com/2qogNb8.gif',
                               'https://i.imgur.com/9nVcYuO.gif',
                               'https://i.imgur.com/MZs215n.gif'
                               ]
                    image = random.choice(choices)

                    embed = discord.Embed(description=bite.format(author, mentions.name), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

        elif author_gender == 'female':
            if mention_gender == 'male':
                    author = ctx.message.author.name

                    bite = '**{0} bites {1}**'

                    choices = ['https://i.imgur.com/8wQK85v.gif',
                               'https://i.imgur.com/bZUlaSX.gif',
                               'https://i.imgur.com/KsQn9Nl.gif',
                               'https://i.imgur.com/qzCS7Fb.gif',
                               'https://i.imgur.com/H5bLbez.gif',
                               'https://i.imgur.com/TloqNAr.gif',
                               'https://i.imgur.com/I0eBNt1.gif',
                               'https://i.imgur.com/g68opeU.gif',
                               'https://i.imgur.com/IWEZeU4.gif'
                               ]
                    image = random.choice(choices)

                    embed = discord.Embed(description=bite.format(author, mentions.name), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

            else:
                    author = ctx.message.author.name


                    bite = '**{0} bites {1}**'

                    choices = ['https://i.imgur.com/pHCvWzF.gif',
                               'https://i.imgur.com/6gWhjNO.gif',
                               'https://i.imgur.com/VhTd8XP.gif',
                               'https://i.imgur.com/F6v2gal.gif',
                               'https://i.imgur.com/k6aiL1L.gif',
                               'https://i.imgur.com/Jc0VO4U.gif',
                               'https://i.imgur.com/E79Jtsk.gif',
                               'https://i.imgur.com/YuZayDZ.gif',
                               'https://i.imgur.com/Gp0YumK.gif'
                               ]
                    image = random.choice(choices)

                    embed = discord.Embed(description=bite.format(author, mentions.name), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

    @bite.error
    async def bite_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()

        raise error

    @commands.command()
    @commands.is_nsfw()
    async def massage(self, ctx, message=None):
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author_gender = determineGender(ctx.author)
        if mentions == message:
            if message == None:
                embed = discord.Embed(description=f"**You can't massage nothing you horni dumbo\nExample use: $massage @User#6969**", colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                if author_gender == 'male':
                    author = ctx.message.author.name

                    massage = '**{0} gives {1} a good massage**'

                    choices = ['https://i.imgur.com/7j0ZQxU.gif',
                               'https://i.imgur.com/p5eAQdw.gif',
                               'https://i.imgur.com/TjS39RP.gif',
                               'https://i.imgur.com/2lQ7Fj9.gif',
                               'https://i.imgur.com/VtD3sir.gif',
                               'https://cdn.discordapp.com/attachments/694996260851286048/704102396426453062/image0.gif',
                               'https://cdn.discordapp.com/attachments/694996260851286048/704102400730071140/image0.gif',
                               'https://cdn.discordapp.com/attachments/694996260851286048/704102442874437712/image0.gif',
                               'https://cdn.discordapp.com/attachments/694996260851286048/704102470904840232/image0.gif',
                               'https://cdn.discordapp.com/attachments/694996260851286048/704102492014641162/image0.gif',
                               'https://cdn.discordapp.com/attachments/694996260851286048/704102506774528088/image0.gif',
                               'https://cdn.discordapp.com/attachments/694996260851286048/704102524289941614/image0.gif',
                               'https://cdn.discordapp.com/attachments/694996260851286048/704102598659276830/image0.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/820749974673031198/20661170.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/820749967432876089/21523587.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/820749964148736028/22422652.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/820749960680308786/22422659.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/820749957971050516/15232583.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/820749951428460574/6179573.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/820749947279638558/6489006.gif']
                    image = random.choice(choices)
                    embed = discord.Embed(description=massage.format(author, mentions),
                                          colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)
                elif author_gender == 'female':
                    author = ctx.message.author.name

                    massage = '**{0} gives {1} a good massage**'

                    choices = ['https://i.imgur.com/6diCV8t.gif',
                               'https://i.imgur.com/QMTb0XJ.gif',
                               'https://cdn.discordapp.com/attachments/694996260851286048/704102458875707442/image0.gif',
                               'https://cdn.discordapp.com/attachments/694996260851286048/704102537543942275/image0.gif',
                               'https://cdn.discordapp.com/attachments/694996260851286048/704102543168503928/image0.gif',
                               'https://cdn.discordapp.com/attachments/694996260851286048/704102555478655117/image0.gif',
                               'https://cdn.discordapp.com/attachments/694996260851286048/704102564853055579/image0.gif']
                    image = random.choice(choices)
                    embed = discord.Embed(description=massage.format(author, mentions),
                                          colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

        mention_gender = determineGender(ctx.message.mentions[0])
        if author_gender == 'male':
            if mention_gender == 'female':
                author = ctx.message.author.name

                massage = '**{0} gives {1} a good massage**'

                choices = ['https://i.imgur.com/7j0ZQxU.gif',
                           'https://i.imgur.com/p5eAQdw.gif',
                           'https://i.imgur.com/TjS39RP.gif',
                           'https://i.imgur.com/2lQ7Fj9.gif',
                           'https://i.imgur.com/VtD3sir.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704102396426453062/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704102400730071140/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704102442874437712/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704102470904840232/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704102492014641162/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704102506774528088/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704102524289941614/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704102598659276830/image0.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820749974673031198/20661170.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820749967432876089/21523587.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820749964148736028/22422652.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820749960680308786/22422659.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820749957971050516/15232583.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820749951428460574/6179573.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820749947279638558/6489006.gif']
                image = random.choice(choices)
                embed = discord.Embed(description=massage.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name

                massage = '**{0} gives {1} a good massage**'

                choices = ['https://i.imgur.com/ShHd8kN.gif',
                           'https://i.imgur.com/4iuasHV.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704104033526349864/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704104037653545062/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704104046193016832/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704104052241203280/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704104060973744189/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704104064484376596/image0.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820336871779467274/21536599_1.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820336865033977876/22759245.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820336865064255558/23686295.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820336863818678302/1687372a.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820336856607752232/22329142.gif']
                image = random.choice(choices)
                embed = discord.Embed(description=massage.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif author_gender == 'female':
            if mention_gender == 'male':
                author = ctx.message.author.name

                massage = '**{0} gives {1} a good massage**'

                choices = ['https://i.imgur.com/6diCV8t.gif',
                           'https://i.imgur.com/QMTb0XJ.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704102458875707442/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704102537543942275/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704102543168503928/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704102555478655117/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704102564853055579/image0.gif']
                image = random.choice(choices)
                embed = discord.Embed(description=massage.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name

                massage = '**{0} gives {1} a good massage**'

                choices = ['https://i.imgur.com/Ed8NcW4.gif',
                           'https://i.imgur.com/VhYzXOf.gif',
                           'https://i.imgur.com/zmQ7m27.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704102378550460476/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704102381549256744/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704102408107720754/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704102425677529138/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704102429624631438/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704102437803524186/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704102453624176701/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704102474096836718/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704102520439439380/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/704102596612456539/image0.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820584864356892702/24313926.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820584755036553236/24474752.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820584746706927636/24179972.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820584740494901269/24176950.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820337115912863774/21384983.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820337113077383248/20685582.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820337110984687676/19881824.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820337101470957578/17282617.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820337097092497428/20867954.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820337079317037056/20693392.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820337073859854356/6179524.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820337073960517672/22422665.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820337052372828170/18322781.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820337030671368253/15008632.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820337018294894623/12956153.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820337009918869504/12477370.gif']
                image = random.choice(choices)
                embed = discord.Embed(description=massage.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

    @massage.error
    async def massage_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()
        raise error

    @commands.command(aliases=['ropeplay'])
    @commands.is_nsfw()
    async def bondage(self, ctx, message=None):
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author_gender = determineGender(ctx.author)
        if mentions == message:
            if message == None:
                embed = discord.Embed(description=f"**You can't bondage nothing you horni dumbo\nExample use: $bondage @User#6969**", colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                if author_gender == 'male':
                    author = ctx.message.author.name

                    sixtynine = '**{0} bondages {1}**'

                    choices = ['https://i.imgur.com/vZO2Y0e.gif',
                               'https://i.imgur.com/LvIz1GP.gif',
                               'https://i.imgur.com/VcYTQ27.gif',
                               'https://i.imgur.com/tpiXCZI.gif',
                               'https://i.imgur.com/3AA1nw9.gif',
                               'https://i.imgur.com/sYXmhWU.gif',
                               'https://i.imgur.com/JWV3vDy.gif',
                               'https://i.imgur.com/NvCICor.gif',
                               'https://i.imgur.com/u0uZi4v.gif',
                               'https://i.imgur.com/SvhpPhu.gif',
                               'https://i.imgur.com/CWEA3AK.gif',
                               'https://i.imgur.com/c3GfhnC.gif',
                               'https://i.imgur.com/ntEjUr7.gif',
                               'https://i.imgur.com/hoeN0Nz.gif',
                               'https://i.imgur.com/EQyDnKn.gif',
                               'https://i.imgur.com/cZS3P04.gif',
                               'https://i.imgur.com/GVQ7Ydf.gif',
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348334381301760/ezgif.com-gif-maker_5.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348342300672020/ezgif.com-gif-maker_4.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348348831334420/ezgif.com-gif-maker_6.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348354082209802/ezgif.com-optimize_5.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348358612189194/ezgif.com-optimize_2.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348363842879498/ezgif.com-optimize_6.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348368934895646/ezgif.com-optimize.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348373049507880/ezgif.com-optimize_3.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348376974589972/ezgif.com-optimize_4.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348382426923018/ezgif.com-optimize_7.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348385594802206/ezgif.com-resize_1.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348386848374792/ezgif.com-optimize_8.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348388748132392/ezgif.com-gif-maker_1.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348394096656435/ezgif.com-optimize_1.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348394637590558/ezgif.com-gif-maker.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348395271061534/ezgif.com-gif-maker_3.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348397304643594/ezgif.com-gif-maker_2.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348621582729256/ezgif.com-optimize_9.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825357946883670046/ezgif.com-gif-maker_4.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825357956702404629/ezgif.com-optimize.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825357962238754866/ezgif.com-optimize_1.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825357967905914932/ezgif.com-gif-maker_1.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825357973097676810/ezgif.com-gif-maker.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825357979162902609/ezgif.com-gif-maker_2.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825357982716002324/ezgif.com-optimize_6.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825357989917360148/ezgif.com-resize.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825357996099633162/ezgif.com-optimize_9.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825358000608116746/ezgif.com-optimize_2.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825358003074760734/ezgif.com-optimize_3.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825358009369624656/ezgif.com-resize_1.gif"
                               ]
                    image = random.choice(choices)

                    embed = discord.Embed(description=sixtynine.format(author, mentions),
                                          colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

                elif author_gender == 'female':
                    author = ctx.message.author.name

                    sixtynine = '**{0} bondages {1}**'

                    choices = ['https://i.imgur.com/vZO2Y0e.gif',
                               'https://i.imgur.com/LvIz1GP.gif',
                               'https://i.imgur.com/VcYTQ27.gif',
                               'https://i.imgur.com/tpiXCZI.gif',
                               'https://i.imgur.com/3AA1nw9.gif',
                               'https://i.imgur.com/sYXmhWU.gif',
                               'https://i.imgur.com/JWV3vDy.gif',
                               'https://i.imgur.com/NvCICor.gif',
                               'https://i.imgur.com/u0uZi4v.gif',
                               'https://i.imgur.com/SvhpPhu.gif',
                               'https://i.imgur.com/CWEA3AK.gif',
                               'https://i.imgur.com/c3GfhnC.gif',
                               'https://i.imgur.com/ntEjUr7.gif',
                               'https://i.imgur.com/hoeN0Nz.gif',
                               'https://i.imgur.com/EQyDnKn.gif',
                               'https://i.imgur.com/cZS3P04.gif',
                               'https://i.imgur.com/GVQ7Ydf.gif',
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348334381301760/ezgif.com-gif-maker_5.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348342300672020/ezgif.com-gif-maker_4.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348348831334420/ezgif.com-gif-maker_6.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348354082209802/ezgif.com-optimize_5.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348358612189194/ezgif.com-optimize_2.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348363842879498/ezgif.com-optimize_6.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348368934895646/ezgif.com-optimize.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348373049507880/ezgif.com-optimize_3.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348376974589972/ezgif.com-optimize_4.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348382426923018/ezgif.com-optimize_7.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348385594802206/ezgif.com-resize_1.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348386848374792/ezgif.com-optimize_8.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348388748132392/ezgif.com-gif-maker_1.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348394096656435/ezgif.com-optimize_1.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348394637590558/ezgif.com-gif-maker.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348395271061534/ezgif.com-gif-maker_3.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348397304643594/ezgif.com-gif-maker_2.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825348621582729256/ezgif.com-optimize_9.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825357946883670046/ezgif.com-gif-maker_4.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825357956702404629/ezgif.com-optimize.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825357962238754866/ezgif.com-optimize_1.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825357967905914932/ezgif.com-gif-maker_1.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825357973097676810/ezgif.com-gif-maker.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825357979162902609/ezgif.com-gif-maker_2.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825357982716002324/ezgif.com-optimize_6.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825357989917360148/ezgif.com-resize.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825357996099633162/ezgif.com-optimize_9.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825358000608116746/ezgif.com-optimize_2.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825358003074760734/ezgif.com-optimize_3.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825358009369624656/ezgif.com-resize_1.gif"
                               ]
                    image = random.choice(choices)

                    embed = discord.Embed(description=sixtynine.format(author, mentions),
                                          colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

        mention_gender = determineGender(ctx.message.mentions[0])

        if author_gender == 'male':
            if mention_gender == 'female':
                author = ctx.message.author.name

                sixtynine = '**{0} bondages {1}**'

                choices = ['https://i.imgur.com/vZO2Y0e.gif',
                           'https://i.imgur.com/LvIz1GP.gif',
                           'https://i.imgur.com/VcYTQ27.gif',
                           'https://i.imgur.com/tpiXCZI.gif',
                           'https://i.imgur.com/3AA1nw9.gif',
                           'https://i.imgur.com/sYXmhWU.gif',
                           'https://i.imgur.com/JWV3vDy.gif',
                           'https://i.imgur.com/NvCICor.gif',
                           'https://i.imgur.com/u0uZi4v.gif',
                           'https://i.imgur.com/SvhpPhu.gif',
                           'https://i.imgur.com/CWEA3AK.gif',
                           'https://i.imgur.com/c3GfhnC.gif',
                           'https://i.imgur.com/ntEjUr7.gif',
                           'https://i.imgur.com/hoeN0Nz.gif',
                           'https://i.imgur.com/EQyDnKn.gif',
                           'https://i.imgur.com/cZS3P04.gif',
                           'https://i.imgur.com/GVQ7Ydf.gif',
                           "https://cdn.discordapp.com/attachments/819857033489940481/825348334381301760/ezgif.com-gif-maker_5.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825348342300672020/ezgif.com-gif-maker_4.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825348348831334420/ezgif.com-gif-maker_6.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825348354082209802/ezgif.com-optimize_5.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825348358612189194/ezgif.com-optimize_2.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825348363842879498/ezgif.com-optimize_6.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825348368934895646/ezgif.com-optimize.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825348373049507880/ezgif.com-optimize_3.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825348376974589972/ezgif.com-optimize_4.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825348382426923018/ezgif.com-optimize_7.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825348385594802206/ezgif.com-resize_1.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825348386848374792/ezgif.com-optimize_8.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825348388748132392/ezgif.com-gif-maker_1.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825348394096656435/ezgif.com-optimize_1.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825348394637590558/ezgif.com-gif-maker.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825348395271061534/ezgif.com-gif-maker_3.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825348397304643594/ezgif.com-gif-maker_2.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825348621582729256/ezgif.com-optimize_9.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825357946883670046/ezgif.com-gif-maker_4.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825357956702404629/ezgif.com-optimize.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825357962238754866/ezgif.com-optimize_1.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825357967905914932/ezgif.com-gif-maker_1.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825357973097676810/ezgif.com-gif-maker.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825357979162902609/ezgif.com-gif-maker_2.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825357982716002324/ezgif.com-optimize_6.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825357989917360148/ezgif.com-resize.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825357996099633162/ezgif.com-optimize_9.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825358000608116746/ezgif.com-optimize_2.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825358003074760734/ezgif.com-optimize_3.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825358009369624656/ezgif.com-resize_1.gif"
                           ]
                image = random.choice(choices)

                embed = discord.Embed(description=sixtynine.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name

                sixtynine = '**{0} bondages {1}**'

                choices = ['https://i.imgur.com/VFNDRBy.gif',
                           'https://i.imgur.com/OYPnfiG.gif',
                           'https://i.imgur.com/PMbIso6.gif',
                           'https://i.imgur.com/76WonL8.gif',
                           'https://i.imgur.com/OOTp5n8.gif',
                           'https://i.imgur.com/zqQs5c7.gif',
                           'https://i.imgur.com/FiamEyG.gif',
                           'https://i.imgur.com/lK2eNHC.gif',
                           'https://i.imgur.com/bnDgk3P.gif',
                           'https://i.imgur.com/bGGkNS2.gif'
                           ]
                image = random.choice(choices)

                embed = discord.Embed(description=sixtynine.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif author_gender == 'female':
            if mention_gender == 'male':
                author = ctx.message.author.name

                sixtynine = '**{0} bondages {1}**'

                choices = ['https://i.imgur.com/aQDmyuD.gif',
                           'https://i.imgur.com/kipMUyV.gif',
                           'https://i.imgur.com/orUMNpW.gif',
                           'https://i.imgur.com/u0T5FEL.gif',
                           'https://i.imgur.com/m2JuNas.gif',
                           'https://i.imgur.com/OfRey1k.gif',
                           'https://i.imgur.com/JL3cTFx.gif',
                           'https://i.imgur.com/4j98RSc.gif',
                           'https://i.imgur.com/rUM9i6E.gif',
                           'https://i.imgur.com/88aDUTL.gif',
                           'https://i.imgur.com/mZLtYRR.gif',
                           'https://i.imgur.com/QOejpgx.gif'
                           ]
                image = random.choice(choices)

                embed = discord.Embed(description=sixtynine.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name

                sixtynine = '**{0} bondages {1}**'

                choices = ['https://i.imgur.com/jYXc3v5.gif',
                           'https://i.imgur.com/kUghQWX.gif',
                           'https://i.imgur.com/iXtEFR6.gif',
                           'https://i.imgur.com/rGcl1jw.gif',
                           'https://i.imgur.com/Hj1n6MF.gif',
                           'https://i.imgur.com/wdpaK77.gif',
                           'https://i.imgur.com/wFkl5f0.gif',
                           'https://i.imgur.com/qwjeb8x.gif',
                           'https://i.imgur.com/TlFBMAU.gif',
                           'https://i.imgur.com/H3OBHEl.gif',
                           'https://i.imgur.com/7iIsj8j.gif',
                           'https://i.imgur.com/UQm9bkS.gif',
                           'https://i.imgur.com/2FwvuWa.gif',
                           'https://i.imgur.com/0m8KsTa.gif',
                           'https://i.imgur.com/zYDRuwJ.gif',
                           'https://i.imgur.com/3pRD4Hr.gif',
                           "https://cdn.discordapp.com/attachments/819857033489940481/825342438163873792/ezgif.com-optimize_3.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825342443208572928/ezgif.com-optimize.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825342449601347594/ezgif.com-gif-maker.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825342456312627210/ezgif.com-gif-maker_1.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825342463316852767/ezgif.com-optimize_4.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825342466562981888/ezgif.com-gif-maker_2.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825342470572605450/ezgif.com-optimize_2.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825342476059148308/ezgif.com-resize.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825342476641894440/ezgif.com-optimize_1.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825342484367409182/ezgif.com-optimize_5.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825357946883670046/ezgif.com-gif-maker_4.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825357956702404629/ezgif.com-optimize.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825357962238754866/ezgif.com-optimize_1.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825357967905914932/ezgif.com-gif-maker_1.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825357973097676810/ezgif.com-gif-maker.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825357979162902609/ezgif.com-gif-maker_2.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825357982716002324/ezgif.com-optimize_6.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825357989917360148/ezgif.com-resize.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825357996099633162/ezgif.com-optimize_9.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825358000608116746/ezgif.com-optimize_2.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825358003074760734/ezgif.com-optimize_3.gif",
                           "https://cdn.discordapp.com/attachments/819857033489940481/825358009369624656/ezgif.com-resize_1.gif"
                           ]
                image = random.choice(choices)

                embed = discord.Embed(description=sixtynine.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

    @bondage.error
    async def bondage_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()
        raise error


    @commands.command()
    @commands.is_nsfw()
    async def cum(self, ctx, message=None):
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author_gender = determineGender(ctx.author)
        if mentions == message:
            if message == None:
                embed = discord.Embed(description=f"**You can't cum on nothing you horni dumbo\nExample use: $cum @User#6969**", colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                if author_gender == 'male':
                    author = ctx.message.author.name

                    cum = '**{0} cums on {1}**'

                    choices = ['https://i.imgur.com/JZFIbJC.gif',
                               'https://i.imgur.com/fTy57w7.gif',
                               'https://i.imgur.com/rwvuHWZ.gif',
                               'https://i.imgur.com/8qsYXbz.gif',
                               'https://i.imgur.com/IQEzJYZ.gif',
                               'https://i.imgur.com/bGuMzZv.gif',
                               'https://i.imgur.com/HKP8JIQ.gif',
                               'https://i.imgur.com/0WyJL3C.gif',
                               'https://i.imgur.com/GFiJwtv.gif',
                               'https://i.imgur.com/xf8AUjI.gif',
                               'https://i.imgur.com/yE6fGtq.gif',
                               'https://i.imgur.com/tgg5lwu.gif',
                               'https://i.imgur.com/wspWi39.gif',
                               'https://i.imgur.com/etntZIw.gif',
                               'https://i.imgur.com/OgOIDyb.gif',
                               'https://i.imgur.com/RroRPMR.gif',
                               'https://i.imgur.com/JkkI775.gif',
                               'https://i.imgur.com/f6SJF3N.gif',
                               'https://i.imgur.com/uyeTfjw.gif'
                               ]
                    image = random.choice(choices)

                    embed = discord.Embed(description=cum.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

                elif author_gender == 'female':
                    author = ctx.message.author.name

                    cum = '**{0} squirts for {1}**'

                    choices = ['https://i.imgur.com/fYdUQEZ.gif',
                               'https://i.imgur.com/gMuqer4.gif',
                               'https://i.imgur.com/Zb4CTGZ.gif',
                               'https://i.imgur.com/mEiknki.gif',
                               'https://i.imgur.com/A1wkvMl.gif',
                               'https://i.imgur.com/bPKxJW4.gif',
                               'https://i.imgur.com/llK0B4D.gif',
                               'https://i.imgur.com/jCg7CWd.gif',
                               'https://i.imgur.com/iw1LHCl.gif',
                               'https://i.imgur.com/IcmKt0N.gif',
                               'https://i.imgur.com/qYbaNYR.gif',
                               'https://i.imgur.com/YeDFzMw.gif',
                               'https://i.imgur.com/oooJIHd.gif',
                               'https://i.imgur.com/pB05kVV.gif',
                               'https://i.imgur.com/C2nk7Fl.gif',
                               'https://i.imgur.com/UtMB2nR.gif'
                               ]
                    image = random.choice(choices)

                    embed = discord.Embed(description=cum.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)


        mention_gender = determineGender(ctx.message.mentions[0])
        if author_gender == 'male':
            if mention_gender == 'female':
                author = ctx.message.author.name

                cum = '**{0} cums on {1}**'

                choices = ['https://i.imgur.com/JZFIbJC.gif',
                           'https://i.imgur.com/fTy57w7.gif',
                           'https://i.imgur.com/rwvuHWZ.gif',
                           'https://i.imgur.com/8qsYXbz.gif',
                           'https://i.imgur.com/IQEzJYZ.gif',
                           'https://i.imgur.com/bGuMzZv.gif',
                           'https://i.imgur.com/HKP8JIQ.gif',
                           'https://i.imgur.com/0WyJL3C.gif',
                           'https://i.imgur.com/GFiJwtv.gif',
                           'https://i.imgur.com/xf8AUjI.gif',
                           'https://i.imgur.com/yE6fGtq.gif',
                           'https://i.imgur.com/tgg5lwu.gif',
                           'https://i.imgur.com/wspWi39.gif',
                           'https://i.imgur.com/etntZIw.gif',
                           'https://i.imgur.com/OgOIDyb.gif',
                           'https://i.imgur.com/RroRPMR.gif',
                           'https://i.imgur.com/JkkI775.gif',
                           'https://i.imgur.com/f6SJF3N.gif',
                           'https://i.imgur.com/uyeTfjw.gif'
                           ]
                image = random.choice(choices)

                embed = discord.Embed(description=cum.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name

                cum = '**{0} cums on {1}**'

                choices = ['https://i.imgur.com/oe6BhDn.gif',
                           'https://i.imgur.com/KPKGWDg.gif',
                           'https://i.imgur.com/PuPVLQ7.gif',
                           'https://i.imgur.com/IxCMqGm.gif',
                           'https://i.imgur.com/eeuBQhm.gif',
                           'https://i.imgur.com/PgpeTaN.gif',
                           'https://i.imgur.com/GFkTXKc.gif',
                           'https://i.imgur.com/ZAMn6KF.gif',
                           'https://i.imgur.com/i0WFqbo.gif',
                           'https://i.imgur.com/xKygyWa.gif',
                           'https://i.imgur.com/zR3SCo1.gif',
                           'https://i.imgur.com/CtTKIbB.gif',
                           'https://i.imgur.com/P7h02RS.gif',
                           'https://i.imgur.com/cuXOLQk.gif',
                           'https://i.imgur.com/uhgDX5u.gif',
                           'https://i.imgur.com/L0xg8Mj.gif'
                           ]
                image = random.choice(choices)

                embed = discord.Embed(description=cum.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif author_gender == 'female':
            if mention_gender == 'male':
                author = ctx.message.author.name

                cum = '**{0} squirts for {1}**'

                choices = ['https://i.imgur.com/fYdUQEZ.gif',
                           'https://i.imgur.com/gMuqer4.gif',
                           'https://i.imgur.com/Zb4CTGZ.gif',
                           'https://i.imgur.com/mEiknki.gif',
                           'https://i.imgur.com/A1wkvMl.gif',
                           'https://i.imgur.com/bPKxJW4.gif',
                           'https://i.imgur.com/llK0B4D.gif',
                           'https://i.imgur.com/jCg7CWd.gif',
                           'https://i.imgur.com/iw1LHCl.gif',
                           'https://i.imgur.com/IcmKt0N.gif',
                           'https://i.imgur.com/qYbaNYR.gif',
                           'https://i.imgur.com/YeDFzMw.gif',
                           'https://i.imgur.com/oooJIHd.gif',
                           'https://i.imgur.com/pB05kVV.gif',
                           'https://i.imgur.com/C2nk7Fl.gif',
                           'https://i.imgur.com/UtMB2nR.gif'
                           ]
                image = random.choice(choices)

                embed = discord.Embed(description=cum.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name

                cum = '**{0} squirts for {1}**'

                choices = ['https://i.imgur.com/RDAlX6W.gif',
                           'https://i.imgur.com/XPNbVEa.gif',
                           'https://i.imgur.com/JCccOIo.gif',
                           'https://i.imgur.com/NYZ5czo.gif',
                           'https://i.imgur.com/bETXlmP.gif',
                           'https://i.imgur.com/CYx8gbR.gif',
                           'https://i.imgur.com/Lsefwon.gif',
                           'https://i.imgur.com/jRrR0WS.gif',
                           'https://i.imgur.com/yMBYE0N.gif',
                           'https://i.imgur.com/RVpZ7ev.gif',
                           'https://i.imgur.com/aRYXZEB.gif',
                           'https://i.imgur.com/U5e8MS9.gif',
                           'https://i.imgur.com/zPtajhY.gif',
                           'https://i.imgur.com/5LtXs05.gif'
                           ]
                image = random.choice(choices)

                embed = discord.Embed(description=cum.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

    @cum.error
    async def cum_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()

        raise error

    @commands.command()
    @commands.is_nsfw()
    async def collar(self, ctx, message=None):
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author_gender = determineGender(ctx.author)
        if mentions == message:
            if message == None:
                embed = discord.Embed(description=f"**You can't collar nothing you horni dumbo\nExample use: $collar @User#6969**", colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                if author_gender == 'male':
                    author = ctx.message.author.name

                    cum = '**{0} collars {1}**'

                    choices = ['https://i.imgur.com/GOyyn9W.gif',
                               'https://i.imgur.com/7yRqNrC.gif',
                               'https://i.imgur.com/2qLPOCG.gif',
                               'https://i.imgur.com/NDqNteW.gif',
                               'https://i.imgur.com/KBgCy2u.gif',
                               'https://i.imgur.com/K2FEEoH.gif',
                               'https://i.imgur.com/Cyp3i2f.gif',
                               'https://i.imgur.com/EFfrDSR.gif',
                               'https://i.imgur.com/wxSksqp.gif',
                               'https://i.imgur.com/ljpl0oO.gif',
                               'https://i.imgur.com/BPgXUjE.gif',
                               'https://i.imgur.com/BcJ7LwB.gif',
                               'https://i.imgur.com/OnppjzI.gif',
                               'https://i.imgur.com/3QYGUa7.gif'
                               ]
                    image = random.choice(choices)

                    embed = discord.Embed(description=cum.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

                elif author_gender == 'female':
                    author = ctx.message.author.name

                    cum = '**{0} collars {1}**'

                    choices = ['https://i.imgur.com/5psSaNC.gif',
                               'https://i.imgur.com/L5Zm9m8.gif',
                               'https://i.imgur.com/6SWhwD8.gif',
                               'https://i.imgur.com/HAWR1OH.gif']
                    image = random.choice(choices)

                    embed = discord.Embed(description=cum.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

        mention_gender = determineGender(ctx.message.mentions[0])
        if author_gender == 'male':
            if mention_gender == 'female':
                author = ctx.message.author.name

                cum = '**{0} collars {1}**'

                choices = ['https://i.imgur.com/GOyyn9W.gif',
                           'https://i.imgur.com/7yRqNrC.gif',
                           'https://i.imgur.com/2qLPOCG.gif',
                           'https://i.imgur.com/NDqNteW.gif',
                           'https://i.imgur.com/KBgCy2u.gif',
                           'https://i.imgur.com/K2FEEoH.gif',
                           'https://i.imgur.com/Cyp3i2f.gif',
                           'https://i.imgur.com/EFfrDSR.gif',
                           'https://i.imgur.com/wxSksqp.gif',
                           'https://i.imgur.com/ljpl0oO.gif',
                           'https://i.imgur.com/BPgXUjE.gif',
                           'https://i.imgur.com/BcJ7LwB.gif',
                           'https://i.imgur.com/OnppjzI.gif',
                           'https://i.imgur.com/3QYGUa7.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820983807188533248/ezgif.com-gif-maker.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820983818155851777/ezgif.com-resize_1.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820983844999659530/ezgif.com-gif-maker_7.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820983858580291594/ezgif.com-gif-maker_6.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820983871067389952/ezgif.com-gif-maker_3.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820983874217705512/ezgif.com-gif-maker_10.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820983874237628466/ezgif.com-gif-maker_2.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820983896241471498/ezgif.com-gif-maker_9.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820983901497458708/ezgif.com-resize.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820983905393704960/ezgif.com-gif-maker_5.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820983909822758942/ezgif.com-gif-maker_15.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820983915019763723/ezgif.com-gif-maker_4.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820983918769471528/ezgif.com-gif-maker_8.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820983926314631188/ezgif.com-gif-maker_13.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820983927950802994/ezgif.com-gif-maker_16.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820983936720830484/ezgif.com-gif-maker_12.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820983941820317706/ezgif.com-gif-maker_11.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820983942031081472/ezgif.com-gif-maker_14.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820983944542814238/ezgif.com-gif-maker_18.gif'
                           ]
                image = random.choice(choices)

                embed = discord.Embed(description=cum.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name
                cum = '**{0} collars {1}**'

                choices = ['https://i.imgur.com/p3nOKYu.gif',
                           'https://i.imgur.com/p5AEVvb.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=cum.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif author_gender == 'female':
            if mention_gender == 'male':
                author = ctx.message.author.name

                cum = '**{0} collars {1}**'

                choices = ['https://i.imgur.com/5psSaNC.gif',
                           'https://i.imgur.com/L5Zm9m8.gif',
                           'https://i.imgur.com/6SWhwD8.gif',
                           'https://i.imgur.com/HAWR1OH.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820971574739075132/ezgif.com-gif-maker_14.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820971602648105000/ezgif.com-gif-maker.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820971608797347900/ezgif.com-gif-maker_2.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820971616149700608/ezgif.com-gif-maker_1.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820971626095050752/ezgif.com-gif-maker_4.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820971649238171648/ezgif.com-gif-maker_8.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820971655882473472/ezgif.com-gif-maker_5.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820971656314617866/ezgif.com-gif-maker_3.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820971659003559966/ezgif.com-resize_1.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820971662911995944/ezgif.com-gif-maker_7.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820971666019844136/ezgif.com-resize.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820971672000659486/ezgif.com-gif-maker_11.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820971672630067220/ezgif.com-gif-maker_12.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820971684987142144/ezgif.com-gif-maker_6.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820971686903152660/ezgif.com-gif-maker_10.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820971689680044082/ezgif.com-gif-maker_13.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820971690204332102/ezgif.com-gif-maker_9.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=cum.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name

                cum = '**{0} collars {1}**'

                choices = ['https://i.imgur.com/QGYjuAH.gif',
                           'https://i.imgur.com/7dWEOr6.gif',
                           'https://i.imgur.com/ecjmuHS.gif',
                           'https://i.imgur.com/nWaf7vI.gif',
                           'https://i.imgur.com/7cyFDFO.gif',
                           'https://i.imgur.com/Fb7yY5W.gif',
                           'https://i.imgur.com/bpa4VFv.gif',
                           'https://i.imgur.com/Gx3iA2r.gif',
                           'https://i.imgur.com/vWnsOAV.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820963293857972245/ezgif.com-gif-maker_1.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820963297317617714/ezgif.com-gif-maker_2.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820963323964817408/ezgif.com-gif-maker_7.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820963326208901210/ezgif.com-gif-maker_4.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820963339051335703/ezgif.com-gif-maker.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820963342507048970/ezgif.com-gif-maker_9.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820963350015246336/ezgif.com-gif-maker_5.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820963349566455818/ezgif.com-gif-maker_3.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820963353789726720/ezgif.com-gif-maker_12.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820963363320233984/ezgif.com-gif-maker_6.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820963369095528448/ezgif.com-gif-maker_10.gif',
                           'https://cdn.discordapp.com/attachments/819857033489940481/820963369334997012/ezgif.com-gif-maker_8.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=cum.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

    @collar.error
    async def collar_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()

        raise error

    @commands.command()
    @commands.is_nsfw()
    async def twerk(self, ctx, message=None):
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message

        author_gender = determineGender(ctx.author)
        author = ctx.author.name
        if mentions == message:
            if message == None:
                twerk = f"**Okay fine i will twerk for you {author}**"
                choices = [
                    'https://cdn.discordapp.com/attachments/819857033489940481/823492122325680128/ezgif.com-optimize_2.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823491581264658432/ezgif.com-optimize_1.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823491126711418920/ezgif.com-optimize.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823490582675980308/ezgif.com-optimize123465465.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823505368927830016/ezgif.com-optimize_6.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823499677076029450/ezgif.com-optimize_4.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823494188925714452/ezgif.com-optimize_3.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823483562711711754/ezgif.com-resize2165.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823483556406755388/ezgif.com-resize_8.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823483552477347870/giphy.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823483549029105734/giphy_3.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823483538670223370/giphy_4.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823483534831910972/giphy_5.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823483530709041182/ezgif.com-gif-maker_1.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823483526561005598/giphy_2.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823483522135621642/ezgif.com-gif-maker_2.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823483491957604352/ezgif.com-resize_2.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823483482201260032/ezgif.com-resize_7.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823483472386457610/ezgif.com-resize_13.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823483467077124096/ezgif.com-resize.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823483463457439744/ezgif.com-resize_1.gif']
                img = random.choice(choices)
                embed = discord.Embed(title=twerk, colour=discord.Colour.blue())
                embed.set_image(url=img)
                await ctx.send(embed=embed)
            else:
                twerk = f"**{author} twerks for {mentions}**"
                choices = [
                    'https://cdn.discordapp.com/attachments/819857033489940481/823492122325680128/ezgif.com-optimize_2.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823491581264658432/ezgif.com-optimize_1.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823491126711418920/ezgif.com-optimize.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823490582675980308/ezgif.com-optimize123465465.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823505368927830016/ezgif.com-optimize_6.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823499677076029450/ezgif.com-optimize_4.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823494188925714452/ezgif.com-optimize_3.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823483562711711754/ezgif.com-resize2165.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823483556406755388/ezgif.com-resize_8.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823483552477347870/giphy.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823483549029105734/giphy_3.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823483538670223370/giphy_4.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823483534831910972/giphy_5.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823483530709041182/ezgif.com-gif-maker_1.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823483526561005598/giphy_2.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823483522135621642/ezgif.com-gif-maker_2.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823483491957604352/ezgif.com-resize_2.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823483482201260032/ezgif.com-resize_7.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823483472386457610/ezgif.com-resize_13.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823483467077124096/ezgif.com-resize.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/823483463457439744/ezgif.com-resize_1.gif']
                img = random.choice(choices)
                embed = discord.Embed(title=twerk, colour=discord.Colour.blue())
                embed.set_image(url=img)
                await ctx.send(embed=embed)

        else:
            mention_gender = determineGender(ctx.message.mentions[0])
            if author_gender == 'male':
                if mention_gender == 'female':
                    twerk = f"**{author} gets twerk from {mentions.name}**"
                    choices = [
                        'https://cdn.discordapp.com/attachments/819857033489940481/823492122325680128/ezgif.com-optimize_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823491581264658432/ezgif.com-optimize_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823491126711418920/ezgif.com-optimize.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823490582675980308/ezgif.com-optimize123465465.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823505368927830016/ezgif.com-optimize_6.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823499677076029450/ezgif.com-optimize_4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823494188925714452/ezgif.com-optimize_3.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483562711711754/ezgif.com-resize2165.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483556406755388/ezgif.com-resize_8.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483552477347870/giphy.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483549029105734/giphy_3.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483538670223370/giphy_4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483534831910972/giphy_5.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483530709041182/ezgif.com-gif-maker_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483526561005598/giphy_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483522135621642/ezgif.com-gif-maker_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483491957604352/ezgif.com-resize_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483482201260032/ezgif.com-resize_7.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483472386457610/ezgif.com-resize_13.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483467077124096/ezgif.com-resize.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483463457439744/ezgif.com-resize_1.gif']
                    img = random.choice(choices)
                    embed = discord.Embed(title=twerk, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    twerk = f"**{author} gets twerk from {mentions.name}**"
                    choices = [
                        'https://cdn.discordapp.com/attachments/819857033489940481/823492122325680128/ezgif.com-optimize_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823491581264658432/ezgif.com-optimize_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823491126711418920/ezgif.com-optimize.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823490582675980308/ezgif.com-optimize123465465.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823505368927830016/ezgif.com-optimize_6.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823499677076029450/ezgif.com-optimize_4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823494188925714452/ezgif.com-optimize_3.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483562711711754/ezgif.com-resize2165.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483556406755388/ezgif.com-resize_8.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483552477347870/giphy.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483549029105734/giphy_3.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483538670223370/giphy_4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483534831910972/giphy_5.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483530709041182/ezgif.com-gif-maker_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483526561005598/giphy_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483522135621642/ezgif.com-gif-maker_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483491957604352/ezgif.com-resize_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483482201260032/ezgif.com-resize_7.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483472386457610/ezgif.com-resize_13.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483467077124096/ezgif.com-resize.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483463457439744/ezgif.com-resize_1.gif']
                    img = random.choice(choices)
                    embed = discord.Embed(title=twerk, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
            elif author_gender == 'female':
                if mention_gender == 'male':
                    twerk = f"**{author} twerks for {mentions.name}**"
                    choices = [
                        'https://cdn.discordapp.com/attachments/819857033489940481/823492122325680128/ezgif.com-optimize_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823491581264658432/ezgif.com-optimize_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823491126711418920/ezgif.com-optimize.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823490582675980308/ezgif.com-optimize123465465.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823505368927830016/ezgif.com-optimize_6.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823499677076029450/ezgif.com-optimize_4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823494188925714452/ezgif.com-optimize_3.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483562711711754/ezgif.com-resize2165.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483556406755388/ezgif.com-resize_8.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483552477347870/giphy.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483549029105734/giphy_3.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483538670223370/giphy_4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483534831910972/giphy_5.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483530709041182/ezgif.com-gif-maker_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483526561005598/giphy_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483522135621642/ezgif.com-gif-maker_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483491957604352/ezgif.com-resize_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483482201260032/ezgif.com-resize_7.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483472386457610/ezgif.com-resize_13.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483467077124096/ezgif.com-resize.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483463457439744/ezgif.com-resize_1.gif']
                    img = random.choice(choices)
                    embed = discord.Embed(title=twerk, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    twerk = f"**{author} twerks for {mentions.name}**"
                    choices = [
                        'https://cdn.discordapp.com/attachments/819857033489940481/823492122325680128/ezgif.com-optimize_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823491581264658432/ezgif.com-optimize_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823491126711418920/ezgif.com-optimize.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823490582675980308/ezgif.com-optimize123465465.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823505368927830016/ezgif.com-optimize_6.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823499677076029450/ezgif.com-optimize_4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823494188925714452/ezgif.com-optimize_3.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483562711711754/ezgif.com-resize2165.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483556406755388/ezgif.com-resize_8.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483552477347870/giphy.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483549029105734/giphy_3.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483538670223370/giphy_4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483534831910972/giphy_5.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483530709041182/ezgif.com-gif-maker_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483526561005598/giphy_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483522135621642/ezgif.com-gif-maker_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483491957604352/ezgif.com-resize_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483482201260032/ezgif.com-resize_7.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483472386457610/ezgif.com-resize_13.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483467077124096/ezgif.com-resize.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823483463457439744/ezgif.com-resize_1.gif']
                    img = random.choice(choices)
                    embed = discord.Embed(title=twerk, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)

    @twerk.error
    async def twerk_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()


    @commands.command()
    @commands.is_nsfw()
    async def thicc(self, ctx):
        thicc = '**Take some thiccness in your life!**'

        choices = ['https://i.imgur.com/Qx7Dq6K.gif',
                   'https://i.imgur.com/NulrQWp.gif',
                   'https://i.imgur.com/oxwBJr7.gif',
                   'https://i.imgur.com/aQ5uBuq.gif',
                   'https://i.imgur.com/1JTdD2D.gif',
                   'https://i.imgur.com/T51u6su.gif',
                   'https://i.imgur.com/es8b4Ah.gif',
                   'https://i.imgur.com/H1SmYLG.gif',
                   'https://i.imgur.com/hRjPtZ1.gif',
                   'https://i.imgur.com/fGMsYlE.gif',
                   'https://i.imgur.com/0DqVCl1.gif',
                   'https://i.imgur.com/nFdkmPa.gif',
                   'https://i.imgur.com/JLQYeXV.gif',
                   'https://i.imgur.com/NkkGSc4.gif',
                   'https://i.imgur.com/vQHc3MO.gif',
                   'https://i.imgur.com/CyVwhw7.gif']

        image = random.choice(choices)

        embed = discord.Embed(description=thicc, colour=discord.Colour.blue())

        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_nsfw()
    async def choke(self, ctx, message=None):
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author_gender = determineGender(ctx.author)
        if mentions == message:
            if message == None:
                embed = discord.Embed(description=f"**You can't choke nothing you horni dumbo\nExample use: $choke @User#6969**", colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                if author_gender == 'male':
                    author = ctx.author.name

                    choke = '**{0} chokes {1}**'
                    choices = ['https://i.imgur.com/gRQLP2S.gif',
                               'https://i.imgur.com/tGGt3eT.gif',
                               'https://i.imgur.com/xaSYsyU.gif',
                               'https://i.imgur.com/5aYhhBW.gif',
                               'https://i.imgur.com/so9zWZ2.gif',
                               'https://i.imgur.com/8lTQkmK.gif',
                               'https://cdn.discordapp.com/attachments/694996260851286048/697223825858887710/image0.gif',
                               'https://cdn.discordapp.com/attachments/694996260851286048/697223839075139584/image0.gif',
                               'https://cdn.discordapp.com/attachments/694996260851286048/697223847669137488/image0.gif',
                               'https://cdn.discordapp.com/attachments/694996260851286048/697223855374336171/image0.gif',
                               'https://cdn.discordapp.com/attachments/694996260851286048/697223880053489664/image0.gif',
                               'https://cdn.discordapp.com/attachments/694996260851286048/697223899938684988/image0.gif']
                    image = random.choice(choices)
                    embed = discord.Embed(description=choke.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

                elif author_gender == 'female':
                    author = ctx.author.name

                    choke = '**{0} gets choked by {1}**'
                    choices = ['https://i.imgur.com/gRQLP2S.gif',
                               'https://i.imgur.com/tGGt3eT.gif',
                               'https://i.imgur.com/xaSYsyU.gif',
                               'https://i.imgur.com/5aYhhBW.gif',
                               'https://i.imgur.com/so9zWZ2.gif',
                               'https://i.imgur.com/8lTQkmK.gif',
                               'https://cdn.discordapp.com/attachments/694996260851286048/697223825858887710/image0.gif',
                               'https://cdn.discordapp.com/attachments/694996260851286048/697223839075139584/image0.gif',
                               'https://cdn.discordapp.com/attachments/694996260851286048/697223847669137488/image0.gif',
                               'https://cdn.discordapp.com/attachments/694996260851286048/697223855374336171/image0.gif',
                               'https://cdn.discordapp.com/attachments/694996260851286048/697223880053489664/image0.gif',
                               'https://cdn.discordapp.com/attachments/694996260851286048/697223899938684988/image0.gif']
                    image = random.choice(choices)
                    embed = discord.Embed(description=choke.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

        mention_gender = determineGender(ctx.message.mentions[0])
        if author_gender == 'male':
            if mention_gender == 'female':
                author = ctx.author.name


                choke = '**{0} chokes {1}**'
                choices = ['https://i.imgur.com/gRQLP2S.gif',
                           'https://i.imgur.com/tGGt3eT.gif',
                           'https://i.imgur.com/xaSYsyU.gif',
                           'https://i.imgur.com/5aYhhBW.gif',
                           'https://i.imgur.com/so9zWZ2.gif',
                           'https://i.imgur.com/8lTQkmK.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/697223825858887710/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/697223839075139584/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/697223847669137488/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/697223855374336171/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/697223880053489664/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/697223899938684988/image0.gif']
                image = random.choice(choices)
                embed = discord.Embed(description=choke.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send (embed=embed)

            else:
                author = ctx.author.name

                choke = '**{0} chokes {1}**'
                choices = ['https://cdn.discordapp.com/attachments/694996260851286048/697225209975144538/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/697225217713373224/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/697225228698517509/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/697223888442097674/image0.gif']
                image = random.choice(choices)
                embed = discord.Embed(description=choke.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif author_gender == 'female':
            if mention_gender == 'male':
                author = ctx.author.name

                choke = '**{0} gets choked by {1}**'
                choices = ['https://i.imgur.com/gRQLP2S.gif',
                           'https://i.imgur.com/tGGt3eT.gif',
                           'https://i.imgur.com/xaSYsyU.gif',
                           'https://i.imgur.com/5aYhhBW.gif',
                           'https://i.imgur.com/so9zWZ2.gif',
                           'https://i.imgur.com/8lTQkmK.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/697223825858887710/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/697223839075139584/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/697223847669137488/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/697223855374336171/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/697223880053489664/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/697223899938684988/image0.gif']
                image = random.choice(choices)
                embed = discord.Embed(description=choke.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.author.name

                choke = '**{0} chokes {1}**'
                choices = ['https://cdn.discordapp.com/attachments/694996260851286048/697226033140858990/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/697226038811558048/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/697226047292178432/image0.gif',
                           'https://cdn.discordapp.com/attachments/694996260851286048/697226060193988669/image0.gif',
                           ]
                image = random.choice(choices)
                embed = discord.Embed(description=choke.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

    @choke.error
    async def choke_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()
        raise error

    @commands.command(aliases=['submit'])
    @commands.is_nsfw()
    async def sub(self, ctx, message=None):
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author_gender = determineGender(ctx.author)
        if mentions == message:
            if message == None:
                embed = discord.Embed(description=f"**You can sub to PewDiePie you horni dumbo\nExample use: $sub @User#6969**", colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                if author_gender == 'male':
                    author = ctx.message.author.name

                    sixtynine = '**{0} submits to {1}**'

                    choices = [
                        'https://media.discordapp.net/attachments/705635462718685277/797959429999951932/img772.gif',
                        'https://media.discordapp.net/attachments/705635462718685277/797425657633832980/img274.gif']
                    image = random.choice(choices)

                    embed = discord.Embed(description=sixtynine.format(author, mentions),
                                          colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)
                elif author_gender == 'female':
                    author = ctx.message.author.name

                    sixtynine = '**{0} submits to {1}**'

                    choices = [
                        'https://media.discordapp.net/attachments/705632503720837150/798625632959463484/img487.gif',
                        'https://media.discordapp.net/attachments/705632503720837150/798625555951517756/img808.gif',
                        'https://media.discordapp.net/attachments/737610314518102046/798584212886257664/img452.gif',
                        'https://media.discordapp.net/attachments/705635462718685277/798452494983495710/img933.gif',
                        'https://media.discordapp.net/attachments/737610314518102046/798167557307498546/img520.gif',
                        'https://media.discordapp.net/attachments/737610314518102046/798166269668229140/img970.gif',
                        'https://media.discordapp.net/attachments/737610314518102046/798164478357274634/img82.gif',
                        'https://media.discordapp.net/attachments/737610314518102046/798158173688823878/img484.gif',
                        'https://media.discordapp.net/attachments/705635462718685277/798019319907876894/img118.gif',
                        'https://media.discordapp.net/attachments/705635462718685277/798005031827275786/img313.gif',
                        'https://media.discordapp.net/attachments/705635462718685277/797885917163421726/img357.gif',
                        'https://media.discordapp.net/attachments/705635462718685277/797882434322169877/img252.gif',
                        'https://media.discordapp.net/attachments/705635462718685277/797877012374749184/img559.gif',
                        'https://media.discordapp.net/attachments/705635462718685277/797837015013916672/img829.gif',
                        'https://media.discordapp.net/attachments/705635462718685277/797835472247455785/img412.gif',
                        'https://media.discordapp.net/attachments/737610314518102046/797657957214847036/img231.gif',
                        'https://media.discordapp.net/attachments/737610314518102046/797637357335085056/img468.gif',
                        'https://media.discordapp.net/attachments/705635462718685277/797362534008225812/img776.gif',
                        'https://media.discordapp.net/attachments/705635462718685277/797247760251617330/img982.gif']
                    image = random.choice(choices)

                    embed = discord.Embed(description=sixtynine.format(author, mentions),
                                          colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)


        mention_gender = determineGender(ctx.message.mentions[0])

        if author_gender == 'male':
            if mention_gender == 'female':
                author = ctx.message.author.name


                sixtynine = '**{0} submits to {1}**'

                choices = ['https://media.discordapp.net/attachments/705635462718685277/797959429999951932/img772.gif',
                           'https://media.discordapp.net/attachments/705635462718685277/797425657633832980/img274.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=sixtynine.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name


                sixtynine = '**{0} submits to {1}**'

                choices = ['https://media.discordapp.net/attachments/705635462718685277/797425657633832980/img274.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=sixtynine.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif author_gender == 'female':
            if mention_gender == 'male':
                author = ctx.message.author.name


                sixtynine = '**{0} submits to {1}**'

                choices = ['https://media.discordapp.net/attachments/705632503720837150/798625632959463484/img487.gif',
                           'https://media.discordapp.net/attachments/705632503720837150/798625555951517756/img808.gif',
                           'https://media.discordapp.net/attachments/737610314518102046/798584212886257664/img452.gif',
                           'https://media.discordapp.net/attachments/705635462718685277/798452494983495710/img933.gif',
                           'https://media.discordapp.net/attachments/737610314518102046/798167557307498546/img520.gif',
                           'https://media.discordapp.net/attachments/737610314518102046/798166269668229140/img970.gif',
                           'https://media.discordapp.net/attachments/737610314518102046/798164478357274634/img82.gif',
                           'https://media.discordapp.net/attachments/737610314518102046/798158173688823878/img484.gif',
                           'https://media.discordapp.net/attachments/705635462718685277/798019319907876894/img118.gif',
                           'https://media.discordapp.net/attachments/705635462718685277/798005031827275786/img313.gif',
                           'https://media.discordapp.net/attachments/705635462718685277/797885917163421726/img357.gif',
                           'https://media.discordapp.net/attachments/705635462718685277/797882434322169877/img252.gif',
                           'https://media.discordapp.net/attachments/705635462718685277/797877012374749184/img559.gif',
                           'https://media.discordapp.net/attachments/705635462718685277/797837015013916672/img829.gif',
                           'https://media.discordapp.net/attachments/705635462718685277/797835472247455785/img412.gif',
                           'https://media.discordapp.net/attachments/737610314518102046/797657957214847036/img231.gif',
                           'https://media.discordapp.net/attachments/737610314518102046/797637357335085056/img468.gif',
                           'https://media.discordapp.net/attachments/705635462718685277/797362534008225812/img776.gif',
                           'https://media.discordapp.net/attachments/705635462718685277/797247760251617330/img982.gif',
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128714345611345/ezgif.com-gif-maker_1.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128745551626320/ezgif.com-gif-maker_9.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128784071983134/ezgif.com-gif-maker_20.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128786467454986/ezgif.com-gif-maker_6.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128789935489034/ezgif.com-gif-maker_13.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128835787489310/ezgif.com-gif-maker_25.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128897619525743/ezgif.com-gif-maker_4.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128902460801024/ezgif.com-gif-maker_17.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128906348134430/ezgif.com-gif-maker.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128911905849364/ezgif.com-gif-maker_2.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128914644205628/ezgif.com-gif-maker_5.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128917924544522/ezgif.com-gif-maker_10.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128929815527454/ezgif.com-gif-maker_15.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128939252842516/ezgif.com-gif-maker_14.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128953823330404/ezgif.com-gif-maker_18.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128963939860520/ezgif.com-gif-maker_22.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128965128028210/ezgif.com-gif-maker_16.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128977613946890/ezgif.com-gif-maker_21.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128993678262332/ezgif.com-gif-maker_8.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128993698840647/ezgif.com-gif-maker_24.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834129014779543622/ezgif.com-gif-maker_3.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834129015216406538/ezgif.com-gif-maker_7.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834129022321295380/ezgif.com-gif-maker_11.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834129024216334367/ezgif.com-gif-maker_23.gif"]
                image = random.choice(choices)

                embed = discord.Embed(description=sixtynine.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name


                sixtynine = '**{0} submits to {1}**'

                choices = [
                    'https://submissivegirl.bdsmlr.com/uploads/pictures/2016/01/3038/bdsmlr-3011-prbyXuMt691.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=sixtynine.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

    @sub.error
    async def sub_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()

    @commands.command(aliases=['ride'])
    @commands.is_nsfw()
    async def cowgirl(self, ctx, message=None):
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author_gender = determineGender(ctx.author)
        if mentions == message:
            if message == None:
                embed = discord.Embed(description=f"**You can't ride nothing you horni dumbo\nExample use: $ride @User#6969**", colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                if author_gender == 'male':
                    author = ctx.message.author.name

                    sixtynine = '**{0} gets ridden by {1}**'

                    choices = [
                        'https://media.discordapp.net/attachments/798913238229188608/798924542286102568/ezgif.com-gif-maker_7.gif',
                        'https://media.discordapp.net/attachments/798913238229188608/798924449469562890/ezgif.com-gif-maker_9.gif',
                        'https://media.discordapp.net/attachments/798913238229188608/798924440694947880/ezgif.com-gif-maker_4.gif',
                        'https://media.discordapp.net/attachments/798913238229188608/798924167775780864/ezgif.com-gif-maker_1.gif?width=446&height=669',
                        'https://media.discordapp.net/attachments/798913238229188608/798924155608891422/ezgif.com-gif-maker_2.gif',
                        'https://media.discordapp.net/attachments/798913238229188608/798924136196866069/ezgif.com-gif-maker_3.gif',
                        'https://media.discordapp.net/attachments/798913238229188608/798923998322753567/7.gif?width=446&height=669',
                        'https://media.discordapp.net/attachments/798913238229188608/798923869209100299/6.gif',
                        'https://media.discordapp.net/attachments/798913238229188608/798923846555009054/5.gif?width=479&height=670',
                        'https://media.discordapp.net/attachments/798913238229188608/798919416732581939/4.gif',
                        'https://media.discordapp.net/attachments/798913238229188608/798918820013015070/3.gif',
                        'https://media.discordapp.net/attachments/798913238229188608/798918317136936961/2.gif',
                        'https://i.imgur.com/rzcjHMc.gif',
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
                        'https://i.imgur.com/TFFTXLA.gif',
                        'https://i.imgur.com/z1CDDXw.gif',
                        'https://i.imgur.com/QEr59Mw.gif',
                        'https://i.imgur.com/nYrqMsT.gif',
                        'https://i.imgur.com/B7mOdCh.gif',
                        'https://i.imgur.com/f0EXhkt.gif',
                        'https://i.imgur.com/K75Tb10.gif',
                        'https://i.imgur.com/9VtZHXQ.gif',
                        'https://i.imgur.com/jNv4kjC.gif',
                        'https://i.imgur.com/JrT7W2n.gif',
                        'https://i.imgur.com/XbnjSq5.gif',
                        'https://i.imgur.com/B4SpAa0.gif'
                    ]
                    image = random.choice(choices)

                    embed = discord.Embed(description=sixtynine.format(author, mentions),
                                          colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)
                elif author_gender == 'female':
                    author = ctx.message.author.name

                    sixtynine = '**{0} rides {1}**'

                    choices = [
                        'https://media.discordapp.net/attachments/798913238229188608/798924542286102568/ezgif.com-gif-maker_7.gif',
                        'https://media.discordapp.net/attachments/798913238229188608/798924449469562890/ezgif.com-gif-maker_9.gif',
                        'https://media.discordapp.net/attachments/798913238229188608/798924440694947880/ezgif.com-gif-maker_4.gif',
                        'https://media.discordapp.net/attachments/798913238229188608/798924167775780864/ezgif.com-gif-maker_1.gif?width=446&height=669',
                        'https://media.discordapp.net/attachments/798913238229188608/798924155608891422/ezgif.com-gif-maker_2.gif',
                        'https://media.discordapp.net/attachments/798913238229188608/798924136196866069/ezgif.com-gif-maker_3.gif',
                        'https://media.discordapp.net/attachments/798913238229188608/798923998322753567/7.gif?width=446&height=669',
                        'https://media.discordapp.net/attachments/798913238229188608/798923869209100299/6.gif',
                        'https://media.discordapp.net/attachments/798913238229188608/798923846555009054/5.gif?width=479&height=670',
                        'https://media.discordapp.net/attachments/798913238229188608/798919416732581939/4.gif',
                        'https://media.discordapp.net/attachments/798913238229188608/798918820013015070/3.gif',
                        'https://media.discordapp.net/attachments/798913238229188608/798918317136936961/2.gif',
                        'https://i.imgur.com/rzcjHMc.gif',
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
                        'https://i.imgur.com/TFFTXLA.gif',
                        'https://i.imgur.com/z1CDDXw.gif',
                        'https://i.imgur.com/QEr59Mw.gif',
                        'https://i.imgur.com/nYrqMsT.gif',
                        'https://i.imgur.com/B7mOdCh.gif',
                        'https://i.imgur.com/f0EXhkt.gif',
                        'https://i.imgur.com/K75Tb10.gif',
                        'https://i.imgur.com/9VtZHXQ.gif',
                        'https://i.imgur.com/jNv4kjC.gif',
                        'https://i.imgur.com/JrT7W2n.gif',
                        'https://i.imgur.com/XbnjSq5.gif',
                        'https://i.imgur.com/B4SpAa0.gif'
                    ]
                    image = random.choice(choices)

                    embed = discord.Embed(description=sixtynine.format(author, mentions),
                                          colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

        mention_gender = determineGender(ctx.message.mentions[0])

        if author_gender == 'male':
            if mention_gender == 'female':
                author = ctx.message.author.name


                sixtynine = '**{0} gets ridden by {1}**'

                choices = [
                    'https://media.discordapp.net/attachments/798913238229188608/798924542286102568/ezgif.com-gif-maker_7.gif',
                    'https://media.discordapp.net/attachments/798913238229188608/798924449469562890/ezgif.com-gif-maker_9.gif',
                    'https://media.discordapp.net/attachments/798913238229188608/798924440694947880/ezgif.com-gif-maker_4.gif',
                    'https://media.discordapp.net/attachments/798913238229188608/798924167775780864/ezgif.com-gif-maker_1.gif?width=446&height=669',
                    'https://media.discordapp.net/attachments/798913238229188608/798924155608891422/ezgif.com-gif-maker_2.gif',
                    'https://media.discordapp.net/attachments/798913238229188608/798924136196866069/ezgif.com-gif-maker_3.gif',
                    'https://media.discordapp.net/attachments/798913238229188608/798923998322753567/7.gif?width=446&height=669',
                    'https://media.discordapp.net/attachments/798913238229188608/798923869209100299/6.gif',
                    'https://media.discordapp.net/attachments/798913238229188608/798923846555009054/5.gif?width=479&height=670',
                    'https://media.discordapp.net/attachments/798913238229188608/798919416732581939/4.gif',
                    'https://media.discordapp.net/attachments/798913238229188608/798918820013015070/3.gif',
                    'https://media.discordapp.net/attachments/798913238229188608/798918317136936961/2.gif',
                    'https://i.imgur.com/rzcjHMc.gif',
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
                    'https://i.imgur.com/TFFTXLA.gif',
                    'https://i.imgur.com/z1CDDXw.gif',
                    'https://i.imgur.com/QEr59Mw.gif',
                    'https://i.imgur.com/nYrqMsT.gif',
                    'https://i.imgur.com/B7mOdCh.gif',
                    'https://i.imgur.com/f0EXhkt.gif',
                    'https://i.imgur.com/K75Tb10.gif',
                    'https://i.imgur.com/9VtZHXQ.gif',
                    'https://i.imgur.com/jNv4kjC.gif',
                    'https://i.imgur.com/JrT7W2n.gif',
                    'https://i.imgur.com/XbnjSq5.gif',
                    'https://i.imgur.com/B4SpAa0.gif'
                    ]
                image = random.choice(choices)

                embed = discord.Embed(description=sixtynine.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name

                sixtynine = '**{0} rides {1}**'

                choices = [
                    'https://media.discordapp.net/attachments/798913238229188608/798933840387112990/ezgif.com-gif-maker_2.gif',
                    'https://media.discordapp.net/attachments/798913238229188608/798933882589282314/ezgif.com-gif-maker_3.gif',
                    'https://media.discordapp.net/attachments/798913238229188608/798933915107721276/ezgif.com-gif-maker_1.gif',
                    'https://media.discordapp.net/attachments/798913238229188608/798933935488761876/ezgif.com-gif-maker.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=sixtynine.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif author_gender == 'female':
            if mention_gender == 'male':
                author = ctx.message.author.name

                sixtynine = '**{0} rides {1}**'

                choices = [
                    'https://media.discordapp.net/attachments/798913238229188608/798924542286102568/ezgif.com-gif-maker_7.gif',
                    'https://media.discordapp.net/attachments/798913238229188608/798924449469562890/ezgif.com-gif-maker_9.gif',
                    'https://media.discordapp.net/attachments/798913238229188608/798924440694947880/ezgif.com-gif-maker_4.gif',
                    'https://media.discordapp.net/attachments/798913238229188608/798924167775780864/ezgif.com-gif-maker_1.gif?width=446&height=669',
                    'https://media.discordapp.net/attachments/798913238229188608/798924155608891422/ezgif.com-gif-maker_2.gif',
                    'https://media.discordapp.net/attachments/798913238229188608/798924136196866069/ezgif.com-gif-maker_3.gif',
                    'https://media.discordapp.net/attachments/798913238229188608/798923998322753567/7.gif?width=446&height=669',
                    'https://media.discordapp.net/attachments/798913238229188608/798923869209100299/6.gif',
                    'https://media.discordapp.net/attachments/798913238229188608/798923846555009054/5.gif?width=479&height=670',
                    'https://media.discordapp.net/attachments/798913238229188608/798919416732581939/4.gif',
                    'https://media.discordapp.net/attachments/798913238229188608/798918820013015070/3.gif',
                    'https://media.discordapp.net/attachments/798913238229188608/798918317136936961/2.gif',
                    'https://i.imgur.com/rzcjHMc.gif',
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
                    'https://i.imgur.com/TFFTXLA.gif',
                    'https://i.imgur.com/z1CDDXw.gif',
                    'https://i.imgur.com/QEr59Mw.gif',
                    'https://i.imgur.com/nYrqMsT.gif',
                    'https://i.imgur.com/B7mOdCh.gif',
                    'https://i.imgur.com/f0EXhkt.gif',
                    'https://i.imgur.com/K75Tb10.gif',
                    'https://i.imgur.com/9VtZHXQ.gif',
                    'https://i.imgur.com/jNv4kjC.gif',
                    'https://i.imgur.com/JrT7W2n.gif',
                    'https://i.imgur.com/XbnjSq5.gif',
                    'https://i.imgur.com/B4SpAa0.gif'
                ]
                image = random.choice(choices)

                embed = discord.Embed(description=sixtynine.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name

                sixtynine = '**{0} gets ridden by {1}**'

                choices = [
                    'https://media.discordapp.net/attachments/798913238229188608/798917866878402590/1.gif',
                    'https://media.discordapp.net/attachments/798913238229188608/798924298777657364/ezgif.com-gif-maker_5.gif',
                    'https://media.discordapp.net/attachments/798913238229188608/798924450271068180/ezgif.com-gif-maker.gif',
                    'https://media.discordapp.net/attachments/798913238229188608/798924506625605682/ezgif.com-gif-maker_10.gif']
                image = random.choice(choices)

                embed = discord.Embed(description=sixtynine.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

    @cowgirl.error
    async def cowgirl_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()

    @commands.command(aliases=['3some', '3sum'])
    @commands.is_nsfw()
    async def threesome(self, ctx, *, message=None):
        try:
            mentions = ctx.message.mentions[1]
        except:
            mentions = message

        author = ctx.author.name
        author_gender = determineGender(ctx.author)

        if mentions == message:
            if message == None:
                embed = discord.Embed(
                    description=f"**You can't threesome nothing you horni dumbo\nExample use: $threesome @User#6969 @User#0420**",
                    colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                words = message.split()
                first = words[0]
                second = words[1]

                if author_gender == 'male':
                    threesome = f"**{author} gets into threesome with {first} and {second}**"
                    choices = ['https://cdn.discordapp.com/attachments/819857033489940481/821081377566490634/ezgif.com-gif-maker_2.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821081444050534431/ezgif.com-gif-maker_1.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821081498454065182/ezgif.com-gif-maker_3.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821091226005930014/ezgif.com-gif-maker_4.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821091234897723453/ezgif.com-gif-maker_7.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821091236076978206/ezgif.com-gif-maker_2.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821091239616315422/ezgif.com-gif-maker_1.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821091249527324703/ezgif.com-gif-maker_9.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821091249473060934/ezgif.com-gif-maker_5.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821091254926180397/ezgif.com-gif-maker_3.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821091255131045940/ezgif.com-gif-maker.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821091254740844584/ezgif.com-resize.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821096123459567626/ezgif.com-gif-maker_4.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821096141067518062/ezgif.com-gif-maker_8.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821096145601560587/ezgif.com-gif-maker_5.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821096150709960734/ezgif.com-gif-maker_6.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821096162186625104/ezgif.com-gif-maker.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821096165243224104/ezgif.com-gif-maker_1.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821096173104267264/ezgif.com-gif-maker_3.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821096177047044176/ezgif.com-gif-maker_7.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821096177037606963/ezgif.com-gif-maker_2.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821096179177226270/ezgif.com-gif-maker_9.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821096181689876480/ezgif.com-gif-maker_10.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821099564453855292/ezgif.com-gif-maker_2.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821099573559820348/ezgif.com-gif-maker_1.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821099575694589972/ezgif.com-gif-maker_7.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821099577540214804/ezgif.com-gif-maker.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821099578026623006/ezgif.com-gif-maker_6.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821099578429800488/ezgif.com-gif-maker_5.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821099583668486184/ezgif.com-gif-maker_3.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821099585283293264/ezgif.com-gif-maker_4.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/821099585291157544/ezgif.com-resize.gif']
                    image = random.choice(choices)
                    embed = discord.Embed(description=threesome, colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)
                elif author_gender == 'female':
                    threesome = f"**{author} gets into threesome with {first} and {second}**"
                    choices = [
                        'https://cdn.discordapp.com/attachments/819857033489940481/821088123332198460/ezgif.com-resize_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821086364300476496/ezgif.com-gif-maker_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821088121323913266/ezgif.com-resize.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821086363754954772/ezgif.com-gif-maker_9.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821086362308313189/ezgif.com-gif-maker_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821086362094141450/ezgif.com-gif-maker_13.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821086362299793438/ezgif.com-gif-maker_3.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821086361301418004/ezgif.com-gif-maker.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821086360970461184/ezgif.com-gif-maker_12.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821086359308468278/ezgif.com-gif-maker_7.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821086357613969428/ezgif.com-gif-maker_6.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821086356129579028/ezgif.com-gif-maker_4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821086316920832050/ezgif.com-gif-maker_8.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821081474086076436/ezgif.com-gif-maker.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821081377566490634/ezgif.com-gif-maker_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821091226005930014/ezgif.com-gif-maker_4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821091236076978206/ezgif.com-gif-maker_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821091239616315422/ezgif.com-gif-maker_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821091249527324703/ezgif.com-gif-maker_9.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821091249473060934/ezgif.com-gif-maker_5.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821091254926180397/ezgif.com-gif-maker_3.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821091255131045940/ezgif.com-gif-maker.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821091254740844584/ezgif.com-resize.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821096123459567626/ezgif.com-gif-maker_4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821096141067518062/ezgif.com-gif-maker_8.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821096145601560587/ezgif.com-gif-maker_5.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821096150709960734/ezgif.com-gif-maker_6.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821096162186625104/ezgif.com-gif-maker.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821096165243224104/ezgif.com-gif-maker_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821096173104267264/ezgif.com-gif-maker_3.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821096177047044176/ezgif.com-gif-maker_7.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821096177037606963/ezgif.com-gif-maker_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821096179177226270/ezgif.com-gif-maker_9.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/821096181689876480/ezgif.com-gif-maker_10.gif']
                    image = random.choice(choices)
                    embed = discord.Embed(description=threesome, colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)
        first_gender = determineGender(ctx.message.mentions[0])

        if mentions == ctx.message.mentions[0]:
            words = message.split()
            msg = words[1]
            first = ctx.message.mentions[0]
            
            
            if author_gender == 'male':
                if first_gender == 'male':
                        threesome = f"**{author} gets into threesome with {first.name} and {msg}**"
                        choices = [
                            'https://cdn.discordapp.com/attachments/819857033489940481/821081377566490634/ezgif.com-gif-maker_2.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821081498454065182/ezgif.com-gif-maker_3.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096123459567626/ezgif.com-gif-maker_4.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096141067518062/ezgif.com-gif-maker_8.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096145601560587/ezgif.com-gif-maker_5.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096150709960734/ezgif.com-gif-maker_6.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096162186625104/ezgif.com-gif-maker.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096165243224104/ezgif.com-gif-maker_1.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096173104267264/ezgif.com-gif-maker_3.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096177047044176/ezgif.com-gif-maker_7.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096177037606963/ezgif.com-gif-maker_2.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096179177226270/ezgif.com-gif-maker_9.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096181689876480/ezgif.com-gif-maker_10.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821099564453855292/ezgif.com-gif-maker_2.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821099573559820348/ezgif.com-gif-maker_1.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821099575694589972/ezgif.com-gif-maker_7.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821099577540214804/ezgif.com-gif-maker.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821099578026623006/ezgif.com-gif-maker_6.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821099578429800488/ezgif.com-gif-maker_5.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821099583668486184/ezgif.com-gif-maker_3.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821099585283293264/ezgif.com-gif-maker_4.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821099585291157544/ezgif.com-resize.gif']
                        image = random.choice(choices)
                        embed = discord.Embed(description=threesome, colour=discord.Colour.blue())
                        embed.set_image(url=image)

                        await ctx.send(embed=embed)
                elif first_gender == 'female':
                        threesome = f"**{author} gets into threesome with {first.name} and {msg}**"
                        choices = [
                            'https://cdn.discordapp.com/attachments/819857033489940481/821081377566490634/ezgif.com-gif-maker_2.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821081444050534431/ezgif.com-gif-maker_1.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821091226005930014/ezgif.com-gif-maker_4.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821091234897723453/ezgif.com-gif-maker_7.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821091236076978206/ezgif.com-gif-maker_2.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821091239616315422/ezgif.com-gif-maker_1.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821091249527324703/ezgif.com-gif-maker_9.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821091249473060934/ezgif.com-gif-maker_5.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821091254926180397/ezgif.com-gif-maker_3.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821091255131045940/ezgif.com-gif-maker.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821091254740844584/ezgif.com-resize.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096123459567626/ezgif.com-gif-maker_4.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096141067518062/ezgif.com-gif-maker_8.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096145601560587/ezgif.com-gif-maker_5.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096150709960734/ezgif.com-gif-maker_6.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096162186625104/ezgif.com-gif-maker.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096165243224104/ezgif.com-gif-maker_1.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096173104267264/ezgif.com-gif-maker_3.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096177047044176/ezgif.com-gif-maker_7.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096177037606963/ezgif.com-gif-maker_2.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096179177226270/ezgif.com-gif-maker_9.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096181689876480/ezgif.com-gif-maker_10.gif']
                        image = random.choice(choices)
                        embed = discord.Embed(description=threesome, colour=discord.Colour.blue())
                        embed.set_image(url=image)

                        await ctx.send(embed=embed)

            elif author_gender == 'female':
                if first_gender == 'male':
                        threesome = f"**{author} gets into threesome with {first.name} and {msg}**"
                        choices = [
                            'https://cdn.discordapp.com/attachments/819857033489940481/821081377566490634/ezgif.com-gif-maker_2.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821081444050534431/ezgif.com-gif-maker_1.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821091226005930014/ezgif.com-gif-maker_4.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821091236076978206/ezgif.com-gif-maker_2.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821091239616315422/ezgif.com-gif-maker_1.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821091249527324703/ezgif.com-gif-maker_9.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821091249473060934/ezgif.com-gif-maker_5.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821091254926180397/ezgif.com-gif-maker_3.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821091255131045940/ezgif.com-gif-maker.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821091254740844584/ezgif.com-resize.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096123459567626/ezgif.com-gif-maker_4.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096141067518062/ezgif.com-gif-maker_8.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096145601560587/ezgif.com-gif-maker_5.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096150709960734/ezgif.com-gif-maker_6.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096162186625104/ezgif.com-gif-maker.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096165243224104/ezgif.com-gif-maker_1.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096173104267264/ezgif.com-gif-maker_3.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096177047044176/ezgif.com-gif-maker_7.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096177037606963/ezgif.com-gif-maker_2.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096179177226270/ezgif.com-gif-maker_9.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096181689876480/ezgif.com-gif-maker_10.gif']
                        image = random.choice(choices)
                        embed = discord.Embed(description=threesome, colour=discord.Colour.blue())
                        embed.set_image(url=image)

                        await ctx.send(embed=embed)

                elif first_gender == 'female':
                        threesome = f"**{author} gets into threesome with {first.name} and {msg}**"
                        choices = [
                            'https://cdn.discordapp.com/attachments/819857033489940481/821088123332198460/ezgif.com-resize_1.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821086364300476496/ezgif.com-gif-maker_1.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821088121323913266/ezgif.com-resize.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821086363754954772/ezgif.com-gif-maker_9.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821086362308313189/ezgif.com-gif-maker_2.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821086362094141450/ezgif.com-gif-maker_13.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821086362299793438/ezgif.com-gif-maker_3.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821086361301418004/ezgif.com-gif-maker.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821086360970461184/ezgif.com-gif-maker_12.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821086359308468278/ezgif.com-gif-maker_7.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821086357613969428/ezgif.com-gif-maker_6.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821086356129579028/ezgif.com-gif-maker_4.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821086316920832050/ezgif.com-gif-maker_8.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821081474086076436/ezgif.com-gif-maker.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821081444050534431/ezgif.com-gif-maker_1.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821091234897723453/ezgif.com-gif-maker_7.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821091236076978206/ezgif.com-gif-maker_2.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821091239616315422/ezgif.com-gif-maker_1.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821091249527324703/ezgif.com-gif-maker_9.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821091249473060934/ezgif.com-gif-maker_5.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821091254926180397/ezgif.com-gif-maker_3.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821091255131045940/ezgif.com-gif-maker.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821091254740844584/ezgif.com-resize.gif']
                        image = random.choice(choices)
                        embed = discord.Embed(description=threesome, colour=discord.Colour.blue())
                        embed.set_image(url=image)
    
                        await ctx.send(embed=embed)
        if mentions == ctx.message.mentions[1]:
            second_gender = determineGender(ctx.message.mentions[1])
            first = ctx.message.mentions[0]
            second = ctx.message.mentions[1]

            if author_gender == 'male':

                if first_gender == 'female':
                    if second_gender == 'female':
                        threesome = f"**{author} gets into threesome with {first.name} and {second.name}**"
                        choices = ['https://cdn.discordapp.com/attachments/819857033489940481/821081444050534431/ezgif.com-gif-maker_1.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821091226005930014/ezgif.com-gif-maker_4.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821091234897723453/ezgif.com-gif-maker_7.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821091236076978206/ezgif.com-gif-maker_2.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821091239616315422/ezgif.com-gif-maker_1.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821091249527324703/ezgif.com-gif-maker_9.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821091249473060934/ezgif.com-gif-maker_5.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821091254926180397/ezgif.com-gif-maker_3.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821091255131045940/ezgif.com-gif-maker.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821091254740844584/ezgif.com-resize.gif']
                        image = random.choice(choices)
                        embed = discord.Embed(description=threesome, colour=discord.Colour.blue())
                        embed.set_image(url=image)

                        await ctx.send(embed=embed)
                    elif second_gender == 'male':
                        threesome = f"**{author} gets into threesome with {first.name} and {second.name}**"
                        choices = [
                            'https://cdn.discordapp.com/attachments/819857033489940481/821081377566490634/ezgif.com-gif-maker_2.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096123459567626/ezgif.com-gif-maker_4.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096141067518062/ezgif.com-gif-maker_8.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096145601560587/ezgif.com-gif-maker_5.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096150709960734/ezgif.com-gif-maker_6.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096162186625104/ezgif.com-gif-maker.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096165243224104/ezgif.com-gif-maker_1.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096173104267264/ezgif.com-gif-maker_3.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096177047044176/ezgif.com-gif-maker_7.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096177037606963/ezgif.com-gif-maker_2.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096179177226270/ezgif.com-gif-maker_9.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096181689876480/ezgif.com-gif-maker_10.gif']
                        image = random.choice(choices)
                        embed = discord.Embed(description=threesome, colour=discord.Colour.blue())
                        embed.set_image(url=image)

                        await ctx.send(embed=embed)
                elif first_gender == 'male':

                    if second_gender == 'female':
                        threesome = f"**{author} gets into threesome with {first.name} and {second.name}**"
                        choices = [
                            'https://cdn.discordapp.com/attachments/819857033489940481/821081377566490634/ezgif.com-gif-maker_2.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096123459567626/ezgif.com-gif-maker_4.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096141067518062/ezgif.com-gif-maker_8.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096145601560587/ezgif.com-gif-maker_5.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096150709960734/ezgif.com-gif-maker_6.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096162186625104/ezgif.com-gif-maker.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096165243224104/ezgif.com-gif-maker_1.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096173104267264/ezgif.com-gif-maker_3.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096177047044176/ezgif.com-gif-maker_7.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096177037606963/ezgif.com-gif-maker_2.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096179177226270/ezgif.com-gif-maker_9.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821096181689876480/ezgif.com-gif-maker_10.gif']
                        image = random.choice(choices)
                        embed = discord.Embed(description=threesome, colour=discord.Colour.blue())
                        embed.set_image(url=image)

                        await ctx.send(embed=embed)
                    elif second_gender == 'male':
                        threesome = f"**{author} gets into threesome with {first.name} and {second.name}**"
                        choices = ['https://cdn.discordapp.com/attachments/819857033489940481/821081498454065182/ezgif.com-gif-maker_3.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821099564453855292/ezgif.com-gif-maker_2.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821099573559820348/ezgif.com-gif-maker_1.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821099575694589972/ezgif.com-gif-maker_7.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821099577540214804/ezgif.com-gif-maker.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821099578026623006/ezgif.com-gif-maker_6.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821099578429800488/ezgif.com-gif-maker_5.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821099583668486184/ezgif.com-gif-maker_3.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821099585283293264/ezgif.com-gif-maker_4.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821099585291157544/ezgif.com-resize.gif']
                        image = random.choice(choices)
                        embed = discord.Embed(description=threesome, colour=discord.Colour.blue())
                        embed.set_image(url=image)

                        await ctx.send(embed=embed)
            elif author_gender == 'female':

                if first_gender == 'female':

                    if second_gender == 'female':
                        threesome = f"**{author} gets into threesome with {first.name} and {second.name}**"
                        choices = [
                            'https://cdn.discordapp.com/attachments/819857033489940481/821088123332198460/ezgif.com-resize_1.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821086364300476496/ezgif.com-gif-maker_1.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821088121323913266/ezgif.com-resize.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821086363754954772/ezgif.com-gif-maker_9.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821086362308313189/ezgif.com-gif-maker_2.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821086362094141450/ezgif.com-gif-maker_13.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821086362299793438/ezgif.com-gif-maker_3.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821086361301418004/ezgif.com-gif-maker.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821086360970461184/ezgif.com-gif-maker_12.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821086359308468278/ezgif.com-gif-maker_7.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821086357613969428/ezgif.com-gif-maker_6.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821086356129579028/ezgif.com-gif-maker_4.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821086316920832050/ezgif.com-gif-maker_8.gif',
                            'https://cdn.discordapp.com/attachments/819857033489940481/821081474086076436/ezgif.com-gif-maker.gif']
                        image = random.choice(choices)
                        embed = discord.Embed(description=threesome, colour=discord.Colour.blue())
                        embed.set_image(url=image)

                        await ctx.send(embed=embed)
                    elif second_gender == 'male':
                        threesome = f"**{author} gets into threesome with {first.name} and {second.name}**"
                        choices = ['https://cdn.discordapp.com/attachments/819857033489940481/821081444050534431/ezgif.com-gif-maker_1.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821091226005930014/ezgif.com-gif-maker_4.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821091234897723453/ezgif.com-gif-maker_7.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821091236076978206/ezgif.com-gif-maker_2.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821091239616315422/ezgif.com-gif-maker_1.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821091249527324703/ezgif.com-gif-maker_9.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821091249473060934/ezgif.com-gif-maker_5.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821091254926180397/ezgif.com-gif-maker_3.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821091255131045940/ezgif.com-gif-maker.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821091254740844584/ezgif.com-resize.gif']
                        image = random.choice(choices)
                        embed = discord.Embed(description=threesome, colour=discord.Colour.blue())
                        embed.set_image(url=image)

                        await ctx.send(embed=embed)
                elif first_gender == 'male':

                    if second_gender == 'female':
                        threesome = f"**{author} gets into threesome with {first.name} and {second.name}**"
                        choices = ['https://cdn.discordapp.com/attachments/819857033489940481/821081444050534431/ezgif.com-gif-maker_1.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821091226005930014/ezgif.com-gif-maker_4.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821091234897723453/ezgif.com-gif-maker_7.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821091236076978206/ezgif.com-gif-maker_2.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821091239616315422/ezgif.com-gif-maker_1.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821091249527324703/ezgif.com-gif-maker_9.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821091249473060934/ezgif.com-gif-maker_5.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821091254926180397/ezgif.com-gif-maker_3.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821091255131045940/ezgif.com-gif-maker.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821091254740844584/ezgif.com-resize.gif']
                        image = random.choice(choices)
                        embed = discord.Embed(description=threesome, colour=discord.Colour.blue())
                        embed.set_image(url=image)

                        await ctx.send(embed=embed)
                    elif second_gender == 'male':
                        threesome = f"**{author} gets into threesome with {first.name} and {second.name}**"
                        choices = ['https://cdn.discordapp.com/attachments/819857033489940481/821081377566490634/ezgif.com-gif-maker_2.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821096123459567626/ezgif.com-gif-maker_4.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821096141067518062/ezgif.com-gif-maker_8.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821096145601560587/ezgif.com-gif-maker_5.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821096150709960734/ezgif.com-gif-maker_6.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821096162186625104/ezgif.com-gif-maker.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821096165243224104/ezgif.com-gif-maker_1.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821096173104267264/ezgif.com-gif-maker_3.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821096177047044176/ezgif.com-gif-maker_7.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821096177037606963/ezgif.com-gif-maker_2.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821096179177226270/ezgif.com-gif-maker_9.gif',
                                   'https://cdn.discordapp.com/attachments/819857033489940481/821096181689876480/ezgif.com-gif-maker_10.gif']
                        image = random.choice(choices)
                        embed = discord.Embed(description=threesome, colour=discord.Colour.blue())
                        embed.set_image(url=image)

                        await ctx.send(embed=embed)

    @threesome.error
    async def threesome_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()

    @commands.command()
    @commands.is_nsfw()
    async def facial(self, ctx, message=None):
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message

        if ctx.author.id == 815647994203602994:
            if mentions == message:
                if message == None:
                    embed = discord.Embed(
                        description=f"**No sir this isn't how it works\nExample use: $facial @User#6969**",
                        colour=discord.Colour.blue())
                    await ctx.send(embed=embed)
                else:
                    author = ctx.author.name
                    facial = "**{0} gives a facial to {1}**"
                    choices = [
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125576319008778/ezgif.com-resize_3.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125583843852288/ezgif.com-resize_4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125587342163988/ezgif.com-resize_5.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125590928687154/ezgif.com-resize_6.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125596439085066/ezgif.com-resize_7.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125601933754378/ezgif.com-resize_8.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125603930505246/ezgif.com-resize_9.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125610758307890/ezgif.com-resize_10.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125615158657054/ezgif.com-resize_11.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125620234027038/ezgif.com-resize_12.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125626584465438/ezgif.com-resize_13.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125630569185300/ezgif.com-resize_14.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125637719687198/ezgif.com-resize.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125644238028840/tumblr_oq7xc49sfB1tgly7xo1_400.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125652210614282/ezgif.com-gif-maker.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125657542492221/816_1000.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125661292331048/ezgif.com-resize_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125663741018112/ezgif.com-resize_2.gif',
                        "https://cdn.discordapp.com/attachments/819857033489940481/825329302617980939/ezgif.com-optimize_1.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825329303306371072/ezgif.com-optimize_6.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825329309878059028/ezgif.com-optimize_3.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825329320007958538/ezgif.com-optimize_2.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825329327871623188/ezgif.com-gif-maker_2.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825329337481035786/ezgif.com-optimize_4.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825329341323542568/ezgif.com-optimize_5.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825329344246185984/ezgif.com-optimize_7.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825329347149037618/ezgif.com-optimize.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825329348282286100/ezgif.com-gif-maker.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825329349862883338/ezgif.com-gif-maker_1.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825329350592561152/ezgif.com-optimize_8.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(description=facial.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)

            else:
                author = ctx.author.name
                facial = "**{0} gives a facial to {1}**"
                choices = [
                    'https://cdn.discordapp.com/attachments/819857033489940481/822125576319008778/ezgif.com-resize_3.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822125583843852288/ezgif.com-resize_4.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822125587342163988/ezgif.com-resize_5.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822125590928687154/ezgif.com-resize_6.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822125596439085066/ezgif.com-resize_7.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822125601933754378/ezgif.com-resize_8.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822125603930505246/ezgif.com-resize_9.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822125610758307890/ezgif.com-resize_10.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822125615158657054/ezgif.com-resize_11.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822125620234027038/ezgif.com-resize_12.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822125626584465438/ezgif.com-resize_13.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822125630569185300/ezgif.com-resize_14.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822125637719687198/ezgif.com-resize.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822125644238028840/tumblr_oq7xc49sfB1tgly7xo1_400.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822125652210614282/ezgif.com-gif-maker.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822125657542492221/816_1000.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822125661292331048/ezgif.com-resize_1.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822125663741018112/ezgif.com-resize_2.gif',
                    "https://cdn.discordapp.com/attachments/819857033489940481/825329302617980939/ezgif.com-optimize_1.gif",
                    "https://cdn.discordapp.com/attachments/819857033489940481/825329303306371072/ezgif.com-optimize_6.gif",
                    "https://cdn.discordapp.com/attachments/819857033489940481/825329309878059028/ezgif.com-optimize_3.gif",
                    "https://cdn.discordapp.com/attachments/819857033489940481/825329320007958538/ezgif.com-optimize_2.gif",
                    "https://cdn.discordapp.com/attachments/819857033489940481/825329327871623188/ezgif.com-gif-maker_2.gif",
                    "https://cdn.discordapp.com/attachments/819857033489940481/825329337481035786/ezgif.com-optimize_4.gif",
                    "https://cdn.discordapp.com/attachments/819857033489940481/825329341323542568/ezgif.com-optimize_5.gif",
                    "https://cdn.discordapp.com/attachments/819857033489940481/825329344246185984/ezgif.com-optimize_7.gif",
                    "https://cdn.discordapp.com/attachments/819857033489940481/825329347149037618/ezgif.com-optimize.gif",
                    "https://cdn.discordapp.com/attachments/819857033489940481/825329348282286100/ezgif.com-gif-maker.gif",
                    "https://cdn.discordapp.com/attachments/819857033489940481/825329349862883338/ezgif.com-gif-maker_1.gif",
                    "https://cdn.discordapp.com/attachments/819857033489940481/825329350592561152/ezgif.com-optimize_8.gif"]
                img = random.choice(choices)
                embed = discord.Embed(description=facial.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=img)
                await ctx.send(embed=embed)

        if not ctx.author.id == 815647994203602994:
            if mentions == message:
                if message == None:
                    embed = discord.Embed(
                        description=f"**No sir this isn't how it works\nExample use: $facial @User#6969**",
                        colour=discord.Colour.blue())
                    await ctx.send(embed=embed)
                else:
                    choices = [
                        'https://cdn.discordapp.com/attachments/798913238229188608/822156703285379119/giphy_1.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822156709862178846/067025659eb25f9b74605738d1b2a7a7.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822155216287039509/IcyCookedCoot-small.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822156711674118174/200.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822156717138772048/giphy.gif']
                    image = random.choice(choices)
                    embed = discord.Embed(description="**This is a custom command**", colour=discord.Colour.blue())
                    embed.set_image(url=image)
                    embed.set_footer(text="$patreon to buy a custom command!")
                    await ctx.send(embed=embed)
            if ctx.message.mentions[0].id == 815647994203602994:

                author_gender = determineGender(ctx.author)
                if author_gender == 'female':
                    author = ctx.author.name
                    facial = "**{0} gets facial from {1}**"
                    choices = [
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125576319008778/ezgif.com-resize_3.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125583843852288/ezgif.com-resize_4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125587342163988/ezgif.com-resize_5.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125590928687154/ezgif.com-resize_6.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125596439085066/ezgif.com-resize_7.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125601933754378/ezgif.com-resize_8.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125603930505246/ezgif.com-resize_9.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125610758307890/ezgif.com-resize_10.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125615158657054/ezgif.com-resize_11.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125620234027038/ezgif.com-resize_12.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125626584465438/ezgif.com-resize_13.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125630569185300/ezgif.com-resize_14.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125637719687198/ezgif.com-resize.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125644238028840/tumblr_oq7xc49sfB1tgly7xo1_400.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125652210614282/ezgif.com-gif-maker.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125657542492221/816_1000.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125661292331048/ezgif.com-resize_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822125663741018112/ezgif.com-resize_2.gif',
                        "https://cdn.discordapp.com/attachments/819857033489940481/825329302617980939/ezgif.com-optimize_1.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825329303306371072/ezgif.com-optimize_6.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825329309878059028/ezgif.com-optimize_3.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825329320007958538/ezgif.com-optimize_2.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825329327871623188/ezgif.com-gif-maker_2.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825329337481035786/ezgif.com-optimize_4.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825329341323542568/ezgif.com-optimize_5.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825329344246185984/ezgif.com-optimize_7.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825329347149037618/ezgif.com-optimize.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825329348282286100/ezgif.com-gif-maker.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825329349862883338/ezgif.com-gif-maker_1.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825329350592561152/ezgif.com-optimize_8.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(description=facial.format(author, mentions.name),
                                          colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    choices = ['https://cdn.discordapp.com/attachments/798913238229188608/822155196053323776/tenor_1.gif',
                               'https://cdn.discordapp.com/attachments/798913238229188608/822155196322283520/tenor.gif',
                               'https://cdn.discordapp.com/attachments/798913238229188608/822155216287039509/IcyCookedCoot-small.gif']
                    image = random.choice(choices)
                    embed = discord.Embed(description="**This is a custom command**", colour=discord.Colour.blue())
                    embed.set_image(url=image)
                    embed.set_footer(text="$patreon to buy a custom command!")
                    await ctx.send(embed=embed)
            else:
                choices = [
                    'https://cdn.discordapp.com/attachments/798913238229188608/822156703285379119/giphy_1.gif',
                    'https://cdn.discordapp.com/attachments/798913238229188608/822156709862178846/067025659eb25f9b74605738d1b2a7a7.gif',
                    'https://cdn.discordapp.com/attachments/798913238229188608/822155216287039509/IcyCookedCoot-small.gif',
                    'https://cdn.discordapp.com/attachments/798913238229188608/822156711674118174/200.gif',
                    'https://cdn.discordapp.com/attachments/798913238229188608/822156717138772048/giphy.gif']
                image = random.choice(choices)
                embed = discord.Embed(description="**This is a custom command**", colour=discord.Colour.blue())
                embed.set_image(url=image)
                embed.set_footer(text="$patreon to buy a custom command!")
                await ctx.send(embed=embed)

    @facial.error
    async def facial_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()

    @commands.command(aliases=['dt'])
    @commands.is_nsfw()
    async def deepthroat(self, ctx, message=None):
        """Fucks the user you mention"""
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message

        author_gender = determineGender(ctx.author)

        if mentions == message:
            if message == None:
                embed = discord.Embed(
                    description=f"**You can't deepthroat nothing you horni dumbo\nExample use: $deepthroat @User#6969**",
                    colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                if author_gender == 'male':
                    author = ctx.message.author.name

                    dt = '**{0} get deepthroat from {1}**'

                    choices = [
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143535750316072/ezgif.com-gif-maker_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143539127255129/ezgif.com-resize_8.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143544445763584/ezgif.com-resize_6.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143549113630740/ezgif.com-resize_9.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143553781366834/ezgif.com-resize_11.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143557871206410/ezgif.com-resize_4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143562404855808/ezgif.com-resize_7.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143567744598096/ezgif.com-resize_10.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143573180547082/ezgif.com-resize_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143578401800222/ezgif.com-resize.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143585045577728/ezgif.com-resize_5.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143589899436052/ezgif.com-resize_3.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143593794895892/ezgif.com-resize_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143598689648651/ezgif.com-gif-maker.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143604486701166/ezgif.com-gif-maker_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143609217482782/ezgif.com-resize_12.gif'
                    ]
                    image = random.choice(choices)

                    embed = discord.Embed(description=dt.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)
                elif author_gender == 'female':
                    author = ctx.message.author.name

                    dt = '**{0} deepthroats {1}**'

                    choices = [
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143535750316072/ezgif.com-gif-maker_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143539127255129/ezgif.com-resize_8.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143544445763584/ezgif.com-resize_6.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143549113630740/ezgif.com-resize_9.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143553781366834/ezgif.com-resize_11.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143557871206410/ezgif.com-resize_4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143562404855808/ezgif.com-resize_7.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143567744598096/ezgif.com-resize_10.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143573180547082/ezgif.com-resize_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143578401800222/ezgif.com-resize.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143585045577728/ezgif.com-resize_5.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143589899436052/ezgif.com-resize_3.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143593794895892/ezgif.com-resize_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143598689648651/ezgif.com-gif-maker.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143604486701166/ezgif.com-gif-maker_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822143609217482782/ezgif.com-resize_12.gif'

                    ]
                    image = random.choice(choices)

                    embed = discord.Embed(description=dt.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

        mention_gender = determineGender(ctx.message.mentions[0])

        if author_gender == 'male':
            if mention_gender == 'male':
                author = ctx.message.author.name

                dt = '**{0} deepthroats {1}**'

                choices = [
                    'https://cdn.discordapp.com/attachments/819857033489940481/822145131708022824/ezgif.com-resize.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822145137718984735/ezgif.com-resize_3.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822145140289306674/ezgif.com-resize_1.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822145144652431370/ezgif.com-gif-maker_3.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822145148406071347/ezgif.com-gif-maker_1.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822145149295001640/ezgif.com-gif-maker_2.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822145151199608872/ezgif.com-gif-maker.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822145158141182032/ezgif.com-gif-maker_4.gif']

                image = random.choice(choices)

                embed = discord.Embed(description=dt.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)
                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name

                dt = '**{0} gets deepthroat from {1}**'

                choices = [
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143535750316072/ezgif.com-gif-maker_2.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143539127255129/ezgif.com-resize_8.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143544445763584/ezgif.com-resize_6.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143549113630740/ezgif.com-resize_9.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143553781366834/ezgif.com-resize_11.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143557871206410/ezgif.com-resize_4.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143562404855808/ezgif.com-resize_7.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143567744598096/ezgif.com-resize_10.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143573180547082/ezgif.com-resize_2.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143578401800222/ezgif.com-resize.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143585045577728/ezgif.com-resize_5.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143589899436052/ezgif.com-resize_3.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143593794895892/ezgif.com-resize_1.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143598689648651/ezgif.com-gif-maker.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143604486701166/ezgif.com-gif-maker_1.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143609217482782/ezgif.com-resize_12.gif'

                    ]

                image = random.choice(choices)

                embed = discord.Embed(description=dt.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif author_gender == 'female':

            if mention_gender == 'female':
                author = ctx.message.author.name

                dt = '**{0} deepthroats {1}**'

                choices = [
                    'https://cdn.discordapp.com/attachments/819857033489940481/822138064969269258/ezgif.com-resize_1.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822138068550418443/ezgif.com-resize.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822138075701575730/ezgif.com-resize_2.gif'
                    ]

                image = random.choice(choices)

                embed = discord.Embed(description=dt.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name

                dt = '**{0} deepthroats {1}**'

                choices = [
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143535750316072/ezgif.com-gif-maker_2.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143539127255129/ezgif.com-resize_8.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143544445763584/ezgif.com-resize_6.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143549113630740/ezgif.com-resize_9.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143553781366834/ezgif.com-resize_11.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143557871206410/ezgif.com-resize_4.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143562404855808/ezgif.com-resize_7.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143567744598096/ezgif.com-resize_10.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143573180547082/ezgif.com-resize_2.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143578401800222/ezgif.com-resize.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143585045577728/ezgif.com-resize_5.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143589899436052/ezgif.com-resize_3.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143593794895892/ezgif.com-resize_1.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143598689648651/ezgif.com-gif-maker.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143604486701166/ezgif.com-gif-maker_1.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822143609217482782/ezgif.com-resize_12.gif'

                ]

                image = random.choice(choices)

                embed = discord.Embed(description=dt.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

    @deepthroat.error
    async def deepthroat_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()

    @commands.command()
    @commands.is_nsfw()
    async def doggy(self, ctx, message=None):
        """Fucks the user you mention"""
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message

        author_gender = determineGender(ctx.author)

        if mentions == message:
            if message == None:
                embed = discord.Embed(
                    description=f"**You can't fuck nothing you horni dumbo\nExample use: $doggy @User#6969**",
                    colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                if author_gender == 'male':
                    author = ctx.message.author.name

                    doggy = '**{0} fucks {1} doggy style**'

                    choices = [
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135388545351700/ezgif.com-gif-maker_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135394363506688/ezgif.com-resize_3.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135398239043614/ezgif.com-gif-maker_5.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135402630479882/ezgif.com-resize.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135406467481641/ezgif.com-resize_4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135411325141022/ezgif.com-resize_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135416260919306/ezgif.com-resize_5.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135422061903882/ezgif.com-gif-maker.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135431327514634/ezgif.com-gif-maker_3.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135431792427039/ezgif.com-gif-maker_6.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135436414681088/ezgif.com-resize_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135441699635200/ezgif.com-resize_6.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135446402105394/ezgif.com-gif-maker_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135451007320104/ezgif.com-gif-maker_4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135457449377852/ezgif.com-gif-maker_8.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135633287315486/mf_doggy1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135665868275793/ezgif.com-gif-maker.gif']
                    image = random.choice(choices)

                    embed = discord.Embed(description=doggy.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)
                elif author_gender == 'female':
                    author = ctx.message.author.name

                    doggy = '**{0} gets fucked by {1} doggy style**'

                    choices = [
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135388545351700/ezgif.com-gif-maker_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135394363506688/ezgif.com-resize_3.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135398239043614/ezgif.com-gif-maker_5.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135402630479882/ezgif.com-resize.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135406467481641/ezgif.com-resize_4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135411325141022/ezgif.com-resize_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135416260919306/ezgif.com-resize_5.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135422061903882/ezgif.com-gif-maker.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135431327514634/ezgif.com-gif-maker_3.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135431792427039/ezgif.com-gif-maker_6.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135436414681088/ezgif.com-resize_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135441699635200/ezgif.com-resize_6.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135446402105394/ezgif.com-gif-maker_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135451007320104/ezgif.com-gif-maker_4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135457449377852/ezgif.com-gif-maker_8.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135633287315486/mf_doggy1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/822135665868275793/ezgif.com-gif-maker.gif']
                    image = random.choice(choices)

                    embed = discord.Embed(description=doggy.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)

        mention_gender = determineGender(ctx.message.mentions[0])

        if author_gender == 'male':
            if mention_gender == 'male':
                author = ctx.message.author.name

                doggy = '**{0} fucks {1} doggy style**'

                choices = [
                    'https://cdn.discordapp.com/attachments/819857033489940481/822136536346132501/ezgif.com-resize_2.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822136540087975966/ezgif.com-resize_1.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822136544302727188/ezgif.com-resize.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822136546500149248/ezgif.com-resize_3.gif'
                    ]

                image = random.choice(choices)

                embed = discord.Embed(description=doggy.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)
                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name

                doggy = '**{0} fucks {1} doggy style**'

                choices = [
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135388545351700/ezgif.com-gif-maker_1.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135394363506688/ezgif.com-resize_3.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135398239043614/ezgif.com-gif-maker_5.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135402630479882/ezgif.com-resize.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135406467481641/ezgif.com-resize_4.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135411325141022/ezgif.com-resize_2.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135416260919306/ezgif.com-resize_5.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135422061903882/ezgif.com-gif-maker.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135431327514634/ezgif.com-gif-maker_3.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135431792427039/ezgif.com-gif-maker_6.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135436414681088/ezgif.com-resize_1.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135441699635200/ezgif.com-resize_6.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135446402105394/ezgif.com-gif-maker_2.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135451007320104/ezgif.com-gif-maker_4.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135457449377852/ezgif.com-gif-maker_8.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135633287315486/mf_doggy1.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135665868275793/ezgif.com-gif-maker.gif']

                image = random.choice(choices)

                embed = discord.Embed(description=doggy.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif author_gender == 'female':

            if mention_gender == 'female':
                author = ctx.message.author.name

                doggy = '**{0} fucks {1} doggy style**'

                choices = [
                    'https://cdn.discordapp.com/attachments/819857033489940481/822129239674454016/ezgif.com-gif-maker_1.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822129245676634122/ezgif.com-resize_1.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822129254296846346/ezgif.com-resize_3.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822129261342883841/ezgif.com-resize_7.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822129264706977833/ezgif.com-resize_6.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822129267604324402/ezgif.com-resize_2.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822129271975051314/ezgif.com-resize.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822129273086148678/ezgif.com-gif-maker.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822129276727328839/ezgif.com-resize_8.gif', ]

                image = random.choice(choices)

                embed = discord.Embed(description=doggy.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

            else:
                author = ctx.message.author.name

                doggy = '**{0} gets fucked by {1} doggy style**'

                choices = [
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135388545351700/ezgif.com-gif-maker_1.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135394363506688/ezgif.com-resize_3.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135398239043614/ezgif.com-gif-maker_5.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135402630479882/ezgif.com-resize.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135406467481641/ezgif.com-resize_4.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135411325141022/ezgif.com-resize_2.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135416260919306/ezgif.com-resize_5.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135422061903882/ezgif.com-gif-maker.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135431327514634/ezgif.com-gif-maker_3.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135431792427039/ezgif.com-gif-maker_6.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135436414681088/ezgif.com-resize_1.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135441699635200/ezgif.com-resize_6.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135446402105394/ezgif.com-gif-maker_2.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135451007320104/ezgif.com-gif-maker_4.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135457449377852/ezgif.com-gif-maker_8.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135633287315486/mf_doggy1.gif',
                    'https://cdn.discordapp.com/attachments/819857033489940481/822135665868275793/ezgif.com-gif-maker.gif']

                image = random.choice(choices)

                embed = discord.Embed(description=doggy.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

    @doggy.error
    async def doggy_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()

    @commands.command(aliases=['kisd'])
    async def kiss(self, ctx, message=None):
        """
            Kisses the member you mention
            """
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author = ctx.author.name
        if ctx.channel.is_nsfw():
            author_gender = determineGender(ctx.author)
            if mentions == message:
                if message == None:
                    kiss = "**I'm giving you a kiss for free this time next one won't be free...**"
                    choices = [
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434169883066388/6ac891a9cf33d5f1264f0ed9e67ea347.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434269023436840/giphy.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434269250715688/tumblr_mxux0rs9dL1sottyfo1_250.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434271586680872/french-kiss-animated-gif.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434280545452042/Friends-Benefits.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434289827577956/8efc1fcc0fcdd3c709ba53ac81c68876.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434298089963520/take-charge-move-HOT.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434316902334484/rude-french-kiss-animated-gif.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434341128372234/unnamed_4.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434342679871498/112f64c195a38c7666282afa47882e1d.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434355367903242/converted.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434355484819476/a0b9df_7d604b3c483c41008be5c7fdc2961fbe_mv2.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434363395801088/199459570002202.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434364624994324/45455dd901bbc966ca22fad95bb50872.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434391980638228/tumblr_inline_mw7okylqq81rxxsf3540.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434394689634345/tumblr_mpohcc72jY1s4jklgo1_500.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434399370870794/tumblr_mx1e4zf92t1saf5c9o1_500.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434400427835402/unnamed_3.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434400775307305/tumblr_n7s90oVLEx1rnnw2ro1_500.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434402348040212/mirelagenova.tumblr.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434416936353812/tumblr_ofxkiugnwT1qztcolo1_500.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434422401138688/tumblr_ngzux2dOjh1u6otdyo1_500.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434423881334794/tumblr_p0m8i2nxsI1v99polo1_500.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434424545083402/tumblr_od3y2ufRKA1v0i32bo1_500.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434441241952287/tumblr_n1encnMwnR1so4hvdo1_400.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434453502558288/unnamed_5.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434460142141481/unnamed_2.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434478156152852/978969085-porn-gif-nsfw-gif-sex-tease-pussy-oily-massage-pleasure-kiss-Hot-Oil.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434490205863977/Hot-Kisses-Love-GIF-HotKisses-Love-Couple-Discover-and-Share-GIFs.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434492392013864/unnamed.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434531080536074/unnamed_1.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434541024182302/Anna-Faris-sexy-kiss-gif.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434545335926814/giphy_1.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822435845633605702/gifcandy-kissing-10.gif']
                    img = random.choice(choices)
                    embed = discord.Embed(description=kiss.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:

                    kiss = '**{0} gave {1} a kiss!**'
                    choices = [
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434169883066388/6ac891a9cf33d5f1264f0ed9e67ea347.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434269023436840/giphy.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434269250715688/tumblr_mxux0rs9dL1sottyfo1_250.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434271586680872/french-kiss-animated-gif.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434280545452042/Friends-Benefits.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434289827577956/8efc1fcc0fcdd3c709ba53ac81c68876.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434298089963520/take-charge-move-HOT.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434316902334484/rude-french-kiss-animated-gif.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434341128372234/unnamed_4.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434342679871498/112f64c195a38c7666282afa47882e1d.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434355367903242/converted.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434355484819476/a0b9df_7d604b3c483c41008be5c7fdc2961fbe_mv2.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434363395801088/199459570002202.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434364624994324/45455dd901bbc966ca22fad95bb50872.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434391980638228/tumblr_inline_mw7okylqq81rxxsf3540.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434394689634345/tumblr_mpohcc72jY1s4jklgo1_500.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434399370870794/tumblr_mx1e4zf92t1saf5c9o1_500.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434400427835402/unnamed_3.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434400775307305/tumblr_n7s90oVLEx1rnnw2ro1_500.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434402348040212/mirelagenova.tumblr.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434416936353812/tumblr_ofxkiugnwT1qztcolo1_500.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434422401138688/tumblr_ngzux2dOjh1u6otdyo1_500.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434423881334794/tumblr_p0m8i2nxsI1v99polo1_500.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434424545083402/tumblr_od3y2ufRKA1v0i32bo1_500.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434441241952287/tumblr_n1encnMwnR1so4hvdo1_400.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434453502558288/unnamed_5.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434460142141481/unnamed_2.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434478156152852/978969085-porn-gif-nsfw-gif-sex-tease-pussy-oily-massage-pleasure-kiss-Hot-Oil.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434490205863977/Hot-Kisses-Love-GIF-HotKisses-Love-Couple-Discover-and-Share-GIFs.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434492392013864/unnamed.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434531080536074/unnamed_1.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434541024182302/Anna-Faris-sexy-kiss-gif.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822434545335926814/giphy_1.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822435845633605702/gifcandy-kissing-10.gif']
                    img = random.choice(choices)
                    embed = discord.Embed(description=kiss.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)

            else:
                mention_gender = determineGender(ctx.message.mentions[0])
                if author_gender == 'male':
                    if mention_gender == 'female':
                        kiss = '**{0} gave {1} a kiss!**'
                        choices = [
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434169883066388/6ac891a9cf33d5f1264f0ed9e67ea347.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434269023436840/giphy.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434269250715688/tumblr_mxux0rs9dL1sottyfo1_250.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434271586680872/french-kiss-animated-gif.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434280545452042/Friends-Benefits.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434289827577956/8efc1fcc0fcdd3c709ba53ac81c68876.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434298089963520/take-charge-move-HOT.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434316902334484/rude-french-kiss-animated-gif.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434341128372234/unnamed_4.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434342679871498/112f64c195a38c7666282afa47882e1d.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434355367903242/converted.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434355484819476/a0b9df_7d604b3c483c41008be5c7fdc2961fbe_mv2.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434363395801088/199459570002202.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434364624994324/45455dd901bbc966ca22fad95bb50872.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434391980638228/tumblr_inline_mw7okylqq81rxxsf3540.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434394689634345/tumblr_mpohcc72jY1s4jklgo1_500.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434399370870794/tumblr_mx1e4zf92t1saf5c9o1_500.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434400427835402/unnamed_3.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434400775307305/tumblr_n7s90oVLEx1rnnw2ro1_500.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434402348040212/mirelagenova.tumblr.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434416936353812/tumblr_ofxkiugnwT1qztcolo1_500.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434422401138688/tumblr_ngzux2dOjh1u6otdyo1_500.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434423881334794/tumblr_p0m8i2nxsI1v99polo1_500.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434424545083402/tumblr_od3y2ufRKA1v0i32bo1_500.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434441241952287/tumblr_n1encnMwnR1so4hvdo1_400.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434453502558288/unnamed_5.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434460142141481/unnamed_2.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434478156152852/978969085-porn-gif-nsfw-gif-sex-tease-pussy-oily-massage-pleasure-kiss-Hot-Oil.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434490205863977/Hot-Kisses-Love-GIF-HotKisses-Love-Couple-Discover-and-Share-GIFs.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434492392013864/unnamed.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434531080536074/unnamed_1.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434541024182302/Anna-Faris-sexy-kiss-gif.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434545335926814/giphy_1.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822435845633605702/gifcandy-kissing-10.gif']
                        img = random.choice(choices)
                        embed = discord.Embed(description=kiss.format(author, mentions.name),
                                              colour=discord.Colour.blue())
                        embed.set_image(url=img)
                        await ctx.send(embed=embed)

                    else:
                        kiss = '**{0} gave {1} a kiss!**'
                        choices = [
                            'https://cdn.discordapp.com/attachments/798913238229188608/822438593439858718/tumblr_m58c705jhK1r5hvf9o1_500.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822438625110261790/b1ffae7532778a98b63fadf3c03a2cdb.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822438650163625994/tenor.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822438692625973288/gay_missionary_s-9304.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822438698603642880/giphy.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822438707071025152/tumblr_m38b1bW9kt1qgdqppo1_500.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822438711219191808/tumblr_o8yd9x6HK51u4tftco1_500.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822438721735360522/monophy.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822438727216529428/22e05cd3a939cb4c4bf68586219696cf.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822438744741118022/de4dd6257aa2411821e9a47a0de7d182.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822438747861024828/tumblr_dbf93aff4c7670a5a3c9fe6cf49aef66_b1038178_400.gif']
                        img = random.choice(choices)
                        embed = discord.Embed(description=kiss.format(author, mentions.name),
                                              colour=discord.Colour.blue())
                        embed.set_image(url=img)
                        await ctx.send(embed=embed)

                elif author_gender == 'female':
                    if mention_gender == 'male':
                        kiss = '**{0} gave {1} a kiss!**'
                        choices = [
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434169883066388/6ac891a9cf33d5f1264f0ed9e67ea347.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434269023436840/giphy.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434269250715688/tumblr_mxux0rs9dL1sottyfo1_250.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434271586680872/french-kiss-animated-gif.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434280545452042/Friends-Benefits.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434289827577956/8efc1fcc0fcdd3c709ba53ac81c68876.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434298089963520/take-charge-move-HOT.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434316902334484/rude-french-kiss-animated-gif.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434341128372234/unnamed_4.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434342679871498/112f64c195a38c7666282afa47882e1d.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434355367903242/converted.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434355484819476/a0b9df_7d604b3c483c41008be5c7fdc2961fbe_mv2.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434363395801088/199459570002202.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434364624994324/45455dd901bbc966ca22fad95bb50872.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434391980638228/tumblr_inline_mw7okylqq81rxxsf3540.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434394689634345/tumblr_mpohcc72jY1s4jklgo1_500.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434399370870794/tumblr_mx1e4zf92t1saf5c9o1_500.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434400427835402/unnamed_3.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434400775307305/tumblr_n7s90oVLEx1rnnw2ro1_500.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434402348040212/mirelagenova.tumblr.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434416936353812/tumblr_ofxkiugnwT1qztcolo1_500.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434422401138688/tumblr_ngzux2dOjh1u6otdyo1_500.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434423881334794/tumblr_p0m8i2nxsI1v99polo1_500.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434424545083402/tumblr_od3y2ufRKA1v0i32bo1_500.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434441241952287/tumblr_n1encnMwnR1so4hvdo1_400.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434453502558288/unnamed_5.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434460142141481/unnamed_2.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434478156152852/978969085-porn-gif-nsfw-gif-sex-tease-pussy-oily-massage-pleasure-kiss-Hot-Oil.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434490205863977/Hot-Kisses-Love-GIF-HotKisses-Love-Couple-Discover-and-Share-GIFs.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434492392013864/unnamed.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434531080536074/unnamed_1.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434541024182302/Anna-Faris-sexy-kiss-gif.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822434545335926814/giphy_1.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822435845633605702/gifcandy-kissing-10.gif']
                        img = random.choice(choices)
                        embed = discord.Embed(description=kiss.format(author, mentions.name),
                                              colour=discord.Colour.blue())
                        embed.set_image(url=img)
                        await ctx.send(embed=embed)

                    else:
                        kiss = '**{0} gave {1} a kiss!**'
                        choices = [
                            'https://cdn.discordapp.com/attachments/798913238229188608/822441150601232384/unnamed_5.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822441156457398272/unnamed_3.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822441163821809664/pd9nilp.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822441187444129792/tumblr_b115e7a2a46ceb2ebe131641747d4cd5_dfdcf082_250.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822441217681784842/lusciousnet_lusciousnet_girlfriend-in-the-moment-183_188765318.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822441220138991656/bed7a191ce2101ea6deda12e100435b7.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822441244324135003/167A03A.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822441252736860220/unnamed_6.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822441253157077022/b38d66a8db0616430a96a94e3026eb42.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822441260891373588/Lesbian-Kissing.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822441276036481054/unnamed_1.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822441290616143892/Bree-Daniels-and-Malena-Morgan-in-hot-lesbian-kissing-gif.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822441293749551104/tumblr_mtg1f6umOA1snae27o1_250.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822441295527280640/unnamed_4.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822441331921780776/unnamed_2.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822441333951299604/tumblr_ndz2g4hpz61tkpgw6o1_400.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822441337785286676/607cd29e1f8ae0449222e3e61cb71bfa.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822441343124897832/original_1.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822441347319332874/tenor.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822441352951758848/original.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822441358002094130/unnamed.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822441386900979722/hot-nude-lesbian-kiss-gifs-6.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822441401806487552/4af5e6422e31a296c2b779612d2a7276.gif',
                            'https://cdn.discordapp.com/attachments/798913238229188608/822441431225991248/4a36a581570677368f9b3564b4ea46db.gif'
                            ]
                        img = random.choice(choices)
                        embed = discord.Embed(description=kiss.format(author, mentions.name),
                                              colour=discord.Colour.blue())
                        embed.set_image(url=img)
                        await ctx.send(embed=embed)

        else:
            if mentions == message:
                if message == None:

                    kiss = '**I will give you a kiss so dont be lonely you baka~~**'

                    choices = ['https://media0.giphy.com/media/bGm9FuBCGg4SY/giphy.gif',
                               'http://giphygifs.s3.amazonaws.com/media/FqBTvSNjNzeZG/giphy.gif',
                               'https://media3.giphy.com/media/12VXIxKaIEarL2/giphy.gif',
                               'https://media.tenor.com/images/197df534507bd229ba790e8e1b5f63dc/tenor.gif',
                               'https://i1.wp.com/loveisaname.com/wp-content/uploads/2016/09/23.gif',
                               'http://33.media.tumblr.com/tumblr_m7x4176tyH1ro4cfco1_500.gif',
                               'https://wethehunted.files.wordpress.com/2015/11/katanagatari-kiss.gif',
                               'https://i0.wp.com/media2.giphy.com/media/ll5leTSPh4ocE/giphy.gif?resize=500%2C290&ssl=1']

                    image = random.choice(choices)

                    embed = discord.Embed(description=kiss, colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)
                else:
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

                    embed = discord.Embed(description=kiss.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=image)

                    await ctx.send(embed=embed)
            else:
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

                embed = discord.Embed(description=kiss.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

    @commands.command()
    @commands.is_nsfw()
    async def brat(self, ctx, message=None):
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author = ctx.author.name
        if ctx.author.id in [707943916384813117, 545407515974828052, 686387166498259010, 733204237324124210, 628462934204481537]:
            if mentions == message:
                if message == None:
                    txt = ["**{0} says Are you finished already?**",
                           "**{0} says No and you can't make me**",
                           "**{0} says You hit like a girl**",
                           "**{0} says You can bring me a coffee**",
                           "**{0} says Is that all you got?**",
                           "**{0} says That was it, I thought there was more!**",
                           "**{0} says What do i look like, your maid?**"]
                    choices = [
                        'https://cdn.discordapp.com/attachments/798913238229188608/822404057204260904/ezgif.com-gif-maker_4.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822404712598863935/ezgif.com-optimize.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822405045772746772/ezgif.com-gif-maker_5.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822405634631794718/ezgif.com-gif-maker_6.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822405736058716200/ezgif.com-gif-maker_7.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822406961995710484/ezgif.com-optimize_1.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822407059936772146/ezgif.com-gif-maker_8.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822407579207991306/ezgif.com-optimize_2.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822408722298568714/ezgif.com-gif-maker_9.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822409280862421002/ezgif.com-gif-maker_10.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822409549754925056/ezgif.com-gif-maker_11.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822409892731551774/ezgif.com-optimize_3.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822410014601248778/ezgif.com-gif-maker_12.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822410635400052766/ezgif.com-gif-maker_13.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822411080083963954/ezgif.com-gif-maker_14.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822411206643154954/ezgif.com-gif-maker_15.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822413681462870036/ezgif.com-optimize_4.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822502400493224027/ezgif-6-fd7f9bdf64b4.gif']
                    brat = random.choice(txt)
                    img = random.choice(choices)
                    embed = discord.Embed(description=brat.format(author), colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    txt = ["**{0} says Are you finished already? to {1}**",
                           "**{0} says No and you can't make me to {1}**",
                           "**{0} says You hit like a girl to {1}**",
                           "**{0} says You can bring me a coffee to {1}**",
                           "**{0} says Is that all you got?**",
                           "**{0} says That was it, I thought there was more! to {1}**",
                           "**{0} says What do i look like, your maid? to {1}**"]
                    choices = [
                        'https://cdn.discordapp.com/attachments/798913238229188608/822404057204260904/ezgif.com-gif-maker_4.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822404712598863935/ezgif.com-optimize.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822405045772746772/ezgif.com-gif-maker_5.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822405634631794718/ezgif.com-gif-maker_6.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822405736058716200/ezgif.com-gif-maker_7.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822406961995710484/ezgif.com-optimize_1.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822407059936772146/ezgif.com-gif-maker_8.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822407579207991306/ezgif.com-optimize_2.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822408722298568714/ezgif.com-gif-maker_9.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822409280862421002/ezgif.com-gif-maker_10.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822409549754925056/ezgif.com-gif-maker_11.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822409892731551774/ezgif.com-optimize_3.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822410014601248778/ezgif.com-gif-maker_12.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822410635400052766/ezgif.com-gif-maker_13.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822411080083963954/ezgif.com-gif-maker_14.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822411206643154954/ezgif.com-gif-maker_15.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822413681462870036/ezgif.com-optimize_4.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822502400493224027/ezgif-6-fd7f9bdf64b4.gif']
                    brat = random.choice(txt)
                    img = random.choice(choices)
                    embed = discord.Embed(description=brat.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)

            else:
                txt = ["**{0} says Are you finished already? to {1}**",
                       "**{0} says No and you can't make me to {1}**",
                       "**{0} says You hit like a girl to {1}**",
                       "**{0} says You can bring me a coffee to {1}**",
                       "**{0} says Is that all you got?**",
                       "**{0} says That was it, I thought there was more! to {1}**",
                       "**{0} says What do i look like, your maid? to {1}**"]
                choices = [
                    'https://cdn.discordapp.com/attachments/798913238229188608/822404057204260904/ezgif.com-gif-maker_4.gif',
                    'https://cdn.discordapp.com/attachments/798913238229188608/822404712598863935/ezgif.com-optimize.gif',
                    'https://cdn.discordapp.com/attachments/798913238229188608/822405045772746772/ezgif.com-gif-maker_5.gif',
                    'https://cdn.discordapp.com/attachments/798913238229188608/822405634631794718/ezgif.com-gif-maker_6.gif',
                    'https://cdn.discordapp.com/attachments/798913238229188608/822405736058716200/ezgif.com-gif-maker_7.gif',
                    'https://cdn.discordapp.com/attachments/798913238229188608/822406961995710484/ezgif.com-optimize_1.gif',
                    'https://cdn.discordapp.com/attachments/798913238229188608/822407059936772146/ezgif.com-gif-maker_8.gif',
                    'https://cdn.discordapp.com/attachments/798913238229188608/822407579207991306/ezgif.com-optimize_2.gif',
                    'https://cdn.discordapp.com/attachments/798913238229188608/822408722298568714/ezgif.com-gif-maker_9.gif',
                    'https://cdn.discordapp.com/attachments/798913238229188608/822409280862421002/ezgif.com-gif-maker_10.gif',
                    'https://cdn.discordapp.com/attachments/798913238229188608/822409549754925056/ezgif.com-gif-maker_11.gif',
                    'https://cdn.discordapp.com/attachments/798913238229188608/822409892731551774/ezgif.com-optimize_3.gif',
                    'https://cdn.discordapp.com/attachments/798913238229188608/822410014601248778/ezgif.com-gif-maker_12.gif',
                    'https://cdn.discordapp.com/attachments/798913238229188608/822410635400052766/ezgif.com-gif-maker_13.gif',
                    'https://cdn.discordapp.com/attachments/798913238229188608/822411080083963954/ezgif.com-gif-maker_14.gif',
                    'https://cdn.discordapp.com/attachments/798913238229188608/822411206643154954/ezgif.com-gif-maker_15.gif',
                    'https://cdn.discordapp.com/attachments/798913238229188608/822413681462870036/ezgif.com-optimize_4.gif',
                    'https://cdn.discordapp.com/attachments/798913238229188608/822502400493224027/ezgif-6-fd7f9bdf64b4.gif']
                brat = random.choice(txt)
                img = random.choice(choices)
                embed = discord.Embed(description=brat.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=img)
                await ctx.send(embed=embed)

        else:
            choices = [
                'https://cdn.discordapp.com/attachments/798913238229188608/822156703285379119/giphy_1.gif',
                'https://cdn.discordapp.com/attachments/798913238229188608/822156709862178846/067025659eb25f9b74605738d1b2a7a7.gif',
                'https://cdn.discordapp.com/attachments/798913238229188608/822155216287039509/IcyCookedCoot-small.gif',
                'https://cdn.discordapp.com/attachments/798913238229188608/822156711674118174/200.gif',
                'https://cdn.discordapp.com/attachments/798913238229188608/822156717138772048/giphy.gif']
            image = random.choice(choices)
            embed = discord.Embed(description="**This is a custom command**", colour=discord.Colour.blue())
            embed.set_image(url=image)
            embed.set_footer(text="$patreon to buy a custom command!")
            await ctx.send(embed=embed)

    @brat.error
    async def brat_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()

    @commands.command()
    @commands.is_nsfw()
    async def porn(self, ctx):
        subreddit = await reddit.subreddit("nsfw", fetch=True)

        all_subs = []
        async for submission in subreddit.hot(limit=50):
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        em = discord.Embed(title=name, colour=discord.Colour.blue())
        em.set_image(url=url)

        await ctx.send(embed=em)

    @porn.error
    async def porn_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()

    @commands.command()
    @commands.is_nsfw()
    async def hentai(self, ctx):
        subreddit = await reddit.subreddit("hentai", fetch=True)

        all_subs = []
        async for submission in subreddit.hot(limit=50):
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        em = discord.Embed(title=name, colour=discord.Colour.blue())
        em.set_image(url=url)

        await ctx.send(embed=em)

    @hentai.error
    async def hentai_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()

    @commands.command()
    @commands.is_nsfw()
    async def missionary(self, ctx, message=None):
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author = ctx.author.name
        author_gender = determineGender(ctx.author)
        if mentions == message:
            if message == None:
                embed = discord.Embed(
                    description=f"**You can't fuck with nothing you horni dumbo\nExample use: $missionary @User#6969 **",
                    colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:

                if author_gender == 'male':
                    missionary = f"{author} fucks {mentions}"
                    choices = ['https://cdn.discordapp.com/attachments/819857033489940481/823970643749371944/ezgif.com-optimize_2.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/823970648397185034/ezgif.com-optimize_4.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/823970650766835742/ezgif.com-optimize_5.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/823970654830592051/ezgif.com-optimize_6.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/823970659520610304/ezgif.com-optimize_8.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/823970663051427880/ezgif.com-optimize_11.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/823970666729570374/ezgif.com-optimize_12.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/823970669741342720/ezgif.com-optimize_13.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/823970674677776384/ezgif.com-gif-maker_1.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/823970676389838878/ezgif.com-gif-maker_2.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/823970715836481566/ezgif.com-gif-maker_7.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/823970723881680907/ezgif.com-gif-maker.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/823970735617736714/ezgif.com-optimize_1.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/823971090832556052/ezgif.com-gif-maker_4.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/823971173653938196/ezgif.com-gif-maker_6.gif']
                    img = random.choice(choices)
                    embed = discord.Embed(title=missionary, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    missionary = f"{author} gets fucked by {mentions}"
                    choices = [
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970643749371944/ezgif.com-optimize_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970648397185034/ezgif.com-optimize_4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970650766835742/ezgif.com-optimize_5.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970654830592051/ezgif.com-optimize_6.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970659520610304/ezgif.com-optimize_8.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970663051427880/ezgif.com-optimize_11.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970666729570374/ezgif.com-optimize_12.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970669741342720/ezgif.com-optimize_13.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970674677776384/ezgif.com-gif-maker_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970676389838878/ezgif.com-gif-maker_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970715836481566/ezgif.com-gif-maker_7.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970723881680907/ezgif.com-gif-maker.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970735617736714/ezgif.com-optimize_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823971090832556052/ezgif.com-gif-maker_4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823971173653938196/ezgif.com-gif-maker_6.gif']
                    img = random.choice(choices)
                    embed = discord.Embed(title=missionary, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
        else:
            mention_gender = determineGender(ctx.message.mentions[0])
            if author_gender == 'male':
                if mention_gender == 'female':
                    missionary = f"{author} fucks {mentions.name}"
                    choices = [
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970643749371944/ezgif.com-optimize_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970648397185034/ezgif.com-optimize_4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970650766835742/ezgif.com-optimize_5.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970654830592051/ezgif.com-optimize_6.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970659520610304/ezgif.com-optimize_8.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970663051427880/ezgif.com-optimize_11.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970666729570374/ezgif.com-optimize_12.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970669741342720/ezgif.com-optimize_13.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970674677776384/ezgif.com-gif-maker_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970676389838878/ezgif.com-gif-maker_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970715836481566/ezgif.com-gif-maker_7.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970723881680907/ezgif.com-gif-maker.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970735617736714/ezgif.com-optimize_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823971090832556052/ezgif.com-gif-maker_4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823971173653938196/ezgif.com-gif-maker_6.gif']
                    img = random.choice(choices)
                    embed = discord.Embed(title=missionary, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    missionary = f"{author} fucks {mentions.name}"
                    choices = ['https://cdn.discordapp.com/attachments/798913238229188608/824014525803921418/ezgif.com-gif-maker_16.gif',
                               'https://cdn.discordapp.com/attachments/798913238229188608/824014536985411624/ezgif.com-crop.gif',
                               'https://cdn.discordapp.com/attachments/798913238229188608/824014551326392400/ezgif.com-gif-maker_17.gif',
                               'https://cdn.discordapp.com/attachments/798913238229188608/824014557604479046/ezgif.com-gif-maker_18.gif']
                    img = random.choice(choices)
                    embed = discord.Embed(title=missionary, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
            elif author_gender == 'female':
                if mention_gender == 'male':
                    missionary = f"{author} gets fucked by {mentions.name}"
                    choices = [
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970643749371944/ezgif.com-optimize_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970648397185034/ezgif.com-optimize_4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970650766835742/ezgif.com-optimize_5.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970654830592051/ezgif.com-optimize_6.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970659520610304/ezgif.com-optimize_8.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970663051427880/ezgif.com-optimize_11.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970666729570374/ezgif.com-optimize_12.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970669741342720/ezgif.com-optimize_13.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970674677776384/ezgif.com-gif-maker_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970676389838878/ezgif.com-gif-maker_2.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970715836481566/ezgif.com-gif-maker_7.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970723881680907/ezgif.com-gif-maker.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823970735617736714/ezgif.com-optimize_1.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823971090832556052/ezgif.com-gif-maker_4.gif',
                        'https://cdn.discordapp.com/attachments/819857033489940481/823971173653938196/ezgif.com-gif-maker_6.gif']
                    img = random.choice(choices)
                    embed = discord.Embed(title=missionary, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    missionary = f"{author} fucks {mentions.name}"
                    choices = ['https://cdn.discordapp.com/attachments/819857033489940481/823973139461570650/missbarbara-fjmao-22a460.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/823973143651680276/rzc9Mn2.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/823973149150019635/tumblr_oa9hjuFj7u1vzj8r7o1_500.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/823973157219860501/ezgif.com-optimize_2.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/823973162206494720/ezgif.com-gif-maker.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/823973168066068531/ezgif.com-gif-maker_1.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/823973173220868096/ezgif.com-optimize.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/823973178237911040/ezgif.com-optimize_1.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/823973183529943070/ezgif.com-optimize_3.gif',
                               'https://cdn.discordapp.com/attachments/819857033489940481/823973189380997140/tumblr_nqr0l0sLdH1t86fsoo1_540.gif']
                    img = random.choice(choices)
                    embed = discord.Embed(title=missionary, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)

    @missionary.error
    async def missionary_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()

    @commands.command(aliases=["public sex"])
    @commands.is_nsfw()
    async def public(self, ctx, message=None):
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author = ctx.author.name
        author_gender = determineGender(ctx.author)
        if mentions == message:
            if message == None:
                if author_gender == 'female':
                    public = f"{author} plays with herself outside"
                    choices = ["https://cdn.discordapp.com/attachments/819857033489940481/824351119492907058/ezgif.com-optimize_9.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824351119715205170/ezgif.com-optimize_8.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824351124777205810/ezgif.com-optimize_12.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824351129869484102/ezgif.com-optimize_6.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824351133497294870/ezgif.com-optimize_11.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824351138794438687/ezgif.com-optimize_5.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824351141852086332/ezgif.com-optimize_7.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824351147107811352/ezgif.com-optimize_3.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824351149431455744/ezgif.com-optimize_1.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824351152547954708/ezgif.com-optimize.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824351275994316810/ezgif.com-optimize_14.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(
                        title=public,
                        colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    public = f"{author} plays with himself outside"
                    choices = ["https://cdn.discordapp.com/attachments/819857033489940481/824369866520657920/ezgif.com-optimize_3.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824369872074047498/ezgif.com-optimize_1.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824369878533931018/ezgif.com-optimize_2.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824369883784675338/ezgif.com-optimize_4.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824369889874935858/ezgif.com-optimize_6.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824369890026061865/ezgif.com-gif-maker.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824369892529799248/ezgif.com-optimize.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824369894535200788/ezgif.com-optimize_5.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824369900910805012/ezgif.com-gif-maker_1.gif"
                               ]
                    img = random.choice(choices)
                    embed = discord.Embed(title=public, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
            else:
                if author_gender == 'male':
                    petplay = f"{author} publicly plays with  {mentions}"
                    choices = [
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367696204005396/ezgif.com-optimize_9.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367701165342790/ezgif.com-gif-maker_1.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367707276705843/ezgif.com-resize.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367713169571870/ezgif.com-gif-maker.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367716331683880/ezgif.com-optimize_6.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367720283111444/ezgif.com-optimize_4.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367724422627388/ezgif.com-optimize_2.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367730613813289/ezgif.com-optimize_8.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367734208200724/ezgif.com-optimize_7.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367739208204288/ezgif.com-optimize_1.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367747399548978/ezgif.com-optimize_10.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    petplay = f"{author} publicly plays with  {mentions}"
                    choices = [
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367696204005396/ezgif.com-optimize_9.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367701165342790/ezgif.com-gif-maker_1.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367707276705843/ezgif.com-resize.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367713169571870/ezgif.com-gif-maker.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367716331683880/ezgif.com-optimize_6.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367720283111444/ezgif.com-optimize_4.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367724422627388/ezgif.com-optimize_2.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367730613813289/ezgif.com-optimize_8.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367734208200724/ezgif.com-optimize_7.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367739208204288/ezgif.com-optimize_1.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367747399548978/ezgif.com-optimize_10.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
        else:
            mention_gender = determineGender(ctx.message.mentions[0])
            if author_gender == 'male':
                if mention_gender == 'female':
                    petplay = f"{author} publicly plays with  {mentions.name}"
                    choices = [
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367696204005396/ezgif.com-optimize_9.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367701165342790/ezgif.com-gif-maker_1.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367707276705843/ezgif.com-resize.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367713169571870/ezgif.com-gif-maker.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367716331683880/ezgif.com-optimize_6.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367720283111444/ezgif.com-optimize_4.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367724422627388/ezgif.com-optimize_2.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367730613813289/ezgif.com-optimize_8.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367734208200724/ezgif.com-optimize_7.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367739208204288/ezgif.com-optimize_1.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824367747399548978/ezgif.com-optimize_10.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    petplay = f"{author} publicly plays with  {mentions.name}"
                    choices = ["https://cdn.discordapp.com/attachments/819857033489940481/824371801316524112/ezgif.com-optimize_2.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824371808932593705/ezgif.com-optimize_3.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824371814393184276/ezgif.com-optimize.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824371818281828362/ezgif.com-gif-maker_4.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824371821595066368/ezgif.com-optimize_1.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824371824212705300/ezgif.com-gif-maker_2.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824371827572473916/ezgif.com-gif-maker_1.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824371833892634663/ezgif.com-gif-maker.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824371834811318282/ezgif.com-gif-maker_3.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
            elif author_gender == 'female':
                if mention_gender == 'male':
                    petplay = f"{author} publicly plays with  {mentions.name}"
                    choices = ["https://cdn.discordapp.com/attachments/819857033489940481/824367696204005396/ezgif.com-optimize_9.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824367701165342790/ezgif.com-gif-maker_1.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824367707276705843/ezgif.com-resize.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824367713169571870/ezgif.com-gif-maker.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824367716331683880/ezgif.com-optimize_6.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824367720283111444/ezgif.com-optimize_4.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824367724422627388/ezgif.com-optimize_2.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824367730613813289/ezgif.com-optimize_8.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824367734208200724/ezgif.com-optimize_7.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824367739208204288/ezgif.com-optimize_1.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824367747399548978/ezgif.com-optimize_10.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    petplay = f"{author} publicly plays with {mentions.name}"
                    choices = ["https://cdn.discordapp.com/attachments/819857033489940481/824356246261727262/ezgif.com-optimize_6.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824356250580942878/ezgif.com-optimize_7.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824356256147177522/ezgif.com-optimize_3.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824356261586927666/ezgif.com-gif-maker.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824356266708172810/ezgif.com-optimize.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824356272182001754/ezgif.com-optimize_2.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824356276090699836/ezgif.com-optimize_1.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824356284853125130/ezgif.com-optimize_5.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824356287461851166/ezgif.com-optimize_8.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)

    @public.error
    async def public_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()

    @commands.command()
    @commands.is_nsfw()
    async def petplay(self, ctx, message=None):
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author = ctx.author.name
        author_gender = determineGender(ctx.author)
        if mentions == message:
            if message == None:
                embed = discord.Embed(
                    description=f"**You can't petplay with nothing you horni dumbo\nExample use: $petplay @User#6969**",
                    colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                if author_gender == 'male':
                    petplay = f"{author} petplays with {mentions}"
                    choices = [
                        "https://cdn.discordapp.com/attachments/819857033489940481/824384698423312484/ezgif.com-optimize_3.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824384702638850158/ezgif.com-gif-maker_2.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824384709659721758/ezgif.com-gif-maker_1.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824384715002740786/ezgif.com-gif-maker_4.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824384723601588264/ezgif.com-optimize_2.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824384728513249340/ezgif.com-gif-maker_3.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824384733419929680/ezgif.com-optimize_1.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824384738978431006/ezgif.com-gif-maker.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824384748155568138/ezgif.com-optimize_4.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392643860758578/ezgif.com-optimize_4.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392649472606241/ezgif.com-optimize_3.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392654317158450/ezgif.com-gif-maker.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392659610107995/ezgif.com-optimize_5.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392666325319690/ezgif.com-gif-maker_1.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392672763576360/ezgif.com-optimize_7.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392677838946324/ezgif.com-optimize_1.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392687276916746/ezgif.com-optimize.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392688773103646/ezgif.com-optimize_2.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392692791509002/ezgif.com-optimize_6.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392701038428211/ezgif.com-optimize_8.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825323973780832296/ezgif.com-optimize_14.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825323980403245106/ezgif.com-optimize_4.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825323984459530240/ezgif.com-optimize_11.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825323989312208916/ezgif.com-optimize_21.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825323994135396392/ezgif.com-optimize_10.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324001181302834/ezgif.com-gif-maker_1.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324005408899092/ezgif.com-optimize_19.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324009721167912/ezgif.com-gif-maker.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324015370633227/ezgif.com-optimize_22.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324020760969226/ezgif.com-optimize.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324025400131614/ezgif.com-optimize_20.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324029682384906/ezgif.com-optimize_13.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324108153094154/ezgif.com-optimize_3.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324113165942784/ezgif.com-resize.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324118169747496/ezgif.com-optimize_5.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324122560397392/ezgif.com-resize_1.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324127375458334/ezgif.com-optimize_16.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324131049406475/ezgif.com-optimize_2.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324135416201226/ezgif.com-optimize_7.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324139505516544/ezgif.com-optimize_9.gif"
                        ]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    petplay = f"{author} petplays with {mentions}"
                    choices = [
                        "https://cdn.discordapp.com/attachments/819857033489940481/824384698423312484/ezgif.com-optimize_3.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824384702638850158/ezgif.com-gif-maker_2.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824384709659721758/ezgif.com-gif-maker_1.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824384715002740786/ezgif.com-gif-maker_4.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824384723601588264/ezgif.com-optimize_2.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824384728513249340/ezgif.com-gif-maker_3.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824384733419929680/ezgif.com-optimize_1.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824384738978431006/ezgif.com-gif-maker.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824384748155568138/ezgif.com-optimize_4.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392643860758578/ezgif.com-optimize_4.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392649472606241/ezgif.com-optimize_3.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392654317158450/ezgif.com-gif-maker.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392659610107995/ezgif.com-optimize_5.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392666325319690/ezgif.com-gif-maker_1.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392672763576360/ezgif.com-optimize_7.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392677838946324/ezgif.com-optimize_1.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392687276916746/ezgif.com-optimize.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392688773103646/ezgif.com-optimize_2.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392692791509002/ezgif.com-optimize_6.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392701038428211/ezgif.com-optimize_8.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825323973780832296/ezgif.com-optimize_14.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825323980403245106/ezgif.com-optimize_4.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825323984459530240/ezgif.com-optimize_11.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825323989312208916/ezgif.com-optimize_21.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825323994135396392/ezgif.com-optimize_10.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324001181302834/ezgif.com-gif-maker_1.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324005408899092/ezgif.com-optimize_19.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324009721167912/ezgif.com-gif-maker.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324015370633227/ezgif.com-optimize_22.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324020760969226/ezgif.com-optimize.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324025400131614/ezgif.com-optimize_20.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324029682384906/ezgif.com-optimize_13.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324108153094154/ezgif.com-optimize_3.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324113165942784/ezgif.com-resize.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324118169747496/ezgif.com-optimize_5.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324122560397392/ezgif.com-resize_1.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324127375458334/ezgif.com-optimize_16.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324131049406475/ezgif.com-optimize_2.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324135416201226/ezgif.com-optimize_7.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324139505516544/ezgif.com-optimize_9.gif"
                        ]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
        else:
            mention_gender = determineGender(ctx.message.mentions[0])
            if author_gender == 'male':
                if mention_gender == 'female':
                    petplay = f"{author} petplays with {mentions.name}"
                    choices = [
                        "https://cdn.discordapp.com/attachments/819857033489940481/824384698423312484/ezgif.com-optimize_3.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824384702638850158/ezgif.com-gif-maker_2.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824384709659721758/ezgif.com-gif-maker_1.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824384715002740786/ezgif.com-gif-maker_4.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824384723601588264/ezgif.com-optimize_2.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824384728513249340/ezgif.com-gif-maker_3.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824384733419929680/ezgif.com-optimize_1.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824384738978431006/ezgif.com-gif-maker.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824384748155568138/ezgif.com-optimize_4.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392643860758578/ezgif.com-optimize_4.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392649472606241/ezgif.com-optimize_3.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392654317158450/ezgif.com-gif-maker.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392659610107995/ezgif.com-optimize_5.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392666325319690/ezgif.com-gif-maker_1.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392672763576360/ezgif.com-optimize_7.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392677838946324/ezgif.com-optimize_1.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392687276916746/ezgif.com-optimize.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392688773103646/ezgif.com-optimize_2.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392692791509002/ezgif.com-optimize_6.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/824392701038428211/ezgif.com-optimize_8.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825323973780832296/ezgif.com-optimize_14.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825323980403245106/ezgif.com-optimize_4.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825323984459530240/ezgif.com-optimize_11.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825323989312208916/ezgif.com-optimize_21.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825323994135396392/ezgif.com-optimize_10.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324001181302834/ezgif.com-gif-maker_1.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324005408899092/ezgif.com-optimize_19.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324009721167912/ezgif.com-gif-maker.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324015370633227/ezgif.com-optimize_22.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324020760969226/ezgif.com-optimize.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324025400131614/ezgif.com-optimize_20.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324029682384906/ezgif.com-optimize_13.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324108153094154/ezgif.com-optimize_3.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324113165942784/ezgif.com-resize.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324118169747496/ezgif.com-optimize_5.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324122560397392/ezgif.com-resize_1.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324127375458334/ezgif.com-optimize_16.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324131049406475/ezgif.com-optimize_2.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324135416201226/ezgif.com-optimize_7.gif",
                        "https://cdn.discordapp.com/attachments/819857033489940481/825324139505516544/ezgif.com-optimize_9.gif"
                        ]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    petplay = f"{author} petplays with {mentions.name}"
                    choices = []
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
            elif author_gender == 'female':
                if mention_gender == 'male':
                    petplay = f"{author} petplays with {mentions.name}"
                    choices = ["https://cdn.discordapp.com/attachments/819857033489940481/824384698423312484/ezgif.com-optimize_3.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824384702638850158/ezgif.com-gif-maker_2.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824384709659721758/ezgif.com-gif-maker_1.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824384715002740786/ezgif.com-gif-maker_4.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824384723601588264/ezgif.com-optimize_2.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824384728513249340/ezgif.com-gif-maker_3.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824384733419929680/ezgif.com-optimize_1.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824384738978431006/ezgif.com-gif-maker.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824384748155568138/ezgif.com-optimize_4.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824392643860758578/ezgif.com-optimize_4.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824392649472606241/ezgif.com-optimize_3.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824392654317158450/ezgif.com-gif-maker.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824392659610107995/ezgif.com-optimize_5.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824392666325319690/ezgif.com-gif-maker_1.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824392672763576360/ezgif.com-optimize_7.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824392677838946324/ezgif.com-optimize_1.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824392687276916746/ezgif.com-optimize.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824392688773103646/ezgif.com-optimize_2.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824392692791509002/ezgif.com-optimize_6.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824392701038428211/ezgif.com-optimize_8.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825323973780832296/ezgif.com-optimize_14.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825323980403245106/ezgif.com-optimize_4.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825323984459530240/ezgif.com-optimize_11.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825323989312208916/ezgif.com-optimize_21.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825323994135396392/ezgif.com-optimize_10.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825324001181302834/ezgif.com-gif-maker_1.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825324005408899092/ezgif.com-optimize_19.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825324009721167912/ezgif.com-gif-maker.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825324015370633227/ezgif.com-optimize_22.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825324020760969226/ezgif.com-optimize.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825324025400131614/ezgif.com-optimize_20.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825324029682384906/ezgif.com-optimize_13.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825324108153094154/ezgif.com-optimize_3.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825324113165942784/ezgif.com-resize.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825324118169747496/ezgif.com-optimize_5.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825324122560397392/ezgif.com-resize_1.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825324127375458334/ezgif.com-optimize_16.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825324131049406475/ezgif.com-optimize_2.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825324135416201226/ezgif.com-optimize_7.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/825324139505516544/ezgif.com-optimize_9.gif"
                               ]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    petplay = f"{author} petplays with {mentions.name}"
                    choices = ["https://cdn.discordapp.com/attachments/819857033489940481/824384698423312484/ezgif.com-optimize_3.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824384702638850158/ezgif.com-gif-maker_2.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824384709659721758/ezgif.com-gif-maker_1.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824384715002740786/ezgif.com-gif-maker_4.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824384723601588264/ezgif.com-optimize_2.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824384728513249340/ezgif.com-gif-maker_3.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824384733419929680/ezgif.com-optimize_1.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824384738978431006/ezgif.com-gif-maker.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824384748155568138/ezgif.com-optimize_4.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824385441225506816/ezgif.com-optimize.gif",
                               "https://cdn.discordapp.com/attachments/819857033489940481/824385447345389658/ezgif.com-optimize_1.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)

    @petplay.error
    async def petplay_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()

    @commands.command()
    @commands.is_nsfw()
    async def whip(self, ctx, message=None):
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author = ctx.author.name
        author_gender = determineGender(ctx.author)
        if mentions == message:
            if message == None:
                embed = discord.Embed(
                    title=f"You can't whip nothing you horni dumbo\nExample use: $whip @User#6969",
                    colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                if author_gender == 'male':
                    whip = f"{author} whips {mentions}"
                    choices = ["https://cdn.discordapp.com/attachments/819857033489940481/826126564898766889/ezgif.com-gif-maker.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126571159945226/ezgif.com-optimize_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126579188760576/ezgif.com-optimize_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126583541661756/ezgif.com-optimize_3.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126587748941824/ezgif.com-optimize_4.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126593298661396/ezgif.com-optimize_5.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126599358644234/ezgif.com-optimize_6.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126603863064592/ezgif.com-optimize_7.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126610554028052/ezgif.com-optimize_8.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126615389667328/ezgif.com-optimize_9.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126618883784724/ezgif.com-optimize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126623061442570/ezgif.com-resize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126728942321714/tumblr_ot7jfhZNvK1vfnyqvo1_500.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=whip, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    whip = f"{author} whips {mentions}"
                    choices = ["https://cdn.discordapp.com/attachments/819857033489940481/826124371323387985/ezgif.com-optimize_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119997687332864/tenor_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120000841449513/tenor_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120003371270224/giphy.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120006814793748/tenor.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120011215142962/giphy_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120707209560064/ezgif.com-optimize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124375907762176/ezgif.com-optimize_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124380391079966/ezgif.com-optimize_3.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124386247114752/ezgif.com-optimize_4.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124391133085728/ezgif.com-optimize_5.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124396107923456/ezgif.com-optimize_6.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124401287233566/ezgif.com-optimize_7.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124403402211389/ezgif.com-optimize_8.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124409408192632/ezgif.com-optimize_9.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124414185766912/ezgif.com-optimize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124420291493888/ezgif.com-resize.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=whip, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
        else:
            mention_gender = determineGender(ctx.message.mentions[0])
            if author_gender == 'male':
                if mention_gender == 'female':
                    whip = f"{author} whips {mentions.name}"
                    choices = ["https://cdn.discordapp.com/attachments/819857033489940481/826126564898766889/ezgif.com-gif-maker.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126571159945226/ezgif.com-optimize_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126579188760576/ezgif.com-optimize_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126583541661756/ezgif.com-optimize_3.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126587748941824/ezgif.com-optimize_4.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126593298661396/ezgif.com-optimize_5.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126599358644234/ezgif.com-optimize_6.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126603863064592/ezgif.com-optimize_7.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126610554028052/ezgif.com-optimize_8.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126615389667328/ezgif.com-optimize_9.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126618883784724/ezgif.com-optimize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126623061442570/ezgif.com-resize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126728942321714/tumblr_ot7jfhZNvK1vfnyqvo1_500.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=whip, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    whip = f"{author} whips {mentions.name}"
                    choices = ["https://cdn.discordapp.com/attachments/819857033489940481/826124587283775548/tenor_3.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=whip, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
            elif author_gender == 'female':
                if mention_gender == 'male':
                    whip = f"{author} whips {mentions.name}"
                    choices = ["https://cdn.discordapp.com/attachments/819857033489940481/826124371323387985/ezgif.com-optimize_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119997687332864/tenor_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120000841449513/tenor_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120003371270224/giphy.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120006814793748/tenor.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120011215142962/giphy_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120707209560064/ezgif.com-optimize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124375907762176/ezgif.com-optimize_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124380391079966/ezgif.com-optimize_3.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124386247114752/ezgif.com-optimize_4.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124391133085728/ezgif.com-optimize_5.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124396107923456/ezgif.com-optimize_6.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124401287233566/ezgif.com-optimize_7.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124403402211389/ezgif.com-optimize_8.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124409408192632/ezgif.com-optimize_9.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124414185766912/ezgif.com-optimize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124420291493888/ezgif.com-resize.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=whip, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    whip = f"{author} whips {mentions.name}"
                    choices = ["https://cdn.discordapp.com/attachments/819857033489940481/826119788077383750/ezgif.com-gif-maker_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119793068867624/ezgif.com-gif-maker_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119799725097050/ezgif.com-gif-maker.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119801700089856/ezgif.com-optimize_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119804528230420/ezgif.com-optimize_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119811770613841/ezgif.com-optimize_3.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119815608664094/ezgif.com-optimize_4.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119819823808512/ezgif.com-optimize_5.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119824844652554/ezgif.com-optimize_6.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119832441192448/ezgif.com-optimize_7.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119832839389264/ezgif.com-optimize_8.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119838963466280/ezgif.com-optimize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119997687332864/tenor_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120000841449513/tenor_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120003371270224/giphy.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120006814793748/tenor.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120011215142962/giphy_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120707209560064/ezgif.com-optimize.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=whip, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)

    @whip.error
    async def whip_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()

    @commands.command()
    @commands.is_nsfw()
    async def AraAra(self, ctx):
        subreddit = await reddit.subreddit("AraAra", fetch=True)

        all_subs = []
        async for submission in subreddit.hot(limit=50):
            all_subs.append(submission)

        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        em = discord.Embed(title=name, colour=discord.Colour.blue())
        em.set_image(url=url)

        await ctx.send(embed=em)

    @AraAra.error
    async def AraAra_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()

    @commands.command()
    @commands.is_nsfw()
    async def punish(self, ctx, message=None):
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author = ctx.author.name
        author_gender = determineGender(ctx.author)
        if mentions == message:
            if message == None:
                embed = discord.Embed(
                    title=f"You can't punish nothing you horni dumbo\nExample use: $punish @User#6969",
                    colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                if author_gender == "male":
                    punish = f"{author} punishes {mentions}"
                    choices = ["https://cdn.discordapp.com/attachments/819857033489940481/826126564898766889/ezgif.com-gif-maker.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126571159945226/ezgif.com-optimize_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126579188760576/ezgif.com-optimize_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126583541661756/ezgif.com-optimize_3.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126587748941824/ezgif.com-optimize_4.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126593298661396/ezgif.com-optimize_5.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126599358644234/ezgif.com-optimize_6.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126603863064592/ezgif.com-optimize_7.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126610554028052/ezgif.com-optimize_8.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126615389667328/ezgif.com-optimize_9.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126618883784724/ezgif.com-optimize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126623061442570/ezgif.com-resize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126728942321714/tumblr_ot7jfhZNvK1vfnyqvo1_500.gif",
                                'https://i.imgur.com/rLSCY75.gif',
                                'https://i.imgur.com/pTtxvfK.gif',
                                'https://i.imgur.com/sHZFIgH.gif',
                                'https://i.imgur.com/jNTHiJs.gif',
                                'https://i.imgur.com/drzE8fi.gif',
                                'https://i.imgur.com/NbXKhlI.gif',
                                'https://i.imgur.com/ijPhdcp.gif',
                                'https://i.imgur.com/Ukck5NT.gif',
                                'https://i.imgur.com/wSfmq1k.gif',
                                'https://i.imgur.com/fQfIAFw.gif',
                                'https://i.imgur.com/Xgvjcea.gif',
                                "https://cdn.discordapp.com/attachments/819857033489940481/826902932292370462/ezgif.com-optimize_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826902934360031232/ezgif.com-optimize_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826902936205525002/ezgif.com-optimize_3.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826902951079051305/ezgif.com-optimize_6.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826902960088023050/ezgif.com-optimize_8.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826902961614487582/ezgif.com-optimize.gif",
                                'https://i.imgur.com/vZO2Y0e.gif',
                                'https://i.imgur.com/LvIz1GP.gif',
                                'https://i.imgur.com/VcYTQ27.gif',
                                'https://i.imgur.com/tpiXCZI.gif',
                                'https://i.imgur.com/3AA1nw9.gif',
                                'https://i.imgur.com/sYXmhWU.gif',
                                'https://i.imgur.com/JWV3vDy.gif',
                                'https://i.imgur.com/NvCICor.gif',
                                'https://i.imgur.com/u0uZi4v.gif',
                                'https://i.imgur.com/SvhpPhu.gif',
                                'https://i.imgur.com/CWEA3AK.gif',
                                'https://i.imgur.com/c3GfhnC.gif',
                                'https://i.imgur.com/ntEjUr7.gif',
                                'https://i.imgur.com/hoeN0Nz.gif',
                                'https://i.imgur.com/EQyDnKn.gif',
                                'https://i.imgur.com/cZS3P04.gif',
                                'https://i.imgur.com/GVQ7Ydf.gif',
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348334381301760/ezgif.com-gif-maker_5.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348342300672020/ezgif.com-gif-maker_4.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348348831334420/ezgif.com-gif-maker_6.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348354082209802/ezgif.com-optimize_5.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348358612189194/ezgif.com-optimize_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348363842879498/ezgif.com-optimize_6.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348368934895646/ezgif.com-optimize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348373049507880/ezgif.com-optimize_3.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348376974589972/ezgif.com-optimize_4.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348382426923018/ezgif.com-optimize_7.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348385594802206/ezgif.com-resize_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348386848374792/ezgif.com-optimize_8.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348388748132392/ezgif.com-gif-maker_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348394096656435/ezgif.com-optimize_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348394637590558/ezgif.com-gif-maker.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348395271061534/ezgif.com-gif-maker_3.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348397304643594/ezgif.com-gif-maker_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348621582729256/ezgif.com-optimize_9.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825357946883670046/ezgif.com-gif-maker_4.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825357956702404629/ezgif.com-optimize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825357962238754866/ezgif.com-optimize_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825357967905914932/ezgif.com-gif-maker_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825357973097676810/ezgif.com-gif-maker.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825357979162902609/ezgif.com-gif-maker_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825357982716002324/ezgif.com-optimize_6.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825357989917360148/ezgif.com-resize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825357996099633162/ezgif.com-optimize_9.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825358000608116746/ezgif.com-optimize_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825358003074760734/ezgif.com-optimize_3.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825358009369624656/ezgif.com-resize_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826919562128654366/ezgif.com-optimize_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826919567779430470/ezgif.com-optimize_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826919573830893664/ezgif.com-optimize_4.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826919585827258408/ezgif.com-optimize_10.gif"
                                ]
                    img = random.choice(choices)
                    embed = discord.Embed(title=punish, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    punish = f"{author} punishes {mentions}"
                    choices = ["https://cdn.discordapp.com/attachments/819857033489940481/826124371323387985/ezgif.com-optimize_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119997687332864/tenor_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120000841449513/tenor_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120003371270224/giphy.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120006814793748/tenor.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120011215142962/giphy_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120707209560064/ezgif.com-optimize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124375907762176/ezgif.com-optimize_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124380391079966/ezgif.com-optimize_3.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124386247114752/ezgif.com-optimize_4.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124391133085728/ezgif.com-optimize_5.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124396107923456/ezgif.com-optimize_6.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124401287233566/ezgif.com-optimize_7.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124403402211389/ezgif.com-optimize_8.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124409408192632/ezgif.com-optimize_9.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124414185766912/ezgif.com-optimize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124420291493888/ezgif.com-resize.gif",
                                'https://i.imgur.com/aQDmyuD.gif',
                                'https://i.imgur.com/kipMUyV.gif',
                                'https://i.imgur.com/orUMNpW.gif',
                                'https://i.imgur.com/u0T5FEL.gif',
                                'https://i.imgur.com/m2JuNas.gif',
                                'https://i.imgur.com/OfRey1k.gif',
                                'https://i.imgur.com/JL3cTFx.gif',
                                'https://i.imgur.com/4j98RSc.gif',
                                'https://i.imgur.com/rUM9i6E.gif',
                                'https://i.imgur.com/88aDUTL.gif',
                                'https://i.imgur.com/mZLtYRR.gif',
                                'https://i.imgur.com/QOejpgx.gif',
                                "https://cdn.discordapp.com/attachments/819857033489940481/826907904489422878/ezgif.com-gif-maker_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826907908091805736/ezgif.com-gif-maker.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826907913960030315/ezgif.com-optimize_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826907921866031155/ezgif.com-optimize_5.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826907938996224040/ezgif.com-optimize_9.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826907947744362526/ezgif.com-resize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826907947728371752/ezgif.com-optimize_10.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826909059898277888/ezgif.com-resize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826919592721907772/ezgif.com-optimize.gif"
                                
                                ]
                    img = random.choice(choices)
                    embed = discord.Embed(title=punish, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
        else:
            mention_gender = determineGender(ctx.message.mentions[0])
            if author_gender == "male":
                if mention_gender == "female":
                    punish = f"{author} punishes {mentions.name}"
                    choices = ["https://cdn.discordapp.com/attachments/819857033489940481/826126564898766889/ezgif.com-gif-maker.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126571159945226/ezgif.com-optimize_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126579188760576/ezgif.com-optimize_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126583541661756/ezgif.com-optimize_3.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126587748941824/ezgif.com-optimize_4.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126593298661396/ezgif.com-optimize_5.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126599358644234/ezgif.com-optimize_6.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126603863064592/ezgif.com-optimize_7.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126610554028052/ezgif.com-optimize_8.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126615389667328/ezgif.com-optimize_9.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126618883784724/ezgif.com-optimize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126623061442570/ezgif.com-resize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826126728942321714/tumblr_ot7jfhZNvK1vfnyqvo1_500.gif",
                                'https://i.imgur.com/rLSCY75.gif',
                                'https://i.imgur.com/pTtxvfK.gif',
                                'https://i.imgur.com/sHZFIgH.gif',
                                'https://i.imgur.com/jNTHiJs.gif',
                                'https://i.imgur.com/drzE8fi.gif',
                                'https://i.imgur.com/NbXKhlI.gif',
                                'https://i.imgur.com/ijPhdcp.gif',
                                'https://i.imgur.com/Ukck5NT.gif',
                                'https://i.imgur.com/wSfmq1k.gif',
                                'https://i.imgur.com/fQfIAFw.gif',
                                'https://i.imgur.com/Xgvjcea.gif',
                                "https://cdn.discordapp.com/attachments/819857033489940481/826902932292370462/ezgif.com-optimize_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826902934360031232/ezgif.com-optimize_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826902936205525002/ezgif.com-optimize_3.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826902951079051305/ezgif.com-optimize_6.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826902960088023050/ezgif.com-optimize_8.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826902961614487582/ezgif.com-optimize.gif",
                                'https://i.imgur.com/vZO2Y0e.gif',
                                'https://i.imgur.com/LvIz1GP.gif',
                                'https://i.imgur.com/VcYTQ27.gif',
                                'https://i.imgur.com/tpiXCZI.gif',
                                'https://i.imgur.com/3AA1nw9.gif',
                                'https://i.imgur.com/sYXmhWU.gif',
                                'https://i.imgur.com/JWV3vDy.gif',
                                'https://i.imgur.com/NvCICor.gif',
                                'https://i.imgur.com/u0uZi4v.gif',
                                'https://i.imgur.com/SvhpPhu.gif',
                                'https://i.imgur.com/CWEA3AK.gif',
                                'https://i.imgur.com/c3GfhnC.gif',
                                'https://i.imgur.com/ntEjUr7.gif',
                                'https://i.imgur.com/hoeN0Nz.gif',
                                'https://i.imgur.com/EQyDnKn.gif',
                                'https://i.imgur.com/cZS3P04.gif',
                                'https://i.imgur.com/GVQ7Ydf.gif',
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348334381301760/ezgif.com-gif-maker_5.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348342300672020/ezgif.com-gif-maker_4.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348348831334420/ezgif.com-gif-maker_6.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348354082209802/ezgif.com-optimize_5.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348358612189194/ezgif.com-optimize_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348363842879498/ezgif.com-optimize_6.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348368934895646/ezgif.com-optimize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348373049507880/ezgif.com-optimize_3.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348376974589972/ezgif.com-optimize_4.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348382426923018/ezgif.com-optimize_7.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348385594802206/ezgif.com-resize_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348386848374792/ezgif.com-optimize_8.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348388748132392/ezgif.com-gif-maker_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348394096656435/ezgif.com-optimize_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348394637590558/ezgif.com-gif-maker.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348395271061534/ezgif.com-gif-maker_3.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348397304643594/ezgif.com-gif-maker_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825348621582729256/ezgif.com-optimize_9.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825357946883670046/ezgif.com-gif-maker_4.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825357956702404629/ezgif.com-optimize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825357962238754866/ezgif.com-optimize_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825357967905914932/ezgif.com-gif-maker_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825357973097676810/ezgif.com-gif-maker.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825357979162902609/ezgif.com-gif-maker_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825357982716002324/ezgif.com-optimize_6.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825357989917360148/ezgif.com-resize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825357996099633162/ezgif.com-optimize_9.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825358000608116746/ezgif.com-optimize_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825358003074760734/ezgif.com-optimize_3.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825358009369624656/ezgif.com-resize_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826919562128654366/ezgif.com-optimize_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826919567779430470/ezgif.com-optimize_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826919573830893664/ezgif.com-optimize_4.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826919585827258408/ezgif.com-optimize_10.gif"
                                ]
                    img = random.choice(choices)
                    embed = discord.Embed(title=punish, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    punish = f"{author} punishes {mentions.name}"
                    choices = ["https://cdn.discordapp.com/attachments/819857033489940481/826920029470588948/ezgif.com-optimize.gif",
                                'https://i.imgur.com/VFNDRBy.gif',
                                'https://i.imgur.com/OYPnfiG.gif',
                                'https://i.imgur.com/PMbIso6.gif',
                                'https://i.imgur.com/76WonL8.gif',
                                'https://i.imgur.com/OOTp5n8.gif',
                                'https://i.imgur.com/zqQs5c7.gif',
                                'https://i.imgur.com/FiamEyG.gif',
                                'https://i.imgur.com/lK2eNHC.gif',
                                'https://i.imgur.com/bnDgk3P.gif',
                                'https://i.imgur.com/bGGkNS2.gif']
                    img = random.choice(choices)
                    embed = discord.Embed(title=punish, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
            elif author_gender == "female":
                if mention_gender == "male":
                    punish = f"{author} punishes {mentions.name}"
                    choices = ["https://cdn.discordapp.com/attachments/819857033489940481/826124371323387985/ezgif.com-optimize_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119997687332864/tenor_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120000841449513/tenor_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120003371270224/giphy.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120006814793748/tenor.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120011215142962/giphy_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120707209560064/ezgif.com-optimize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124375907762176/ezgif.com-optimize_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124380391079966/ezgif.com-optimize_3.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124386247114752/ezgif.com-optimize_4.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124391133085728/ezgif.com-optimize_5.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124396107923456/ezgif.com-optimize_6.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124401287233566/ezgif.com-optimize_7.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124403402211389/ezgif.com-optimize_8.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124409408192632/ezgif.com-optimize_9.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124414185766912/ezgif.com-optimize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826124420291493888/ezgif.com-resize.gif",
                                'https://i.imgur.com/aQDmyuD.gif',
                                'https://i.imgur.com/kipMUyV.gif',
                                'https://i.imgur.com/orUMNpW.gif',
                                'https://i.imgur.com/u0T5FEL.gif',
                                'https://i.imgur.com/m2JuNas.gif',
                                'https://i.imgur.com/OfRey1k.gif',
                                'https://i.imgur.com/JL3cTFx.gif',
                                'https://i.imgur.com/4j98RSc.gif',
                                'https://i.imgur.com/rUM9i6E.gif',
                                'https://i.imgur.com/88aDUTL.gif',
                                'https://i.imgur.com/mZLtYRR.gif',
                                'https://i.imgur.com/QOejpgx.gif',
                                "https://cdn.discordapp.com/attachments/819857033489940481/826907904489422878/ezgif.com-gif-maker_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826907908091805736/ezgif.com-gif-maker.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826907913960030315/ezgif.com-optimize_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826907921866031155/ezgif.com-optimize_5.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826907938996224040/ezgif.com-optimize_9.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826907947744362526/ezgif.com-resize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826907947728371752/ezgif.com-optimize_10.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826909059898277888/ezgif.com-resize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826919592721907772/ezgif.com-optimize.gif"
                                
                                ]
                    img = random.choice(choices)
                    embed = discord.Embed(title=punish, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    punish = f"{author} punishes {mentions.name}"
                    choices = ["https://cdn.discordapp.com/attachments/819857033489940481/826902932292370462/ezgif.com-optimize_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826902934360031232/ezgif.com-optimize_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826902936205525002/ezgif.com-optimize_3.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826902951079051305/ezgif.com-optimize_6.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826902960088023050/ezgif.com-optimize_8.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826902961614487582/ezgif.com-optimize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119788077383750/ezgif.com-gif-maker_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119793068867624/ezgif.com-gif-maker_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119799725097050/ezgif.com-gif-maker.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119801700089856/ezgif.com-optimize_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119804528230420/ezgif.com-optimize_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119811770613841/ezgif.com-optimize_3.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119815608664094/ezgif.com-optimize_4.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119819823808512/ezgif.com-optimize_5.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119824844652554/ezgif.com-optimize_6.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119832441192448/ezgif.com-optimize_7.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119832839389264/ezgif.com-optimize_8.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119838963466280/ezgif.com-optimize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826119997687332864/tenor_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120000841449513/tenor_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120003371270224/giphy.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120006814793748/tenor.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120011215142962/giphy_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/826120707209560064/ezgif.com-optimize.gif",
                                'https://i.imgur.com/jYXc3v5.gif',
                                'https://i.imgur.com/kUghQWX.gif',
                                'https://i.imgur.com/iXtEFR6.gif',
                                'https://i.imgur.com/rGcl1jw.gif',
                                'https://i.imgur.com/Hj1n6MF.gif',
                                'https://i.imgur.com/wdpaK77.gif',
                                'https://i.imgur.com/wFkl5f0.gif',
                                'https://i.imgur.com/qwjeb8x.gif',
                                'https://i.imgur.com/TlFBMAU.gif',
                                'https://i.imgur.com/H3OBHEl.gif',
                                'https://i.imgur.com/7iIsj8j.gif',
                                'https://i.imgur.com/UQm9bkS.gif',
                                'https://i.imgur.com/2FwvuWa.gif',
                                'https://i.imgur.com/0m8KsTa.gif',
                                'https://i.imgur.com/zYDRuwJ.gif',
                                'https://i.imgur.com/3pRD4Hr.gif',
                                "https://cdn.discordapp.com/attachments/819857033489940481/825342438163873792/ezgif.com-optimize_3.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825342443208572928/ezgif.com-optimize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825342449601347594/ezgif.com-gif-maker.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825342456312627210/ezgif.com-gif-maker_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825342463316852767/ezgif.com-optimize_4.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825342466562981888/ezgif.com-gif-maker_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825342470572605450/ezgif.com-optimize_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825342476059148308/ezgif.com-resize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825342476641894440/ezgif.com-optimize_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825342484367409182/ezgif.com-optimize_5.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825357946883670046/ezgif.com-gif-maker_4.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825357956702404629/ezgif.com-optimize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825357962238754866/ezgif.com-optimize_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825357967905914932/ezgif.com-gif-maker_1.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825357973097676810/ezgif.com-gif-maker.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825357979162902609/ezgif.com-gif-maker_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825357982716002324/ezgif.com-optimize_6.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825357989917360148/ezgif.com-resize.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825357996099633162/ezgif.com-optimize_9.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825358000608116746/ezgif.com-optimize_2.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825358003074760734/ezgif.com-optimize_3.gif",
                                "https://cdn.discordapp.com/attachments/819857033489940481/825358009369624656/ezgif.com-resize_1.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=punish, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)

    @punish.error
    async def punish_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()

    @commands.command()
    @commands.is_nsfw()
    async def swallow(self, ctx, message=None):
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author = ctx.author.name
        author_gender = determineGender(ctx.author)
        if mentions == message:
            if message == None:
                embed = discord.Embed(
                    description=f"**You can't swallow nothing you horni dumbo\nExample use: $swallow @User#6969**",
                    colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                if author_gender == 'male':
                    petplay = f"{author} gets swallowed by {mentions}"
                    choices = ["https://cdn.discordapp.com/attachments/798913238229188608/828959658920116274/ezgif.com-gif-maker_29.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959772429647922/ezgif.com-gif-maker_23.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959799424974848/ezgif.com-gif-maker_30.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959820400033822/ezgif.com-gif-maker_24.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959853787086848/ezgif.com-gif-maker_27.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959855917531177/ezgif.com-gif-maker_25.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959859713114132/ezgif.com-gif-maker_28.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959871184404530/ezgif.com-gif-maker_21.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959878503727104/ezgif.com-gif-maker_33.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959881956032532/ezgif.com-gif-maker_35.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959897428820058/ezgif.com-gif-maker_34.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959902697127936/ezgif.com-gif-maker_26.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959903338856478/ezgif.com-gif-maker_36.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959910716375050/ezgif.com-gif-maker_31.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959913182101534/ezgif.com-gif-maker_32.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828968762681327626/ezgif.com-gif-maker_48.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828968891971141642/ezgif.com-gif-maker_61.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969057574846504/ezgif.com-gif-maker_55.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969061366628352/ezgif.com-gif-maker_56.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969093364580412/ezgif.com-gif-maker_50.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969102751563786/ezgif.com-gif-maker_59.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969105256087562/ezgif.com-gif-maker_54.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969106907856916/ezgif.com-gif-maker_53.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969109877293096/ezgif.com-gif-maker_57.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969127267401768/ezgif.com-gif-maker_60.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969156246372382/ezgif.com-gif-maker_49.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969167070953533/ezgif.com-gif-maker_58.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969176017928213/ezgif.com-gif-maker_62.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969176449679360/ezgif.com-gif-maker_51.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969188843716638/ezgif.com-gif-maker_52.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    petplay = f"{author} swallows {mentions}"
                    choices = ["https://cdn.discordapp.com/attachments/798913238229188608/828959658920116274/ezgif.com-gif-maker_29.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959772429647922/ezgif.com-gif-maker_23.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959799424974848/ezgif.com-gif-maker_30.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959820400033822/ezgif.com-gif-maker_24.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959853787086848/ezgif.com-gif-maker_27.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959855917531177/ezgif.com-gif-maker_25.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959859713114132/ezgif.com-gif-maker_28.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959871184404530/ezgif.com-gif-maker_21.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959878503727104/ezgif.com-gif-maker_33.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959881956032532/ezgif.com-gif-maker_35.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959897428820058/ezgif.com-gif-maker_34.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959902697127936/ezgif.com-gif-maker_26.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959903338856478/ezgif.com-gif-maker_36.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959910716375050/ezgif.com-gif-maker_31.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959913182101534/ezgif.com-gif-maker_32.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828968762681327626/ezgif.com-gif-maker_48.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828968891971141642/ezgif.com-gif-maker_61.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969057574846504/ezgif.com-gif-maker_55.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969061366628352/ezgif.com-gif-maker_56.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969093364580412/ezgif.com-gif-maker_50.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969102751563786/ezgif.com-gif-maker_59.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969105256087562/ezgif.com-gif-maker_54.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969106907856916/ezgif.com-gif-maker_53.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969109877293096/ezgif.com-gif-maker_57.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969127267401768/ezgif.com-gif-maker_60.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969156246372382/ezgif.com-gif-maker_49.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969167070953533/ezgif.com-gif-maker_58.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969176017928213/ezgif.com-gif-maker_62.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969176449679360/ezgif.com-gif-maker_51.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969188843716638/ezgif.com-gif-maker_52.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
        else:
            mention_gender = determineGender(ctx.message.mentions[0])
            if author_gender == 'male':
                if mention_gender == 'female':
                    petplay = f"{author} gets swallowed by {mentions.name}"
                    choices = ["https://cdn.discordapp.com/attachments/798913238229188608/828959658920116274/ezgif.com-gif-maker_29.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959772429647922/ezgif.com-gif-maker_23.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959799424974848/ezgif.com-gif-maker_30.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959820400033822/ezgif.com-gif-maker_24.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959853787086848/ezgif.com-gif-maker_27.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959855917531177/ezgif.com-gif-maker_25.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959859713114132/ezgif.com-gif-maker_28.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959871184404530/ezgif.com-gif-maker_21.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959878503727104/ezgif.com-gif-maker_33.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959881956032532/ezgif.com-gif-maker_35.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959897428820058/ezgif.com-gif-maker_34.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959902697127936/ezgif.com-gif-maker_26.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959903338856478/ezgif.com-gif-maker_36.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959910716375050/ezgif.com-gif-maker_31.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959913182101534/ezgif.com-gif-maker_32.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828968762681327626/ezgif.com-gif-maker_48.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828968891971141642/ezgif.com-gif-maker_61.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969057574846504/ezgif.com-gif-maker_55.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969061366628352/ezgif.com-gif-maker_56.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969093364580412/ezgif.com-gif-maker_50.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969102751563786/ezgif.com-gif-maker_59.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969105256087562/ezgif.com-gif-maker_54.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969106907856916/ezgif.com-gif-maker_53.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969109877293096/ezgif.com-gif-maker_57.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969127267401768/ezgif.com-gif-maker_60.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969156246372382/ezgif.com-gif-maker_49.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969167070953533/ezgif.com-gif-maker_58.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969176017928213/ezgif.com-gif-maker_62.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969176449679360/ezgif.com-gif-maker_51.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969188843716638/ezgif.com-gif-maker_52.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    petplay = f"{author} gets swallowed by {mentions.name}"
                    choices = ["https://cdn.discordapp.com/attachments/798913238229188608/828961560365629480/ezgif.com-gif-maker_45.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828961592841732096/ezgif.com-gif-maker_43.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828961596747284540/ezgif.com-gif-maker_44.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828961614748450832/ezgif.com-gif-maker_47.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828961623628185636/ezgif.com-gif-maker_46.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
            elif author_gender == 'female':
                if mention_gender == 'male':
                    petplay = f"{author} swallows {mentions.name}"
                    choices = ["https://cdn.discordapp.com/attachments/798913238229188608/828959658920116274/ezgif.com-gif-maker_29.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959772429647922/ezgif.com-gif-maker_23.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959799424974848/ezgif.com-gif-maker_30.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959820400033822/ezgif.com-gif-maker_24.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959853787086848/ezgif.com-gif-maker_27.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959855917531177/ezgif.com-gif-maker_25.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959859713114132/ezgif.com-gif-maker_28.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959871184404530/ezgif.com-gif-maker_21.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959878503727104/ezgif.com-gif-maker_33.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959881956032532/ezgif.com-gif-maker_35.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959897428820058/ezgif.com-gif-maker_34.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959902697127936/ezgif.com-gif-maker_26.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959903338856478/ezgif.com-gif-maker_36.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959910716375050/ezgif.com-gif-maker_31.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959913182101534/ezgif.com-gif-maker_32.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828968762681327626/ezgif.com-gif-maker_48.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828968891971141642/ezgif.com-gif-maker_61.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969057574846504/ezgif.com-gif-maker_55.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969061366628352/ezgif.com-gif-maker_56.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969093364580412/ezgif.com-gif-maker_50.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969102751563786/ezgif.com-gif-maker_59.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969105256087562/ezgif.com-gif-maker_54.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969106907856916/ezgif.com-gif-maker_53.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969109877293096/ezgif.com-gif-maker_57.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969127267401768/ezgif.com-gif-maker_60.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969156246372382/ezgif.com-gif-maker_49.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969167070953533/ezgif.com-gif-maker_58.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969176017928213/ezgif.com-gif-maker_62.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969176449679360/ezgif.com-gif-maker_51.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828969188843716638/ezgif.com-gif-maker_52.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    petplay = f"{author} swallows {mentions.name}"
                    choices = ["https://cdn.discordapp.com/attachments/798913238229188608/828959631753478144/ezgif.com-gif-maker_42.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959763328401428/ezgif.com-gif-maker_41.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959782516817930/ezgif.com-gif-maker_38.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959807817383966/ezgif.com-gif-maker_39.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959854563426344/ezgif.com-gif-maker_20.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959889832935434/ezgif.com-gif-maker_40.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959892860829696/ezgif.com-gif-maker_37.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828959911899562004/ezgif.com-gif-maker_22.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)

    @swallow.error
    async def swallow_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete() 

    @commands.command()
    @commands.is_nsfw()
    async def masturbate(self, ctx, message=None):
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author = ctx.author.name
        author_gender = determineGender(ctx.author)
        if mentions == message:
            if message == None:
                if author_gender == 'male':
                    masturbate = f"{author} masturbates by himself"
                    choices = ["https://cdn.discordapp.com/attachments/798913238229188608/828992661801009162/ezgif.com-gif-maker_7.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828992680284389376/ezgif.com-gif-maker_1.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828992699680030760/ezgif.com-gif-maker_20.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828992753055957062/ezgif.com-gif-maker_8.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828992755891175504/ezgif.com-gif-maker.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828992782835908688/ezgif.com-gif-maker_13.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828992811524292608/ezgif.com-gif-maker_4.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828992812749160488/ezgif.com-gif-maker_17.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828992818542411856/ezgif.com-gif-maker_3.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828992838091407450/ezgif.com-gif-maker_11.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828992843519361035/ezgif.com-gif-maker_16.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828992849256251432/ezgif.com-gif-maker_5.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828992862213242900/ezgif.com-gif-maker_6.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828992887697178624/ezgif.com-gif-maker_21.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828992901375328286/ezgif.com-gif-maker_2.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828992907679367198/ezgif.com-gif-maker_12.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828992913555587152/ezgif.com-gif-maker_15.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828992917896429628/ezgif.com-gif-maker_18.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828992927392464966/ezgif.com-gif-maker_9.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828992927354191903/ezgif.com-gif-maker_10.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828992931288318002/ezgif.com-gif-maker_22.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=masturbate, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)

                else:
                    masturbate = f"{author} masturbates by herself"
                    choices = ["https://cdn.discordapp.com/attachments/798913238229188608/828989469520691240/ezgif.com-gif-maker_21.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828990080533790741/ezgif.com-gif-maker_26.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828990218345906246/ezgif.com-gif-maker_47.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828990328987582464/ezgif.com-gif-maker_30.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828990341591859230/ezgif.com-gif-maker_22.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828990344154316800/ezgif.com-gif-maker_24.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828990350067892234/ezgif.com-gif-maker_29.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828990351729623090/ezgif.com-gif-maker_38.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828990391427924010/ezgif.com-gif-maker_43.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828990412239667230/ezgif.com-gif-maker_32.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828990413531643914/ezgif.com-gif-maker_44.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828990421958656030/ezgif.com-gif-maker_20.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828990432464863252/ezgif.com-gif-maker_34.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828990453781102662/ezgif.com-gif-maker_27.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828990463477284884/ezgif.com-gif-maker_39.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828990466534932520/ezgif.com-gif-maker_42.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/828990653621993512/ezgif.com-gif-maker_25.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=masturbate, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)

            else:
                if author_gender == 'male':
                    petplay = f"{author} masturbates with {mentions}"
                    choices = ["https://cdn.discordapp.com/attachments/828979138160754738/828979374807580702/ezgif.com-gif-maker_50.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979376741810176/ezgif.com-gif-maker_49.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979554945073172/ezgif.com-gif-maker_25.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979555813031986/ezgif.com-gif-maker_22.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979578193444874/ezgif.com-gif-maker_48.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979586427125840/ezgif.com-gif-maker_41.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979800810323988/ezgif.com-gif-maker_40.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979818284187678/ezgif.com-gif-maker_35.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979824570662962/ezgif.com-gif-maker_33.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979838538874910/ezgif.com-gif-maker_47.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979872591511612/ezgif.com-gif-maker_23.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979872738836560/ezgif.com-gif-maker_27.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979872931512340/ezgif.com-gif-maker_20.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979883073732638/ezgif.com-gif-maker_32.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979890070093834/ezgif.com-gif-maker_36.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979924500742144/ezgif.com-gif-maker_21.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979935241961522/ezgif.com-gif-maker_29.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979963604631603/ezgif.com-gif-maker_42.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980011473829898/ezgif.com-gif-maker_38.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980013050757120/ezgif.com-gif-maker_45.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980045556613130/ezgif.com-gif-maker_52.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980049193467954/ezgif.com-gif-maker_34.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980082273681408/ezgif.com-gif-maker_31.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980121910116422/ezgif.com-gif-maker_46.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980125654843462/ezgif.com-gif-maker_24.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980130256257074/ezgif.com-gif-maker_43.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980135608713237/ezgif.com-gif-maker_44.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980164930830366/ezgif.com-gif-maker_28.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980169292120104/ezgif.com-gif-maker_37.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980183729700864/ezgif.com-gif-maker_53.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980206856962088/ezgif.com-gif-maker_30.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980221146431558/ezgif.com-gif-maker_51.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980231070416896/ezgif.com-gif-maker_26.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980232258060348/ezgif.com-gif-maker_54.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980238267711548/ezgif.com-gif-maker_55.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980239409348718/ezgif.com-gif-maker_39.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    petplay = f"{author} masturbates with {mentions}"
                    choices = ["https://cdn.discordapp.com/attachments/828979138160754738/828979374807580702/ezgif.com-gif-maker_50.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979376741810176/ezgif.com-gif-maker_49.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979554945073172/ezgif.com-gif-maker_25.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979555813031986/ezgif.com-gif-maker_22.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979578193444874/ezgif.com-gif-maker_48.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979586427125840/ezgif.com-gif-maker_41.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979800810323988/ezgif.com-gif-maker_40.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979818284187678/ezgif.com-gif-maker_35.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979824570662962/ezgif.com-gif-maker_33.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979838538874910/ezgif.com-gif-maker_47.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979872591511612/ezgif.com-gif-maker_23.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979872738836560/ezgif.com-gif-maker_27.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979872931512340/ezgif.com-gif-maker_20.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979883073732638/ezgif.com-gif-maker_32.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979890070093834/ezgif.com-gif-maker_36.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979924500742144/ezgif.com-gif-maker_21.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979935241961522/ezgif.com-gif-maker_29.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979963604631603/ezgif.com-gif-maker_42.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980011473829898/ezgif.com-gif-maker_38.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980013050757120/ezgif.com-gif-maker_45.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980045556613130/ezgif.com-gif-maker_52.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980049193467954/ezgif.com-gif-maker_34.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980082273681408/ezgif.com-gif-maker_31.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980121910116422/ezgif.com-gif-maker_46.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980125654843462/ezgif.com-gif-maker_24.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980130256257074/ezgif.com-gif-maker_43.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980135608713237/ezgif.com-gif-maker_44.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980164930830366/ezgif.com-gif-maker_28.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980169292120104/ezgif.com-gif-maker_37.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980183729700864/ezgif.com-gif-maker_53.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980206856962088/ezgif.com-gif-maker_30.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980221146431558/ezgif.com-gif-maker_51.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980231070416896/ezgif.com-gif-maker_26.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980232258060348/ezgif.com-gif-maker_54.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980238267711548/ezgif.com-gif-maker_55.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980239409348718/ezgif.com-gif-maker_39.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
        else:
            mention_gender = determineGender(ctx.message.mentions[0])
            if author_gender == 'male':
                if mention_gender == 'female':
                    petplay = f"{author} masturbates with {mentions.name}"
                    choices = ["https://cdn.discordapp.com/attachments/828979138160754738/828979374807580702/ezgif.com-gif-maker_50.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979376741810176/ezgif.com-gif-maker_49.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979554945073172/ezgif.com-gif-maker_25.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979555813031986/ezgif.com-gif-maker_22.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979578193444874/ezgif.com-gif-maker_48.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979586427125840/ezgif.com-gif-maker_41.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979800810323988/ezgif.com-gif-maker_40.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979818284187678/ezgif.com-gif-maker_35.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979824570662962/ezgif.com-gif-maker_33.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979838538874910/ezgif.com-gif-maker_47.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979872591511612/ezgif.com-gif-maker_23.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979872738836560/ezgif.com-gif-maker_27.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979872931512340/ezgif.com-gif-maker_20.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979883073732638/ezgif.com-gif-maker_32.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979890070093834/ezgif.com-gif-maker_36.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979924500742144/ezgif.com-gif-maker_21.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979935241961522/ezgif.com-gif-maker_29.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979963604631603/ezgif.com-gif-maker_42.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980011473829898/ezgif.com-gif-maker_38.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980013050757120/ezgif.com-gif-maker_45.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980045556613130/ezgif.com-gif-maker_52.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980049193467954/ezgif.com-gif-maker_34.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980082273681408/ezgif.com-gif-maker_31.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980121910116422/ezgif.com-gif-maker_46.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980125654843462/ezgif.com-gif-maker_24.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980130256257074/ezgif.com-gif-maker_43.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980135608713237/ezgif.com-gif-maker_44.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980164930830366/ezgif.com-gif-maker_28.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980169292120104/ezgif.com-gif-maker_37.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980183729700864/ezgif.com-gif-maker_53.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980206856962088/ezgif.com-gif-maker_30.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980221146431558/ezgif.com-gif-maker_51.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980231070416896/ezgif.com-gif-maker_26.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980232258060348/ezgif.com-gif-maker_54.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980238267711548/ezgif.com-gif-maker_55.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980239409348718/ezgif.com-gif-maker_39.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    petplay = f"{author} masturbates with {mentions.name}"
                    choices = ["https://cdn.discordapp.com/attachments/828979138160754738/828982631664320542/ezgif.com-gif-maker_43.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828982639452749862/ezgif.com-gif-maker_44.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828982642614992907/ezgif.com-gif-maker_42.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828982656904593448/ezgif.com-gif-maker_30.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828982662970605608/ezgif.com-gif-maker_41.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828982692992253982/ezgif.com-gif-maker_27.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828982717919002645/ezgif.com-gif-maker_38.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828982719517032468/ezgif.com-gif-maker_34.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828982740539277352/ezgif.com-gif-maker_39.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828982754178760704/ezgif.com-gif-maker_33.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828982803097059358/ezgif.com-gif-maker_29.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828982810332233748/ezgif.com-gif-maker_37.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828982815877103697/ezgif.com-gif-maker_40.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828982820869111858/ezgif.com-gif-maker_36.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828982821938659408/ezgif.com-gif-maker_28.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828982823091306546/ezgif.com-gif-maker_35.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828982842401751150/ezgif.com-gif-maker_31.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828982846349770782/ezgif.com-gif-maker_32.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
            elif author_gender == 'female':
                if mention_gender == 'male':
                    petplay = f"{author} masturbates with {mentions.name}"
                    choices = ["https://cdn.discordapp.com/attachments/828979138160754738/828979374807580702/ezgif.com-gif-maker_50.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979376741810176/ezgif.com-gif-maker_49.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979554945073172/ezgif.com-gif-maker_25.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979555813031986/ezgif.com-gif-maker_22.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979578193444874/ezgif.com-gif-maker_48.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979586427125840/ezgif.com-gif-maker_41.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979800810323988/ezgif.com-gif-maker_40.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979818284187678/ezgif.com-gif-maker_35.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979824570662962/ezgif.com-gif-maker_33.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979838538874910/ezgif.com-gif-maker_47.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979872591511612/ezgif.com-gif-maker_23.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979872738836560/ezgif.com-gif-maker_27.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979872931512340/ezgif.com-gif-maker_20.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979883073732638/ezgif.com-gif-maker_32.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979890070093834/ezgif.com-gif-maker_36.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979924500742144/ezgif.com-gif-maker_21.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979935241961522/ezgif.com-gif-maker_29.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828979963604631603/ezgif.com-gif-maker_42.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980011473829898/ezgif.com-gif-maker_38.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980013050757120/ezgif.com-gif-maker_45.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980045556613130/ezgif.com-gif-maker_52.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980049193467954/ezgif.com-gif-maker_34.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980082273681408/ezgif.com-gif-maker_31.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980121910116422/ezgif.com-gif-maker_46.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980125654843462/ezgif.com-gif-maker_24.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980130256257074/ezgif.com-gif-maker_43.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980135608713237/ezgif.com-gif-maker_44.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980164930830366/ezgif.com-gif-maker_28.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980169292120104/ezgif.com-gif-maker_37.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980183729700864/ezgif.com-gif-maker_53.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980206856962088/ezgif.com-gif-maker_30.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980221146431558/ezgif.com-gif-maker_51.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980231070416896/ezgif.com-gif-maker_26.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980232258060348/ezgif.com-gif-maker_54.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980238267711548/ezgif.com-gif-maker_55.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828980239409348718/ezgif.com-gif-maker_39.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    petplay = f"{author} masturbates with {mentions.name}"
                    choices = ["https://cdn.discordapp.com/attachments/828979138160754738/828981279361728542/ezgif.com-gif-maker_62.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828981304149803008/ezgif.com-gif-maker_60.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828981425919361094/ezgif.com-gif-maker_56.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828981487680356402/ezgif.com-gif-maker_61.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828981529244860446/ezgif.com-gif-maker_63.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828981551441379418/ezgif.com-gif-maker_20.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828981558832267274/ezgif.com-gif-maker_59.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828981583335653416/ezgif.com-gif-maker_58.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828981595334508584/ezgif.com-gif-maker_25.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828981595942682664/ezgif.com-gif-maker_26.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828981609410723890/ezgif.com-gif-maker_21.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828981609998843995/ezgif.com-gif-maker_23.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828981616881434664/ezgif.com-gif-maker_22.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828981629120806982/ezgif.com-gif-maker_57.gif",
                                "https://cdn.discordapp.com/attachments/828979138160754738/828981644647071784/ezgif.com-gif-maker_24.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
    
    @masturbate.error
    async def masturbate_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete() 

    @commands.command()
    @commands.is_nsfw()
    async def tame(self, ctx, message=None):
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message

        if ctx.author.id == 815647994203602994:
            if mentions == message:
                if message == None:
                    embed = discord.Embed(
                        description=f"**No sir this isn't how it works\nExample use: $tame @User#6969**",
                        colour=discord.Colour.blue())
                    await ctx.send(embed=embed)
                else:
                    author = ctx.author.name
                    facial = "{0} tames the brat {1}"
                    choices = [
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046665849569350/ezgif.com-gif-maker_48.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046648539545630/ezgif.com-gif-maker_60.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046644739113020/ezgif.com-gif-maker_45.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046642603950130/ezgif.com-gif-maker_24.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046638024425502/ezgif.com-gif-maker_31.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046634048487434/ezgif.com-gif-maker_61.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046625616887838/ezgif.com-gif-maker_32.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046619317829702/ezgif.com-gif-maker_74.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046619191214110/ezgif.com-gif-maker_26.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046617941835776/ezgif.com-gif-maker_39.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046617207308328/ezgif.com-gif-maker_49.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046608127557692/ezgif.com-gif-maker_43.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046608068575281/ezgif.com-gif-maker_35.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046603430068224/ezgif.com-gif-maker_27.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046600820555786/ezgif.com-gif-maker_34.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046578075238430/ezgif.com-gif-maker_66.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046572307939329/ezgif.com-gif-maker_71.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046573071040522/ezgif.com-gif-maker_51.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046553382715402/ezgif.com-gif-maker_70.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046552842174494/ezgif.com-gif-maker_59.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046540360056832/ezgif.com-gif-maker_40.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046535774765056/ezgif.com-gif-maker_64.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046530281013258/ezgif.com-gif-maker_69.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046520181260308/ezgif.com-gif-maker_33.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046518536830976/ezgif.com-gif-maker_30.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046505245081670/ezgif.com-gif-maker_29.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046502824574997/ezgif.com-gif-maker_23.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046498332999721/ezgif.com-gif-maker_65.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046491080261682/ezgif.com-gif-maker_36.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046490510753842/ezgif.com-gif-maker_76.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046488056299562/ezgif.com-gif-maker_25.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046479995371580/ezgif.com-gif-maker_52.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046473556983838/ezgif.com-gif-maker_38.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046471048527882/ezgif.com-gif-maker_72.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046432486883338/ezgif.com-gif-maker_57.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046427411251230/ezgif.com-gif-maker_78.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046417013178448/ezgif.com-gif-maker_56.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046410001350686/ezgif.com-gif-maker_58.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046315985109003/ezgif.com-gif-maker_28.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046314957635614/ezgif.com-gif-maker_41.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046314635329686/ezgif.com-gif-maker_63.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046306468102194/ezgif.com-gif-maker_55.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046274663350302/ezgif.com-gif-maker_37.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046250491314216/ezgif.com-gif-maker_42.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046249929670716/ezgif.com-gif-maker_62.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046239096045608/ezgif.com-gif-maker_54.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046199971053598/ezgif.com-gif-maker_73.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046187426414632/ezgif.com-gif-maker_77.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046110842617877/ezgif.com-gif-maker_46.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046097625317376/ezgif.com-gif-maker_50.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046041174441994/ezgif.com-gif-maker_53.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834045986719531079/ezgif.com-gif-maker_44.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834045928351727646/ezgif.com-gif-maker_67.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834045891765207100/ezgif.com-gif-maker_68.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834128714345611345/ezgif.com-gif-maker_1.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128745551626320/ezgif.com-gif-maker_9.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128784071983134/ezgif.com-gif-maker_20.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128786467454986/ezgif.com-gif-maker_6.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128789935489034/ezgif.com-gif-maker_13.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128835787489310/ezgif.com-gif-maker_25.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128897619525743/ezgif.com-gif-maker_4.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128902460801024/ezgif.com-gif-maker_17.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128906348134430/ezgif.com-gif-maker.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128911905849364/ezgif.com-gif-maker_2.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128914644205628/ezgif.com-gif-maker_5.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128917924544522/ezgif.com-gif-maker_10.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128929815527454/ezgif.com-gif-maker_15.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128939252842516/ezgif.com-gif-maker_14.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128953823330404/ezgif.com-gif-maker_18.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128963939860520/ezgif.com-gif-maker_22.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128965128028210/ezgif.com-gif-maker_16.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128977613946890/ezgif.com-gif-maker_21.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128993678262332/ezgif.com-gif-maker_8.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128993698840647/ezgif.com-gif-maker_24.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834129014779543622/ezgif.com-gif-maker_3.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834129015216406538/ezgif.com-gif-maker_7.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834129022321295380/ezgif.com-gif-maker_11.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834129024216334367/ezgif.com-gif-maker_23.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=facial.format(author, mentions), colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)

            else:
                author = ctx.author.name
                facial = "{0} tames the brat {1}"
                choices = [
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046665849569350/ezgif.com-gif-maker_48.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046648539545630/ezgif.com-gif-maker_60.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046644739113020/ezgif.com-gif-maker_45.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046642603950130/ezgif.com-gif-maker_24.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046638024425502/ezgif.com-gif-maker_31.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046634048487434/ezgif.com-gif-maker_61.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046625616887838/ezgif.com-gif-maker_32.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046619317829702/ezgif.com-gif-maker_74.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046619191214110/ezgif.com-gif-maker_26.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046617941835776/ezgif.com-gif-maker_39.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046617207308328/ezgif.com-gif-maker_49.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046608127557692/ezgif.com-gif-maker_43.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046608068575281/ezgif.com-gif-maker_35.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046603430068224/ezgif.com-gif-maker_27.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046600820555786/ezgif.com-gif-maker_34.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046578075238430/ezgif.com-gif-maker_66.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046572307939329/ezgif.com-gif-maker_71.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046573071040522/ezgif.com-gif-maker_51.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046553382715402/ezgif.com-gif-maker_70.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046552842174494/ezgif.com-gif-maker_59.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046540360056832/ezgif.com-gif-maker_40.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046535774765056/ezgif.com-gif-maker_64.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046530281013258/ezgif.com-gif-maker_69.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046520181260308/ezgif.com-gif-maker_33.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046518536830976/ezgif.com-gif-maker_30.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046505245081670/ezgif.com-gif-maker_29.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046502824574997/ezgif.com-gif-maker_23.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046498332999721/ezgif.com-gif-maker_65.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046491080261682/ezgif.com-gif-maker_36.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046490510753842/ezgif.com-gif-maker_76.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046488056299562/ezgif.com-gif-maker_25.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046479995371580/ezgif.com-gif-maker_52.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046473556983838/ezgif.com-gif-maker_38.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046471048527882/ezgif.com-gif-maker_72.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046432486883338/ezgif.com-gif-maker_57.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046427411251230/ezgif.com-gif-maker_78.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046417013178448/ezgif.com-gif-maker_56.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046410001350686/ezgif.com-gif-maker_58.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046315985109003/ezgif.com-gif-maker_28.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046314957635614/ezgif.com-gif-maker_41.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046314635329686/ezgif.com-gif-maker_63.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046306468102194/ezgif.com-gif-maker_55.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046274663350302/ezgif.com-gif-maker_37.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046250491314216/ezgif.com-gif-maker_42.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046249929670716/ezgif.com-gif-maker_62.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046239096045608/ezgif.com-gif-maker_54.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046199971053598/ezgif.com-gif-maker_73.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046187426414632/ezgif.com-gif-maker_77.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046110842617877/ezgif.com-gif-maker_46.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046097625317376/ezgif.com-gif-maker_50.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046041174441994/ezgif.com-gif-maker_53.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834045986719531079/ezgif.com-gif-maker_44.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834045928351727646/ezgif.com-gif-maker_67.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834045891765207100/ezgif.com-gif-maker_68.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834128714345611345/ezgif.com-gif-maker_1.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128745551626320/ezgif.com-gif-maker_9.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128784071983134/ezgif.com-gif-maker_20.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128786467454986/ezgif.com-gif-maker_6.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128789935489034/ezgif.com-gif-maker_13.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128835787489310/ezgif.com-gif-maker_25.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128897619525743/ezgif.com-gif-maker_4.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128902460801024/ezgif.com-gif-maker_17.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128906348134430/ezgif.com-gif-maker.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128911905849364/ezgif.com-gif-maker_2.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128914644205628/ezgif.com-gif-maker_5.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128917924544522/ezgif.com-gif-maker_10.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128929815527454/ezgif.com-gif-maker_15.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128939252842516/ezgif.com-gif-maker_14.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128953823330404/ezgif.com-gif-maker_18.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128963939860520/ezgif.com-gif-maker_22.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128965128028210/ezgif.com-gif-maker_16.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128977613946890/ezgif.com-gif-maker_21.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128993678262332/ezgif.com-gif-maker_8.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128993698840647/ezgif.com-gif-maker_24.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834129014779543622/ezgif.com-gif-maker_3.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834129015216406538/ezgif.com-gif-maker_7.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834129022321295380/ezgif.com-gif-maker_11.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834129024216334367/ezgif.com-gif-maker_23.gif"]
                img = random.choice(choices)
                embed = discord.Embed(title=facial.format(author, mentions.name), colour=discord.Colour.blue())
                embed.set_image(url=img)
                await ctx.send(embed=embed)

        if not ctx.author.id == 815647994203602994:
            if mentions == message:
                if message == None:
                    embed = discord.Embed(
                        description=f"**No sir this isn't how it works\nExample use: $tame @User#6969**",
                        colour=discord.Colour.blue())
                    await ctx.send(embed=embed)
                else:
                    choices = [
                        'https://cdn.discordapp.com/attachments/798913238229188608/822156703285379119/giphy_1.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822156709862178846/067025659eb25f9b74605738d1b2a7a7.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822155216287039509/IcyCookedCoot-small.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822156711674118174/200.gif',
                        'https://cdn.discordapp.com/attachments/798913238229188608/822156717138772048/giphy.gif']
                    image = random.choice(choices)
                    embed = discord.Embed(description="**This is a custom command**", colour=discord.Colour.blue())
                    embed.set_image(url=image)
                    embed.set_footer(text="$patreon to buy a custom command!")
                    await ctx.send(embed=embed)
            if ctx.message.mentions[0].id == 815647994203602994:

                author_gender = determineGender(ctx.author)
                if author_gender == 'female':
                    author = ctx.author.name
                    facial = "{0} gets tamed by {1}"
                    choices = [
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046665849569350/ezgif.com-gif-maker_48.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046648539545630/ezgif.com-gif-maker_60.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046644739113020/ezgif.com-gif-maker_45.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046642603950130/ezgif.com-gif-maker_24.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046638024425502/ezgif.com-gif-maker_31.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046634048487434/ezgif.com-gif-maker_61.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046625616887838/ezgif.com-gif-maker_32.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046619317829702/ezgif.com-gif-maker_74.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046619191214110/ezgif.com-gif-maker_26.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046617941835776/ezgif.com-gif-maker_39.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046617207308328/ezgif.com-gif-maker_49.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046608127557692/ezgif.com-gif-maker_43.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046608068575281/ezgif.com-gif-maker_35.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046603430068224/ezgif.com-gif-maker_27.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046600820555786/ezgif.com-gif-maker_34.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046578075238430/ezgif.com-gif-maker_66.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046572307939329/ezgif.com-gif-maker_71.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046573071040522/ezgif.com-gif-maker_51.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046553382715402/ezgif.com-gif-maker_70.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046552842174494/ezgif.com-gif-maker_59.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046540360056832/ezgif.com-gif-maker_40.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046535774765056/ezgif.com-gif-maker_64.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046530281013258/ezgif.com-gif-maker_69.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046520181260308/ezgif.com-gif-maker_33.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046518536830976/ezgif.com-gif-maker_30.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046505245081670/ezgif.com-gif-maker_29.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046502824574997/ezgif.com-gif-maker_23.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046498332999721/ezgif.com-gif-maker_65.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046491080261682/ezgif.com-gif-maker_36.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046490510753842/ezgif.com-gif-maker_76.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046488056299562/ezgif.com-gif-maker_25.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046479995371580/ezgif.com-gif-maker_52.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046473556983838/ezgif.com-gif-maker_38.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046471048527882/ezgif.com-gif-maker_72.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046432486883338/ezgif.com-gif-maker_57.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046427411251230/ezgif.com-gif-maker_78.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046417013178448/ezgif.com-gif-maker_56.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046410001350686/ezgif.com-gif-maker_58.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046315985109003/ezgif.com-gif-maker_28.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046314957635614/ezgif.com-gif-maker_41.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046314635329686/ezgif.com-gif-maker_63.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046306468102194/ezgif.com-gif-maker_55.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046274663350302/ezgif.com-gif-maker_37.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046250491314216/ezgif.com-gif-maker_42.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046249929670716/ezgif.com-gif-maker_62.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046239096045608/ezgif.com-gif-maker_54.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046199971053598/ezgif.com-gif-maker_73.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046187426414632/ezgif.com-gif-maker_77.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046110842617877/ezgif.com-gif-maker_46.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046097625317376/ezgif.com-gif-maker_50.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834046041174441994/ezgif.com-gif-maker_53.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834045986719531079/ezgif.com-gif-maker_44.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834045928351727646/ezgif.com-gif-maker_67.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834045891765207100/ezgif.com-gif-maker_68.gif",
                            "https://cdn.discordapp.com/attachments/798913238229188608/834128714345611345/ezgif.com-gif-maker_1.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128745551626320/ezgif.com-gif-maker_9.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128784071983134/ezgif.com-gif-maker_20.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128786467454986/ezgif.com-gif-maker_6.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128789935489034/ezgif.com-gif-maker_13.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128835787489310/ezgif.com-gif-maker_25.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128897619525743/ezgif.com-gif-maker_4.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128902460801024/ezgif.com-gif-maker_17.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128906348134430/ezgif.com-gif-maker.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128911905849364/ezgif.com-gif-maker_2.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128914644205628/ezgif.com-gif-maker_5.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128917924544522/ezgif.com-gif-maker_10.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128929815527454/ezgif.com-gif-maker_15.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128939252842516/ezgif.com-gif-maker_14.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128953823330404/ezgif.com-gif-maker_18.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128963939860520/ezgif.com-gif-maker_22.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128965128028210/ezgif.com-gif-maker_16.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128977613946890/ezgif.com-gif-maker_21.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128993678262332/ezgif.com-gif-maker_8.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834128993698840647/ezgif.com-gif-maker_24.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834129014779543622/ezgif.com-gif-maker_3.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834129015216406538/ezgif.com-gif-maker_7.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834129022321295380/ezgif.com-gif-maker_11.gif",
                           "https://cdn.discordapp.com/attachments/798913238229188608/834129024216334367/ezgif.com-gif-maker_23.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=facial.format(author, mentions.name),
                                          colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    choices = ['https://cdn.discordapp.com/attachments/798913238229188608/822155196053323776/tenor_1.gif',
                               'https://cdn.discordapp.com/attachments/798913238229188608/822155196322283520/tenor.gif',
                               'https://cdn.discordapp.com/attachments/798913238229188608/822155216287039509/IcyCookedCoot-small.gif']
                    image = random.choice(choices)
                    embed = discord.Embed(description="**This is a custom command**", colour=discord.Colour.blue())
                    embed.set_image(url=image)
                    embed.set_footer(text="$patreon to buy a custom command!")
                    await ctx.send(embed=embed)
            else:
                choices = [
                    'https://cdn.discordapp.com/attachments/798913238229188608/822156703285379119/giphy_1.gif',
                    'https://cdn.discordapp.com/attachments/798913238229188608/822156709862178846/067025659eb25f9b74605738d1b2a7a7.gif',
                    'https://cdn.discordapp.com/attachments/798913238229188608/822155216287039509/IcyCookedCoot-small.gif',
                    'https://cdn.discordapp.com/attachments/798913238229188608/822156711674118174/200.gif',
                    'https://cdn.discordapp.com/attachments/798913238229188608/822156717138772048/giphy.gif']
                image = random.choice(choices)
                embed = discord.Embed(description="**This is a custom command**", colour=discord.Colour.blue())
                embed.set_image(url=image)
                embed.set_footer(text="$patreon to buy a custom command!")
                await ctx.send(embed=embed)
   
    @commands.command()
    @commands.is_nsfw()
    async def titfuck(self, ctx, message=None):
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author = ctx.author.name
        author_gender = determineGender(ctx.author)
        if mentions == message:
            if message == None:
                embed = discord.Embed(
                    description=f"**You can't titfuck nothing you horni dumbo\nExample use: $titfuck @User#6969**",
                    colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                if author_gender == 'male':
                    petplay = f"{author} titfucks {mentions}"
                    choices = ["https://cdn.discordapp.com/attachments/798913238229188608/850491816382169138/ezgif.com-gif-maker_26.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850491930642874438/ezgif.com-gif-maker_38.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850491952512368691/ezgif.com-gif-maker_32.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850491975685767198/ezgif.com-gif-maker_28.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492001992179722/ezgif.com-gif-maker_29.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492005016535090/ezgif.com-gif-maker_36.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492008291631104/ezgif.com-gif-maker_40.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492014730412062/ezgif.com-gif-maker_34.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492000796147752/ezgif.com-gif-maker_30.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492022656991242/ezgif.com-gif-maker_35.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492047358296104/ezgif.com-gif-maker_27.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492055338876979/ezgif.com-gif-maker_31.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492057482690602/ezgif.com-gif-maker_33.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492060847177798/ezgif.com-gif-maker_37.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492063073828874/ezgif.com-gif-maker_39.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    petplay = f"{author} titfucked by {mentions}"
                    choices = ["https://cdn.discordapp.com/attachments/798913238229188608/850491816382169138/ezgif.com-gif-maker_26.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850491930642874438/ezgif.com-gif-maker_38.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850491952512368691/ezgif.com-gif-maker_32.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850491975685767198/ezgif.com-gif-maker_28.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492001992179722/ezgif.com-gif-maker_29.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492005016535090/ezgif.com-gif-maker_36.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492008291631104/ezgif.com-gif-maker_40.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492014730412062/ezgif.com-gif-maker_34.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492000796147752/ezgif.com-gif-maker_30.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492022656991242/ezgif.com-gif-maker_35.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492047358296104/ezgif.com-gif-maker_27.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492055338876979/ezgif.com-gif-maker_31.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492057482690602/ezgif.com-gif-maker_33.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492060847177798/ezgif.com-gif-maker_37.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492063073828874/ezgif.com-gif-maker_39.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
        else:
            mention_gender = determineGender(ctx.message.mentions[0])
            if author_gender == 'male':
                if mention_gender == 'female':
                    petplay = f"{author} titfucks {mentions.name}"
                    choices = ["https://cdn.discordapp.com/attachments/798913238229188608/850491816382169138/ezgif.com-gif-maker_26.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850491930642874438/ezgif.com-gif-maker_38.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850491952512368691/ezgif.com-gif-maker_32.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850491975685767198/ezgif.com-gif-maker_28.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492001992179722/ezgif.com-gif-maker_29.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492005016535090/ezgif.com-gif-maker_36.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492008291631104/ezgif.com-gif-maker_40.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492014730412062/ezgif.com-gif-maker_34.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492000796147752/ezgif.com-gif-maker_30.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492022656991242/ezgif.com-gif-maker_35.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492047358296104/ezgif.com-gif-maker_27.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492055338876979/ezgif.com-gif-maker_31.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492057482690602/ezgif.com-gif-maker_33.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492060847177798/ezgif.com-gif-maker_37.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492063073828874/ezgif.com-gif-maker_39.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    petplay = f"{author} titfucks {mentions.name}"
                    choices = ["https://cdn.discordapp.com/attachments/798913238229188608/850491816382169138/ezgif.com-gif-maker_26.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850491930642874438/ezgif.com-gif-maker_38.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850491952512368691/ezgif.com-gif-maker_32.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850491975685767198/ezgif.com-gif-maker_28.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492001992179722/ezgif.com-gif-maker_29.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492005016535090/ezgif.com-gif-maker_36.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492008291631104/ezgif.com-gif-maker_40.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492014730412062/ezgif.com-gif-maker_34.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492000796147752/ezgif.com-gif-maker_30.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492022656991242/ezgif.com-gif-maker_35.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492047358296104/ezgif.com-gif-maker_27.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492055338876979/ezgif.com-gif-maker_31.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492057482690602/ezgif.com-gif-maker_33.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492060847177798/ezgif.com-gif-maker_37.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492063073828874/ezgif.com-gif-maker_39.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
            elif author_gender == 'female':
                if mention_gender == 'male':
                    petplay = f"{author} titfucked by {mentions.name}"
                    choices = ["https://cdn.discordapp.com/attachments/798913238229188608/850491816382169138/ezgif.com-gif-maker_26.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850491930642874438/ezgif.com-gif-maker_38.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850491952512368691/ezgif.com-gif-maker_32.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850491975685767198/ezgif.com-gif-maker_28.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492001992179722/ezgif.com-gif-maker_29.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492005016535090/ezgif.com-gif-maker_36.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492008291631104/ezgif.com-gif-maker_40.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492014730412062/ezgif.com-gif-maker_34.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492000796147752/ezgif.com-gif-maker_30.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492022656991242/ezgif.com-gif-maker_35.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492047358296104/ezgif.com-gif-maker_27.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492055338876979/ezgif.com-gif-maker_31.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492057482690602/ezgif.com-gif-maker_33.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492060847177798/ezgif.com-gif-maker_37.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492063073828874/ezgif.com-gif-maker_39.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    petplay = f"{author} titfucked by {mentions.name}"
                    choices = ["https://cdn.discordapp.com/attachments/798913238229188608/850491816382169138/ezgif.com-gif-maker_26.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850491930642874438/ezgif.com-gif-maker_38.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850491952512368691/ezgif.com-gif-maker_32.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850491975685767198/ezgif.com-gif-maker_28.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492001992179722/ezgif.com-gif-maker_29.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492005016535090/ezgif.com-gif-maker_36.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492008291631104/ezgif.com-gif-maker_40.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492014730412062/ezgif.com-gif-maker_34.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492000796147752/ezgif.com-gif-maker_30.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492022656991242/ezgif.com-gif-maker_35.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492047358296104/ezgif.com-gif-maker_27.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492055338876979/ezgif.com-gif-maker_31.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492057482690602/ezgif.com-gif-maker_33.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492060847177798/ezgif.com-gif-maker_37.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492063073828874/ezgif.com-gif-maker_39.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)

    @titfuck.error
    async def titfuck_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()

    @commands.group()
    @commands.is_nsfw()
    async def shower(self, ctx):
        if ctx.invoked_subcommand is None:
            message = await ctx.send('**This is not a command!**')
            await asyncio.sleep(5)
            await message.delete()

    @shower.command(name="sex")
    async def _sex(self, ctx, message=None):
        try:
            mentions = ctx.message.mentions[0]
        except:
            mentions = message
        author = ctx.author.name
        author_gender = determineGender(ctx.author)
        if mentions == message:
            if message == None:
                embed = discord.Embed(
                    description=f"**You can't fuck nothing you horni dumbo\nExample use: $shower sex @User#6969**",
                    colour=discord.Colour.blue())
                await ctx.send(embed=embed)
            else:
                if author_gender == 'male':
                    petplay = f"{author} fucks {mentions} in shower"
                    choices = ["https://cdn.discordapp.com/attachments/798913238229188608/850491816382169138/ezgif.com-gif-maker_26.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850491930642874438/ezgif.com-gif-maker_38.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850491952512368691/ezgif.com-gif-maker_32.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850491975685767198/ezgif.com-gif-maker_28.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492001992179722/ezgif.com-gif-maker_29.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492005016535090/ezgif.com-gif-maker_36.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492008291631104/ezgif.com-gif-maker_40.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492014730412062/ezgif.com-gif-maker_34.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492000796147752/ezgif.com-gif-maker_30.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492022656991242/ezgif.com-gif-maker_35.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492047358296104/ezgif.com-gif-maker_27.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492055338876979/ezgif.com-gif-maker_31.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492057482690602/ezgif.com-gif-maker_33.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492060847177798/ezgif.com-gif-maker_37.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492063073828874/ezgif.com-gif-maker_39.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    petplay = f"{author} gets by {mentions} in shower"
                    choices = ["https://cdn.discordapp.com/attachments/798913238229188608/850491816382169138/ezgif.com-gif-maker_26.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850491930642874438/ezgif.com-gif-maker_38.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850491952512368691/ezgif.com-gif-maker_32.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850491975685767198/ezgif.com-gif-maker_28.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492001992179722/ezgif.com-gif-maker_29.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492005016535090/ezgif.com-gif-maker_36.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492008291631104/ezgif.com-gif-maker_40.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492014730412062/ezgif.com-gif-maker_34.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492000796147752/ezgif.com-gif-maker_30.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492022656991242/ezgif.com-gif-maker_35.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492047358296104/ezgif.com-gif-maker_27.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492055338876979/ezgif.com-gif-maker_31.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492057482690602/ezgif.com-gif-maker_33.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492060847177798/ezgif.com-gif-maker_37.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/850492063073828874/ezgif.com-gif-maker_39.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
        else:
            mention_gender = determineGender(ctx.message.mentions[0])
            if author_gender == 'male':
                if mention_gender == 'female':
                    petplay = f"{author} fucks {mentions.name} in shower"
                    choices = ["https://cdn.discordapp.com/attachments/798913238229188608/875332417328644096/ezgif.com-gif-maker_90.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332443970891847/ezgif.com-gif-maker_82.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332511402692629/ezgif.com-gif-maker_84.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332518604337172/ezgif.com-gif-maker_83.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332571280584704/ezgif.com-gif-maker_88.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332638292996106/ezgif.com-gif-maker_80.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332648782929920/ezgif.com-gif-maker_86.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332655862939678/ezgif.com-gif-maker_89.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332677287432203/ezgif.com-gif-maker_87.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332691283820584/ezgif.com-gif-maker_91.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332699265564692/ezgif.com-gif-maker_79.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332728474726400/ezgif.com-gif-maker_85.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332780333072404/ezgif.com-gif-maker_81.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    petplay = f"{author} fucks {mentions.name} in shower"
                    choices = ["https://cdn.discordapp.com/attachments/798913238229188608/875332731905658920/ezgif.com-gif-maker_-_2021-08-12T135521.181.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332706962145340/ezgif.com-gif-maker_-_2021-08-12T135527.916.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332703468257380/ezgif.com-gif-maker_-_2021-08-12T135506.084.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332649315602452/ezgif.com-gif-maker_-_2021-08-12T135613.026.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332620584640572/ezgif.com-gif-maker_-_2021-08-12T135514.258.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332574166265876/ezgif.com-gif-maker_-_2021-08-12T135459.258.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332538556641331/ezgif.com-gif-maker_-_2021-08-12T135705.202.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332423129395220/ezgif.com-gif-maker_100.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
            elif author_gender == 'female':
                if mention_gender == 'male':
                    petplay = f"{author} fucked by {mentions.name} in shower"
                    choices = ["https://cdn.discordapp.com/attachments/798913238229188608/875332417328644096/ezgif.com-gif-maker_90.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332443970891847/ezgif.com-gif-maker_82.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332511402692629/ezgif.com-gif-maker_84.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332518604337172/ezgif.com-gif-maker_83.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332571280584704/ezgif.com-gif-maker_88.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332638292996106/ezgif.com-gif-maker_80.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332648782929920/ezgif.com-gif-maker_86.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332655862939678/ezgif.com-gif-maker_89.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332677287432203/ezgif.com-gif-maker_87.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332691283820584/ezgif.com-gif-maker_91.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332699265564692/ezgif.com-gif-maker_79.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332728474726400/ezgif.com-gif-maker_85.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332780333072404/ezgif.com-gif-maker_81.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    petplay = f"{author} fucked by {mentions.name} in shower"
                    choices = ["https://cdn.discordapp.com/attachments/798913238229188608/875332776906330123/ezgif.com-gif-maker_97.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332704365854720/ezgif.com-gif-maker_94.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332704047104050/ezgif.com-gif-maker_98.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332688779833364/ezgif.com-gif-maker_99.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332686410031114/ezgif.com-gif-maker_92.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332682538709052/ezgif.com-gif-maker_93.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332623399014400/ezgif.com-gif-maker_95.gif",
                                "https://cdn.discordapp.com/attachments/798913238229188608/875332597482418186/ezgif.com-gif-maker_96.gif"]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
    

    @commands.command()
    @commands.is_nsfw()
    async def cuddlefuck(self, ctx, message=None):
        try:
                mentions = ctx.message.mentions[0]
        except:
                mentions = message
        author = ctx.author.name
        author_gender = determineGender(ctx.author)
        if mentions == message:
                if message == None:
                    embed = discord.Embed(
                        description=f"**You can't cuddlefuck nothing you horni dumbo\nExample use: $cuddlefuck @User#6969**",
                        colour=discord.Colour.blue())
                    await ctx.send(embed=embed)
                else:
                    if author_gender == 'male':
                        petplay = f"{author} fucks {mentions}"
                        choices = ["https://cdn.discordapp.com/attachments/798913238229188608/875357893963161610/ezgif.com-gif-maker_89.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357891513684028/ezgif.com-gif-maker_80.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357878381326396/ezgif.com-gif-maker_88.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357873830522930/ezgif.com-gif-maker_87.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357865446100992/ezgif.com-gif-maker_86.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357855425888297/ezgif.com-gif-maker_83.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357854436044850/ezgif.com-gif-maker_79.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357844436815882/ezgif.com-gif-maker_85.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357843501502585/ezgif.com-gif-maker_81.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357785045491712/ezgif.com-gif-maker_82.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357751470080060/ezgif.com-gif-maker_84.gif"]
                        img = random.choice(choices)
                        embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                        embed.set_image(url=img)
                        await ctx.send(embed=embed)
                    else:
                        petplay = f"{author} gets fucked {mentions}"
                        choices = ["https://cdn.discordapp.com/attachments/798913238229188608/875357893963161610/ezgif.com-gif-maker_89.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357891513684028/ezgif.com-gif-maker_80.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357878381326396/ezgif.com-gif-maker_88.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357873830522930/ezgif.com-gif-maker_87.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357865446100992/ezgif.com-gif-maker_86.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357855425888297/ezgif.com-gif-maker_83.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357854436044850/ezgif.com-gif-maker_79.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357844436815882/ezgif.com-gif-maker_85.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357843501502585/ezgif.com-gif-maker_81.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357785045491712/ezgif.com-gif-maker_82.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357751470080060/ezgif.com-gif-maker_84.gif"]
                        img = random.choice(choices)
                        embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                        embed.set_image(url=img)
                        await ctx.send(embed=embed)
        else:
                mention_gender = determineGender(ctx.message.mentions[0])
                if author_gender == 'male':
                    if mention_gender == 'female':
                        petplay = f"{author} fucks {mentions.name}"
                        choices = ["https://cdn.discordapp.com/attachments/798913238229188608/875357893963161610/ezgif.com-gif-maker_89.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357891513684028/ezgif.com-gif-maker_80.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357878381326396/ezgif.com-gif-maker_88.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357873830522930/ezgif.com-gif-maker_87.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357865446100992/ezgif.com-gif-maker_86.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357855425888297/ezgif.com-gif-maker_83.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357854436044850/ezgif.com-gif-maker_79.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357844436815882/ezgif.com-gif-maker_85.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357843501502585/ezgif.com-gif-maker_81.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357785045491712/ezgif.com-gif-maker_82.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357751470080060/ezgif.com-gif-maker_84.gif"]
                        img = random.choice(choices)
                        embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                        embed.set_image(url=img)
                        await ctx.send(embed=embed)
                    else:
                        petplay = f"{author} fucks {mentions.name}"
                        choices = ["https://cdn.discordapp.com/attachments/798913238229188608/875356565702598666/chicolu420-tgv0d-3e4a08.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875356571528486922/eFkrX.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875356572300247102/tumblr_nm0percH351te42yzo1_500.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875356575680856134/tumblr_mxnxyqmUPJ1r8dpz8o1_500.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875356577111093248/tumblr_nx7iogTYbo1une9rio1_500.gif"]
                        img = random.choice(choices)
                        embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                        embed.set_image(url=img)
                        await ctx.send(embed=embed)
                elif author_gender == 'female':
                    if mention_gender == 'male':
                        petplay = f"{author} fucked by {mentions.name}"
                        choices = ["https://cdn.discordapp.com/attachments/798913238229188608/875357893963161610/ezgif.com-gif-maker_89.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357891513684028/ezgif.com-gif-maker_80.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357878381326396/ezgif.com-gif-maker_88.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357873830522930/ezgif.com-gif-maker_87.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357865446100992/ezgif.com-gif-maker_86.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357855425888297/ezgif.com-gif-maker_83.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357854436044850/ezgif.com-gif-maker_79.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357844436815882/ezgif.com-gif-maker_85.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357843501502585/ezgif.com-gif-maker_81.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357785045491712/ezgif.com-gif-maker_82.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357751470080060/ezgif.com-gif-maker_84.gif"]
                        img = random.choice(choices)
                        embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                        embed.set_image(url=img)
                        await ctx.send(embed=embed)
                    else:
                        petplay = f"{author} fucked by {mentions.name}"
                        choices = ["https://cdn.discordapp.com/attachments/798913238229188608/875356644094148608/17503323.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875356894582165504/18117521.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357759195979816/ezgif.com-gif-maker_92.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357782314979388/ezgif.com-gif-maker_90.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357868390490152/ezgif.com-gif-maker_95.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357874858127360/ezgif.com-gif-maker_94.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357882642743306/ezgif.com-gif-maker_91.gif",
                                    "https://cdn.discordapp.com/attachments/798913238229188608/875357889655623710/ezgif.com-gif-maker_93.gif"]
                        img = random.choice(choices)
                        embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                        embed.set_image(url=img)
                        await ctx.send(embed=embed)

    @cuddlefuck.error
    async def cuddlefuck_error(self, ctx, error):
        if isinstance(error, commands.NSFWChannelRequired):
            message = await ctx.send("**Channel isn't NSFW!**")
            await asyncio.sleep(10)
            await message.delete()   

    @commands.command()
    @commands.is_nsfw()
    async def sprinkles(self, ctx, message=None):
        try:
                mentions = ctx.message.mentions[0]
        except:
                mentions = message
        author = ctx.author.name
        author_gender = determineGender(ctx.author)
        if mentions == message:
                if message == None:
                    petplay = f"{author} sprinkles"
                    choices = ["https://media.discordapp.net/attachments/819857033489940481/888543764413575218/ezgif.com-gif-maker_8.gif",
                                    "https://media.discordapp.net/attachments/819857033489940481/888543758285692978/ezgif.com-gif-maker_7.gif",
                                    "https://media.discordapp.net/attachments/819857033489940481/888543752677908521/ezgif.com-gif-maker_5.gif",
                                    "https://media.discordapp.net/attachments/819857033489940481/888543745593720852/ezgif.com-gif-maker_4.gif",
                                    "https://media.discordapp.net/attachments/819857033489940481/852374119294304266/image0-1.gif"
                                    ]
                    img = random.choice(choices)
                    embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                    embed.set_image(url=img)
                    await ctx.send(embed=embed)
                else:
                    if author_gender == 'male':
                        petplay = f"{author} sprinkles {mentions}"
                        choices = ["https://media.discordapp.net/attachments/819857033489940481/888543764413575218/ezgif.com-gif-maker_8.gif",
                                    "https://media.discordapp.net/attachments/819857033489940481/888543758285692978/ezgif.com-gif-maker_7.gif",
                                    "https://media.discordapp.net/attachments/819857033489940481/888543752677908521/ezgif.com-gif-maker_5.gif",
                                    "https://media.discordapp.net/attachments/819857033489940481/888543745593720852/ezgif.com-gif-maker_4.gif",
                                    "https://media.discordapp.net/attachments/819857033489940481/852374119294304266/image0-1.gif"
                                    ]
                        img = random.choice(choices)
                        embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                        embed.set_image(url=img)
                        await ctx.send(embed=embed)
                    else:
                        petplay = f"{author} sprinkles {mentions}"
                        choices = ["https://media.discordapp.net/attachments/819857033489940481/888543764413575218/ezgif.com-gif-maker_8.gif",
                                    "https://media.discordapp.net/attachments/819857033489940481/888543758285692978/ezgif.com-gif-maker_7.gif",
                                    "https://media.discordapp.net/attachments/819857033489940481/888543752677908521/ezgif.com-gif-maker_5.gif",
                                    "https://media.discordapp.net/attachments/819857033489940481/888543745593720852/ezgif.com-gif-maker_4.gif",
                                    "https://media.discordapp.net/attachments/819857033489940481/852374119294304266/image0-1.gif"
                                    ]
                        img = random.choice(choices)
                        embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                        embed.set_image(url=img)
                        await ctx.send(embed=embed)
        else:
                mention_gender = determineGender(ctx.message.mentions[0])
                if author_gender == 'male':
                    if mention_gender == 'female':
                        petplay = f"{author} sprinkles {mentions.name}"
                        choices = ["https://media.discordapp.net/attachments/819857033489940481/888543764413575218/ezgif.com-gif-maker_8.gif",
                                    "https://media.discordapp.net/attachments/819857033489940481/888543758285692978/ezgif.com-gif-maker_7.gif",
                                    "https://media.discordapp.net/attachments/819857033489940481/888543752677908521/ezgif.com-gif-maker_5.gif",
                                    "https://media.discordapp.net/attachments/819857033489940481/888543745593720852/ezgif.com-gif-maker_4.gif",
                                    "https://media.discordapp.net/attachments/819857033489940481/852374119294304266/image0-1.gif"
                                    ]
                        img = random.choice(choices)
                        embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                        embed.set_image(url=img)
                        await ctx.send(embed=embed)
                    else:
                        petplay = f"{author} sprinkles {mentions.name}"
                        choices = ["https://media.discordapp.net/attachments/819857033489940481/888543764413575218/ezgif.com-gif-maker_8.gif",
                                    "https://media.discordapp.net/attachments/819857033489940481/888543758285692978/ezgif.com-gif-maker_7.gif",
                                    "https://media.discordapp.net/attachments/819857033489940481/888543752677908521/ezgif.com-gif-maker_5.gif",
                                    "https://media.discordapp.net/attachments/819857033489940481/888543745593720852/ezgif.com-gif-maker_4.gif",
                                    "https://media.discordapp.net/attachments/819857033489940481/852374119294304266/image0-1.gif"
                                    ]
                        img = random.choice(choices)
                        embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                        embed.set_image(url=img)
                        await ctx.send(embed=embed)
                elif author_gender == 'female':
                    if mention_gender == 'male':
                        petplay = f"{author} sprinkles {mentions.name}"
                        choices = ["https://media.discordapp.net/attachments/819857033489940481/888543764413575218/ezgif.com-gif-maker_8.gif",
                                    "https://media.discordapp.net/attachments/819857033489940481/888543758285692978/ezgif.com-gif-maker_7.gif",
                                    "https://media.discordapp.net/attachments/819857033489940481/888543752677908521/ezgif.com-gif-maker_5.gif",
                                    "https://media.discordapp.net/attachments/819857033489940481/888543745593720852/ezgif.com-gif-maker_4.gif",
                                    "https://media.discordapp.net/attachments/819857033489940481/852374119294304266/image0-1.gif"
                                    ]
                        img = random.choice(choices)
                        embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                        embed.set_image(url=img)
                        await ctx.send(embed=embed)
                    else:
                        petplay = f"{author} sprinkles {mentions.name}"
                        choices = ["https://media.discordapp.net/attachments/819857033489940481/888543764413575218/ezgif.com-gif-maker_8.gif",
                                    "https://media.discordapp.net/attachments/819857033489940481/888543758285692978/ezgif.com-gif-maker_7.gif",
                                    "https://media.discordapp.net/attachments/819857033489940481/888543752677908521/ezgif.com-gif-maker_5.gif",
                                    "https://media.discordapp.net/attachments/819857033489940481/888543745593720852/ezgif.com-gif-maker_4.gif",
                                    "https://media.discordapp.net/attachments/819857033489940481/852374119294304266/image0-1.gif"
                                    ]
                        img = random.choice(choices)
                        embed = discord.Embed(title=petplay, colour=discord.Colour.blue())
                        embed.set_image(url=img)
                        await ctx.send(embed=embed)
        

def setup(client):
    client.add_cog(Nsfw(client))