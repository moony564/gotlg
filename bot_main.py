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
    embed.add_field(name='```[접두사]```', value='```!```', inline=False)
    embed.add_field(name='[1]', value='나이', inline=False)
    embed.add_field(name='[2]', value='혈액형', inline=False)
    embed.add_field(name='[3]', value='사는곳', inline=False)
    embed.add_field(name='[4]', value='방송계기', inline=False)
    embed.add_field(name='[5]', value='트위치', inline=False)
    embed.add_field(name='[6]', value='유튜브', inline=False)
    embed.add_field(name='[삼국지]', value='장비', inline=False)
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
    
@app.command()
async def 장비(ctx):
    embed = discord.Embed(colour = 0x00ff00)
    embed.add_field(name='```[삼국지]```', value='```장비```', inline=False)
    embed.add_field(name='마우스', value='G402', inline=False)
    embed.add_field(name='키보드', value='G610K V2', inline=False)
    embed.add_field(name='그래픽카드', value='NVIDIA GeForce GTX 1650', inline=False)
    embed.add_field(name='CPU', value='AMD Ryzen 5 5600X', inline=False)
    embed.add_field(name='헤드셋', value='ABKO HACKER N550 ENC 가상 7.1 RGB 3D 진동 헤드셋', inline=False)
    await ctx.send(embed=embed)
    
@app.command()
async def 살려줘(ctx):
    await ctx.reply('여기서 1년만 하면 꺼내주신다고 하셨는데..')
    await ctx.reply('10년이나 같혀있다..')
    
access_token = os.environ["BOT_TOKEN"]
app.run(access_token)
