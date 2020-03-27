import discord
import random
from discord.ext import commands

class Actions(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['gm'])
    async def morning(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.author
            if member == ctx.author:
                author = ctx.message.author.name

                morning = '**{0} says good morning to everyone!**'

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

        elif member:
            author = ctx.message.author.name
            mention = member.name
            morning = '**{0} says good morning to {1}!**'

            choices = ['https://media.giphy.com/media/h2ZVjT3kt193cxnwm1/giphy.gif',
                       'https://media.giphy.com/media/3ohc0SH8Y6TJvc2FMI/giphy.gif',
                       'https://media.giphy.com/media/1xm0bJZjPrXaF74GKP/giphy.gif',
                       'https://media.giphy.com/media/QF8BVLZX6LCWk/giphy.gif',
                       'https://media.giphy.com/media/d3erWmTEGXoiYVgY/giphy.gif',
                       'https://media.giphy.com/media/3oKIPmZqRXPAxenD3y/giphy.gif',
                       'https://media.giphy.com/media/l2JeckYqVLzKM5CJG/giphy.gif',
                       'https://media.giphy.com/media/3ohhwHZXd5AQ3U08bm/giphy.gif']

            image = random.choice(choices)

            embed = discord.Embed(description=morning.format(author, mention), colour=discord.Colour.blue())
            embed.set_image(url=image)

            await ctx.send(embed=embed)


    @commands.command(aliases = ['gn'])
    async def goodnight(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.author
            if member == ctx.author:
                author = ctx.message.author.name

                goodnight = '**{0} says goodnight to everyone**'

                choices = ['https://media.giphy.com/media/OjmrBW4ZQbWjkq6RkC/giphy.gif',
                   'https://media.giphy.com/media/3o6fJ5LANL0x31R1Ic/giphy.gif',
                   'https://media.giphy.com/media/qof7GwPnu4zbG/giphy.gif',
                   'https://media.giphy.com/media/3o6ozrsVQF6Fv1ljNe/giphy.gif',
                   'https://media.giphy.com/media/3oEdv5XT0tYl7B77yM/giphy.gif',
                   'https://media.giphy.com/media/l2Sq5ju2l1nNeOr4I/giphy.gif',
                   'https://media.giphy.com/media/VtlWK4InL33ck/giphy.gif'
                   ]

                image = random.choice(choices)

                embed = discord.Embed(description=goodnight.format(author), colour=discord.Colour.blue())
                embed.set_image(url=image)

                await ctx.send(embed=embed)

        elif member:
            author = ctx.message.author.name
            mention = member.name
            goodnight = '**{0} says goodnight to {1}**'

            choices = ['https://media.giphy.com/media/OjmrBW4ZQbWjkq6RkC/giphy.gif',
                   'https://media.giphy.com/media/3o6fJ5LANL0x31R1Ic/giphy.gif',
                   'https://media.giphy.com/media/qof7GwPnu4zbG/giphy.gif',
                   'https://media.giphy.com/media/3o6ozrsVQF6Fv1ljNe/giphy.gif',
                   'https://media.giphy.com/media/3oEdv5XT0tYl7B77yM/giphy.gif',
                   'https://media.giphy.com/media/l2Sq5ju2l1nNeOr4I/giphy.gif',
                   'https://media.giphy.com/media/VtlWK4InL33ck/giphy.gif'
                   ]

            image = random.choice(choices)

            embed = discord.Embed(description=goodnight.format(author, mention), colour=discord.Colour.blue())
            embed.set_image(url=image)

            await ctx.send(embed=embed)

    @commands.command()
    async def happybirthday(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
            if member == ctx.author:
                author = ctx.message.author.name

                hbd = "Happy birthday to you hoe!"

                choices = ['https://media1.giphy.com/media/RiOzBjWEl7cYM/source.gif',
                           '']


def setup(client):
    client.add_cog(Actions(client))