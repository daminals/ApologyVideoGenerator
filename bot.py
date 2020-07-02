# bot.py
# Handles discord bot functionality
# Daniel Kogan, 06/01/2020

import os, sys
import discord, random, asyncio
from dotenv import load_dotenv

load_dotenv()
from discord.ext import commands, tasks
TOKEN = os.environ.get('TOKEN', 3)
bot = commands.Bot(command_prefix='s!')

from main import *
bot.remove_command('help')

@bot.event
async def on_ready():
    print('bot.py is active')
    servers = list(bot.guilds)
    server_num = len(servers)
    await bot.change_presence(
        # "you all code"
        # "myself break over & over"
        activity=discord.Activity(type=discord.ActivityType.watching, name=f"over {server_num} servers| s!help"))


@bot.command(name='sorry')
async def sorry(ctx,*,sor):
    print('transforming '+ sor+ ' into an apology video')
    await ctx.send('Processing... \nthis may take a while...')
    ID = gen_ID(4)
    try:
        main(True,ID,sor)
    except Exception as e:
        await ctx.send(f'Whoopsie {ctx.author.mention}, I suffered a *'+str(e)+'* error, I\'ll try again now')
        main(True,ID,sor)
    await ctx.send(text=f'{ctx.author.mention} Your apology video is finished! Enjoy!',  file=discord.File("Finished/apology" + ID + ".mp4"))
    os.remove("Finished/apology" + ID + ".mp4")

@bot.command(name='help')
async def help(ctx):
    embed = discord.Embed(title='Help!',
                          color=discord.Color(6345206))
    embed.add_field(name='**s!sorry (reason)**',
                    value='Use s!sorry to create your own apology!',
                    inline=False)
    await ctx.channel.send(embed=embed)

bot.run(TOKEN)
