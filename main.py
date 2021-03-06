import os
from dotenv import load_dotenv
import discord
from discord.ext import commands
import requests
from bs4 import BeautifulSoup
load_dotenv()

bot = commands.Bot(command_prefix="<")
bot.remove_command('help')
case_insensitive = True

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game('<help'))

@bot.command()
async def t(ctx, *, args):
  soup = BeautifulSoup(requests.get("https://time.is/?q=" + "+".join(args.split()),
                       headers={'User-Agent': 'Mozilla/5.0'}).text, 'html.parser')
  time, where = soup.find(id="clock"), soup.find(id="msgdiv")
  here, ampm = where.find('span'), time.find('span')
  await ctx.send(f"**{time.contents[0][:-3]} {ampm.contents[0].lower()}** - {here.contents[0]}")

@bot.command(name="help")
async def helpDef(ctx):
    embed=discord.Embed(title="Time Everywhere",color=0x60d1f6)
    embed.add_field(name=":alarm_clock: Commands:", value="`<t <place>` - shows the local time\n`<invite` - bot invite link\n`<info` - additinal information", inline=True)
    embed.set_footer(text="<help | bot made by gorgonzola#6770")
    await ctx.send(embed=embed)

@bot.command(name="info")
async def infoDef(ctx):
    embed=discord.Embed(title="Time Everywhere",color=0x60d1f6)
    embed.add_field(name=":scroll: Additional Information:", value="-> Every place worldwide is built into the bot!\n-> If you find bugs/ have suggestions contact gorgonzola#6770\n-> Source used: [www.time.is](https://www.time.is)", inline=True)
    embed.set_footer(text="<help | bot made by gorgonzola#6770")
    await ctx.send(embed=embed)

bot.run(os.getenv("TOKEN"))
