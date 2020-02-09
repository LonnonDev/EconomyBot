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
from discord.ext import menus

os.chdir('C:/Users/Lemon/Desktop/EconomyBot')

class MyMenu(menus.Menu):
	async def send_initial_message(self, ctx, channel):
		return await channel.send(f'Hello {ctx.author}')

	@menus.button('\N{THUMBS UP SIGN}')
	async def on_thumbs_up(self, payload):
		await self.message.edit(content=f'Thanks {self.ctx.author}!')

	@menus.button('\N{THUMBS DOWN SIGN}')
	async def on_thumbs_down(self, payload):
		await self.message.edit(content=f"That's not nice {self.ctx.author}...")

	@menus.button('\N{BLACK SQUARE FOR STOP}\ufe0f')
	async def on_stop(self, payload):
		self.stop()

"""
	@commands.command()
	@commands.check(mod)
	async def guilds(self, ctx):
		guilds = len([s for s in self.bot.guilds])
		guildname = []
		full = ''
		for guild in self.bot.guilds:
			guildname = guild.name
			full += f"`{guildname}`, "
		await ctx.send(f"{full}")
		await ctx.send(f'This bot is in {guilds} servers')
"""
class beta(commands.Cog, name='Beta Commands'):
	def __init__(self, bot):
		self.bot = bot 

	async def beta(ctx):
		return ctx.author.id == 600798393459146784 or ctx.author.id == 362255701323677713 or ctx.author.id == 620244349984309251

	@commands.command()
	@commands.check(beta)
	async def bait(self, ctx):
		await ctx.send('test')

	@commands.command()
	@commands.check(beta)
	async def controlledfish(self, ctx):
		pass

	@commands.command()
	async def menu_example(self, ctx):
		m = MyMenu()
		await m.start(ctx)

def setup(bot):
	print('BetaCommands')
	bot.add_cog(beta(bot))