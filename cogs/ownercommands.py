import time
import json
import random
import discord
import os
import sys
from discord.ext import commands
import asyncio
from datetime import datetime
import sqlite3
from uuid import uuid4
import psutil
from tokengamer import *
import itertools

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
		print(person)
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
		print(person)
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
		print(person)
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


def setup(bot):
	print("OwnerCommands")
	bot.add_cog(owner(bot))
