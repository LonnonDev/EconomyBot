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
import itertools
os.chdir('C:/Users/Lemon/Desktop/EconomyBot')


class beta(commands.Cog, name='Beta Commands'):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def bait(self, ctx):
		pass

	@commands.command()
	async def controlledfish(self, ctx):
		pass




def setup(bot):
	print('Beta')
	bot.add_cog(beta(bot))