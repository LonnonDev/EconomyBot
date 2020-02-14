import time
import json
import random
import math
import discord
import os
import sys
from discord.ext import commands
import asyncio
from datetime import datetime
import sqlite3
from uuid import uuid4
import psutil
from os import listdir
import itertools
from datetime import datetime
os.chdir('C:/Users/Lemon/Desktop/EconomyBot')
version = open("versi.on", "r", encoding='utf-8')
version = version.read()

conn = sqlite3.connect("users.db")
c = conn.cursor()

c.execute("SELECT * from ran")
conn.commit()
fetchone = c.fetchone()
rannumber = int(fetchone[0])

class general(commands.Cog, name='General Commands'):
	def __init__(self, bot):
		self.bot = bot

#===========================================================================================================#
#                                Normal Commands
#===========================================================================================================#

	@commands.command(aliases=['new', 'n'])
	async def news(self, ctx, botversion=version):
		await ctx.send(version)
		news = {'1.0.1r': 'Update 1.0.1r-+ Fixed "f1news" command\n+ Added a real version system', '1.0.0r': 'Update 1.0.0r-+ Fixed "f1sell cod 1" command'}
		news= news[version].split('-')
		newsheader = news[0]
		news = news[1]
		embed=discord.Embed(title="News", color=0x09a600)
		embed.add_field(name=newsheader, value=f"```diff\n{news}```", inline=False)
		await ctx.send(embed=embed)

	@commands.command(name="start")
	async def start(self, ctx): 
		easylog(ctx) # logs the command used
		person = str(ctx.author.id) # defins the person using the commands
		c.execute("SELECT * from people WHERE name=?", (person,)) #gets the persons table if exists or not exists
		conn.commit() # commits that
		fetch = c.fetchone() # fetchs the data
		if fetch == None: # if it's none than it registers the person using the command
			personhandler(person) # runs the personhandeler function
			await ctx.send(f"{ctx.author.mention} You just got registed!") # sends a message saying that you registered
		else: # else statement
			await ctx.send(f"{ctx.author.mention} You're already registered") # sends a message if the person is already registered
			await ctx.send("Do `f!help` for help!") # tells them to do "f!help" for help, aka telling them all commands

	@commands.command()
	async def restart(self, ctx, arg):
		easylog(ctx)
		if arg == 'yes':
			await ctx.send("Restarting")
			person = str(ctx.author.id)
			c.execute("DELETE from items where name=?", (person,))
			conn.commit()
			c.execute("DELETE from people where name=?", (person,))
			conn.commit()
			await ctx.send("Done!")
			log(ctx, f'restared the game')
		else:
			await ctx.send(f"{ctx.author.mention} Do `f!restart yes` to restart")

	@commands.group(aliases=['balance', 'b'])
	async def bal(self, ctx):
		if ctx.invoked_subcommand is None:
			await ctx.send(f"{ctx.author.mention} That's not a bal, please pick between `coin` or `fish`!")

	@bal.command()
	async def coin(self, ctx):
		easylog(ctx)
		person = str(ctx.author.id)
		personhandler(person)
		c.execute("SELECT * from people where name=?", (person,))
		conn.commit()
		bal = c.fetchone()
		await ctx.send(f"{ctx.author.mention} You have {bal[1]} <:coin:662071327242321942>")

	@bal.command(name="fish")
	async def fishingbal(self, ctx, person=None):
		easylog(ctx)
		person = str(ctx.author.id)
		personhandler(person)
		c.execute("SELECT * from items where name=?", (person,))
		conn.commit()
		bal = c.fetchone()
		embed=discord.Embed(title="Fish Bal", color=0x09a600)
		if bal[1] != 0:
			embed.add_field(name=f"Cod", value=int(bal[1]), inline=False)
		if bal[2] != 0:
			embed.add_field(name=f"Tuna", value=int(bal[2]), inline=False)
		if bal[3] != 0:
			embed.add_field(name=f"Salmon", value=int(bal[3]), inline=False)
		if bal[4] != 0:
			embed.add_field(name=f"Catfish", value=int(bal[4]), inline=False)
		if bal[5] != 0:
			embed.add_field(name=f"Red Snapper", value=int(bal[5]), inline=False)
		if bal[6] != 0:
			embed.add_field(name=f"Rainbow Trout", value=int(bal[6]), inline=False)
		if bal[7] != 0:
			embed.add_field(name=f"Trout", value=int(bal[7]), inline=False)
		if bal[8] != 0:
			embed.add_field(name=f"Bass", value=int(bal[8]), inline=False)
		if bal[9] != 0:
			embed.add_field(name=f"Sardine", value=int(bal[9]), inline=False)
		await ctx.send(embed=embed)


	@commands.command()
	async def update(self, ctx):
		easylog(ctx)
		person = str(ctx.author.id)
		personhandler(person)
		await ctx.send(f"{ctx.author.mention} Updated user Data")

	@commands.command(aliases=['f'])
	async def fish(self, ctx):
		now = datetime.now()

		cod = random.randint(1,1)
		sardine = random.randint(1,5)
		tuna = random.randint(1,10)
		salmon = random.randint(1,20)
		catfish = random.randint(1,50)
		redsnapper = random.randint(1,50)
		bass = random.randint(1,50)
		trout = random.randint(1,100)
		raingbowtrout = random.randint(1,1000)


		current_time = now.strftime("%H:%M:%S")
		rods = {"standard": str(1) + '-You caught-30-240', "ironrod": str(random.randint(1,3)) + '-You caught-30-200', "god": str(random.randint(1,1000)) + '-You caught-1-60', "luv": str(2) + '-You caught-30-60'}
		mention = ctx.author.mention
		person = str(ctx.author.id)
		randexp = random.randint(1,4)
		easylog(ctx)
		c.execute("SELECT * from items WHERE name=?", (person,))
		conn.commit()
		fishing = c.fetchone()
		fishing = fishing
		mention = ctx.author.mention
		person = str(ctx.author.id)
		randexp = random.randint(1,4)
		personhandler(person)
		c.execute("SELECT * from items WHERE name=?", (person,))
		conn.commit()
		if fishing[10] == 0:
			c.execute("SELECT * from items WHERE name=?", (person,))
			conn.commit()
			fishing = c.fetchone()

			fishing3 = fishing[11]
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
			c.execute("UPDATE items SET name=?, cod=?, fishing=1 WHERE name=?", (person, fishamm, person))
			conn.commit()
			timesleep = random.randint(int(timemin),int(timemax))

			c.execute("SELECT * from items WHERE name=?", (person,))
			conn.commit()
			fishing = c.fetchone()
			await ctx.send("{} You started fishing... ({:,.0f}sec cool down)".format(mention, timesleep))
			await asyncio.sleep(timesleep)
			c.execute("UPDATE items SET name=?, cod=?, fishing=0 WHERE name=?", (person, float(fishamm)+float(fishget), person))
			conn.commit()
			levelyn = getexp(person, randexp)

			try:
				if fishget < 2:
					if levelyn == 1:
						await ctx.send("{} caught {:,.0f} {} <:fish:662055365449351168>!".format(mention, fishget, fishtype), file=discord.File(f'img/fish/{randomimg}'))
						await ctx.send(f"{mention} You Leveled up!")
					else:
						await ctx.send("{} caught {:,.0f} {} <:fish:662055365449351168>!".format(mention, fishget, fishtype), file=discord.File(f'img/fish/{randomimg}'))
				else:
					if getlevelyn == 1:
						await ctx.send("{} caught {:,.0f} {}'s <:fish:662055365449351168>!".format(mention, fishget, fishtype), file=discord.File(f'img/fish/{randomimg}'))
						await ctx.send(f"{mention} You Leveled up!")
					else:
						await ctx.send("{} caught {:,.0f} {}'s <:fish:662055365449351168>!".format(mention, fishget, fishtype), file=discord.File(f'img/fish/{randomimg}'))
			except:
				if fishget < 2:
					if levelyn == 1:
						await ctx.send("{} caught {:,.0f} {} <:fish:662055365449351168>!".format(mention, fishget, fishtype))
						await ctx.send(f"{mention} You Leveled up!")
					else:
						await ctx.send("{} caught {:,.0f} {} <:fish:662055365449351168>!".format(mention, fishget, fishtype))
				else:
					if levelyn == 1:
						await ctx.send("{} caught {:,.0f} {}'s <:fish:662055365449351168>!".format(mention, fishget, fishtype))
						await ctx.send(f"{mention} You Leveled up!")
					else:
						await ctx.send("{} caught {:,.0f} {}'s <:fish:662055365449351168>!".format(mention, fishget, fishtype))

			fishing = c.fetchone()
			log(ctx, f'caught {fishget} fish')
		else:
			await ctx.send("You're already fishing!")


	@commands.command(aliases=['lvl', 'l'])
	async def level(self, ctx):
		easylog(ctx)
		person = str(ctx.author.id)
		personhandler(person)
		c.execute("SELECT * from levels WHERE name=?", (person,))
		conn.commit()
		fetchlevel = c.fetchall()
		level = fetchlevel[0][1]
		exp = fetchlevel[0][2]
		levelingform = level**int(level/4)
		exppercent = round((exp/levelingform), 2)
		if math.isclose(exppercent, 0.00, abs_tol=0.10):
			v1 = ":white_large_square:"
			v2 = ":white_large_square:"
			v3 = ":white_large_square:"
			v4 = ":white_large_square:"
			v5 = ":white_large_square:"
			embed=discord.Embed(title="Leveling", color=0x09a600)
			embed.add_field(name=f"You're level {level}", value=f"{v1}{v2}{v3}{v4}{v5} ~{exppercent*100}%", inline=False)
			embed.add_field(name=f"You need {levelingform} exp to Level up", value=f"You have {exp} exp", inline=False)
			embed.add_field(name=f"To get to Level {level+1}", value=f"You need {levelingform-exp} exp to level up!", inline=False)
			embed.set_author(name="Upvote The Bot!", url="https://top.gg/bot/627932116319076353/vote", icon_url=str(ctx.author.avatar_url))
			await ctx.send(embed=embed)
		elif math.isclose(exppercent, 0.20, abs_tol=0.10):
			v1 = ":green_square:"
			v2 = ":white_large_square:"
			v3 = ":white_large_square:"
			v4 = ":white_large_square:"
			v5 = ":white_large_square:"
			embed=discord.Embed(title="Leveling", color=0x09a600)
			embed.add_field(name=f"You're level {level}", value=f"{v1}{v2}{v3}{v4}{v5} ~{exppercent*100}%", inline=False)
			embed.add_field(name=f"You need {levelingform} exp to Level up", value=f"You have {exp} exp", inline=False)
			embed.add_field(name=f"To get to Level {level+1}", value=f"You need {levelingform-exp} exp to level up!", inline=False)
			embed.set_author(name="Upvote The Bot!", url="https://top.gg/bot/627932116319076353/vote", icon_url=str(ctx.author.avatar_url))
			await ctx.send(embed=embed)
		elif math.isclose(exppercent, 0.40, abs_tol=0.10):
			v1 = ":green_square:"
			v2 = ":green_square:"
			v3 = ":white_large_square:"
			v4 = ":white_large_square:"
			v5 = ":white_large_square:"
			embed=discord.Embed(title="Leveling", color=0x09a600)
			embed.add_field(name=f"You're level {level}", value=f"{v1}{v2}{v3}{v4}{v5} ~{exppercent*100}%", inline=False)
			embed.add_field(name=f"You need {levelingform} exp to Level up", value=f"You have {exp} exp", inline=False)
			embed.add_field(name=f"To get to Level {level+1}", value=f"You need {levelingform-exp} exp to level up!", inline=False)
			embed.set_author(name="Upvote The Bot!", url="https://top.gg/bot/627932116319076353/vote", icon_url=str(ctx.author.avatar_url))
			await ctx.send(embed=embed)
		elif math.isclose(exppercent, 0.60, abs_tol=0.10):
			v1 = ":green_square:"
			v2 = ":green_square:"
			v3 = ":green_square:"
			v4 = ":white_large_square:"
			v5 = ":white_large_square:"
			embed=discord.Embed(title="Leveling", color=0x09a600)
			embed.add_field(name=f"You're level {level}", value=f"{v1}{v2}{v3}{v4}{v5} ~{exppercent*100}%", inline=False)
			embed.add_field(name=f"You need {levelingform} exp to Level up", value=f"You have {exp} exp", inline=False)
			embed.add_field(name=f"To get to Level {level+1}", value=f"You need {levelingform-exp} exp to level up!", inline=False)
			embed.set_author(name="Upvote The Bot!", url="https://top.gg/bot/627932116319076353/vote", icon_url=str(ctx.author.avatar_url))
			await ctx.send(embed=embed)
		elif math.isclose(exppercent, 0.80, abs_tol=0.10):
			v1 = ":green_square:"
			v2 = ":green_square:"
			v3 = ":green_square:"
			v4 = ":green_square:"
			v5 = ":white_large_square:"
			embed=discord.Embed(title="Leveling", color=0x09a600)
			embed.add_field(name=f"You're level {level}", value=f"{v1}{v2}{v3}{v4}{v5} ~{exppercent*100}%", inline=False)
			embed.add_field(name=f"You need {levelingform} exp to Level up", value=f"You have {exp} exp", inline=False)
			embed.add_field(name=f"To get to Level {level+1}", value=f"You need {levelingform-exp} exp to level up!", inline=False)
			embed.set_author(name="Upvote The Bot!", url="https://top.gg/bot/627932116319076353/vote", icon_url=str(ctx.author.avatar_url))
			await ctx.send(embed=embed)
		elif math.isclose(exppercent, 1.00, abs_tol=0.10):
			v1 = ":green_square:"
			v2 = ":green_square:"
			v3 = ":green_square:"
			v4 = ":green_square:"
			v5 = ":green_square:"
			embed=discord.Embed(title="Leveling", color=0x09a600)
			embed.add_field(name=f"You're level {level}", value=f"{v1}{v2}{v3}{v4}{v5} ~{exppercent*100}%", inline=False)
			embed.add_field(name=f"You need {levelingform} exp to Level up", value=f"You have {exp} exp", inline=False)
			embed.add_field(name=f"To get to Level {level+1}", value=f"You need {levelingform-exp} exp to level up!", inline=False)
			embed.set_author(name="Upvote The Bot!", url="https://top.gg/bot/627932116319076353/vote", icon_url=str(ctx.author.avatar_url))
			await ctx.send(embed=embed)

	@commands.command()
	async def status(self, ctx):
		easylog(ctx)
		ping1 = self.bot.latencies
		ping = round(ping1[0][1]*1000, 1)
		cpu = psutil.cpu_percent()
		ram = psutil.virtual_memory()
		embed=discord.Embed(title="Status")
		embed.add_field(name="Ping", value=("%gms" % (float(ping))), inline=True)
		embed.add_field(name="CPU Usage", value=f"{cpu}%", inline=True)
		embed.add_field(name="RAM Usage", value=f"{ram[2]}%", inline=True)
		embed.add_field(name="Discord", value="[Click here to invite](https://discordapp.com/api/oauth2/authorize?client_id=627932116319076353&permissions=1812462657&scope=bot)", inline=True)
		embed.add_field(name="Trello", value="[Click here to go to Trello](https://trello.com/b/rzd1Y7C6/fishing-bot-thing)", inline=True)
		embed.add_field(name="Github", value="[Click here to go to Github](https://github.com/LonnonjamesD/EconomyBot)", inline=True)
		embed.add_field(name="DONATE!", value="[Donate $$$](https://www.patreon.com/Lonnon)", inline=True)
		embed.set_author(name="Upvote The Bot!", url="https://top.gg/bot/627932116319076353/vote", icon_url=str(ctx.author.avatar_url))
		await ctx.send(embed=embed)

	@commands.command()
	async def invite(self, ctx):
		easylog(ctx)
		await ctx.send(f"{ctx.author.mention} Do `f!status` to see invite link")

	@commands.command()
	async def vote(self, ctx):
		easylog(ctx)
		await ctx.send("https://top.gg/bot/627932116319076353/vote")

