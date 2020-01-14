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
from tokengamer import *
import itertools


class CommandErrorHandler(commands.Cog, name="ErrorHandler"):
	def __init__(self, bot):
		self.bot = bot
	
	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send("Missing Required Argument")
		elif isinstance(error, commands.BadArgument):
			await ctx.send("Bad Argument")	
		elif isinstance(error, commands.CommandNotFound):
			await ctx.send(f"That is **NOT** a command.")

		print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
		traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)		

def setup(bot):
	print("ErrorHandler")
	bot.add_cog(CommandErrorHandler(bot))