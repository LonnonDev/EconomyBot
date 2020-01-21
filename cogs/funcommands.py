import time
import json
import random
import math
import discord
import os
import sys
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
from datetime import datetime
import sqlite3
from uuid import uuid4
import psutil
import itertools
os.chdir('C:/Users/Lemon/Desktop/EconomyBot')


conn = sqlite3.connect("users.db")
c = conn.cursor()

c.execute("SELECT * from ran")
fetchone = c.fetchone()
rannumber = int(fetchone[0])


class fun(commands.Cog, name='Fun Commands'):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	@commands.cooldown(1, 5, commands.BucketType.user)
	async def bully(self, ctx, member: discord.Member):
		randint = random.randint(1,2)
		if randint == 1:
			await ctx.send(f"{member} has small pp")
		elif randint == 2:
			await ctx.send(f"{member} has small brain")

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

def setup(bot):
	print('FunCommands')
	bot.add_cog(fun(bot))