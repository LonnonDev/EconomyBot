import time
import json
import random
import discord
import math
import os
import sys
from discord.ext import commands
import asyncio
from datetime import datetime
import sqlite3
from uuid import uuid4
import psutil
import itertools
os.chdir('C:/Users/Lemon/Desktop/EconomyBot')

splashesfile = open('splash.es', 'r', encoding="utf8")
#   list(str(splashesfile.read()).split("-"))
splashes = list(str(splashesfile.read()).split("-"))

conn = sqlite3.connect("users.db")
c = conn.cursor()

class owner(commands.Cog, name="Mod Commands"):
	def __init__(self, bot):
		self.bot = bot

	async def mod(ctx):
		return ctx.author.id == 600798393459146784 or ctx.author.id == 362255701323677713 or ctx.author.id == 620244349984309251

	@commands.command()
	@commands.check(mod)
	async def sudo(self, ctx, member: discord.Member, *, command):
		await ctx.message.delete()
		person = member
		ctx.author = person
		command = self.bot.get_command(command)
		await ctx.invoke(command)

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
	async def set(self, ctx, member: discord.Member, item, amount):
		person = str(member.id)
		if item == 'fish':
			c.execute('SELECT * from items where name=?', (person,))
			conn.commit()
			fetchone = c.fetchone()
			c.execute("UPDATE items SET fish=? WHERE name=?", (int(amount), person))
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

	@commands.command()
	@commands.check(mod)
	async def reload(self, ctx):
		initial_extensions = ['cogs.generalcommands', 'cogs.errorhandling', 'cogs.ownercommands', 'cogs.helpcommand']
		print("\nReloaded Extensions\n")
		for extension in initial_extensions:
			self.bot.reload_extension(extension)
		await ctx.send("Reloaded")

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
		splashran1 = random.randint(1,len(splashes))
		game=discord.Game(f'{version} | {splashes[splashran1]}') 
		await ctx.send(f'{version} | {splashes[splashran1]}')
		await self.bot.change_presence(status=discord.Status.online, activity=game)


def setup(bot):
	print("OwnerCommands")
	bot.add_cog(owner(bot))
