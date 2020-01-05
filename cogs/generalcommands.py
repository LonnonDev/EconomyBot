import time
import json
import random
import discord
import os
import sys
import math
from discord.ext import commands
import asyncio
from datetime import datetime
import sqlite3
import psutil


conn = sqlite3.connect("users.db")
c = conn.cursor()

class general(commands.Cog, name='General Commands'):
	def __init__(self, bot):
		self.bot = bot

#===========================================================================================================#
#                                Normal Commands
#===========================================================================================================#


	@commands.command()
	async def start(self, ctx):
		person = str(ctx.author.id) # User ID
		personhandler(person) # Person Handeler
		c.execute("SELECT * from people WHERE name=?", (person,)) # Get the User's obj's from people table
		conn.commit() # Commit the changes
		fetch = c.fetchone()
		if fetch == None:
			c.execute("INSERT INTO people (name, coins) VALUES (?, 1)", (person,)) 
			conn.commit()
			await ctx.send("Your life begins with 1 coin!")
			c.execute("SELECT * from people WHERE name=?", (person,))
			conn.commit()
			fetch = c.fetchone()
			c.execute("INSERT INTO items (name, fish, fishing) VALUES (?, 0, 0)", (person,))
			conn.commit()
			await ctx.send(fetch)
			c.execute("INSERT INTO inventory (name, hairdryer) VALUES (?, 0)", (person,))
			conn.commit()
		else:
			await ctx.send("You're already registered")
			await ctx.send("Do `f!bal coin` to get your coin value!")

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
			await ctx.send("do `f!restart yes` to restart")

	
	@commands.group(aliases=['balance'])
	async def bal(self, ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send("That's not a bal, please pick between `coin` or `fish`!")

	@bal.command()
	async def coin(self, ctx):
		person = str(ctx.author.id)
		personhandler(person)
		c.execute("SELECT * from people where name=?", (person,))
		conn.commit()
		bal = c.fetchone()
		print(bal)
		await ctx.send("You have {} <:coin:662071327242321942>".format(bal[1]))

	@bal.command(name="fish")
	async def fishingbal(self, ctx):
		person = str(ctx.author.id)
		personhandler(person)
		c.execute("SELECT * from items where name=?", (person,))
		conn.commit()
		bal = c.fetchone()
		await ctx.send("You have {} <:fish:662055365449351168>".format(int(bal[1])))

	@commands.command()
	async def update(self, ctx):
		person = str(ctx.author.id)
		personhandler(person)
		print(person)
		await ctx.send("Updated user Data")

	@commands.command()
	async def fish(self, ctx):
		person = str(ctx.author.id)
		randexp = random.randint(1,4)
		personhandler(person)
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
				getexp(person, randexp)
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
				getexp(person)
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
				getexp(person, randexp)
			else:
				await ctx.send("You're already fishing!")
#:white_large_square: :green_square:
	@commands.command()
	async def level(self, ctx):
		person = str(ctx.author.id)
		c.execute("SELECT * from levels WHERE name=?", (person,))
		fetchlevel = c.fetchall()
		level = fetchlevel[0][1]
		exp = fetchlevel[0][2]
		levelingform = level**int(level/4)
		print(levelingform)
		print(level)
		print(exp)
		if math.isclose(float(exp), float(exp)*0.00, rel_tol=0.2):
			v1 = ":white_large_square:"
			v2 = ":white_large_square:"
			v3 = ":white_large_square:"
			v4 = ":white_large_square:"
			v5 = ":white_large_square:"
			embed=discord.Embed(title="Leveling", color=0x09a600)
			embed.add_field(name=f"You're level {level}", value=f"~{v1}{v2}{v3}{v4}{v5}", inline=False)
			embed.add_field(name=f"{levelingform}", value=f"{exp}", inline=False)
			print(2)
		elif math.isclose(float(exp), float(exp)*0.20, rel_tol=0.2):
			v1 = ":green_square:"
			v2 = ":white_large_square:"
			v3 = ":white_large_square:"
			v4 = ":white_large_square:"
			v5 = ":white_large_square:"
			embed=discord.Embed(title="Leveling", color=0x09a600)
			embed.add_field(name=f"You're level {level}", value=f"~{v1}{v2}{v3}{v4}{v5}", inline=False)
			embed.add_field(name=f"{levelingform}", value=f"{exp}", inline=False)
			print(2)
		elif math.isclose(float(exp), float(exp)*0.40, rel_tol=0.2):
			v1 = ":green_square:"
			v2 = ":green_square:"
			v3 = ":white_large_square:"
			v4 = ":white_large_square:"
			v5 = ":white_large_square:"
			embed=discord.Embed(title="Leveling", color=0x09a600)
			embed.add_field(name=f"You're level {level}", value=f"~{v1}{v2}{v3}{v4}{v5}", inline=False)
			embed.add_field(name=f"{levelingform}", value=f"{exp}", inline=False)
			print(3)
		elif math.isclose(float(exp), float(exp)*0.60, rel_tol=0.2):
			v1 = ":green_square:"
			v2 = ":green_square:"
			v3 = ":green_square:"
			v4 = ":white_large_square:"
			v5 = ":white_large_square:"
			embed=discord.Embed(title="Leveling", color=0x09a600)
			embed.add_field(name=f"You're level {level}", value=f"~{v1}{v2}{v3}{v4}{v5}", inline=False)
			embed.add_field(name=f"{levelingform}", value=f"{exp}", inline=False)
			print(4)
		elif math.isclose(float(exp), float(exp)*0.80, rel_tol=0.2):
			v1 = ":green_square:"
			v2 = ":green_square:"
			v3 = ":green_square:"
			v4 = ":green_square:"
			v5 = ":white_large_square:"
			embed=discord.Embed(title="Leveling", color=0x09a600)
			embed.add_field(name=f"You're level {level}", value=f"~{v1}{v2}{v3}{v4}{v5}", inline=False)
			embed.add_field(name=f"You need {levelingform} exp to Level up", value=f"You have {exp} exp", inline=False)
			embed.add_field(name=f"To get to Level {level+1}", value=f"You need {levelingform-exp} exp to level up!", inline=False)
			print(5)
		await ctx.send(embed=embed)


	@commands.command()
	async def status(self, ctx):
		ping1 = self.bot.latencies
		ping = round(ping1[0][1]*1000, 1)
		cpu = psutil.cpu_percent()
		ram = psutil.virtual_memory()
		embed=discord.Embed(title="Status")
		embed.add_field(name="Ping", value=("%gms" % (float(ping))), inline=True)
		embed.add_field(name="CPU Usage", value=f"{cpu}%", inline=True)
		embed.add_field(name="RAM Usage", value=f"{ram[2]}%", inline=True)
		embed.add_field(name="Invite", value="[Click here to invite](https://discordapp.com/api/oauth2/authorize?client_id=627932116319076353&permissions=1812462657&scope=bot)", inline=True)
		embed.add_field(name="Trello", value="[Click here to go to Trello](https://trello.com/b/rzd1Y7C6/fishing-bot-thing)", inline=True)
		await ctx.send(embed=embed)

	@commands.command()
	async def invite(self, ctx):
		await ctx.send("Do `f!status` to see invite link")

#===========================================================================================================#

#===========================================================================================================#
#                                Shop Group
#===========================================================================================================#

	@commands.group()
	async def shop(self, ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send("Invalid use, please do `[] = optional, <> = required` `f!shop <buy or sell or info> <item> [amount]`")


	@shop.command()
	async def buy(self, ctx, arg1, arg2):
		person = str(ctx.author.id)
		personhandler(person)
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
				await ctx.send("Bought " + str(arg2) + " hairdryer(s)")
				c.execute("UPDATE inventory set hairdryer=? where name=?", (int(irn)+int(arg2), person))
				conn.commit()
				c.execute("UPDATE people set coins=? where name=?", (int(crn)-5*int(arg2), person))
				conn.commit()
			else:
				await ctx.send("Sorry you don't have enough coins!")
		elif arg11 == 'ironrod':
			c.execute("SELECT * from items where name=?", (person,))
			conn.commit()
			e = c.fetchone()
			if str(e[0]) == 'ironrod':
				if float(coins) >= float(50):
					c.execute("SELECT * from items where name=?", (person,))
					conn.commit()
					d = c.fetchall()
					c.execute("SELECT * from people where name=?", (person,))
					conn.commit()
					f = c.fetchall()
					crn = f[0][1]
					irn = d[0][3]
					await ctx.send("Bought " + str(arg2) + " Iron rod(s)")
					c.execute("UPDATE items set fishingrods=? where name=?", (str(arg11), person))
					conn.commit()
					c.execute("UPDATE people set coins=? where name=?", (int(crn)-25, person))
					conn.commit()
				await ctx.send("Sorry you don't have enough coins!")
			else:
				await ctx.send("You already have the iron rod!")
		else:
			embed=discord.Embed(title="Shop", color=0x50fe54)
			embed.add_field(name="Invalid Item", value="Sorry that isn't an item...", inline=True)
			await ctx.send(embed=embed)


	@buy.error
	async def error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			embed=discord.Embed(title="Shop")
			embed.add_field(name="Hairdryer `hairdryer` [Buy/Sell]", value="5<:coin:662071327242321942>/2<:coin:662071327242321942>", inline=False)
			embed.add_field(name="Fish `fish` [Sell]", value="0.25<:coin:662071327242321942>", inline=False)
			embed.add_field(name="Iron rod `ironrod` [Buy]", value="25<:coin:662071327242321942>", inline=False)
			await ctx.send(embed=embed)

	@shop.command()
	async def sell(self, ctx, arg1, arg2):
		person = str(ctx.author.id)
		personhandler(person)
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
			await ctx.send("Do `f!sell fishing <amount to sell>`")

	@shop.command()
	async def info(self, ctx, arg):
		arg1 = str(arg.lower())
		if arg1 == 'all':
			embed=discord.Embed(title="Shop")
			embed.add_field(name="Hairdryer [Buy/Sell]", value="5<:coin:662071327242321942>/2<:coin:662071327242321942>", inline=False)
			embed.add_field(name="Fish [Sell]", value="0.25<:coin:662071327242321942>", inline=False)
			embed.add_field(name="Iron rod `ironrod` [Buy]", value="25<:coin:662071327242321942>", inline=False)
			await ctx.send(embed=embed)
		elif arg1 == 'hairdryer':
			embed=discord.Embed(title="Info", color=0x50fe54)
			embed.add_field(name="Hairdryer", value="5<:coin:662071327242321942>", inline=False)
			embed.add_field(name="Description", value="When used can get you 3 - 25 fish!", inline=True)
			await ctx.send(embed=embed)
		else:
			embed=discord.Embed(title="Info", color=0x50fe54)
			embed.add_field(name="Invalid Item", value="Sorry that isn't an item...", inline=True)
			await ctx.send(embed=embed)

	@info.error
	async def error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			embed=discord.Embed(title="Shop")
			embed.add_field(name="Hairdryer [Buy/Sell]", value="5<:coin:662071327242321942>/2<:coin:662071327242321942>", inline=False)
			embed.add_field(name="Fish [Sell]", value="0.25<:coin:662071327242321942>", inline=False)
			embed.add_field(name="Iron rod `ironrod` [Buy]", value="25<:coin:662071327242321942>", inline=False)
			await ctx.send(embed=embed)

#===========================================================================================================#

#===========================================================================================================#
#                                Inventory Group
#===========================================================================================================#

	@commands.group()
	async def inventory(self, ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send("DO `f!inventory <info or use> <item>")

	@inventory.command(name='info')
	async def info1(self, ctx):
		person = str(ctx.author.id)
		personhandler(person)
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
	async def use(self, ctx, arg1):
		arg = arg1.lower()
		person = str(ctx.author.id)
		personhandler(person)
		c.execute("SELECT * from inventory where name=?", (person,))
		conn.commit()
		fetch0 = c.fetchall()
		fetchall = fetch0[0]
		toc = ('name', 'hairdryer')
		print(fetch0)
		if arg in toc:
			print(int(arg in toc))
			print(fetchall[int(arg in toc)])
			print(int(fetchall[1])-1)
			if fetchall[int(arg in toc)] >= 1:
				c.execute("UPDATE inventory SET name=?, {}=? WHERE name=?".format(arg), (person, int(fetchall[1])-1, person))
				if arg == 'hairdryer':
					c.execute("SELECT * from items where name=?", (person,))
					conn.commit()
					fish1 = c.fetchall()
					fishamm = fish1[0]
					randint = random.randint(3,25)
					c.execute("UPDATE items SET name=?, fish=? WHERE name=?", (person, fishamm[1], person))
					conn.commit()
					await ctx.send(f"You got {randint} fish!")
				else:
					await ctx.send("HACKER?!!?!?!?!?!?")
			else:
				await ctx.send("You don't have enough of that item!")
		else:
			await ctx.send("You don't have that item")

#===========================================================================================================#

def personhandler(person):
	print('epic')
	c.execute("SELECT * from people WHERE name=?", (person,))
	conn.commit()
	if c.fetchone() == None:
		c.execute("INSERT INTO people (name, coins) VALUES (?, 0)", (person,))
		conn.commit()
	c.execute("SELECT * from items WHERE name=?", (person,))
	conn.commit()
	if c.fetchone() == None:
		c.execute("INSERT INTO items (name, fish, fishing, fishingrods) VALUES (?, 0, 0, standard)", (person,))
		conn.commit()
	c.execute("SELECT * from inventory WHERE name=?", (person,))
	conn.commit()
	if c.fetchone() == None:
		c.execute("INSERT INTO inventory (name, hairdryer) VALUES (?, 0)", (person,))
		conn.commit()
	c.execute("SELECT * from levels WHERE name=?", (person,))
	conn.commit()
	print(str(c.fetchone))
	if c.fetchone() == None:
		c.execute("INSERT INTO levels (name, level, exp) VALUES (?, 0, 0.0)", (person,))
		conn.commit()

def getexp(person):
	print('epic')
	c.execute("SELECT * from levels WHERE name=?", (person,))
	fetchlevel = c.fetchall()
	fetchlevel1 = (fetchlevel[0])[1]
	fetchlevel2 = (fetchlevel[0])[2]
	c.execute("UPDATE levels SET name=?, level=?, exp=? WHERE name=?", (person, fetchlevel1, int(fetchlevel2)+randexp, person))
	conn.commit()
	checklevel(person)



def checklevel(person):
	c.execute("SELECT * from levels WHERE name=?", (person,))
	fetchlevel = c.fetchall()
	fetchlevel11 = fetchlevel[0][1]
	fetchlevel22 = fetchlevel[0][2]
	fetchlevel1 = int(fetchlevel11)
	fetchlevel2 = int(fetchlevel22)
	print(fetchlevel1)
	if str(fetchlevel1) == '0':
		c.execute("UPDATE levels SET name=?, level=?, exp=? WHERE name=?", (person, 1, int(fetchlevel2), person))
		conn.commit()
	elif str(fetchlevel1) != '0':
		levelingform = fetchlevel1**int(fetchlevel1/4)
		print(levelingform)
		print(fetchlevel2)
		if int(fetchlevel2) >= levelingform:
			c.execute("UPDATE levels SET name=?, level=?, exp=? WHERE name=?", (person, int(fetchlevel1)+1, int(fetchlevel2)-int(levelingform), person))
			conn.commit()


def setup(bot):
	print('GeneralCommands')
	bot.add_cog(general(bot))