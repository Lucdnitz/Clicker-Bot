import discord
from discord.ext import commands
import os
import sqlite3

class Desativadoclicker(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def start(self,ctx):
        embed=discord.Embed(description="Command disabled for maintenance.", colour=discord.Colour.orange())
        await ctx.send(embed=embed)

    @commands.command()
    async def stop(self,ctx):
        embed=discord.Embed(description="Command disabled for maintenance.", colour=discord.Colour.orange())
        await ctx.send(embed=embed)
      
    @commands.command()
    async def rank(self, ctx):
        embed=discord.Embed(description="Command disabled for maintenance.", colour=discord.Colour.orange())
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Desativadoclicker(client))