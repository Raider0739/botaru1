import discord
from discord.ext import commands

"""class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):

        embed = discord.Embed(colour=ctx.author.color, timestamp=ctx.message.created_at)

        embed.set_author(name='Help', icon_url=ctx.author.avatar_url)
        embed.add_field(name='Fun Commands', value='ping, hug, kiss, cuddle, pat, smile, gay, nap, holdhand')
        embed.add_field(name='Actions', value='morning(gm), goodnight(gn)')
        embed.add_field(name='Moderation', value='purge, kick, ban')
        embed.add_field(name='User', value='avatar(av), userinfo')
        embed.add_field(name='NSFW', value='fuck')

        await ctx.send(embed=embed)"""




def setup(client):
    client.add_cog(Help(client))