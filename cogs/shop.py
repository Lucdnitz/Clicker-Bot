import discord
from discord.ext import commands
import sqlite3


class shop(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def shop(self,ctx):
        db= sqlite3.connect('./db/clicker.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT newspaper FROM shop WHERE user = (?)", (str(ctx.message.author.id),))
        newspaper = int(str(cursor.fetchone())[1:-2])
        cursor.execute("SELECT icecream FROM shop WHERE user = (?)", (str(ctx.message.author.id),))
        icecream = int(str(cursor.fetchone())[1:-2])
        cursor.execute("SELECT clothing FROM shop WHERE user = (?)", (str(ctx.message.author.id),))
        clothing = int(str(cursor.fetchone())[1:-2])
        cursor.execute("SELECT factory FROM shop WHERE user = (?)", (str(ctx.message.author.id),))
        factory = int(str(cursor.fetchone())[1:-2])
        Pnewspaper=int(100*(1.2**newspaper))
        Picecream = int(1500*(1.2**icecream))
        Pclothing=int(14400*(1.2**clothing))
        Pfactory=int(138240*(1.2**factory))
        embed=discord.Embed(title="Clicker Shop", colour=discord.Colour.orange())
        embed.add_field(name=f'1. Newspaper stand - {Pnewspaper} money', value=f'1 money per second ({newspaper} newspaper stands on total)', inline=False)
        embed.add_field(name=f'2. Ice cream truck - {Picecream} money', value=f'5 money per second ({icecream} ice cream trucks on total)', inline=False)
        embed.add_field(name=f'3. Clothing store - {Pclothing} money', value=f'25 money per second ({clothing} clothing stores on total)', inline=False)
        embed.add_field(name=f'4. Factory - {Pfactory} money', value=f'100 money per second ({factory} factories on total)', inline=False)
        await ctx.send(embed=embed)
        db.commit()
        cursor.close()
        db.close()
    
    @commands.group()
    async def buy(self,ctx):
        if ctx.invoked_subcommand is None:
            embed=discord.Embed(description='You have to place a valid number after this command.', colour=discord.Colour.orange())
            await ctx.send(embed=embed)

    @buy.command(aliases=['1'])
    async def _1(self, ctx):
        db= sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT money FROM main")
        money = int(str(cursor.fetchone())[1:-2])
        cursor.close()
        db.close()

        db= sqlite3.connect('./db/clicker.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT newspaper FROM shop WHERE user = (?)", (str(ctx.message.author.id),))
        newspaper = int(str(cursor.fetchone())[1:-2])
        cursor.close()
        db.close()
        Pnewspaper=int(100*(1.20**newspaper))


        if money>=Pnewspaper:
            
            db= sqlite3.connect('./db/upgrade.sqlite')
            cursor = db.cursor()
            cursor.execute("SELECT newspaper FROM main WHERE user = (?)", (str(ctx.message.author.id),))
            newspaperTimes = int(str(cursor.fetchone())[1:-2])
            cursor.close()
            db.close()


            db = sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
            cursor = db.cursor()
            money -= Pnewspaper
            newspaper+=1
            cursor.execute("UPDATE main SET money = (?)", (money,))
            cursor.execute("SELECT seg FROM main")
            seg = int(str(cursor.fetchone())[1:-2])
            cursor.execute("UPDATE main SET seg = (?)", (seg+(1*newspaperTimes),))
            db.commit()
            cursor.close()
            db.close()

            db= sqlite3.connect(f'./db/clicker.sqlite')
            cursor = db.cursor()
            cursor.execute("UPDATE shop SET newspaper = (?) WHERE user = (?)", (newspaper,str(ctx.message.author.id)))
            db.commit()
            cursor.close()
            db.close()
            embed=discord.Embed(description="You purchased 1 newspaper stand.", colour=discord.Colour.orange())
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(description="Insufficient money.", colour=discord.Colour.orange())
            await ctx.send(embed=embed)

    @buy.command(aliases=['2'])
    async def _2(self, ctx):
        db= sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT money FROM main")
        money = int(str(cursor.fetchone())[1:-2])
        cursor.close()
        db.close()

        db= sqlite3.connect('./db/clicker.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT icecream FROM shop WHERE user = (?)", (str(ctx.message.author.id),))
        icecream = int(str(cursor.fetchone())[1:-2])
        cursor.close()
        db.close()
        Picecream=int(1500*(1.20**icecream))

        if money >= Picecream:
            
            db= sqlite3.connect('./db/upgrade.sqlite')
            cursor = db.cursor()
            cursor.execute("SELECT icecream FROM main WHERE user = (?)", (str(ctx.message.author.id),))
            icecreamTimes = int(str(cursor.fetchone())[1:-2])
            cursor.close()
            db.close()


            db= sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
            cursor = db.cursor()
            money -= Picecream
            icecream+=1
            cursor.execute("UPDATE main SET money = (?)", (money,))
            cursor.execute("SELECT seg FROM main")
            seg = int(str(cursor.fetchone())[1:-2])
            cursor.execute("UPDATE main SET seg = (?)", (seg+(5*icecreamTimes),))
            db.commit()
            cursor.close()
            db.close()

                
            db= sqlite3.connect(f'./db/clicker.sqlite')
            cursor = db.cursor()
            cursor.execute("UPDATE shop SET icecream = (?) WHERE user = (?)", (icecream,str(ctx.message.author.id)))
            db.commit()
            cursor.close()
            db.close()
            embed=discord.Embed(description="You purchased 1 ice cream truck.", colour=discord.Colour.orange())
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(description='Insufficient money.', colour=discord.Colour.orange())
            await ctx.send(embed=embed)
    
    @buy.command(aliases=['3'])
    async def _3(self, ctx):
        db= sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT money FROM main")
        money = int(str(cursor.fetchone())[1:-2])
        cursor.close()
        db.close()

        db= sqlite3.connect('./db/clicker.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT clothing FROM shop WHERE user = (?)", (str(ctx.message.author.id),))
        clothing = int(str(cursor.fetchone())[1:-2])
        cursor.close()
        db.close()
        Pclothing=int(14400*(1.20**clothing))

        if money >= Pclothing:
            
            db= sqlite3.connect('./db/upgrade.sqlite')
            cursor = db.cursor()
            cursor.execute("SELECT clothing FROM main WHERE user = (?)", (str(ctx.message.author.id),))
            clothingTimes = int(str(cursor.fetchone())[1:-2])
            cursor.close()
            db.close()


            db= sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
            cursor = db.cursor()
            money -= Pclothing
            clothing+=1
            cursor.execute("UPDATE main SET money = (?)", (money,))
            cursor.execute("SELECT seg FROM main")
            seg = int(str(cursor.fetchone())[1:-2])
            cursor.execute("UPDATE main SET seg = (?)", (seg+(25*clothingTimes),))
            db.commit()
            cursor.close()
            db.close()

                
            db= sqlite3.connect(f'./db/clicker.sqlite')
            cursor = db.cursor()
            cursor.execute("UPDATE shop SET clothing = (?) WHERE user = (?)", (clothing,str(ctx.message.author.id)))
            db.commit()
            cursor.close()
            db.close()
            embed=discord.Embed(description="You purchased 1 clothing store.", colour=discord.Colour.orange())
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(description='Insufficient money.', colour=discord.Colour.orange())
            await ctx.send(embed=embed)
    
    @buy.command(aliases=['4'])
    async def _4(self, ctx):
        db= sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT money FROM main")
        money = int(str(cursor.fetchone())[1:-2])
        cursor.close()
        db.close()

        db= sqlite3.connect('./db/clicker.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT factory FROM shop WHERE user = (?)", (str(ctx.message.author.id),))
        factory = int(str(cursor.fetchone())[1:-2])
        cursor.close()
        db.close()
        Pfactory=int(138240*(1.20**factory))

        if money >= Pfactory:
            
            db= sqlite3.connect('./db/upgrade.sqlite')
            cursor = db.cursor()
            cursor.execute("SELECT factory FROM main WHERE user = (?)", (str(ctx.message.author.id),))
            factoryTimes = int(str(cursor.fetchone())[1:-2])
            cursor.close()
            db.close()


            db= sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
            cursor = db.cursor()
            money -= Pfactory
            factory+=1
            cursor.execute("UPDATE main SET money = (?)", (money,))
            cursor.execute("SELECT seg FROM main")
            seg = int(str(cursor.fetchone())[1:-2])
            cursor.execute("UPDATE main SET seg = (?)", (seg+(100*factoryTimes),))
            db.commit()
            cursor.close()
            db.close()

                
            db= sqlite3.connect(f'./db/clicker.sqlite')
            cursor = db.cursor()
            cursor.execute("UPDATE shop SET factory = (?) WHERE user = (?)", (factory,str(ctx.message.author.id)))
            db.commit()
            cursor.close()
            db.close()
            embed=discord.Embed(description="You purchased 1 factory.", colour=discord.Colour.orange())
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(description='Insufficient money.', colour=discord.Colour.orange())
            await ctx.send(embed=embed)

def setup(client):
    client.add_cog(shop(client))