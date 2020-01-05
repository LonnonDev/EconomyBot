import time
import json
import random
import discord
import os
import sys
from discord.ext import commands
from config import *
import asyncio
from datetime import datetime
import sqlite3
from uuid import uuid4
import psutil

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
# Options
shardids = 1
shardcount = 1
initial_extensions = ['cogs.generalcommands']
commandprefix = ('f!', 'f! ', 'f1', 'f1 ', 'F1', 'F!')
#====================#

#====================#
bot = commands.AutoShardedBot(command_prefix=commandprefix, case_insensitive=True, loop=None, shard_id=shardids, shard_count=shardcount)
for extension in initial_extensions:
	bot.load_extension(extension)
print('Main Loaded, with {} shard(s)'.format(shardcount))
#====================#
#py C:\Users\Lemon\Desktop\EconomyBot\bot.py 1

class owner(commands.Cog, name="Owner Only"):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(aliases=['reload'])
	@commands.is_owner()
	async def reloadextension(self, ctx):
		await ctx.send("Reloaded Extensions")
		for extension in initial_extensions:
			bot.reload_extension(extension)

class MyHelpCommand(commands.MinimalHelpCommand):
	def get_command_signature(self, command):
		return '{0.clean_prefix}{1.qualified_name} {1.signature}'.format(self, command)

class MyCog(commands.Cog):
	def __init__(self, bot):
		self._original_help_command = bot.help_command
		bot.help_command = MyHelpCommand()
		bot.help_command.cog = self

	def cog_unload(self):
		self.bot.help_command = self._original_help_command



#===============================#
bot.add_cog(MyCog(bot))
bot.add_cog(owner(bot))
bot.run(config)
#===============================#