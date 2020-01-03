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
from bot import c, conn



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
			c.execute("INSERT INTO inventory (name, hairdryer) VALUES (?, 0)", (person,))
			conn.commit()

		else:
			await ctx.send("You're already registered")
			await ctx.send("Do `gbbal coin` to get your coin value!")

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
		c.execute("SELECT * from people where name=?", (person,))
		conn.commit()
		bal = c.fetchone()
		print(bal)
		await ctx.send("You have {} <:coin:662071327242321942>".format(bal[1]))

	@bal.command(name="fish")
	async def fishingbal(self, ctx):
		person = str(ctx.author.id)
		c.execute("SELECT * from items where name=?", (person,))
		conn.commit()
		bal = c.fetchone()
		await ctx.send("You have {} <:fish:662055365449351168>".format(int(bal[1])))

	@commands.group()
	async def shop(self, ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send("Invalid use, please do `[] = optional, <> = required` `gbshop <buy or sell or info> <item> [amount]`")


	@shop.command()
	async def buy(self, ctx, arg1, arg2):
		print(arg1)
		print(arg2)
		person = str(ctx.author.id)
		c.execute("SELECT * from people where name=?", (person,))
		conn.commit()
		e = c.fetchone()
		coins = e[1]
		arg11 = arg1.lower()
		if arg11 == 'hairdryer':
			if float(coins) >= float(5)*float(arg2):
				c.execute("SELECT * from inventory where name=?", (person,))
				conn.commit()
				d = c.fetchone()
				c.execute("SELECT * from people where name=?", (person,))
				conn.commit()
				f = c.fetchone()
				crn = f[1]
				hrn = d[1]
				print(crn)
				print(hrn)
				print(int(hrn)+int(arg2))
				await ctx.send("Bought " + str(arg2) + " hairdryers")
				c.execute("UPDATE inventory set hairdryer=? where name=?", (int(hrn)+int(arg2), person))
				conn.commit()
				c.execute("UPDATE people set coins=? where name=?", (int(crn)-5, person))
				conn.commit()
			else:
				await ctx.send("Sorry you don't have enough coins!")
		else:
			embed=discord.Embed(title="Shop", color=0x50fe54)
			embed.add_field(name="Invalid Item", value="Sorry that isn't an item...", inline=True)
			await self.bot.say(embed=embed)


	@buy.error
	async def error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			embed=discord.Embed(title="Shop")
			embed.add_field(name="Hairdryer [Buy/Sell]", value="5<:coin:662071327242321942>/2<:coin:662071327242321942>", inline=False)
			embed.add_field(name="Fish [Sell]", value="0.25<:coin:662071327242321942>", inline=False)
			await ctx.send(embed=embed)

	@shop.command()
	async def sell(self, ctx, arg1, arg2):
		person = str(ctx.author.id)
		argtwo = arg2
		c.execute("SELECT * from items WHERE name=?", (person,))
		conn.commit()
		fishing = c.fetchone()
		print(fishing)
		if str(arg1) == 'fish':
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
			await ctx.send("You can't sell that!")

	@sell.error
	async def error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send("Do `gbsell fishing <amount to sell>`")

	@shop.command()
	async def info(self, ctx, arg1):
		if arg1 == 'all':
			embed=discord.Embed(title="Shop")
			embed.add_field(name="Hairdryer [Buy/Sell]", value="5 <:coin:662071327242321942>/2 <:coin:662071327242321942>", inline=False)
			embed.add_field(name="Fish [Sell]", value="0.25 <:coin:662071327242321942>", inline=False)
			await self.bot.say(embed=embed)
		elif arg1 == 'Hairdryer':
			embed=discord.Embed(title="Info", color=0x50fe54)
			embed.add_field(name="Hairdryer", value="5 <:coin:662071327242321942>", inline=False)
			embed.add_field(name="Description", value="When used can get you 3 - 25 fish!", inline=True)
			await ctx.send(embed=embed)
		else:
			embed=discord.Embed(title="Info", color=0x50fe54)
			embed.add_field(name="Invalid Item", value="Sorry that isn't an item...", inline=True)
			await self.bot.say(embed=embed)

	@info.error
	async def error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			embed=discord.Embed(title="Shop", color=0x50fe54)
			embed.add_field(name="Hairdryer", value="5 <:coin:662071327242321942>", inline=False)
			await ctx.send(embed=embed)

	@commands.group()
	async def inventory(self, ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send("DO `gbinventory <info or use> <item>")

	@inventory.command()
	async def info(self, ctx):
		person = str(ctx.author.id)
		c.execute("SELECT * from items WHERE name=?", (person,))
		conn.commit()
		fetch0 = c.fetchall()
		c.execute("SELECT * from inventory where name=?", (person,))
		conn.commit()
		fetch1 = c.fetchall()
		fetchall = fetch1[0]
		print(fetchall)
		check = 0
		toc = ('name', 'hairdryer')
		lentoc = len(toc) 
		embed=discord.Embed(title="Inventory", color=0x50fe54)
		while check != lentoc:
			check += 1
			if fetchall[check-1] == 0 or fetchall[check-1] == str(ctx.author.id):
				print(check)
				print(111)
				pass
			elif fetchall[check-1] != 0 or fetchall[check-1] != str(ctx.author.id):
				print(check)
				print(222)
				itemname1 = toc[check-1].capitalize()
				itemammount = fetchall[check-1]
				print(itemammount)
				if itemammount > 1:
					embed.add_field(name=itemname1, value="You have " + str(itemammount) + " " + str(itemname1) + "s", inline=False)
				else:
					embed.add_field(name=itemname1, value="You have " + str(itemammount) + " " + str(itemname1), inline=False)
		await ctx.send(embed=embed)

	@inventory.command()
	async def use(self, ctx):
		await ctx.send("not avaible yet!")

	@commands.command()
	async def fish(self, ctx):
		person = str(ctx.author.id)
		c.execute("SELECT * from items WHERE name=?", (person,))
		conn.commit()
		fishing = c.fetchone()
		print(fishing)
		if fishing[3] == 'standard':
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
		elif fishing[3] == 'god':
			if fishing[2] == 0:
				fishamm = float(fishing[1])
				c.execute("UPDATE items SET name=?, fish=?, fishing=1 WHERE name=?", (person, fishamm, person))
				conn.commit()
				c.execute("SELECT * from items WHERE name=?", (person,))
				conn.commit()
				fishing = c.fetchone()
				print(fishing)
				await ctx.send("You started fishing...")
				await asyncio.sleep(random.randint(1,1))
				print(fishamm+1)
				c.execute("UPDATE items SET name=?, fish=?, fishing=0 WHERE name=?", (person, fishamm+10, person))
				conn.commit()
				c.execute("SELECT * from items WHERE name=?", (person,))
				conn.commit()
				fishing = c.fetchone()
				print(fishing)
				await ctx.send("You caught 10 <:fish:662055365449351168>!")
			else:
				await ctx.send("You're already fishing!")
		elif fishing[3] == 'luv':
			if fishing[2] == 0:
				fishamm = float(fishing[1])
				c.execute("UPDATE items SET name=?, fish=?, fishing=1 WHERE name=?", (person, fishamm, person))
				conn.commit()
				c.execute("SELECT * from items WHERE name=?", (person,))
				conn.commit()
				fishing = c.fetchone()
				print(fishing)
				await ctx.send("You started fishing...")
				await asyncio.sleep(random.randint(1,30))
				print(fishamm+1)
				c.execute("UPDATE items SET name=?, fish=?, fishing=0 WHERE name=?", (person, fishamm+10, person))
				conn.commit()
				c.execute("SELECT * from items WHERE name=?", (person,))
				conn.commit()
				fishing = c.fetchone()
				print(fishing)
				await ctx.send("You caught a couple (2) of <:fish:662055365449351168> :heart:!")
			else:
				await ctx.send("You're already fishing!")