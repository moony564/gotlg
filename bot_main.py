import discord
from discord import message
from discord import embeds
from discord import colour
from discord.ext import commands
import time
import os

app = commands.Bot(command_prefix='!')

@app.event
async def on_ready():
    print(app.user.name)
    print("start")
    game = discord.Game('!명령어')
    await app.change_presence(status=discord.Status.online, activity=game)

@app.command()
async def 명령어(ctx):
    embed = discord.Embed(colour = 0x00ff00)
    embed.add_field(name='```접두사```', value='```!```', inline=False)
    embed.add_field(name='1', value='나이', inline=False)
    embed.add_field(name='2', value='혈액형', inline=False)
    embed.add_field(name='3', value='사는곳', inline=False)
    embed.add_field(name='4', value='방송계기', inline=False)
    embed.add_field(name='5', value='트위치', inline=False)
    embed.add_field(name='6', value='유튜브', inline=False)
    await ctx.send(embed=embed)

# embed.add_field(value='', inline=False) #임배드

@app.command()
async def 나이(ctx):
    await ctx.send('09년생')

@app.command()
async def 혈액형(ctx):
    await ctx.send('O형')

@app.command()
async def 사는곳(ctx):
    await ctx.send('대한민국')
    
@app.command()
async def 방송계기(ctx):
    await ctx.send('다른 스트리머가 게임하면서 방송하는게 멋있어서')
@app.command()
async def 트위치(ctx):
    await ctx.send('https://www.twitch.tv/cozy06242021')

@app.command()
async def 유튜브(ctx):
    await ctx.send('https://www.youtube.com/channel/UCXPOGWwjH-noqWCn_URbWGA')
    
access_token = os.environ["BOT_TOKEN"]
app.run(access_token)
