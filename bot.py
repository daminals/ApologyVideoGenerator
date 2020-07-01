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
    ID = ''
    for i in range(4):
        ID += str(random.randint(0, 9))
    main(True,ID,sor)
    await ctx.send(file=discord.File("Finished/apology" + ID + ".mp4"))


bot.run(TOKEN)
