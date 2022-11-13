import asyncio
import json
import os
import random
import string
import time

import discord
import requests
from discord.ext import commands
from discord.utils import get


class colors:
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'

f = open('config.json')
config = json.load(f)

bot = discord.Bot(intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f'\n{colors.OKGREEN}Logged in as {bot.user}{colors.END}')
    await bot.change_presence(status=discord.Status.idle, activity=discord.Activity(type=discord.ActivityType.watching, name='/help'))

@bot.event
async def on_command_error(ctx, error):
    await ctx.respond(f"**Error:** ```\n{error}\n```")

print('\n')

for f in os.listdir("./cogs"):
    if f.endswith(".py"):
        try:
            bot.load_extension("cogs." + f[:-3])
            print(f"{colors.OKBLUE}Loaded: {f[:-3]}.py{colors.END}")
        except Exception as e:
            print(f"\n{colors.FAIL}Couldn't load {f[:-3]}.py: {e}{colors.END}\n")

bot.run(config["TOKEN"])