#===========================================================================================================#

#===========================================================================================================#
#                                Shop Group
#=======================================================================================================.avatar

	@commands.group(aliases=['sh'])
	async def shop(self, ctx):
		easylog(ctx)
		if ctx.invoked_subcommand is None:
			embed=discord.Embed(title="Shop")
			embed.add_field(name="Hairdryer `hairdryer` [Buy/Sell]", value="5<:coin:662071327242321942>/2<:coin:662071327242321942>", inline=False)
			embed.add_field(name="Fish `fish` [Sell]", value="0.25<:coin:662071327242321942>", inline=False)
			embed.add_field(name="Iron rod `ironrod` [Buy]", value="150<:coin:662071327242321942>", inline=False)
			embed.add_field(name="Luv Rod `luvrod` [Can't Buy]", value="1000<:coin:662071327242321942>", inline=False)
			embed.set_author(name="Upvote The Bot!", url="https://top.gg/bot/627932116319076353/vote", icon_url=ctx.author.avatar_url)
			await ctx.send(embed=embed)
			await ctx.send(f"{ctx.author.mention} For more info do `[] = optional, <> = required` `f!shop <buy or sell or info> <item> [amount]`")


	@shop.command()
	async def buy(self, ctx, item, amount):
		arg1 = item
		arg2 = amount
		easylog(ctx)
		mention = ctx.author.mention
		person = str(ctx.author.id)
		personhandler(person)
		c.execute("SELECT * from people where name=?", (person,))
		conn.commit()
		e = c.fetchone()
		c.execute("SELECT * from items where name=?", (person,))
		conn.commit()
		d = c.fetchone()
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
				fishing = c.fetchone()
				log(ctx, f'bought {str(arg2)} {str(arg1)}(s)')
			else:
				await ctx.send("Sorry you don't have enough coins!")
		elif arg11 == 'ironrod':
			c.execute("SELECT * from items where name=?", (person,))
			conn.commit()
			e = c.fetchone()
			if str(d[3]) != 'ironrod':
				if float(coins) >= float(150):
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
					fishing = c.fetchone()
					log(ctx, f'bought {str(arg2)} {str(arg1)}(s)')
				else:
					await ctx.send(f"{ctx.author.mention} Sorry you don't have enough coins!")
			else:
				await ctx.send(f"{ctx.author.mention} You already have the iron rod!")
		else:
			
			embed=discord.Embed(title="Shop", color=0x50fe54)
			embed.add_field(name="Invalid Item", value="Sorry that isn't an item...", inline=True)
			embed.set_author(name="Upvote The Bot!", url="https://top.gg/bot/627932116319076353/vote", icon_url=ctx.author.avatar_url)
			await ctx.send(embed=embed)


	@shop.command()
	async def sell(self, ctx, item, amount):
		arg1 = item
		arg2 = amount
		easylog(ctx)
		mention = ctx.author.mention
		person = str(ctx.author.id)
		personhandler(person)
		argtwo = arg2
		c.execute("SELECT * from items WHERE name=?", (person,))
		conn.commit()
		fishing = c.fetchone()
		if str(arg1) == 'cod':
			fishing1 = fishing[1]
			fishing2 = fishing[10]
			fishing = c.fetchone()
			if int(fishing1) >= int(arg2):
				c.execute("SELECT * from people WHERE name=?", (person,))
				conn.commit()
				money = c.fetchone()
				moneyrn = float(money[1])
				moneyget = float(arg2)*0.25
				moneyearned = float(moneyrn) + float(moneyget)

				newfishbal = int(fishing1) - int(arg2)

				c.execute("UPDATE items SET name=?, cod=?, fishing=? WHERE name=?", (person, newfishbal, fishing2, person))
				conn.commit()
				c.execute("UPDATE people SET name=?, coins=? WHERE name=?", (person, float(moneyearned), person))
				conn.commit()
				await ctx.send(f"{mention} Sold " + str(argtwo) + f" <:fish:662055365449351168> for {str(moneyget)} ")
				fishing = c.fetchone()
				log(ctx, f'solded {str(argtwo)} {str(arg1)} for {str(moneyget)} <:coin:662071327242321942>')
			elif float(fishing2) < float(arg2):
				await ctx.send(f"{mention} You don't have that many fish!")
		else:
			await ctx.send(f"{mention} You can't sell that!")

	@commands.command(name="sell")
	async def sell_(self, ctx, item, amount):
		command = self.bot.get_command("shop sell")
		await ctx.invoke(command, item, amount)

	@commands.command(name="buy")
	async def buy_(self, ctx, item, amount):
		command = self.bot.get_command("shop buy")
		await ctx.invoke(command, item, amount)

	@shop.command()
	async def info(self, ctx, item):
		easylog(ctx)
		arg1 = str(arg.lower())
		if arg1 == 'all':
			embed=discord.Embed(title="Shop")
			embed.add_field(name="Hairdryer `hairdryer` [Buy/Sell]", value="5<:coin:662071327242321942>/2<:coin:662071327242321942>", inline=False)
			embed.add_field(name="Fish `fish` [Sell]", value="0.25<:coin:662071327242321942>", inline=False)
			embed.add_field(name="Iron rod `ironrod` [Buy]", value="25<:coin:662071327242321942>", inline=False)
			embed.set_author(name="Upvote The Bot!", url="https://top.gg/bot/627932116319076353/vote", icon_url=ctx.author.avatar_url)
			await ctx.send(embed=embed)
		elif arg1 == 'hairdryer':
			embed=discord.Embed(title="Info", color=0x50fe54)
			embed.add_field(name="Hairdryer", value="5<:coin:662071327242321942>", inline=False)
			embed.add_field(name="Description", value="When used can get you 3 - 25 fish!", inline=True)
			embed.set_author(name="Upvote The Bot!", url="https://top.gg/bot/627932116319076353/vote", icon_url=ctx.author.avatar_url)
			await ctx.send(embed=embed)
		else:
			embed=discord.Embed(title="Info", color=0x50fe54)
			embed.add_field(name="Invalid Item", value="Sorry that isn't an item...", inline=True)
			embed.set_author(name="Upvote The Bot!", url="https://top.gg/bot/627932116319076353/vote", icon_url=ctx.author.avatar_url)
			await ctx.send(embed=embed)
			
			embed=discord.Embed(title="Shop", color=0x50fe54)
			embed.add_field(name="Invalid Item", value="Sorry that isn't an item...", inline=True)
			embed.set_author(name="Upvote The Bot!", url="https://top.gg/bot/627932116319076353/vote", icon_url=ctx.author.avatar_url)
			await ctx.send(embed=embed)


