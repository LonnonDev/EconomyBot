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
from uuid import uuid4
import psutil
import itertools
from tokengamer import *


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

class MyHelpCommand(commands.DefaultHelpCommand):
	async def send_bot_help(self, mapping):
		ctx = self.context
		bot = ctx.bot

		if bot.description:
			# <description> portion
			self.paginator.add_line(bot.description, empty=True)

		no_category = "No Category:"
		def get_category(command, *, no_category=no_category):
			cog = command.cog
			return cog.qualified_name + ':' if cog is not None else no_category

		filtered = await self.filter_commands(bot.commands, sort=True, key=get_category)
		max_size = self.get_max_size(filtered)
		to_iterate = itertools.groupby(filtered, key=get_category)

		# Now we can add the commands to the page.
		embed=discord.Embed(title="--------------------")
		for category, commands in to_iterate:
			commands = sorted(commands, key=lambda c: c.name) if self.sort_commands else list(commands)
			self.add_indented_commands(commands, heading=category, max_size=max_size)
			value = ", ".join([command.name for command in commands])
			commands = value
			embed.add_field(name=category, value=commands, inline=False)


		note = self.get_ending_note()
		if note:
			pass
		embed.set_footer(text=f"{note}")
		embed.set_author(name="Help")
		destination = self.get_destination()
		await destination.send(embed=embed)

	async def send_command_help(self, command):
		self.add_command_formatting(command)
		self.paginator.close_page()
		await self.send_pages()

	async def send_group_help(self, group):
		self.add_command_formatting(group)

		filtered = await self.filter_commands(group.commands, sort=self.sort_commands)
		self.add_indented_commands(filtered, heading=self.commands_heading)

		if filtered:
			note = self.get_ending_note()
			if note:
				self.paginator.add_line()
				self.paginator.add_line(note)

		await self.send_pages()

	async def send_cog_help(self, cog):
		if cog.description:
			self.paginator.add_line(cog.description, empty=True)

		filtered = await self.filter_commands(cog.get_commands(), sort=self.sort_commands)
		self.add_indented_commands(filtered, heading=self.commands_heading)

		note = self.get_ending_note()
		if note:
			self.paginator.add_line()
			self.paginator.add_line(note)

		await self.send_pages()



class MyCog(commands.Cog, name="Help"):
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