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
from tokengamer import *
import itertools
import shutil
import dbl

class TopGG(commands.Cog):
	"""Handles interactions with the top.gg API"""

	def __init__(self, bot):
		self.bot = bot
		self.token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjYyNzkzMjExNjMxOTA3NjM1MyIsImJvdCI6dHJ1ZSwiaWF0IjoxNTc5MTI2MjExfQ.J2s1F1QbOEKUbkVgVlSEi8BBXxLwlywxpKE0QWsObSY' # set this to your DBL token
		self.dblpy = dbl.DBLClient(self.bot, self.token, webhook_path='/dblwebhook', webhook_auth='epicgamerauthotokenthing', webhook_port=19209, autopost=True)

	@commands.Cog.listener()
	async def on_dbl_vote(self, data):
		print(data)

	@commands.Cog.listener()
	async def on_dbl_test(data):
		print(data)

def setup(bot):
	print("Topggcog")
	bot.add_cog(TopGG(bot))