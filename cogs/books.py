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

now = datetime.now()

f = open('config.json')
config = json.load(f)


class Books(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Get a book from google books")
    async def getbook(self, ctx:discord.ApplicationContext, book):

        data = requests.get(f'https://www.googleapis.com/books/v1/volumes?q={book}&key={config["API_KEY"]}')
        res = data.json()

        embed=discord.Embed(title=f"{res['items'][0]['volumeInfo']['title']}",description=f"{BeautifulSoup(unescape(res['items'][0]['searchInfo']['textSnippet']), 'lxml').text}",color=0x55ACEE)
        embed.set_author(name=f"{res['items'][0]['volumeInfo']['authors'][0]}", icon_url=f"{res['items'][0]['volumeInfo']['imageLinks']['smallThumbnail']}")
        embed.set_thumbnail(url=f"{res['items'][0]['volumeInfo']['imageLinks']['thumbnail']}")
        embed.add_field(name="ISBN 13",value=f"{res['items'][0]['volumeInfo']['industryIdentifiers'][0]['identifier']}",inline=True)
        embed.add_field(name="Page Count",value=f"{res['items'][0]['volumeInfo']['pageCount']}",inline=True)
        embed.add_field(name="Categories",value=f"{res['items'][0]['volumeInfo']['categories']}",inline=True)
        try:
            embed.add_field(name="Price",value=f"${int(res['items'][0]['saleInfo']['listPrice']['amount'])} {res['items'][0]['saleInfo']['listPrice']['currencyCode']}",inline=True)
        except:
            embed.add_field(name="Price",value=f"{res['items'][0]['saleInfo']['saleability']}",inline=True)
        embed.add_field(name="Published",value=f"{res['items'][0]['volumeInfo']['publishedDate']}",inline=True)
        try:
            embed.add_field(name="Purchase Link",value=f"[Link]({res['items'][0]['saleInfo']['buyLink']})",inline=True)
        except:
            embed.add_field(name="Purchase Link",value=f"Unavailable",inline=True)
            
        await ctx.respond(embed=embed)  

def setup(bot):
    bot.add_cog(Books(bot))
    