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
init()

os.chdir('C:/Users/Lemon/Desktop/EconomyBot')

splashes = list(str(open('containerfiles/splash.es', 'r', encoding="utf-8").read()).split("-"))

conn = sqlite3.connect("users.db")
c = conn.cursor()

clear = lambda: os.system('cls')

class Guilds(menus.Menu):
	async def send_initial_message(self, ctx, channel):
		return await channel.send(f':one: [guilds number] :left_right_arrow: [guilds list] :stop_button: [stop]')

	@menus.button('1\N{combining enclosing keycap}')
	async def one(self, payload):
		guilds = len([s for s in self.bot.guilds])
		guildname = []
		full = ''
		for guild in self.bot.guilds:
			guildname = guild.name
			full += f"`{guildname}`, "
		await self.message.edit(content=f'This bot is in {guilds} servers')

	@menus.button('\U00002194')
	async def leftrightarrow(self, payload):
		guilds = len([s for s in self.bot.guilds])
		guildname = []
		full = ''
		for guild in self.bot.guilds:
			guildname = guild.name
			full += f"`{guildname}`, "
		await self.message.edit(content=full)

	@menus.button('\N{BLACK SQUARE FOR STOP}\ufe0f')
	async def on_stop(self, payload):
		await self.author.message.delete()
		await self.message.delete()
		self.stop()


class owner(commands.Cog, name="Mod Commands"):
	def __init__(self, bot):
		self.bot = bot

	async def mod(ctx):
		return ctx.author.id == 600798393459146784 or ctx.author.id == 362255701323677713 or ctx.author.id == 620244349984309251
	async def code(ctx):
		return mod(ctx) or ctx.author.id == 370120271367110656

	@commands.command()
	@commands.check(mod)
	async def sudo(self, ctx, member: discord.Member, command, *args):
		print(r'{}'.format(args))
		print(r'{}'.format(*args))
		await ctx.message.delete()
		person = member
		ctx.author = person
		command = self.bot.get_command(command)
		await ctx.invoke(command, *args)

	@commands.command()
	@commands.check(mod)
	async def add(self, ctx, member: discord.Member, item, amount):
		person = str(member.id)
		if item == 'fish':
			c.execute('SELECT * from items where name=?', (person,))
			conn.commit()
			fetchone = c.fetchone()
			c.execute("UPDATE items SET fish=? WHERE name=?", (int(fetchone[1])+int(amount), person))
			conn.commit()
			await ctx.send(f"Updated {item} for <@!{person}>")
		else:
			c.execute('SELECT * from inventory where name=?', (person,))
			conn.commit()
			fetchone = c.fetchone()
			toc = ['name', 'hairdryer']
			n = -1
			for item in toc:
				n += 1
				print(n)
			c.execute("UPDATE inventory SET {}=? WHERE name=?".format(item), (int(fetchone[int(n)])+int(amount), person))
			conn.commit()
			await ctx.send(f"Updated {item} for <@!{person}>")

	@commands.command()
	@commands.check(mod)
	async def set(self, ctx, member: discord.Member, item, typeof, amount):
		person = str(member.id)
		if typeof == 'fish':
			c.execute('SELECT * from items where name=?', (person,))
			conn.commit()
			fetchone = c.fetchone()
			c.execute("UPDATE items SET {}=? WHERE name=?".format(item), (int(amount), person))
			conn.commit()
			await ctx.send(f"Updated {item} for <@!{person}>")
		else:
			c.execute('SELECT * from inventory where name=?', (person,))
			conn.commit()
			fetchone = c.fetchone()
			c.execute("UPDATE inventory SET {}=? WHERE name=?".format(item), (int(amount), person))
			conn.commit()
			await ctx.send(f"Updated {item} for <@!{person}>")

	@commands.command()
	@commands.check(mod)
	async def remove(self, ctx, member: discord.Member, item, amount):
		person = str(member.id)
		if item == 'fish':
			c.execute('SELECT * from items where name=?', (person,))
			conn.commit()
			fetchone = c.fetchone()
			c.execute("UPDATE items SET fish=? WHERE name=?", (int(fetchone[1])-int(amount), person))
			conn.commit()
			await ctx.send(f"Updated {item} for <@!{person}>")
		else:
			c.execute('SELECT * from inventory where name=?', (person,))
			conn.commit()
			fetchone = c.fetchone()
			toc = ['name', 'hairdryer']
			n = -1
			for item in toc:
				n += 1
			c.execute("UPDATE inventory SET {}=? WHERE name=?".format(item), (int(fetchone[int(n)])-int(amount), person))
			conn.commit()
			await ctx.send(f"Updated {item} for <@!{person}>")

	@commands.command(aliases=['guild'])
	@commands.check(mod)
	async def guilds(self, ctx):
		g = Guilds()
		await g.start(ctx)

	@commands.command()
	@commands.check(mod)
	async def reload(self, ctx):
		c.execute("UPDATE items SET fishing=0")
		conn.commit()
		os.chdir('C:/Users/Lemon/Desktop/EconomyBot')
		initial_extensions = list(str(open('containerfiles/co.gs', 'r', encoding='utf-8').read()).split("-"))
		clear()
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
	@commands.check(mod)
	async def splash(self, ctx):
		c.execute("SELECT * from ran")
		fetchone = c.fetchone()
		rannumber = int(fetchone[0])
		c.execute("UPDATE ran SET ran=?", (rannumber,))
		conn.commit()
		rannum = str(rannumber).zfill(3)
		version = 'Version {}.{}.{}'.format(str(rannum)[0], str(rannum)[1], str(rannum)[2])
		splashran1 = random.randint(1-1,len(splashes)-1)
		game=discord.Game(f'{version} | {splashes[splashran1]}') 
		await ctx.send(f'{version} | {splashes[splashran1]}')
		await self.bot.change_presence(status=discord.Status.online, activity=game)

	@commands.command()
	@commands.check(mod)
	async def newsplash(self, ctx):
		splashopen = open('containerfiles/splash.es', 'a', encoding="utf-8")
		r = RandomWords()
		randomword1 = r.get_random_word()
		randomword2 = r.get_random_word()
		splashopen.write(f'\b{randomword1} {randomword2}-'.replace('', ''))
		splashopen.close()
		await ctx.send(f'{randomword1} {randomword2}')

	@commands.command()
	@commands.check(mod)
	async def eval(self, ctx, *, code):
		os.chdir('C:/Users/Lemon/Desktop/EconomyBot')
		# opens the dummy file and writes the code
		df = open('dummyfile.py', 'w', encoding="utf-8")
		df.write(f'{code}')
		df.close()
		# opens the output and clears it
		dfo = open('dummyfileout.txt', 'w', encoding="utf-8")
		dfo.write('')
		# sub process
		sp = subprocess.Popen(["python", "dummyfile.py", ">", "dummyfileout.txt"], shell=True)
		# checks the files
		dfr = open('dummyfile.py', 'r', encoding="utf-8")
		dfor = open('dummyfileout.txt', 'r', encoding="utf-8")
		print(dfr.read())
		print(dfor.read())
		if dfr.read() == '':
			dfrread = 'None'
		else:
			dfrread = str(dfr.read())
		if dfor.read() == '':
			dforread = 'None'
		else:
			dforread = str(dfor.read())
		dfor.close()
		dfr.close()
		await ctx.send(f"""
In:
```
{dfrread}
```
Out:```
{dforread}
```""")

def kill(proc_pid):
	process = psutil.Process(proc_pid)
	for proc in process.children(recursive=True):
		proc.kill()
	process.kill()

def setup(bot):
	print("OwnerCommands")
	bot.add_cog(owner(bot))