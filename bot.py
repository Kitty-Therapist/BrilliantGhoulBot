import asyncio
import datetime
import discord
import datetime
import time
import math
from discord.ext import commands
from discord import utils

TOKEN = "SpongeBobSquarePants"

bot = commands.Bot(command_prefix = "+")

bot.starttime = datetime.datetime.now()
bot.startup_done = False

initial_extensions = ['announce', 'Reload', 'serversuggest']

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(f"cogs.{extension}")


@bot.event
async def on_ready():
        print(f'\n\nLogged in as: {bot.user.name} - {bot.user.id}' + f'\nVersion: {discord.__version__}\n')
        await bot.change_presence(activity=discord.Activity(name='Brilliant Things going on!', type=discord.ActivityType.watching))

bot.run(TOKEN)
