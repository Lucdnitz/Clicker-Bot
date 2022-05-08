import discord
from discord.ext import commands
import os
import sqlite3

class Desativadocreate(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def create(self,ctx):
        embed=discord.Embed(description="Command disabled for maintenance.", colour=discord.Colour.orange())
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(Desativadocreate(client))