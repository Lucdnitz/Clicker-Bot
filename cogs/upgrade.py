import discord
from discord.ext import commands
import os
import sqlite3

class upgrade(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.group()
    async def upgrade(self,ctx):
        if ctx.invoked_subcommand is None:
            db= sqlite3.connect('./db/upgrade.sqlite')
            cursor = db.cursor()
            cursor.execute("SELECT timer FROM main WHERE user = (?)", (str(ctx.message.author.id),))
            timer = int(str(cursor.fetchone())[1:-2])
            cursor.execute("SELECT newspaper FROM main WHERE user = (?)", (str(ctx.message.author.id),))
            newspaper = int(str(cursor.fetchone())[1:-2])
            cursor.execute("SELECT icecream FROM main WHERE user = (?)", (str(ctx.message.author.id),))
            icecream = int(str(cursor.fetchone())[1:-2])
            cursor.execute("SELECT clothing FROM main WHERE user = (?)", (str(ctx.message.author.id),))
            clothing = int(str(cursor.fetchone())[1:-2])
            cursor.execute("SELECT factory FROM main WHERE user = (?)", (str(ctx.message.author.id),))
            factory = int(str(cursor.fetchone())[1:-2])
            db.commit()
            cursor.close()
            db.close()
            Pfactory = int(691200*(1.9**(factory-1)))
            Pclothing = int(72000*(1.9**(clothing-1)))
            Picecream = int(7500*(1.9**(icecream-1)))
            Pnewspaper = int(500*(1.9**(newspaper-1)))
            Ptimer = int(500*(1.8**timer))

            db= sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
            cursor = db.cursor()
            cursor.execute("SELECT click FROM main")
            click = int(str(cursor.fetchone())[1:-2])
            cursor.close()
            db.close()
            Pclick=int(20*(1.4**(click-1)))

            embed=discord.Embed(title="Clicker Shop", colour=discord.Colour.orange())
            embed.add_field(name=f'1. Timer - {Ptimer} money', value=f'+10 seconds ({10*(timer+1)} seconds on total)', inline=False)
            embed.add_field(name=f'2. Money per click - {Pclick} money', value=f'+1 money per click ({click} money per click on total)', inline=False)
            embed.add_field(name=f'3. Newspaper stand - {Pnewspaper} money', value=f'+100% production ({newspaper*100}% production on total)', inline=False)
            embed.add_field(name=f'4. Ice cream truck - {Picecream} money', value=f'+100% production ({icecream*100}% production on total)', inline=False)
            embed.add_field(name=f'5. Clothing store - {Pclothing} money', value=f'+100% production ({clothing*100}% production on total)', inline=False)
            embed.add_field(name=f'6. Factory - {Pfactory} money', value=f'+100% production ({factory*100}% production on total)', inline=False)
            await ctx.send(embed=embed)


    @upgrade.command(aliases=['1'])
    async def _1(self,ctx):
        db= sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT money FROM main")
        money = int(str(cursor.fetchone())[1:-2])
        cursor.close()
        db.close()

        db= sqlite3.connect('./db/upgrade.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT timer FROM main WHERE user = (?)", (str(ctx.message.author.id),))
        timer = int(str(cursor.fetchone())[1:-2])
        cursor.close()
        db.close()
        Ptimer=int(500*(1.8**timer))

        if money>=Ptimer:
            db = sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
            cursor = db.cursor()
            money -= Ptimer
            timer+=1
            cursor.execute("UPDATE main SET money = (?)", (money,))
            db.commit()
            cursor.close()
            db.close()

            db= sqlite3.connect('./db/upgrade.sqlite')
            cursor = db.cursor()
            cursor.execute("UPDATE main SET timer = (?) WHERE user = (?)", (timer,str(ctx.message.author.id)))
            db.commit()
            cursor.close()
            db.close()
            embed=discord.Embed(description="You purchased 1 timer upgrade.", colour=discord.Colour.orange())
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(description="Insufficient money.", colour=discord.Colour.orange())
            await ctx.send(embed=embed)

    @upgrade.command(aliases=['2'])
    async def _2(self,ctx):
        db= sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT money FROM main")
        money = int(str(cursor.fetchone())[1:-2])
        cursor.close()
        db.close()

        db= sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT click FROM main")
        click = int(str(cursor.fetchone())[1:-2])
        cursor.close()
        db.close()
        Pclick=int(20*(1.4**(click-1)))

        if money>=Pclick:
            db = sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
            cursor = db.cursor()
            money -= Pclick
            click+=1
            cursor.execute("UPDATE main SET money = (?)", (money,))
            db.commit()
            cursor.close()
            db.close()

            db= sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
            cursor = db.cursor()
            cursor.execute("UPDATE main SET click = (?)", (click, ))
            db.commit()
            cursor.close()
            db.close()
            embed=discord.Embed(description="You purchased 1 click upgrade.", colour=discord.Colour.orange())
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(description="Insufficient money.", colour=discord.Colour.orange())
            await ctx.send(embed=embed)

    @upgrade.command(aliases=['3'])
    async def _3(self,ctx):
        db= sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT money FROM main")
        money = int(str(cursor.fetchone())[1:-2])
        cursor.execute("SELECT seg FROM main")
        seg = int(str(cursor.fetchone())[1:-2])
        cursor.close()
        db.close()

        db= sqlite3.connect('./db/upgrade.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT newspaper FROM main WHERE user = (?)", (ctx.message.author.id, ))
        newspaper = int(str(cursor.fetchone())[1:-2])
        cursor.close()
        db.close()
        Pnewspaper=int(500*(1.9**(newspaper-1)))

        if money>=Pnewspaper:
            db= sqlite3.connect('./db/clicker.sqlite')
            cursor = db.cursor()
            cursor.execute("SELECT newspaper FROM shop WHERE user = (?)", (ctx.message.author.id, ))
            newspaperShop = int(str(cursor.fetchone())[1:-2])
            cursor.close()
            db.close()
            print(newspaperShop)
            db = sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
            cursor = db.cursor()
            money -= Pnewspaper
            newspaper+=1
            cursor.execute("UPDATE main SET money = (?)", (money,))
            cursor.execute("UPDATE main SET seg = (?)", (seg+newspaperShop,))
            db.commit()
            cursor.close()
            db.close()

            db= sqlite3.connect('./db/upgrade.sqlite')
            cursor = db.cursor()
            cursor.execute("UPDATE main SET newspaper = (?) WHERE user = (?)", (newspaper, ctx.message.author.id))
            db.commit()
            cursor.close()
            db.close()



            embed=discord.Embed(description="You purchased 1 newspaper stand upgrade.", colour=discord.Colour.orange())
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(description="Insufficient money.", colour=discord.Colour.orange())
            await ctx.send(embed=embed)
        
    @upgrade.command(aliases=['4'])
    async def _4(self,ctx):
        db= sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT money FROM main")
        money = int(str(cursor.fetchone())[1:-2])
        cursor.execute("SELECT seg FROM main")
        seg = int(str(cursor.fetchone())[1:-2])
        cursor.close()
        db.close()

        db= sqlite3.connect('./db/upgrade.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT icecream FROM main WHERE user = (?)", (ctx.message.author.id, ))
        icecream = int(str(cursor.fetchone())[1:-2])
        cursor.close()
        db.close()
        Picecream=int(7500*(1.9**(icecream-1)))

        if money>=Picecream:
            db= sqlite3.connect('./db/clicker.sqlite')
            cursor = db.cursor()
            cursor.execute("SELECT icecream FROM shop WHERE user = (?)", (ctx.message.author.id, ))
            icecreamShop = int(str(cursor.fetchone())[1:-2])
            cursor.close()
            db.close()
            db = sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
            cursor = db.cursor()
            money -= Picecream
            icecream+=1
            cursor.execute("UPDATE main SET money = (?)", (money,))
            cursor.execute("UPDATE main SET seg = (?)", (seg+(icecreamShop*5),))
            db.commit()
            cursor.close()
            db.close()

            db= sqlite3.connect('./db/upgrade.sqlite')
            cursor = db.cursor()
            cursor.execute("UPDATE main SET icecream = (?) WHERE user = (?)", (icecream, ctx.message.author.id))
            db.commit()
            cursor.close()
            db.close()



            embed=discord.Embed(description="You purchased 1 icecream stand upgrade.", colour=discord.Colour.orange())
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(description="Insufficient money.", colour=discord.Colour.orange())
            await ctx.send(embed=embed)
    

    @upgrade.command(aliases=['5'])
    async def _5(self,ctx):
        db= sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT money FROM main")
        money = int(str(cursor.fetchone())[1:-2])
        cursor.execute("SELECT seg FROM main")
        seg = int(str(cursor.fetchone())[1:-2])
        cursor.close()
        db.close()

        db= sqlite3.connect('./db/upgrade.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT clothing FROM main WHERE user = (?)", (ctx.message.author.id, ))
        clothing = int(str(cursor.fetchone())[1:-2])
        cursor.close()
        db.close()
        Pclothing=int(72000*(1.9**(clothing-1)))

        if money>=Pclothing:
            db= sqlite3.connect('./db/clicker.sqlite')
            cursor = db.cursor()
            cursor.execute("SELECT clothing FROM shop WHERE user = (?)", (ctx.message.author.id, ))
            clothingShop = int(str(cursor.fetchone())[1:-2])
            cursor.close()
            db.close()
            db = sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
            cursor = db.cursor()
            money -= Pclothing
            clothing+=1
            cursor.execute("UPDATE main SET money = (?)", (money,))
            cursor.execute("UPDATE main SET seg = (?)", (seg+(clothingShop*25),))
            db.commit()
            cursor.close()
            db.close()

            db= sqlite3.connect('./db/upgrade.sqlite')
            cursor = db.cursor()
            cursor.execute("UPDATE main SET clothing = (?) WHERE user = (?)", (clothing, ctx.message.author.id))
            db.commit()
            cursor.close()
            db.close()



            embed=discord.Embed(description="You purchased 1 clothing store upgrade.", colour=discord.Colour.orange())
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(description="Insufficient money.", colour=discord.Colour.orange())
            await ctx.send(embed=embed)

    @upgrade.command(aliases=['6'])
    async def _6(self,ctx):
        db= sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT money FROM main")
        money = int(str(cursor.fetchone())[1:-2])
        cursor.execute("SELECT seg FROM main")
        seg = int(str(cursor.fetchone())[1:-2])
        cursor.close()
        db.close()

        db= sqlite3.connect('./db/upgrade.sqlite')
        cursor = db.cursor()
        cursor.execute("SELECT factory FROM main WHERE user = (?)", (ctx.message.author.id, ))
        factory = int(str(cursor.fetchone())[1:-2])
        cursor.close()
        db.close()
        Pfactory=int(691200*(1.9**(factory-1)))

        if money>=Pfactory:
            db= sqlite3.connect('./db/clicker.sqlite')
            cursor = db.cursor()
            cursor.execute("SELECT factory FROM shop WHERE user = (?)", (ctx.message.author.id, ))
            factoryShop = int(str(cursor.fetchone())[1:-2])
            cursor.close()
            db.close()
            db = sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
            cursor = db.cursor()
            money -= Pfactory
            factory+=1
            cursor.execute("UPDATE main SET money = (?)", (money,))
            cursor.execute("UPDATE main SET seg = (?)", (seg+(factoryShop*100),))
            db.commit()
            cursor.close()
            db.close()

            db= sqlite3.connect('./db/upgrade.sqlite')
            cursor = db.cursor()
            cursor.execute("UPDATE main SET factory = (?) WHERE user = (?)", (factory, ctx.message.author.id))
            db.commit()
            cursor.close()
            db.close()



            embed=discord.Embed(description="You purchased 1 factory upgrade.", colour=discord.Colour.orange())
            await ctx.send(embed=embed)
        else:
            embed=discord.Embed(description="Insufficient money.", colour=discord.Colour.orange())
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(upgrade(client))