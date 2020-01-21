import traceback
import sys
from discord.ext import commands
import discord
import time
import json
import random
import os
import asyncio
from datetime import datetime
import sqlite3
from uuid import uuid4
import psutil
import itertools
os.chdir('C:/Users/Lemon/Desktop/EconomyBot')

conn = sqlite3.connect("users.db")
c = conn.cursor()

c.execute("SELECT * from ran")
fetchone = c.fetchone()
rannumber = int(fetchone[0])


class CommandErrorHandler(commands.Cog, name="ErrorHandler"):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send("Missing Required Argument")
		elif isinstance(error, commands.BadArgument):
			await ctx.send("Bad Argument")
		elif isinstance(error, commands.MissingPermissions):
			await ctx.send("Missing Permissions")
		elif isinstance(error, commands.CheckFailure):
			await ctx.send("You don't have required permissions")
		elif isinstance(error, commands.CommandOnCooldown):
			await ctx.send('You are on a cooldown. Try again in {:.2f}s'.format(error.retry_after))

		ctx.author = 'console'
		erro = traceback.format_exception(type(error), error, error.__traceback__)
		dw = ''
		error = dw.join(erro)
		log(ctx, '\n\nIgnoring exception in command {}:'.format(ctx.command))
		log(ctx, error)

def log(ctx, logtext):
	os.chdir('C:/Users/Lemon/Desktop/EconomyBot/errorlogs')
	errorlog = open("errorlog{}.log".format(rannumber), "a", encoding='utf-8')
	os.chdir('C:/Users/Lemon/Desktop/EconomyBot')
	now = datetime.now()
	ct = now.strftime("%H:%M:%S")
	if ctx.author == 'console':
		person = ''
	else:
		person = str(ctx.author.id)
	errorlog.write(f"\n{ct} | {ctx.author} {person} {logtext}")
	errorlog.close()

def setup(bot):
	print("ErrorHandler")
	bot.add_cog(CommandErrorHandler(bot))