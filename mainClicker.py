import discord as disc
import os
from discord.ext import commands

bot = commands.Bot(command_prefix='c!', help_command=None)

@bot.command()
async def load(ctx, extension):
    if ctx.message.author.id == 164390451045072896:
        bot.unload_extension(f'cogs.Desativado{extension}')
        bot.load_extension(f'cogs.{extension}')
        embed=disc.Embed(description=f"Ativado a extensão {extension} com sucesso.", colour=disc.Colour.orange())
        await ctx.send(embed=embed)
    else:
        embed=disc.Embed(description="Permissão insuficiente.", colour=disc.Colour.orange())
        await ctx.send(embed=embed)

        
@bot.command()
async def unload(ctx, extension):
    if ctx.message.author.id == 164390451045072896:
        bot.unload_extension(f'cogs.{extension}')
        bot.load_extension(f'cogs.Desativado{extension}')
        embed=disc.Embed(description=f"Desativado a extensão {extension} com sucesso.", colour=disc.Colour.orange())
        await ctx.send(embed=embed)
    else:
        embed=disc.Embed(description="Permissão insuficiente.", colour=disc.Colour.orange())
        await ctx.send(embed=embed)


@bot.command()
async def help(context):
    embed= disc.Embed(title="Help Command", colour=disc.Colour.orange())
    embed.add_field(name="Clicker Commands\n", value="c!create - creates a clicker profile\nc!start - starts the clicker.\nc!stop - stops the clicker.\nc!shop - open the shop.\nc!buy <number> - buys a building.\nc!rank - shows the ranking.\nc!upgrade - shows the upgrades.\nc!upgrade <number> - buys an upgrade.\nc!claim - it doubles your money by using your vote."
    , inline=False)
    await context.send(embed=embed)

for filename in os.listdir('./cogs'):
    if filename.endswith('.py') and 'Desativado' not in filename:
        bot.load_extension(f'cogs.{filename[:-3]}')



bot.run('OTA2NjQwMDY0NDIxOTg2MzA3.YYbkWw.detduVXdzHqXjwHLq0JdkyK9IeI')
