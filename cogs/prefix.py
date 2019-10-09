import discord
from discord.ext import commands
import json


class Prefix(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.is_owner()
    async def prefix(self, ctx, *, pre):
        with open(r"C:\Users\utku1utku\Desktop\discord1\prefixes.json", 'r') as f:
            prefixes = json.load(f)

        prefixes[str(ctx.guild.id)] = pre
        await ctx.send(f"**New prefix is '{pre}'**")

        with open(r"C:\Users\utku1utku\Desktop\discord1\prefixes.json", 'w') as f:
            json.dump(prefixes, f, indent=4)


def setup(client):
    client.add_cog(Prefix(client))