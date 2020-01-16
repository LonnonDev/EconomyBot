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

conn = sqlite3.connect("users.db")
c = conn.cursor()

c.execute("SELECT * from ran")
fetchone = c.fetchone()
rannumber = int(fetchone[0])+1

class event(commands.Cog, name='Event Commands'):
	def __init__(self, bot):
		self.bot = bot

	@commands.command()
	async def splashtext(self, ctx, *, text):
		person = str(ctx.author.id)
		c.execute("SELECT * from event WHERE name=?", (person,))
		fetchone = c.fetchone()
		if fetchone is None:
			c.execute("INSERT INTO event (name) VALUES (?)", (person,))
			conn.commit()
		c.execute("UPDATE event SET splashtxt=? WHERE name=?", (str(arg), person))
		conn.commit()
		await ctx.send("Submitted entry for splashtxt, and or edited entry")

def setup(bot):
	print('EventCommands')
	bot.add_cog(event(bot))