import discord
from discord.ext import commands
import urllib.request
import json
import os
import random

BOT_TOKEN = os.environ["BOT_TOKEN"]

bot = commands.Bot(command_prefix='$')

@bot.event
async def on_ready():
    print("== ikanostage ==")
    print(bot.user.name)
    print(bot.user.id)

@bot.command()
async def stage(arg):
    api_url = "https://spla2.yuu26.com/schedule"
    headers = { "User-Agent" :  "DiscordSplatoon2StageBot/0.1 (@tokoro10g)" }

    result = json.loads(urllib.request.urlopen(urllib.request.Request(api_url, None, headers)).read())["result"]

    idx = 1 if arg == "next" else 0

    str_time_start = result["gachi"][idx]["start"][11:]
    str_time_end = result["gachi"][idx]["end"][11:]

    str_gachi_rule  = result["gachi"][idx]["rule"]
    str_league_rule = result["league"][idx]["rule"]

    str_regular = ", ".join(result["regular"][idx]["maps"])
    str_gachi   = ", ".join(result["gachi"][idx]["maps"])
    str_league  = ", ".join(result["league"][idx]["maps"])

    await bot.say('''\
```asciidoc
%s 〜 %s

[レギュラーマッチ]
%s

[ガチマッチ(%s)]
%s

[リーグマッチ(%s)]
%s
```\
        ''' % (str_time_start, str_time_end, str_regular, str_gachi_rule, str_gachi, str_league_rule, str_league))

@bot.command()
async def buki():
    api_url = "https://stat.ink/api/v2/weapon"
    region = "ja_JP"
    bukis = json.loads(urllib.request.urlopen(urllib.request.Request(api_url, None)).read()) # array
    b = random.choice(bukis)
    await bot.say('''\
```asciidoc
%s
(%s / %s)
```\
        ''' % (b["name"][region], b["sub"]["name"][region], b["special"]["name"][region]))


bot.run(BOT_TOKEN)
