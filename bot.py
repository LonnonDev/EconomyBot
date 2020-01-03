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
from uuid import uuid4

os.chdir('C:/Users/Lemon/Desktop/EconomyBot')
bottype = len(sys.argv) - 1

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
		fishing interger
		)""")

c.execute("""CREATE TABLE IF NOT EXISTS inventory (
		name blob,
		hairdryer blob
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
#====================#
# Shards
shardids = 1
shardcount = 1
#====================#

#====================#
import generalcommands
def setup():
	if bottype == 1:
		bot =  commands.AutoShardedBot(command_prefix='gb', case_insensitive=True, loop=None)
	elif bottype == 0:
		bot = commands.AutoShardedBot(command_prefix='bb', case_insensitive=True, loop=None, shard_id=shardids, shard_count=shardcount)
	if bottype == 1:
		print('epic0')
		bot.run(config)
	elif bottype == 0:
		print('epic1')
		bot.run(config2)
setup()
#====================#
#py C:\Users\Lemon\Desktop\EconomyBot\bot.py 1