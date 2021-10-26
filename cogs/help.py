import discord
from discord.ext import commands
import asyncio

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group(aliases=['h', 'he'])
    async def help(self, ctx):

        user = ctx.author
        if ctx.invoked_subcommand is None:
            em = discord.Embed(colour=discord.Colour.blue())
            em.set_author(name='Help')
            em.add_field(name='Interaction commands',
                         value="dab, morning(gm), goodnight(gn), ping,"
                               " hug, cuddle, kiss, pat, smile, kill, fistbump, bunny, punch, popcorn, goodjob(gj), weed"
                               "gay, nap, holdhand, spooky, penis, lewd, nom, blowkiss, slap, poke, fu, boop, grouphug, feed, suplex, coffee, "
                               "cat, yeet, meme, taco", inline=False)
            em.add_field(name='Level and Economy',
                         value="rank, levels(lb), balance(bal), work, daily, rep, profile, refresh, token"
                               "gamble, pantyboard, marry, divorce, sidechick, residechick, showsc, convertpanty",
                         inline=False)
            em.add_field(name='Moderation(Not fully functional yet)',
                         value="avatar(av), userinfo, roleall, slowmode, serverinfo, purge", inline=False)
            em.set_footer(text="$nsfw for NSFW command list")

            emb = discord.Embed(colour=discord.Colour.blue())
            emb.set_author(name='Help')
            emb.add_field(name='Interaction commands',
                          value="dab, morning(gm), goodnight(gn), ping,"
                                " hug, cuddle, kiss, pat, smile, kill, fistbump, bunny, punch, popcorn, goodjob(gj), weed"
                                "gay, nap, holdhand, spooky, penis, lewd, nom, blowkiss, slap, poke, fu, boop, grouphug, feed, suplex, coffee, "
                                "cat, yeet, meme, taco", inline=False)
            emb.add_field(name='Level and Economy',
                          value="rank, levels(lb), balance(bal), work, daily, rep, profile, refresh, token"
                                "gamble, pantyboard, marry, divorce, sidechick, residechick, showsc, convertpanty",
                          inline=False)
            emb.add_field(name='Moderation(Not fully functional yet)',
                          value="avatar(av), userinfo, roleall, slowmode, serverinfo, purge", inline=False)
            em.add_field(name="RPG Commands(Early Alpha Testing)",
                     value="start, hunt, stats, upgrade str, upgrade int, upgrade agi, reset, job, mine, fish, craft, inventory, equip, sell", inline=False)
            emb.set_footer(text="$nsfw for NSFW command list")
            try:
                msg = await ctx.send('**Trying to send info in DMs...($help nsfw or $nsfw for nsfw command list)**')
                await user.send(embed=em)
                await asyncio.sleep(10)
                await msg.delete()
            except Exception:
                await ctx.send(embed=emb)

    @help.command(name="dab")
    async def _dab(self, ctx):
        embed = discord.Embed(description=f"**Example use: $dab @User#6969 or $dab**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="morning")
    async def _morning(self, ctx):
        embed = discord.Embed(description=f"**Example use: $gm @User#6969 or $gm**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="goodnight")
    async def _goodnight(self, ctx):
        embed = discord.Embed(description=f"**Example use: $gn @User#6969 or $gn**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="ping")
    async def _ping(self, ctx):
        embed = discord.Embed(description=f"**Example use: $ping**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="hug")
    async def _hug(self, ctx):
        embed = discord.Embed(description=f"**Example use: $hug @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="cuddle")
    async def _cuddle(self, ctx):
        embed = discord.Embed(description=f"**Example use: $cuddle @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="kiss")
    async def _kiss(self, ctx):
        embed = discord.Embed(
            description=f"**It gives different gifs on NSFW Channels\nExample use: $kiss @User#6969**",
            colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="pat")
    async def _pat(self, ctx):
        embed = discord.Embed(description=f"**Example use: $pat @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="smile")
    async def _smile(self, ctx):
        embed = discord.Embed(description=f"**Example use: $smile @User#6969 or $smile**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="kill")
    async def _kill(self, ctx):
        embed = discord.Embed(description=f"**Example use: $kill @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="fistbump")
    async def _fistbump(self, ctx):
        embed = discord.Embed(description=f"**Example use: $fistbump @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="bunny")
    async def _bunny(self, ctx):
        embed = discord.Embed(description=f"**Example use: $bunny**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="punch")
    async def _punch(self, ctx):
        embed = discord.Embed(description=f"**Example use: $punch @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="popcorn")
    async def _popcorn(self, ctx):
        embed = discord.Embed(description=f"**Example use: $popcorn @User#6969 or $popcorn**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="goodjob")
    async def _goodjob(self, ctx):
        embed = discord.Embed(description=f"**Example use: $gj @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="weed")
    async def _weed(self, ctx):
        embed = discord.Embed(description=f"**Example use: $weed @User#0420 or $weed**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="gay")
    async def _gay(self, ctx):
        embed = discord.Embed(description=f"**Example use: $gay @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="nap")
    async def _nap(self, ctx):
        embed = discord.Embed(description=f"**Example use: $nap @User#6969 or $nap**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="holdhand")
    async def _holdhand(self, ctx):
        embed = discord.Embed(description=f"**Example use: $holdhand @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="spooky")
    async def _spooky(self, ctx):
        embed = discord.Embed(description=f"**Example use: $spooky @User#6969 or $spooky**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="penis")
    async def _penis(self, ctx):
        embed = discord.Embed(description=f"**Example use: $penis or $penis @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="lewd")
    async def _lewd(self, ctx):
        embed = discord.Embed(description=f"**Example use: $lewd or $lewd @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="nom")
    async def _nom(self, ctx):
        embed = discord.Embed(description=f"**Example use: $nom @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="blowkiss")
    async def _blowkiss(self, ctx):
        embed = discord.Embed(description=f"**Example use: $blowkiss @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="slap")
    async def _slap(self, ctx):
        embed = discord.Embed(description=f"**Example use: $slap @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="poke")
    async def _poke(self, ctx):
        embed = discord.Embed(description=f"**Example use: $poke @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="fu")
    async def _fu(self, ctx):
        embed = discord.Embed(description=f"**Example use: $fu @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="boop")
    async def _boop(self, ctx):
        embed = discord.Embed(description=f"**Example use: $boop @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="grouphug")
    async def _grouphug(self, ctx):
        embed = discord.Embed(description=f"**Example use: $grouphug @User#6969 @User#0420**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="feed")
    async def _feed(self, ctx):
        embed = discord.Embed(description=f"**Example use: $feed @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="suplex")
    async def _suplex(self, ctx):
        embed = discord.Embed(description=f"**Example use: $suplex @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="coffee")
    async def _coffee(self, ctx):
        embed = discord.Embed(description=f"**Example use: $coffee or $coffee @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="rank")
    async def _rank(self, ctx):
        embed = discord.Embed(description=f"**Example use: $rank or $rank @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="levels")
    async def _levels(self, ctx):
        embed = discord.Embed(description=f"**Example use: $lb**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="balance")
    async def _balance(self, ctx):
        embed = discord.Embed(description=f"**Example use: $balance or $bal**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="work")
    async def _work(self, ctx):
        embed = discord.Embed(description=f"**Example use: $work**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="daily")
    async def _daily(self, ctx):
        embed = discord.Embed(description=f"**Example use: $daily**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="rep")
    async def _rep(self, ctx):
        embed = discord.Embed(description=f"**Example use: $rep @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="profile")
    async def _profile(self, ctx):
        embed = discord.Embed(description=f"**Example use: $profile or $profile @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="refresh")
    async def _refresh(self, ctx):
        embed = discord.Embed(description=f"**Example use: $refresh (use only if your name in leaderboard is old)**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="token")
    async def _token(self, ctx):
        embed = discord.Embed(description=f"**Gambling currency\nExample use: $token**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="gamble")
    async def _gamble(self, ctx):
        embed = discord.Embed(description=f"**Be careful its risky\nExample use: $gamble (amount)**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="pantyboard")
    async def _pantyboard(self, ctx):
        embed = discord.Embed(description=f"**Example use: $pb or $pantyboard**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="marry")
    async def _marry(self, ctx):
        embed = discord.Embed(description=f"**Other side has to say yes\nExample use: $marry @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="divorce")
    async def _divorce(self, ctx):
        embed = discord.Embed(description=f"**Example use: $divorce @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="sidechick")
    async def _sidechick(self, ctx):
        embed = discord.Embed(description=f"**Completely experimental and buggy will be fixed later**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="residechick")
    async def _residechick(self, ctx):
        embed = discord.Embed(description=f"**Completely experimental and buggy will be fixed later**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="convertpanty")
    async def _convertpanty(self, ctx):
        embed = discord.Embed(description=f"**Example use: $cop (amount)**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="avatar")
    async def _avatar(self, ctx):
        embed = discord.Embed(description=f"**Example use: $av or $av @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="userinfo")
    async def _userinfo(self, ctx):
        embed = discord.Embed(description=f"**Example use: $userinfo @User#6969**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="roleall")
    async def _roleall(self, ctx):
        embed = discord.Embed(
            description=f"**It might take a while to give all members role\nExample use: $roleall (role name)**",
            colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="slowmode")
    async def _slowmode(self, ctx):
        embed = discord.Embed(description=f"**Example use: $slowmode 0-120**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="serverinfo")
    async def _serverinfo(self, ctx):
        embed = discord.Embed(description=f"**Example use: $serverinfo**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="purge")
    async def _purge(self, ctx):
        embed = discord.Embed(description=f"**Example use: $purge (amount)**",
                              colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @help.command(name="nsfw")
    async def _nsfw(self, ctx):
        em = discord.Embed(colour=discord.Colour.blue())
        em.set_author(name='Nsfw Command List')
        em.add_field(name='Commands',
                     value="**fuck, spank, suck, anal, dom, 69, creampie, lick, tits, tease, finger, booty," 
                               "bite, massage, cum, collar, twerk, thicc, choke, sub, ride, threesome,"
                                "deepthroat, doggy, facial, brat, porn, hentai, missionary, public,"
                                 "ropeplay(bondage), petplay, whip, punish, swallow, masturbate, titfuck, shower sex**", inline=False)
        await ctx.send(embed=em)

    @help.command(name="rpg")
    async def _rpg(self, ctx):
        em = discord.Embed(colour=discord.Colour.blue())
        em.set_author(name="RPG Command List")
        em.add_field(name="Commands",
                     value="start, hunt, stats, upgrade str, upgrade int, upgrade agi, reset, job, mine, fish, craft, inventory, equip, sell")
        em.set_footer(text="This is Alpha version all data might be reseted")
        await ctx.send(embed=em)
    
    @help.command(name='taco')
    async def _taco(self, ctx):
        embed = discord.Embed(
            description=f"**This is a custom command to buy your own check $patreon\nExample use: $taco @User#6969 or $taco**",
            colour=discord.Colour.blue())
        await ctx.send(embed=embed)

    @commands.command()
    async def invite(self, ctx):
        embed = discord.Embed(title="Click to invite Botaru to your server",
                              url="https://discord.com/api/oauth2/authorize?client_id=489808074929078272&permissions=268827894&redirect_uri=https%3A%2F%2Fdiscordapp.com%2Fapi%2Foauth2%2Fauthorize%3Fclient_id%3D489808074929078272%26permissions%3D8%26scope%3Dbot&scope=bot")
        embed.set_thumbnail(
            url="https://vignette.wikia.nocookie.net/tensei-shitara-slime-datta-ken/images/3/34/Rimuru_Slime_Anime.png/revision/latest?cb=20180922214304")

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))