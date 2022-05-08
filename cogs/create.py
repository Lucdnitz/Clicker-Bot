import discord
from discord.ext import commands
import os
import sqlite3

class create(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def create(self,ctx):
        if os.path.exists(f'./db/{ctx.message.author.id}.sqlite') == False:
            open(f"./db/{ctx.message.author.id}.sqlite", "x")
            db = sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
            cursor = db.cursor()
            cursor.execute('''
            CREATE TABLE main (
                money   INT,
                seg     INT,
                clicker INT,
                click INT
            );
            ''')
            cursor.execute('INSERT INTO main(money,clicker,seg,click) VALUES (?,?,?,?)', (0, 0, 0, 1))
            db.commit()
            cursor.close()
            db.close()

            db = sqlite3.connect('./db/clicker.sqlite')
            cursor = db.cursor()
            cursor.execute('INSERT INTO rank(money,user) VALUES (?,?)', (0,ctx.message.author.id))
            cursor.execute('INSERT INTO shop(icecream,newspaper,clothing,user) VALUES (?,?,?,?)', (0,0,0,ctx.message.author.id))
            db.commit()
            cursor.close()
            db.close()

            db = sqlite3.connect('./db/upgrade.sqlite')
            cursor = db.cursor()
            cursor.execute('INSERT INTO main(timer,user,newspaper,icecream,clothing) VALUES (?,?,?,?,?)', (0,ctx.message.author.id,1,1,1))
            db.commit()
            cursor.close()
            db.close()
            embed=discord.Embed(description='Clicker profile created successfully.', colour=discord.Colour.orange())
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(description='Clicker profile already exists.', colour=discord.Colour.orange())
            await ctx.send(embed=embed)



def setup(client):
    client.add_cog(create(client))