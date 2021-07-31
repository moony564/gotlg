import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():

    print(client.user.name)
    print("start")
    game = discord.Game('/명령어')
    await client.change_presence(status=discord.Status.online, activity=game)


@client.event
async def on_message(message):
    if "시발" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "시발" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "씨발" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "tlqkf" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "Tlqkf" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "미친" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "병신" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "지랄" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "존나" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "존1나" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "ㅈㄴ" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if "ㅅㅂ" in message.content:
        await message.delete()
        await message.channel.send(f"{message.author.mention} 님이 욕을 사용하셨습니다.")

    if message.content == "!봇정보":
        await message.channel.send("만든사람 : 마딩")
        await message.channel.send("버전 : 1.0v")
        await message.channel.send("개발자의 한마디 : 이하린TV수준이 뛰떨어지고 시궁창 인생")

    if message.content == "/명령어":
        await message.channel.send("https://moonytv.neocities.org/갓엘지/도움말.html + !봇정보")

    if "바보지?" in message.content:
        await message.channel.send("당연하지!")

    if message.content == "!나이":
        await message.channel.send("09년생")

    if message.content == "!혈액형":
        await message.channel.send("O형")

    if message.content == "!사는곳":
        await message.channel.send("대한민국")

    if message.content == "!방송계기":
        await message.channel.send("다른 스트리머가 게임하면서 방송하는게 멋있어서")

    if message.content == "!유튜브":
        await message.channel.send("https://www.youtube.com/channel/UCXPOGWwjH-noqWCn_URbWGA")

    if message.content == "!트위치":
        await message.channel.send("https://www.twitch.tv/cozy06242021")

    if message.content == "!디코":
        await message.channel.send("게임방 디스코드 방 : https://discord.gg/SFw3xdT")
        await message.channel.send("추가예정 : 이유 : 올바르지 않은 초대장")

    
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
