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
from tokengamer import *
import itertools
import shutil
import dbl

os.chdir('C:/Users/Lemon/Desktop/EconomyBot')
bottype = list(sys.argv)
print(bottype)

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
		fish real,
		fishing real
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

c.execute("UPDATE items SET fishing=0")
conn.commit()
aaaaaaaaaaaasdsaddsdsa="standard"
c.execute("UPDATE items SET fishingrods=?", (aaaaaaaaaaaasdsaddsdsa,))
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
splashesfile = open('splash.es', 'r', encoding="utf8")
#   list(str(splashesfile.read()).split("-"))
splashes = list(str(splashesfile.read()).split("-"))
initial_extensions = ['cogs.generalcommands', 'cogs.errorhandling', 'cogs.ownercommands', 'cogs.helpcommand', 'cogs.eventcommands', 'cogs.funcommands']
commandprefix = ('f! ', 'f1 ', 'F! ', 'F1 ', 'f!', 'f1', 'F1', 'F!')
#====================#

#====================#
bot = commands.AutoShardedBot(case_insensitive=True, loop=None, shard_id=shardids, shard_count=shardcount, command_prefix=commands.when_mentioned_or(*commandprefix))
for extension in initial_extensions:
	bot.load_extension(extension)
print('Main Loaded, with {} shard(s)'.format(shardcount))
#====================#
#py C:\Users\Lemon\Desktop\EconomyBot\bot.py
#===============================#


c.execute("SELECT * from ran")
fetchone = c.fetchone()
rannumber = int(fetchone[0])+1
c.execute("UPDATE ran SET ran=?", (rannumber,))
conn.commit()

os.chdir('C:/Users/Lemon/Desktop/EconomyBot/logs')
log = open("log{}.log".format(rannumber), "a+", encoding='utf-8')
f = log
os.remove("log{}.log".format(rannumber-3))
os.chdir('C:/Users/Lemon/Desktop/EconomyBot')
now = datetime.now()
ct = now.strftime("%H:%M:%S")
f.write(f"Log{rannumber}.log | {ct}\n")
f.close()
rannum = str(rannumber).zfill(3)
print('Version {}.{}.{}'.format(str(rannum)[0], str(rannum)[1], str(rannum)[2]))
version = 'Version {}.{}.{}'.format(str(rannum)[0], str(rannum)[1], str(rannum)[2])

splashran1 = random.randint(0,len(splashes)-1)
game=discord.Game(f'{version} | {splashes[splashran1]}') 

@bot.event
async def on_ready():
	await bot.change_presence(status=discord.Status.online, activity=game)



bot.run(config)
#===============================#