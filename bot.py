import time
import json
import random
import discord
import os
import sys
from discord.ext import commands
from configthree import *
import asyncio
from datetime import datetime
import sqlite3
os.chdir('C:/Users/Lemon/Desktop/EconomyBot')
bottype = len(sys.argv) - 1
print(bottype)

if bottype == 1:
	bot = commands.Bot(command_prefix='gb', case_insensitive=True)
elif bottype == 0:
	bot = commands.Bot(command_prefix='bb', case_insensitive=True)

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

c.execute("UPDATE items SET fishing=0")
conn.commit()
class general(commands.Cog, name='General Commands'):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def start(self, ctx):
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

	@commands.command()
	async def fish(self, ctx):
		person = str(ctx.author.id)
		c.execute("SELECT * from items WHERE name=?", (person,))
		conn.commit()
		fishing = c.fetchone()
		print(fishing)
		if fishing[2] == 0:
			fishamm = float(fishing[1])
			c.execute("UPDATE items SET name=?, fish=?, fishing=1 WHERE name=?", (person, fishamm, person))
			conn.commit()
			c.execute("SELECT * from items WHERE name=?", (person,))
			conn.commit()
			fishing = c.fetchone()
			print(fishing)
			await ctx.send("You started fishing...")
			await asyncio.sleep(random.randint(10,120))
			print(fishamm+1)
			c.execute("UPDATE items SET name=?, fish=?, fishing=0 WHERE name=?", (person, fishamm+1, person))
			conn.commit()
			c.execute("SELECT * from items WHERE name=?", (person,))
			conn.commit()
			fishing = c.fetchone()
			print(fishing)
			await ctx.send("You caught 1 <:fish:662055365449351168>!")
		else:
			await ctx.send("You're already fishing!")

	@commands.command()
	async def restart(self, ctx, arg):
		if arg == 'yes':
			await ctx.send("Restarting")
			person = str(ctx.author.id)
			c.execute("DELETE from items where name=?", (person,))
			c.execute("DELETE from people where name=?", (person,))
			conn.commit()
			await ctx.send("Done!")

	@restart.error
	async def error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send("do `gbrestart yes` to restart")

	
	@commands.group(aliases=['balance'])
	async def bal(self, ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send("That's not a bal, please pick between `coin` or `fish`!")

	@bal.command()
	async def coin(self, ctx):
		person = str(ctx.author.id)
		c.execute("SELECT * from items where name=?", (person,))
		conn.commit()
		bal = c.fetchone()
		print(bal)
		await ctx.send("You have {} <:coin:662071327242321942>".format(bal[1]))

	@bal.command()
	async def fish(self, ctx):
		person = str(ctx.author.id)
		c.execute("SELECT * from people where name=?", (person,))
		conn.commit()
		bal = c.fetchone()
		await ctx.send("You have {} <:fish:662055365449351168>".format(bal[1]))

	@commands.group()
	async def shop(self, ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send("Invalid use, please do `[] = optional, <> = required` `gbshop <buy or sell or info> <item> [amount]`")


	@shop.command()
	async def buy(self, ctx, arg1, arg2):
		person = ctx.author.id
		if arg1 == 'Hairdryer':
			return None

	@buy.error
	async def error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			embed=discord.Embed(title="Shop", color=0x50fe54)
			embed.add_field(name="Hairdryer", value="5 <:coin:662071327242321942>", inline=False)
			await ctx.send(embed=embed)

	@shop.command()
	async def sell(self, ctx, arg1, arg2):
		return None

	@shop.command()
	async def info(self, ctx, arg1):
		if arg1 == 'Hairdryer':
			embed=discord.Embed(title="Info", color=0x50fe54)
			embed.add_field(name="Hairdryer", value="5 <:coin:662071327242321942>", inline=False)
			embed.add_field(name="Description", value="When used can get you 3 - 25 fish!", inline=True)
			await ctx.send(embed=embed)

	@info.error
	async def error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			embed=discord.Embed(title="Shop", color=0x50fe54)
			embed.add_field(name="Hairdryer", value="5 <:coin:662071327242321942>", inline=False)
			await ctx.send(embed=embed)


	@commands.command()
	async def sell(self, ctx, arg1, arg2):
		person = str(ctx.author.id)
		argtwo = arg2
		c.execute("SELECT * from items WHERE name=?", (person,))
		conn.commit()
		fishing = c.fetchone()
		print(fishing)
		if str(arg1) == 'fishing':
			fishing1 = fishing[1]
			fishing2 = fishing[2]
			fishing = c.fetchone()
			print(str(fishing1))
			print(str(fishing2))
			if int(fishing1) >= int(arg2):
				c.execute("SELECT * from people WHERE name=?", (person,))
				conn.commit()
				money = c.fetchone()
				moneyrn = float(money[1])
				moneygetting = float(arg2) * 0.25
				moneyearned = moneyrn + moneygetting
				print(moneyrn)
				print(moneygetting)
				print(moneyearned)
				newfishbal = float(fishing1) - float(arg2)
				print(newfishbal)
				c.execute("UPDATE items SET name=?, fish=?, fishing=? WHERE name=?", (person, newfishbal, fishing2, person))
				conn.commit()
				print(c.fetchone())
				c.execute("UPDATE people SET name=?, coins=? WHERE name=?", (person, float(moneyearned), person))
				conn.commit()
				print(c.fetchone())
				await ctx.send("Sold " + str(argtwo) + " <:fish:662055365449351168>")
			elif float(fishing2) < float(arg2):
				await ctx.send("You don't have that many fish!")
		else:
			await ctx.send("Not a valid Sell Shop!")

	@sell.error
	async def error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send("Do `gbsell fishing <anount to sell>`")





bot.add_cog(general(bot))
if bottype == 1:
	print('epic0')
	bot.run(config)
elif bottype == 0:
	print('epic1')
	bot.run(config2)
#py C:\Users\Lemon\Desktop\EconomyBot\bot.py