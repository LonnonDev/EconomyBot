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
		if isinstance(error, commands.CommandError):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.ConversionError):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.MissingRequiredArgument):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.ArgumentParsingError):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.UnexpectedQuoteError):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.InvalidEndOfQuotedStringError):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.ExpectedClosingQuoteError):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.BadArgument):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.BadUnionArgument):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.PrivateMessageOnly):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.NoPrivateMessage):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.CheckFailure):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.CheckAnyFailure):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.CommandNotFound):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.DisabledCommand):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.CommandInvokeError):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.TooManyArguments):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.UserInputError):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.CommandOnCooldown):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.MaxConcurrencyReached):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.NotOwner):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.MissingPermissions):
			await ctx.send("Missing Permissions Use this link to give me correct perms! https://discordapp.com/api/oauth2/authorize?client_id=627932116319076353&permissions=8&scope=bot")
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.BotMissingRole):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.MissingAnyRole):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.BotMissingAnyRole):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.NSFWChannelRequired):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.ExtensionError):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.ExtensionAlreadyLoaded):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.ExtensionNotLoaded):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.NoEntryPointError):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.ExtensionFailed):
			await ctx.send(f"{error}", delete_after=5)
		elif isinstance(error, commands.ExtensionNotFound):
			await ctx.message.delete()
			await ctx.send(f"{error}", delete_after=5)

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