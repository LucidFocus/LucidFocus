import discord
import requests
import asyncio
from json import loads



client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    gmae = discord.Game("무무 시청")
    await client.change_presence(status=discord.Status.online, activity=gmae)
    twitch = "collet11"
    name = "코렛트"
    channel = client.get_channel(715169332308738108)
    a = 0
    while True:
        headers = {'Client-ID': '03zhvzm18ktmiqdqjrbpduv10bjzq5'}
        response = requests.get("https://api.twitch.tv/helix/streams?user_login=" + twitch, headers=headers)
        try:
            if loads(response.text)['data'][0]['type'] == 'live' and a == 0:
                await channel.send(name + "님이 방송중입니다.")
                a = 1
        except:
            a = 0
        await asyncio.sleep(5)





@client.event
async def on_message(message):
    if message.content.startswith("헤이 루시드"):
        await message.channel.send("넵 LucidFocus에요")
    if message.content.startswith("잘가"):
        await message.channel.send("안녕히계세요")
    if message.content.startswith("너 주인 뭐해"):
        await message.channel.send("게임중!")
    if message.content.startswith("안녕 루시드"):
        await message.channel.send("넵 LucidFocus에요")
    if message.content.startswith("hey Lucid"):
        await message.channel.send("넵 LucidFocus에요")
    if message.content.startswith("뭐하니"):
        await message.channel.send("대기중이에요")
    if message.content.startswith("주인 불러와"):
        await message.channel.send("알겠습니다 우무많사님을 부릅니다....")
    if message.content.startswith("잘있어"):
        await message.channel.send("안녕히가세요")


client.run("NzE1MTQyNjQ5NzA2NzA5MDYy.Xs460Q.IzlDc-f6BW7q2H4wqJlQLkKHiaI")

