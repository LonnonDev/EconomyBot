import time
import json
import random
import discord
from discord.ext import commands
from configthree import config
import asyncio
from datetime import datetime
import sqlite3

print('help')

bot = commands.Bot(command_prefix='gb', case_insensitive=True)

conn = sqlite3.connect("users.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS people (
			name blob,
			coins real
			)""")

c.execute("""CREATE TABLE IF NOT EXISTS items (
		name blob,
		fish real,
		fishing interger
		)""")


@bot.command()
async def start(ctx):
	person = str(ctx.author.id)
	c.execute("SELECT * from people WHERE name=?", (person,)) # Get person name
	conn.commit()
	fetch = c.fetchone()
	if fetch == None:
		c.execute("INSERT INTO people (name, coins) VALUES (?, 1)", (person,)) # insert values
		conn.commit()
		await ctx.send("Your life begins with 1 coin!")
		c.execute("SELECT * from people WHERE name=?", (person,)) # Get person name
		conn.commit()
		fetch = c.fetchone()
		c.execute("INSERT INTO items (name, fish, fishing) VALUES (?, 0, 0)", (person,))
		conn.commit()
		await ctx.send(fetch)
	else:
		await ctx.send("You're already registered")
		await ctx.send("Do `gbget` to get your coin value!")

@bot.command()
async def get(ctx):
	person = str(ctx.author.id)
	c.execute("SELECT * from people WHERE name=?", (person,)) # Get person name
	conn.commit()
	fetch = c.fetchone()
	if fetch != None:
		c.execute("SELECT * from people WHERE name=?", (person,)) # Get person name
		conn.commit()
		fetch = c.fetchone()

		await ctx.send("You have " + str(fetch[1]) + " Coin(s)!")
	else:
		await ctx.send("Do >start to register!")

@bot.command()
async def fish(ctx):
	person = str(ctx.author.id)
	c.execute("SELECT * from items WHERE name=?", (person,))
	conn.commit()
	fishing = c.fetchone()
	print(fishing)
	if fishing[2] == 0:
		fishamm = float(fishing[1])
		c.execute("INSERT INTO items (name, fish, fishing) VALUES (?, ?, 1)", (person, fishamm))
		conn.commit()
		await ctx.send("You started fishing...")
		await asyncio.sleep(random.randint(10,10))
		print(fishamm+1)
		c.execute("INSERT INTO items (name, fish, fishing) VALUES (?, ?, 0)", (person, fishamm+1))
		conn.commit()
		c.execute("SELECT * from items WHERE name=?", (person,))
		conn.commit()
		fishing = c.fetchone()
		print(fishing)
		await ctx.send("You caught 1 fish!")
	else:
		await ctx.send("Has something gone wrong?")

@bot.command()
async def getfish(ctx):
	person = str(ctx.author.id)
	c.execute("SELECT * from items WHERE name=?", (person,))
	conn.commit()
	fetch = c.fetchone()
	if fetch != None:
		await ctx.send("You have " + str(int(fetch[1])) + " Fish(es)!")
	else:
		await ctx.send("Do `gbfish` to get fish!")

@bot.command()
async def restart(ctx, arg):
	if arg == 'yes':
		await ctx.send("Restarting")
		person = str(ctx.author.id)
		c.execute("DELETE from items where name=?", (person,))
		c.execute("DELETE from people where name=?", (person,))
		conn.commit()
		await ctx.send("Done!")

@restart.error
async def error(ctx, error):
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send("do `gbrestart yes` to restart")

bot.run(config)