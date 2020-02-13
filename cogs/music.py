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

ytdl_format_options = {
	'format': 'bestaudio/best',
	'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
	'restrictfilenames': True,
	'noplaylist': True,
	'nocheckcertificate': True,
	'ignoreerrors': False,
	'logtostderr': False,
	'quiet': True,
	'no_warnings': True,
	'default_search': 'auto',
	'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
	'options': '-vn'
}

queue = []

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

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

	@commands.command()
	async def download(self, ctx, *, url):
		await YTDLSource.from_url(url, loop=self.bot.loop, stream=True)


def setup(bot):
	print('Music')
	bot.add_cog(Music(bot))