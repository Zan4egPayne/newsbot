# NewsBot Copyright 2020 By Zan4eg#5557
# Импорты библиотек

import discord
import random
from discord.ext import commands
import asyncio
import socket
import datetime
from datetime import timedelta
import requests
import os


PREFIX = 'n.' # Переменная префикса

Bot = commands.Bot( command_prefix = PREFIX ) # Установка префикса бота

# При загрузке бота
@Bot.event
async def on_ready():
	activity = discord.Game(name = "NewsBot| n.news", url='https://twitch.com/zan4egpayne')
	await Bot.change_presence( status = discord.Status.online, activity = activity )
	print("Logged in as NewsBot!")
	print("NewsBot Copyright 2020 By Zan4eg#5557")
	print("Бот запущен и готов к работе!")
	while True:
		await asyncio.sleep(8)
		await Bot.change_presence( status = discord.Status.online, activity = discord.Game(name = "Zan4eg#5557") )
		await asyncio.sleep(8)
		await Bot.change_presence( status = discord.Status.online, activity = discord.Streaming(name = "n.news", url='https://twitch.com/zan4egpayne') )

@Bot.command()
@commands.has_permissions( administrator = True ) # Установка нужных прав для комманды
async def news ( ctx, *, text):
    emb = discord.Embed(title= text, colour= 7419530)
    emb.set_footer(text= "Инфа/Новости")
    await ctx.send(embed= emb)
    await ctx.send('||@everyone||')

# Задаем параметры ошибки
@news.error
async def clear_error( ctx, error ):
	if isinstance( error, commands.MissingRequiredArgument ):
		await ctx.send( f'⚠️ {ctx.author.mention} укажите аргумент!' )

	if isinstance( error, commands.MissingPermissions ):
		await ctx.send( f'🛑 {ctx.author.mention} у вас недостаточно прав!' ) 

token = os.environ.get('BOT_TOKEN')
Bot.run(str(token))
