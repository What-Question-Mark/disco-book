import asyncio
import json
import os
import random
import re
import string
import time
from datetime import datetime
from html import unescape

import aiohttp
import discord
import requests
from bs4 import BeautifulSoup
from discord.ext import commands
from discord.ui import Button, Select, View
from discord.utils import get

f = open('config.json')
config = json.load(f)

class Other(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Evaluate some code")
    async def e(self, ctx:discord.ApplicationContext, *, code):
        if ctx.author.id in config["OWNER"]:
            try:
                res = await eval(code)
                await ctx.respond(f"```html\n{res}\n```")             
            except Exception as e:
               await ctx.respond(f"**Error:** ```\n{e}\n```")
        else:
            await ctx.respond(f"**Error:** ```You do not have permission to run this command```")
            
    @commands.slash_command(description="See the ping of the bot")
    async def ping(self, ctx:discord.ApplicationContext):
        await ctx.respond(f"Pong 🏓 **|** `{round(self.bot.latency * 1000)}ms`")

    @commands.slash_command(description="See the ping of the bot")
    async def help(self, ctx:discord.ApplicationContext):
        embed=discord.Embed(title="Help",color=0xFFAC33)
        embed.add_field(name="Books (1)",value="`getbook`",inline=False)
        embed.add_field(name="Info (2)",value="`help`,`ping`",inline=False)
        embed.add_field(name="Dev (1)",value="`eval`",inline=False)

        invite = Button(label="Invite",style=discord.ButtonStyle.url, url="https://shorturl.at/isvCW")
        github = Button(label="Github",style=discord.ButtonStyle.url, url="https://github.com/what-question-mark/disbook")

        view=View()
        view.add_item(invite)
        view.add_item(github)
        await ctx.respond(embed=embed, view=view)


def setup(bot):
    bot.add_cog(Other(bot))