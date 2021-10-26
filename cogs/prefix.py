import discord
from discord.ext import commands
import json


class Prefix(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def prefix(self, ctx, *, pre):
        with open(r"prefixes.json", 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = pre
        await ctx.send(f"**New prefix is '{pre}'**")

        with open(r"prefixes.json", 'w') as f:
            json.dump(prefixes, f, indent=4)

    @prefix.error
    async def prefix_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("You need to write an input(My default is $)!")
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("This command is only for the bot Owner which is <@464802706930794496>")

        raise error


def setup(client):
    client.add_cog(Prefix(client))