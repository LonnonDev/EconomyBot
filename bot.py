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

if bottype == 1:
	bot = commands.Bot(command_prefix='gb', case_insensitive=True)
elif bottype == 0:
	bot = commands.Bot(command_prefix='bb', case_insensitive=True)



from generalcommands import *
bot.add_cog(general(bot))
if bottype == 1:
	print('epic0')
	bot.run(config)
elif bottype == 0:
	print('epic1')
	bot.run(config2)
#py C:\Users\Lemon\Desktop\EconomyBot\bot.py 1