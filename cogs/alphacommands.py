import time
import json
import random
import discord
import math
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
from random_word import RandomWords
from os.path import isfile, join
from os import listdir
import subprocess
import shlex
import psutil
from threading import Thread
from discord.ext import menus
from colorama import init
from termcolor import colored
os.chdir('C:/Users/Lemon/Desktop/EconomyBot')

conn = sqlite3.connect("users.db")
c = conn.cursor()

c.execute("SELECT * from ran")
conn.commit()
fetchone = c.fetchone()
rannumber = int(fetchone[0])

clear = lambda: os.system('cls')

class beta(commands.Cog, name='Alpha Commands'):
	def __init__(self, bot):
		self.bot = bot

	async def beta(ctx):
		# 234834826081992704 222388637541597185 109475170602729472 109496491072077824 164120455228293120 362255701323677713 488929293905428482 600798393459146784
		return ctx.author.id == 234834826081992704 or ctx.author.id == 222388637541597185 or ctx.author.id == 109475170602729472 or ctx.author.id == 109496491072077824 or ctx.author.id == 164120455228293120 or ctx.author.id == 362255701323677713 or ctx.author.id == 488929293905428482 or ctx.author.id == 600798393459146784
	async def mod(ctx):
		return ctx.author.id == 600798393459146784


	@commands.command()
	@commands.check(beta)
	async def bait(self, ctx):
		await ctx.send('test')

	@commands.command()
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
	@commands.check(mod)
	async def reload(self, ctx):
		c.execute("UPDATE items SET fishing=0")
		conn.commit()
		os.chdir('C:/Users/Lemon/Desktop/EconomyBot')
		initial_extensions = ['cogs.alphacommands', 'cogs.helpcommand', 'cogs.errorhandling']
		print(colored("\nReloading...\n--------------------------------------", 'green'))
		time.sleep(2)
		for extension in initial_extensions:
			self.bot.reload_extension(extension)
		await ctx.send("Reloaded")

	@commands.command()
	@commands.check(mod)
	async def selreload(self, ctx, reloadvar : str):
		c.execute("UPDATE items SET fishing=0")
		conn.commit()
		os.chdir('C:/Users/Lemon/Desktop/EconomyBot')
		initial_extensions = [f'cogs.{reloadvar}']
		print("Reloading")
		time.sleep(2)
		for extension in initial_extensions:
			self.bot.reload_extension(extension)
		await ctx.send(f"Reloaded {reloadvar}.py")

	@commands.command()
	@commands.is_owner()
	async def controlledfish(self, ctx):
		pass

	@commands.command(name='fishbeta', aliases=['fb', 'fishb', 'fbeta'])
	@commands.is_owner()
	async def fishbeta(self, ctx):
		rods = {"standard": str(1) + '-You caught-30-240', "ironrod": str(random.randint(1,3)) + '-You caught-30-200', "god": str(random.randint(1,10000000000000000000000)) + '-You caught-1-10000000000000000000000', "luv": str(2) + '-You caught-30-60'}
		mention = ctx.author.mention
		person = str(ctx.author.id)
		randexp = random.randint(1,4)
		easylog(ctx)
		c.execute("SELECT * from items WHERE name=?", (person,))
		conn.commit()
		fishing = c.fetchone()
		mention = ctx.author.mention
		person = str(ctx.author.id)
		randexp = random.randint(1,4)
		personhandler(person)
		c.execute("SELECT * from items WHERE name=?", (person,))
		c.execute("SELECT * from items WHERE name=?", (person,))
		conn.commit()
		fishing = c.fetchone()

		fishing3 = fishing[3]
		path = f'C:/Users/Lemon/Desktop/EconomyBot/img/fish'
		files = ''
		for f in listdir(path):
			files += f + ':'
		files = files.split(':')
		filerand = random.randint(0, (int((len(files))-1)))
		randomimg = files[filerand]
		fishtype = randomimg.split('-')[0]
		fishamount = int(rods[fishing3].split('-')[0])
		timemin = int(rods[fishing3].split('-')[2])
		timemax = int(rods[fishing3].split('-')[3])
		fishget = fishamount
		fishamm = float(fishing[1])
		c.execute("UPDATE items SET name=?, fish=?, fishing=0 WHERE name=?", (person, fishamm, person))
		conn.commit()
		timesleep = random.randint(1,1)

		c.execute("SELECT * from items WHERE name=?", (person,))
		conn.commit()
		fishing = c.fetchone()
		await ctx.send(f"{mention} You started fishing... (1sec cool down)")
		await asyncio.sleep(timesleep)
		c.execute("UPDATE items SET name=?, fish=?, fishing=0 WHERE name=?", (person, float(fishamm)+float(fishget), person))
		conn.commit()

	@commands.command()
	async def menu_example(self, ctx):
		m = MyMenu()
		await m.start(ctx)

def easylog(ctx):
	os.chdir('C:/Users/Lemon/Desktop/EconomyBot/logs') 
	log = open("log{}.log".format(rannumber), "a", encoding='utf-8')
	os.chdir('C:/Users/Lemon/Desktop/EconomyBot')
	now = datetime.now()
	ct = now.strftime("%H:%M:%S")
	person = str(ctx.author.id)
	log.write(f"\n{ct} | {ctx.author} {person} uses {ctx.command}")
	log.close()

def personhandler(person):
	c.execute("SELECT * from people WHERE name=?", (person,))
	conn.commit()
	if c.fetchone() == None:
		c.execute("INSERT INTO people (name, coins) VALUES (?, 0)", (person,))
		conn.commit()
	c.execute("SELECT * from items WHERE name=?", (person,))
	conn.commit()
	if c.fetchone() == None:
		rod = 'standard'
		c.execute("INSERT INTO items (name, fish, fishing, fishingrods) VALUES (?, 0, 0, ?)", (person, rod))
		conn.commit()
	c.execute("SELECT * from inventory WHERE name=?", (person,))
	conn.commit()
	if c.fetchone() == None:
		c.execute("INSERT INTO inventory (name, hairdryer) VALUES (?, 0)", (person,))
		conn.commit()
	c.execute("SELECT * from levels WHERE name=?", (person,))
	conn.commit()
	if c.fetchone() == None:
		c.execute("INSERT INTO levels (name, level, exp, strength) VALUES (?, 0, 0.0, 0)", (person,))
		conn.commit()

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

def setup(bot):
	print('AlphaCommands')
	bot.add_cog(beta(bot))