import discord
from discord.ext import commands
import sqlite3


class vote(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def claim(self,ctx):
        try:
            db = sqlite3.connect('//var//www//FlaskApp//FlaskApp//static//vote.sqlite')
            cursor = db.cursor()
            cursor.execute("SELECT qtd FROM main WHERE user = (?)", (str(ctx.message.author.id),))
            vote = int(str(cursor.fetchone())[1:-2])
            cursor.close()
            db.close()
            if vote>0:
                db = sqlite3.connect('//var//www//FlaskApp//FlaskApp//static//vote.sqlite')
                cursor = db.cursor()
                cursor.execute("UPDATE main SET qtd = (?) WHERE user = (?)", (vote-1,str(ctx.message.author.id)))
                db.commit()
                cursor.close()
                db.close()

                db= sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
                cursor = db.cursor()
                cursor.execute("SELECT money FROM main")
                money = int(str(cursor.fetchone())[1:-2])
                cursor.execute("UPDATE main SET money = (?)", (money*2,))
                db.commit()
                cursor.close()
                db.close()
                embed=discord.Embed(description='You claimed your vote successfully', colour=discord.Colour.orange())
                await ctx.send(embed=embed)
            else:
                embed=discord.Embed(description="You don't have any vote.\nVote on: https://top.gg/bot/906640064421986307/vote", colour=discord.Colour.orange())
                await ctx.send(embed=embed)
        except:
            embed=discord.Embed(description="You don't have any vote.\nVote on: https://top.gg/bot/906640064421986307/vote", colour=discord.Colour.orange())
            await ctx.send(embed=embed)



def setup(client):
    client.add_cog(vote(client))