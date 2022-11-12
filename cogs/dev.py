import discord, asyncio, random, time, json, os, string, requests, aiohttp
from discord.ext import commands
from discord.utils import get

f = open('config.json')
config = json.load(f)

class Dev(commands.Cog):
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
    async def ping(self, ctx):
        await ctx.respond(f"Pong 🏓 **|** `{round(self.bot.latency * 1000)}ms`")

    @commands.slash_command(description="See the ping of the bot")
    async def help(self, ctx):
        embed=discord.Embed(title="Help",color=0xFFAC33)
        embed.add_field(name="Books (1)",value="`getbook`",inline=False)
        embed.add_field(name="Info (2)",value="`help`,`ping`",inline=False)
        embed.add_field(name="Dev (1)",value="`eval`",inline=False)
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Dev(bot))