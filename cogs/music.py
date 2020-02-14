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
import youtube_dl
import lavalink
import asyncio
from discord.ext import tasks

ffmpeg_options = {
	'options': '-vn'
}

queue = []

class Music(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	async def beta(ctx):
		return ctx.author.id == 600798393459146784 or ctx.author.id == 362255701323677713 or ctx.author.id == 620244349984309251

	@tasks.loop()
	async def queue(self):
		pass

	@commands.command(name="join")
	async def vcjoin(self, ctx):
		channel = ctx.message.author.voice.channel
		await channel.connect()
		await ctx.send("Joining...")

	@commands.command(name="leave")
	async def vcleave(self, ctx):
		try:
			await ctx.voice_client.disconnect()
		except:
			await ctx.send("I'm not in a vc :/")

	@commands.command()
	async def play(self, ctx, vol : float, *, query : str):
		async with ctx.typing():
			source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(f"C:/Users/Lemon/Desktop/EconomyBot/music/{query}.mp3", executable='C:/Users/Lemon/AppData/Local/ffmpeg/ffmpeg.exe', options=ffmpeg_options), volume=vol)
			ctx.voice_client.play(source, after=lambda e: print('Player error: %s' % e) if e else None)
			await ctx.send('Now playing: {}'.format(query))

	@commands.command(aliases=['music', 'muslib'])
	async def musiclib(self, ctx):
		path = f'C:/Users/Lemon/Desktop/EconomyBot/Music'
		files = ''
		for f in listdir(path):
			files += f"{f}\n"
		await ctx.send(f"""```css
Here is all the music we have currently
Do "play <filename>", remove the .mp3 btw
------------------
{files}```""")


def setup(bot):
	print('Music')
	bot.add_cog(Music(bot))