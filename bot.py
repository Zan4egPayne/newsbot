import discord
from discord.ext import commands
import asyncio
import os


PREFIX = '*'

Bot = commands.Bot( command_prefix= PREFIX, self_bot = True ) #префикс

# Статус бота
@Bot.event  
async def on_ready():
    activity = discord.Streaming(name="хентай", url='https://twitch.tv/zan4egpayne')
    await Bot.change_presence(status=discord.Status.online, activity=activity)
    print("Бот запущен!")

token = os.environ.get('BOT_TOKEN')
Bot.run( str(token), bot = False )