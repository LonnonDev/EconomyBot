import time
import json
import random
import math
import discord
import os
from os import listdir
from os.path import isfile, join
import sys
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
from datetime import datetime
import sqlite3
from uuid import uuid4
import psutil
import itertools
import youtube_dl
import lavalink
from discord.ext import menus
os.chdir('C:/Users/Lemon/Desktop/EconomyBot')

ffmpeg_options = {
	'options': '-vn'
}

conn = sqlite3.connect("users.db")
c = conn.cursor()

c.execute("SELECT * from ran")
fetchone = c.fetchone()
rannumber = int(fetchone[0])


class fun(commands.Cog, name='Fun Commands'):
	def __init__(self, bot):
		self.bot = bot

	async def beta(ctx):
		# 234834826081992704 222388637541597185 109475170602729472 109496491072077824 164120455228293120 362255701323677713 488929293905428482 600798393459146784
		return ctx.author.id == 234834826081992704 or ctx.author.id == 222388637541597185 or ctx.author.id == 109475170602729472 or ctx.author.id == 109496491072077824 or ctx.author.id == 164120455228293120 or ctx.author.id == 362255701323677713 or ctx.author.id == 488929293905428482 or ctx.author.id == 600798393459146784

	@commands.command()
	async def bully(self, ctx, member: discord.Member):
		randint = random.randint(1,2)
		if randint == 1:
			await ctx.send(f"{member} has small pp")
		elif randint == 2:
			await ctx.send(f"{member} has small brain")

	@commands.command()
	@commands.cooldown(1, 60, commands.BucketType.user)
	@commands.check(beta)
	async def fishingmeme(self, ctx, laugh : int):
		await ctx.message.delete()
		await ctx.send("Fishing I barely know her!")
		ha = ''
		for x in range(laugh):
			await asyncio.sleep(1)
			ha += "HA"
			await ctx.send(f"**{ha}**")

	@commands.command()
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def dpy(self, ctx):
		await ctx.send("Discord.py > Discord.js")

	@commands.command()
	async def encode(self, ctx, encoding, *, text):
		text = str(text).encode(encoding=str(encoding), errors='namereplace')
		await ctx.send(text)

	@commands.command()
	async def decode(self, ctx, encoding, *, text):
		text1 = text.encode()
		text = text1.decode(str(encoding), errors='namereplace')
		await ctx.send(text)

	@commands.command(aliases=['axolotl'])
	@commands.cooldown(1, 5, commands.BucketType.user)
	async def randomaxolotl(self, ctx):
		pics = 20
		randint = random.randint(1, pics)
		await ctx.send('', file=discord.File(f'C:/Users/Lemon/Desktop/EconomyBot/img/axolotl/axolotl{randint}.jpg'))

	@commands.command()
	async def files(self, ctx, path):
		if path == 'home':
			path = f'C:/Users/Lemon/Desktop/EconomyBot'
			files = ''
			for f in listdir(path):
				files += f"{f}\n"
			await ctx.send(f"""```css
Here are the files in {path}
------------------
{files}```""")
		else:
			path = f'C:/Users/Lemon/Desktop/EconomyBot/{path}'
			files = ''
			for f in listdir(path):
				files += f"{f}\n"
			await ctx.send(f"""```css
Here are the files in {path}
------------------
{files}```""")

	@commands.command()
	async def code(self, ctx, start, end, file):
		os.chdir('C:/Users/Lemon/Desktop/EconomyBot')
		read = open(f"{file}", "r").readlines()[int(start)-1:int(end)]
		read = ' '.join(read)
		read = codeblock(read)
		await ctx.send(f'''>>> ```py
 {read}
```''')
		await ctx.send("[+] = ```")
		await ctx.send("[-] = `")
		os.chdir('C:/Users/Lemon/Desktop/EconomyBot')

def codeblock(text):
	codeblockformat = text.replace('```', '[+]').replace('`', '[-]')
	return codeblockformat


def setup(bot):
	print('FunCommands')
	bot.add_cog(fun(bot))