#===========================================================================================================#

#===========================================================================================================#
#                                Inventory Group
#===========================================================================================================#

	@commands.group(aliases=['i', 'inv'])
	async def inventory(self, ctx):
		easylog(ctx)
		if ctx.invoked_subcommand is None:
			person = str(ctx.author.id)
			personhandler(person)
			c.execute("SELECT * from items WHERE name=?", (person,))
			conn.commit()
			fetch0 = c.fetchall()
			c.execute("SELECT * from inventory where name=?", (person,))
			conn.commit()
			fetch1 = c.fetchall()
			fetchall = fetch1[0]
			check = 0
			toc = ('name', 'hairdryer')
			lentoc = len(toc) 
			embed=discord.Embed(title="Inventory", color=0x50fe54)
			while check != lentoc:
				check += 1
				if fetchall[check-1] == 0 or fetchall[check-1] == str(ctx.author.id):
					pass
				elif fetchall[check-1] != 0 or fetchall[check-1] != str(ctx.author.id):
					itemname1 = toc[check-1].capitalize()
					itemammount = fetchall[check-1]
					if itemammount > 1:
						embed.add_field(name=itemname1, value="You have {:,.0f} {}s".format(itemammount, itemname1), inline=False)
						embed.set_author(name="Upvote The Bot!", url="https://top.gg/bot/627932116319076353/vote", icon_url=str(ctx.author.avatar_url))
					else:
						embed.add_field(name=itemname1, value="You have {:,.0f} {}".format(itemammount, itemname1), inline=False)
						embed.set_author(name="Upvote The Bot!", url="https://top.gg/bot/627932116319076353/vote", icon_url=str(ctx.author.avatar_url))
			await ctx.send(embed=embed)
			await ctx.send(f"{ctx.author.mention}  Do `f!inventory info <item>` for more info")

	@inventory.command(name='info')
	async def info1(self, ctx):
		easylog(ctx)
		person = str(ctx.author.id)
		personhandler(person)
		c.execute("SELECT * from items WHERE name=?", (person,))
		conn.commit()
		fetch0 = c.fetchall()
		c.execute("SELECT * from inventory where name=?", (person,))
		conn.commit()
		fetch1 = c.fetchall()
		fetchall = fetch1[0]
		check = 0
		toc = ('name', 'hairdryer')
		lentoc = len(toc) 
		embed=discord.Embed(title="Inventory", color=0x50fe54)
		while check != lentoc:
			check += 1
			if fetchall[check-1] == 0 or fetchall[check-1] == str(ctx.author.id):
				pass
			elif fetchall[check-1] != 0 or fetchall[check-1] != str(ctx.author.id):
				itemname1 = toc[check-1].capitalize()
				itemammount = fetchall[check-1]
				if itemammount > 1:
					embed.add_field(name=itemname1, value="You have {:,.0f} {}s".format(itemammount, itemname1), inline=False)
					embed.set_author(name="Upvote The Bot!", url="https://top.gg/bot/627932116319076353/vote", icon_url=str(ctx.author.avatar_url))
				else:
					embed.add_field(name=itemname1, value="You have {:,.0f} {}".format(itemammount, itemname1), inline=False)
					embed.set_author(name="Upvote The Bot!", url="https://top.gg/bot/627932116319076353/vote", icon_url=str(ctx.author.avatar_url))
		await ctx.send(embed=embed)

	@inventory.command()
	async def use(self, ctx, arg1):
		easylog(ctx)
		arg = arg1.lower()
		person = str(ctx.author.id)
		personhandler(person)
		c.execute("SELECT * from inventory where name=?", (person,))
		conn.commit()
		fetch0 = c.fetchall()
		fetchall = fetch0[0]
		toc = ('hairdryer')
		if arg in toc:
			if fetchall[int(arg in toc)] >= 1:
				c.execute("UPDATE inventory SET name=?, {}=? WHERE name=?".format(arg), (person, int(fetchall[1])-1, person))
				conn.commit()
				if arg == 'hairdryer':
					c.execute("SELECT * from items where name=?", (person,))
					conn.commit()
					fish1 = c.fetchall()
					fishamm = fish1[0]
					randint = random.randint(3,25)
					c.execute("UPDATE items SET name=?, cod=? WHERE name=?", (person, fishamm[1], person))
					conn.commit()
					await ctx.send(f"{ctx.author.mention} You got {randint} fish!")
				else:
					await ctx.send("HACKER?!!?!?!?!?!?")
			else:
				await ctx.send("You don't have enough of that item!")
		else:
			await ctx.send("You don't have that item")

