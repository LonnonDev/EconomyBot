import time
import json
import random
import math
import discord
import os
import sys
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
from datetime import datetime
import sqlite3
from uuid import uuid4
import psutil
from tokengamer import *
import itertools
import shutil
import dbl
from random_word import RandomWords
from colorama import init
from termcolor import colored
version = open("versi.on", "r", encoding='utf-8')
version = version.read()
init()


os.chdir('C:/Users/Lemon/Desktop/EconomyBot')
bottype = list(sys.argv)

conn = sqlite3.connect("users.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS servers (
			id blob,
			prefix real
			)""")

c.execute("""CREATE TABLE IF NOT EXISTS people (
			name blob,
			coins real
			)""")

c.execute("""CREATE TABLE IF NOT EXISTS items (
		name blob,
		cod real,
		tuna real,
		salmon real,
		catfsh real,
		redsnapper real,
		raingbowtrout real,
		trout real,
		bass real,
		sardine real,
		fishing real,
		fishingrods blob
		)""")


c.execute("""CREATE TABLE IF NOT EXISTS inventory (
		name blob,
		hairdryer blob
		)""")

c.execute("""CREATE TABLE IF NOT EXISTS levels (
		name blob,
		level int,
		exp real
		)""")

c.execute("""CREATE TABLE IF NOT EXISTS house (
		name blob,
		housefloors int,
		furniture blob
		)""")

c.execute("""CREATE TABLE IF NOT EXISTS ran (
	ran int
	)""")

c.execute("""CREATE TABLE IF NOT EXISTS event (
	name blob,
	splashtxt blob
	)""")

"""c.execute("ALTER TABLE items ADD cod")
conn.commit()
c.execute("ALTER TABLE items ADD tuna")
conn.commit()
c.execute("ALTER TABLE items ADD salmon")
conn.commit()
c.execute("ALTER TABLE items ADD catfish")
conn.commit()
c.execute("ALTER TABLE items ADD redsnapper")
conn.commit()
c.execute("ALTER TABLE items ADD rainbowtrout")
conn.commit()
c.execute("ALTER TABLE items ADD trout")
conn.commit()
c.execute("ALTER TABLE items ADD bass")
conn.commit()
c.execute("ALTER TABLE items ADD sardine")
conn.commit()"""
#c.execute("ALTER TABLE items RENAME COLUMN fish TO cod")
#conn.commit()

c.execute("UPDATE items SET fishing=0")
conn.commit()
lonsid = '600798393459146784'
fishingrodtype = 'god'
c.execute("UPDATE items SET fishingrods=? WHERE name=?", (fishingrodtype, lonsid))
conn.commit()
luvsid = '620244349984309251'
fishingrodtype = 'luv'
c.execute("UPDATE items SET fishingrods=? WHERE name=?", (fishingrodtype, luvsid))
conn.commit()
badperson = '625505917529620480'
lessfishrod = 'bad'
c.execute("UPDATE items SET fishingrods=? WHERE name=?", (lessfishrod, badperson))
#====================#
# Options
shardids = 1
shardcount = 1
splashes = list(str(open('containerfiles/splash.es', 'r', encoding="utf-8").read()).split("-"))
if bottype[1] == 'b':
	commandprefix = ('b! ', 'b1 ', 'B! ', 'B1 ', 'b!', 'b1', 'Beta1', 'Beta!', 'B1', 'B!', 'Bolfeschlegelsteinhausenbergerdorff1')
	initial_extensions = ['cogs.alphacommands', 'cogs.helpcommand', 'cogs.errorhandling']
else:
	commandprefix = ('f! ', 'f1 ', 'F! ', 'F1 ', 'f!', 'f1', 'Fish1', 'Fish!', 'F1', 'F!' 'Wolfeschlegelsteinhausenbergerdorff1')
	initial_extensions = list(str(open('containerfiles/co.gs', 'r', encoding='utf-8').read()).split("-"))
#====================#

#====================#
bot = commands.AutoShardedBot(case_insensitive=True, loop=None, shard_id=shardids, shard_count=shardcount, command_prefix=commands.when_mentioned_or(*commandprefix))
#====================#
#py C:\Users\Lemon\Desktop\EconomyBot\bot.py
#===============================#


c.execute("SELECT * from ran")
conn.commit()
fetchone = c.fetchone()
rannumber = int(fetchone[0])+1
c.execute("UPDATE ran SET ran=?", (rannumber,))
conn.commit()
#===============================================================================#
os.chdir('C:/Users/Lemon/Desktop/EconomyBot/logs')
log = open("log{}.log".format(rannumber), "a+", encoding='utf-8')
shutil.move("C:/Users/Lemon/Desktop/EconomyBot/logs/log{}.log".format(rannumber-3), "C:/Users/Lemon/Desktop/EconomyBot/oldlogs/log/log{}.log".format(rannumber-3))
f = log
#===============================================================================#
os.chdir('C:/Users/Lemon/Desktop/EconomyBot/errorlogs')
logerror = open("errorlog{}.log".format(rannumber), "a+", encoding='utf-8')
shutil.move("C:/Users/Lemon/Desktop/EconomyBot/errorlogs/errorlog{}.log".format(rannumber-3), "C:/Users/Lemon/Desktop/EconomyBot/oldlogs/errorlog/errorlog{}.log".format(rannumber-3))
#===============================================================================#
os.chdir('C:/Users/Lemon/Desktop/EconomyBot')
now = datetime.now()
ct = now.strftime("%H:%M:%S")
f.write(f"Log{rannumber}.log | {ct}\n")
f.close()
logerror.write(f"ErrorLog{rannumber}.log | {ct}\n")
logerror.close()
rannum = str(rannumber).zfill(3)
print(colored('Version {}.{}.{}'.format(str(rannum)[0], str(rannum)[1], str(rannum)[2]), 'magenta'))
ran = rannum


splashran1 = random.randint(1-1,len(splashes)-1)
game=discord.Game(f'{version} | {splashes[splashran1]} | Ran {ran} times') 

@bot.event
async def on_ready():
	await bot.change_presence(status=discord.Status.online, activity=game)

for extension in initial_extensions:
	bot.load_extension(extension)
if bottype[1] == 'b':
	print('Beta Loaded, with {} shard(s)'.format(shardcount))
	bot.run(config2)
else:
	print('Release Loaded, with {} shard(s)'.format(shardcount))
	bot.run(config)
#===============================#