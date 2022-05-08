import discord
from discord.ext import commands
import sqlite3
import asyncio
from discord.utils import get
from discord_components import *
import discord_components
import os


class clicker(commands.Cog):

    def __init__(self, client):
        self.client = client



    @commands.command()
    async def start(self,ctx):
        if os.path.exists(f'./db/{ctx.message.author.id}.sqlite') == True:
            embed=discord.Embed(description='Creating the clicker...', colour=discord.Colour.orange())
            msg = await ctx.send(embed=embed)
            await asyncio.sleep(1.5)
            ddb=DiscordComponents(self.client)
            db = sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
            cursor = db.cursor()
            cursor.execute("SELECT clicker FROM main")
            clickerOn=int(str(cursor.fetchone())[1:-2])
            cursor.close()
            db.close()
            if clickerOn==0:
                db = sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
                cursor = db.cursor()
                cursor.execute("SELECT seg FROM main")
                seg = int(str(cursor.fetchone())[1:-2])
                cursor.execute("SELECT money FROM main")
                money = int(str(cursor.fetchone())[1:-2])
                cursor.execute("UPDATE main SET clicker = (?)", (1,))
                db.commit()
                cursor.close()
                db.close()

                async def clickerGame(msg):
                    try:
                        db = sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
                        cursor = db.cursor()
                        cursor.execute("SELECT clicker FROM main")
                        clickerOn = int(str(cursor.fetchone())[1:-2])
                        cursor.close()
                        db.close()
                        while clickerOn:
                            await asyncio.sleep(1)
                            db = sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
                            cursor = db.cursor()
                            cursor.execute("SELECT clicker FROM main")
                            clickerOn = int(str(cursor.fetchone())[1:-2])
                            cursor.execute("SELECT seg FROM main")
                            seg = int(str(cursor.fetchone())[1:-2])
                            cursor.close()
                            db.close()
                            if clickerOn:
                                try:
                                    db = sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
                                    cursor = db.cursor()
                                    cursor.execute("SELECT money FROM main")
                                    money = int(str(cursor.fetchone())[1:-2])
                                    cursor.execute("UPDATE main SET money = (?)", (money+seg,))
                                    db.commit()
                                    cursor.close()
                                    db.close()
                                    embed=discord.Embed(title=f"{str(ctx.message.author)[:-5]}'s Clicker", colour=discord.Colour.orange())
                                    embed.add_field(name="Money\n", value=f"{money+seg}", inline=False)
                                    embed.add_field(name="Money per second\n", value=f"{seg}", inline=False)
                                    await msg.edit(embed=embed)
                                except:
                                    pass
                    except:
                        pass
            

                embed=discord.Embed(title=f"{str(ctx.message.author)[:-5]}'s Clicker", colour=discord.Colour.orange())
                embed.add_field(name="Money\n", value=f"{money}", inline=False)
                embed.add_field(name="Money per second\n", value=f"{seg}", inline=False)

                await msg.edit(embed=embed, components=[Button(style=discord_components.ButtonStyle.green, label='Click')])
                self.client.loop.create_task(clickerGame(msg))
                
                def click():
                    db = sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
                    cursor = db.cursor()
                    cursor.execute("SELECT clicker FROM main")
                    clickerOn = int(str(cursor.fetchone())[1:-2])
                    cursor.execute("SELECT click FROM main")
                    click = int(str(cursor.fetchone())[1:-2])
                    cursor.close()
                    db.close()
                    if clickerOn==1:
                        db = sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
                        cursor = db.cursor()
                        cursor.execute("SELECT money FROM main")
                        money = int(str(cursor.fetchone())[1:-2])
                        money+=click
                        cursor.execute("UPDATE main SET money = (?)", (money,))
                        db.commit()
                        cursor.close()
                        db.close()
                
                db = sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
                cursor = db.cursor()
                cursor.execute("SELECT clicker FROM main")
                clickerOn = cursor.fetchone()
                cursor.close()
                db.close()
                if clickerOn is not None:
                    clickerOn = int(str(clickerOn)[1:-2])

                db = sqlite3.connect('./db/upgrade.sqlite')
                cursor = db.cursor()
                cursor.execute("SELECT timer FROM main WHERE user = (?)", (ctx.message.author.id, ))
                timer = int(str(cursor.fetchone())[1:-2])
                timer = float(10*(timer+1))
                cursor.close()
                db.close()

                def check(res):
                    return (res.user.id != self.client.user.id) and (res.user == ctx.message.author)
                while True:
                    db = sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
                    cursor = db.cursor()
                    cursor.execute("SELECT clicker FROM main")
                    clickerOn = cursor.fetchone()
                    cursor.close()
                    db.close()
                    if clickerOn is not None:
                        clickerOn = int(str(clickerOn)[1:-2])
                    try:
                        res = await self.client.wait_for('button_click', timeout=timer, check=check)
                    except asyncio.TimeoutError:
                        try:
                            db = sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
                            cursor = db.cursor()
                            cursor.execute('SELECT money FROM main')
                            money=int(str(cursor.fetchone())[1:-2])
                            cursor.execute("SELECT clicker FROM main")
                            clickerOn=int(str(cursor.fetchone())[1:-2])
                            if clickerOn==1:
                                cursor.execute("UPDATE main SET clicker = (?)", (0,))
                                await msg.delete()
                                embed=discord.Embed(description=f"{str(ctx.message.author)[:-5]}'s Clicker finished.", colour=discord.Colour.orange())
                                await ctx.send(embed=embed)
                            db.commit()
                            cursor.close()
                            db.close()
                            db = sqlite3.connect(f'./db/clicker.sqlite')
                            cursor = db.cursor()
                            cursor.execute("UPDATE rank SET money = (?) WHERE user = (?)", (money,ctx.message.author.id))
                            db.commit()
                            cursor.close()
                            db.close()
                        except:
                            db = sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
                            cursor = db.cursor()
                            cursor.execute('SELECT money FROM main')
                            money=int(str(cursor.fetchone())[1:-2])
                            cursor.execute("SELECT clicker FROM main")
                            clickerOn=int(str(cursor.fetchone())[1:-2])
                            if clickerOn==1:
                                cursor.execute("UPDATE main SET clicker = (?)", (0,))
                                await msg.delete()
                                embed=discord.Embed(description=f"{str(ctx.message.author)[:-5]}'s Clicker finished.", colour=discord.Colour.orange())
                                await ctx.send(embed=embed)
                            db.commit()
                            cursor.close()
                            db.close()
                            db = sqlite3.connect(f'./db/clicker.sqlite')
                            cursor = db.cursor()
                            cursor.execute("UPDATE rank SET money = (?) WHERE user = (?)", (money,ctx.message.author.id))
                            db.commit()
                            cursor.close()
                            db.close()
                        break
                    if res.author==ctx.message.author:
                        try:
                            await res.respond(content='Clicking...', type=7)
                            click()
                        except:
                            await msg.delete()
                            embed=discord.Embed(description="An error has occurred. Please, restart your clicker later.", colour=discord.Colour.orange())
                            await ctx.send(embed=embed)
                            db = sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
                            cursor = db.cursor()
                            cursor.execute("SELECT clicker FROM main")
                            clickerOn=int(str(cursor.fetchone())[1:-2])
                            if clickerOn==1:
                                cursor.execute("UPDATE main SET clicker = (?)", (0,))
                            db.commit()
                            cursor.close()
                            db.close()
                            break
            else:
                embed=discord.Embed(description="Clicker already started.", colour=discord.Colour.orange())   
                await msg.edit(embed=embed)
        else:
            embed=discord.Embed(description="Clicker profile doesn't exist.", colour=discord.Colour.orange())   
            await ctx.send(embed=embed)

    @commands.command()
    async def stop(self,ctx):
        try:
            db = sqlite3.connect(f'./db/{ctx.message.author.id}.sqlite')
            cursor = db.cursor()
            cursor.execute("SELECT clicker FROM main")
            clickerOn=int(str(cursor.fetchone())[1:-2])
            cursor.execute("SELECT money FROM main")
            money=int(str(cursor.fetchone())[1:-2])
            if clickerOn is None or clickerOn ==0:
                embed=discord.Embed(description="There is no clicker running", colour=discord.Colour.orange())
                await ctx.send(embed=embed)
            else:
                cursor.execute("UPDATE main SET clicker = (?)", (0,))
                embed=discord.Embed(description=f"{str(ctx.message.author)[:-5]}'s Clicker finished.", colour=discord.Colour.orange())
                await ctx.send(embed=embed)
            db.commit()
            cursor.close()
            db.close()

            db = sqlite3.connect(f'./db/clicker.sqlite')
            cursor = db.cursor()
            cursor.execute("UPDATE rank SET money = (?) WHERE user = (?)", (money,ctx.message.author.id))
            db.commit()
            cursor.close()
            db.close()

        except:
            embed=discord.Embed(description=f"{str(ctx.message.author)[:-5]}'s Clicker finished.")
            await ctx.send(embed=embed)

    @commands.command()
    async def rank(self, ctx):
        try:
            db = sqlite3.connect('./db/clicker.sqlite')
            cursor = db.cursor()
            cursor.execute("SELECT user FROM rank ORDER BY money DESC")
            users = cursor.fetchall()
            cursor.execute("SELECT money FROM rank ORDER BY money DESC")
            qtd = cursor.fetchall()
            pages=[]
            rang = 1
            for i in range(rang):
                page=discord.Embed(
                    title = f'Page {i+1}',
                    description= f'Ranking list:',
                    colour=discord.Colour.orange()
                  )
                try:
                  for j in range(5):
                      user = await self.client.fetch_user(int(str(users[5*i+j])[1:-2]))
                      page.add_field(name=f'{5*i+j+1}. {str(user)[:-5]}',value=f"{str(qtd[5*i+j])[1:-2]} money.", inline=False)
                except:
                  pass
                pages.append(page)
            if len(pages)<1:
              embed=discord.Embed(description=f"There is nobody on the ranking.", colour=discord.Colour.orange())
              await ctx.send(embed=embed)
            else:
              msg=await ctx.send(embed=pages[0])

            
        except:
            pass
        cursor.close()
        db.close()


def setup(client):
    client.add_cog(clicker(client))
