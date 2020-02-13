import time
import json
import random
import math
import discord
import os
from os import listdir
from os.path import isfile, join
import sys
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
from datetime import datetime
import sqlite3
from uuid import uuid4
import psutil
import itertools
from discord.ext import menus

os.chdir('C:/Users/Lemon/Desktop/EconomyBot')

conn = sqlite3.connect("users.db")
c = conn.cursor()

c.execute("SELECT * from ran")
conn.commit()
fetchone = c.fetchone()
rannumber = int(fetchone[0])


class beta(commands.Cog, name='Beta Commands'):
	def __init__(self, bot):
		self.bot = bot 

	async def beta(ctx):
		# 234834826081992704 222388637541597185 109475170602729472 109496491072077824 164120455228293120 362255701323677713 488929293905428482 600798393459146784
		return ctx.author.id == 234834826081992704 or ctx.author.id == 222388637541597185 or ctx.author.id == 109475170602729472 or ctx.author.id == 109496491072077824 or ctx.author.id == 164120455228293120 or ctx.author.id == 362255701323677713 or ctx.author.id == 488929293905428482 or ctx.author.id == 600798393459146784

	@commands.command()
	@commands.check(beta)
	async def beta(self, ctx):
		await ctx.send('https://discordapp.com/api/oauth2/authorize?client_id=677309227131469824&permissions=1878523201&scope=bot')


def setup(bot):
	print('BetaCommands')
	bot.add_cog(beta(bot))