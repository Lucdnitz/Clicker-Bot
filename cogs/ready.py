import discord
from discord.ext import commands
from os import listdir
from os.path import isfile, join
import sqlite3

class ready(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot está pronto")
        await self.client.change_presence(activity=discord.Game('c!help'))
    
    @commands.command()
    async def guilds(self, ctx):
        if ctx.message.author.id == 164390451045072896:
            embed=discord.Embed(description=f"O bot está em {len(self.client.guilds)} servidores.", colour=discord.Colour.orange())
            await ctx.send(embed=embed)
    
    @commands.command()
    async def stopAll(self,ctx):
        if ctx.message.author.id == 164390451045072896:
            onlyfiles = [f for f in listdir('./db') if isfile(join('./db', f)) and f not in ['clicker.sqlite', 'upgrade.sqlite']]
            for i in onlyfiles:
                db = sqlite3.connect(f'./db/{i}')
                cursor = db.cursor()
                cursor.execute("SELECT clicker FROM main")
                clickerOn=int(str(cursor.fetchone())[1:-2])
                cursor.execute("SELECT money FROM main")
                money=int(str(cursor.fetchone())[1:-2])
                if clickerOn == 1:
                    cursor.execute("UPDATE main SET clicker = (?)", (0,))
                db.commit()
                cursor.close()
                db.close()

                db = sqlite3.connect(f'./db/clicker.sqlite')
                cursor = db.cursor()
                cursor.execute("UPDATE rank SET money = (?) WHERE user = (?)", (money,i[:-7]))
                db.commit()
                cursor.close()
                db.close()

            embed=discord.Embed(description="Todos os clickers foram parados.", colour=discord.Colour.orange())
            await ctx.send(embed=embed)

    @commands.command()
    async def insert(self,ctx):
        if ctx.message.author.id == 164390451045072896:
            db = sqlite3.connect('./db/upgrade.sqlite')
            cursor = db.cursor()
            cursor.executescript('''
            PRAGMA foreign_keys = 0;

            CREATE TABLE sqlitestudio_temp_table AS SELECT *
                                                    FROM main;

            DROP TABLE main;

            CREATE TABLE main (
                user      STRING,
                timer     INT,
                newspaper INT,
                icecream  INT,
                clothing  INT,
                factory   INT
            );

            INSERT INTO main (
                                user,
                                timer,
                                newspaper,
                                icecream,
                                clothing
                            )
                            SELECT user,
                                    timer,
                                    newspaper,
                                    icecream,
                                    clothing
                            FROM sqlitestudio_temp_table;

            DROP TABLE sqlitestudio_temp_table;

            PRAGMA foreign_keys = 1;
            ''')

            onlyfiles = [f for f in listdir('./db') if isfile(join('./db', f)) and f not in ['clicker.sqlite', 'upgrade.sqlite']]
            for i in onlyfiles:
                cursor.execute("UPDATE main SET factory = (?) WHERE user = (?)", (int(1), i[:-7]))
            db.commit()
            cursor.close()
            db.close()

            db = sqlite3.connect('./db/clicker.sqlite')
            cursor = db.cursor()
            cursor.executescript('''
            PRAGMA foreign_keys = 0;

            CREATE TABLE sqlitestudio_temp_table AS SELECT *
                                                    FROM shop;

            DROP TABLE shop;

            CREATE TABLE shop (
                user      STRING,
                newspaper INT,
                icecream  INT,
                clothing  INT,
                factory   INT
            );

            INSERT INTO shop (
                                user,
                                newspaper,
                                icecream,
                                clothing
                            )
                            SELECT user,
                                    newspaper,
                                    icecream,
                                    clothing
                            FROM sqlitestudio_temp_table;

            DROP TABLE sqlitestudio_temp_table;

            PRAGMA foreign_keys = 1;
            ''')

            for i in onlyfiles:
                cursor.execute("UPDATE shop SET factory = (?) WHERE user = (?)", (int(0), i[:-7]))
            db.commit()
            cursor.close()
            db.close()

            embed=discord.Embed(description='Inserido com sucesso', colour=discord.Colour.orange())
            await ctx.send(embed=embed)




def setup(client):
    client.add_cog(ready(client))