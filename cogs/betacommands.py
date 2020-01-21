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
import itertools
os.chdir('C:/Users/Lemon/Desktop/EconomyBot')


class beta(commands.Cog, name='Beta Commands'):
	def __init__(self, bot):
		self.bot = bot 

	async def beta(ctx):
		return ctx.author.id == 600798393459146784 or ctx.author.id == 362255701323677713 or ctx.author.id == 620244349984309251

	@commands.command()
	@commands.check(beta)
	async def bait(self, ctx):
		await ctx.send('test')

	@commands.command()
	async def controlledfish(self, ctx):
		pass




def setup(bot):
	print('BetaCommands')
	bot.add_cog(beta(bot))