#===========================================================================================================#

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
		c.execute("INSERT INTO items (name, cod, tuna, salmon, catfsh, redsnapper, raingbowtrout, trout, bass, sardine, fishing, fishingrods) VALUES (?, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ?)", (person, rod))
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

def getexp(person, randexp):
	c.execute("SELECT * from levels WHERE name=?", (person,))
	conn.commit()
	fetchlevel = c.fetchall()
	fetchlevel1 = (fetchlevel[0])[1]
	fetchlevel2 = (fetchlevel[0])[2]
	c.execute("UPDATE levels SET name=?, level=?, exp=? WHERE name=?", (person, fetchlevel1, int(fetchlevel2)+randexp, person))
	conn.commit()
	if checklevel(person) == 1:
		return 1
	else:
		return 0



def checklevel(person):
	c.execute("SELECT * from levels WHERE name=?", (person,))
	conn.commit()
	fetchlevel = c.fetchall()
	fetchlevel11 = fetchlevel[0][1]
	fetchlevel22 = fetchlevel[0][2]
	fetchlevel1 = int(fetchlevel11)
	fetchlevel2 = int(fetchlevel22)
	if str(fetchlevel1) == '0':
		c.execute("UPDATE levels SET name=?, level=?, exp=? WHERE name=?", (person, 1, int(fetchlevel2), person))
		conn.commit()
		return 0
	elif str(fetchlevel1) != '0':
		levelingform = fetchlevel1**int(fetchlevel1/4)
		if int(fetchlevel2) >= levelingform:
			c.execute("UPDATE levels SET name=?, level=?, exp=? WHERE name=?", (person, int(fetchlevel1)+1, int(fetchlevel2)-int(levelingform), person))
			conn.commit()
			return 1

def houseformat(person):
	c.execute("SELECT * from house WHERE name=?", (person,))
	conn.commit()
	fetchall = c.fetchall()
	fetchall = fetchall[0]

def log(ctx, logtext : str):
	os.chdir('C:/Users/Lemon/Desktop/EconomyBot/logs')
	log = open("log{}.log".format(rannumber), "a", encoding='utf-8')
	os.chdir('C:/Users/Lemon/Desktop/EconomyBot')
	now = datetime.now()
	ct = now.strftime("%H:%M:%S")
	person = str(ctx.author.id)
	log.write(f"\n{ct} | {ctx.author} {person} {logtext}")
	log.close()

def easylog(ctx):
	os.chdir('C:/Users/Lemon/Desktop/EconomyBot/logs') 
	log = open("log{}.log".format(rannumber), "a", encoding='utf-8')
	os.chdir('C:/Users/Lemon/Desktop/EconomyBot')
	now = datetime.now()
	ct = now.strftime("%H:%M:%S")
	person = str(ctx.author.id)
	log.write(f"\n{ct} | {ctx.author} {person} uses {ctx.command}")
	log.close()

def setup(bot):
	print('GeneralCommands')
	bot.add_cog(general(bot))