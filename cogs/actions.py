import discord
import random
from discord.ext import commands

class Actions(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases = ['gm'])
    async def morning(self, ctx):
        """
        Morning gifs (gm)
        """

        author = ctx.message.author.name

        morning = '{0} says good morning to everyone!'

        choices = ['https://media.giphy.com/media/h2ZVjT3kt193cxnwm1/giphy.gif',
                   'https://media.giphy.com/media/3ohc0SH8Y6TJvc2FMI/giphy.gif',
                   'https://media.giphy.com/media/1xm0bJZjPrXaF74GKP/giphy.gif',
                   'https://media.giphy.com/media/QF8BVLZX6LCWk/giphy.gif',
                   'https://media.giphy.com/media/d3erWmTEGXoiYVgY/giphy.gif',
                   'https://media.giphy.com/media/3oKIPmZqRXPAxenD3y/giphy.gif',
                   'https://media.giphy.com/media/l2JeckYqVLzKM5CJG/giphy.gif',
                   'https://media.giphy.com/media/3ohhwHZXd5AQ3U08bm/giphy.gif']

        image = random.choice(choices)

        embed = discord.Embed(description=morning.format(author), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await ctx.send(embed=embed)

    @commands.command(aliases = ['gn'])
    async def goodnight(self, ctx):
        """
        Goodnight gifs (gn)
        """

        author = ctx.message.author.name

        goodnight = '{0} says goodnight to everyone'

        choices = ['https://media.giphy.com/media/OjmrBW4ZQbWjkq6RkC/giphy.gif',
                   'https://media.giphy.com/media/3o6fJ5LANL0x31R1Ic/giphy.gif',
                   'https://media.giphy.com/media/qof7GwPnu4zbG/giphy.gif',
                   'https://media.giphy.com/media/3o6ozrsVQF6Fv1ljNe/giphy.gif',
                   'https://media.giphy.com/media/3oEdv5XT0tYl7B77yM/giphy.gif',
                   'https://media.giphy.com/media/l2Sq5ju2l1nNeOr4I/giphy.gif',
                   'https://media.giphy.com/media/VtlWK4InL33ck/giphy.gif',
                   'http://giphygifs.s3.amazonaws.com/media/LlI2llpB2gSCQ/giphy.gif']

        image = random.choice(choices)

        embed = discord.Embed(description=goodnight.format(author), colour=discord.Colour.blue())
        embed.set_image(url=image)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Actions(client))