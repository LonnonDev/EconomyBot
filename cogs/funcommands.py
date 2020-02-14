import time
import json
import random
from math import *
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
from discord.ext import menus
from baseconv import base2, base16, base36, base56, base58, base62, base64
from baseconv import BaseConverter
os.chdir('C:/Users/Lemon/Desktop/EconomyBot')

ffmpeg_options = {
	'options': '-vn'
}

conn = sqlite3.connect("users.db")
c = conn.cursor()

c.execute("SELECT * from ran")
fetchone = c.fetchone()
rannumber = int(fetchone[0])


class fun(commands.Cog, name='Fun Commands'):
	def __init__(self, bot):
		self.bot = bot

	async def beta(ctx):
		# 234834826081992704 222388637541597185 109475170602729472 109496491072077824 164120455228293120 362255701323677713 488929293905428482 600798393459146784
		return ctx.author.id == 234834826081992704 or ctx.author.id == 222388637541597185 or ctx.author.id == 109475170602729472 or ctx.author.id == 109496491072077824 or ctx.author.id == 164120455228293120 or ctx.author.id == 362255701323677713 or ctx.author.id == 488929293905428482 or ctx.author.id == 600798393459146784

	@commands.command()
	async def bully(self, ctx, member: discord.Member):
		randint = random.randint(1,2)
		if randint == 1:
			await ctx.send(f"{member} has small pp")
		elif randint == 2:
			await ctx.send(f"{member} has small brain")

	@commands.command()
	async def tobinary(self, ctx, number: int):
		await ctx.send(base2.encode(number))

	@commands.command()
	async def tooctal(self, ctx, number: int):
		await ctx.send(base8.encode(number))

	@commands.command()
	async def tohex(self, ctx, number: int):
		await ctx.send(base16.encode(number))

	@commands.command()
	async def base64(self, ctx, number: int):
		await ctx.send(base64.encode(number))

	@commands.command()
	async def custombase(self, ctx, base: str, number: int):
		myconv = BaseConverter(base)
		await ctx.send(myconv.encode(number))

	@commands.command()
	async def base26(self, ctx, number: int):
		myconv = BaseConverter('abcdefghijklmnopqrstuvwxyz')
		await ctx.send(myconv.encode(number))

	@commands.command()
	async def base26(self, ctx, number: int):
		myconv = BaseConverter('abcdefghijklmnopqrstuvwxyz')
		await ctx.send(myconv.encode(number))

	@commands.command()
	async def math(self, ctx, *, math):
		async with ctx.typing():
			newmath = math.replace('^', '**')
			embed=discord.Embed(title="Math")
			embed.add_field(name="Problem", value=f"```diff\n{math}\n```", inline=False)
			embed.add_field(name="Answer", value=f"```diff\n{eval(newmath)}\n```", inline=False)
			await ctx.send(embed=embed)
			pass

	@commands.command()
	async def mathfunc(self, ctx,):
		embed=discord.Embed(title="Math", description="Math Functions Python")
		embed.add_field(name="ceil(x)", value="Returns the smallest integer greater than or equal to x.", inline=False)
		embed.add_field(name="copysign(x, y)", value="Returns x with the sign of y", inline=False)
		embed.add_field(name="fabs(x)", value="Returns the absolute value of x", inline=False)
		embed.add_field(name="factorial(x)", value="Returns the factorial of x", inline=False)
		embed.add_field(name="floor(x)", value="Returns the largest integer less than or equal to x", inline=False)
		embed.add_field(name="fmod(x, y)", value="Returns the remainder when x is divided by y", inline=False)
		embed.add_field(name="frexp(x)", value="Returns the mantissa and exponent of x as the pair (m, e)", inline=False)
		embed.add_field(name="fsum(iterable)", value="Returns an accurate floating point sum of values in the iterable", inline=False)
		embed.add_field(name="isfinite(x)", value="Returns True if x is neither an infinity nor a NaN (Not a Number)", inline=False)
		embed.add_field(name="isinf(x)", value="Returns True if x is a positive or negative infinity", inline=False)
		embed.add_field(name="isnan(x)", value="Returns True if x is a NaN", inline=False)
		embed.add_field(name="ldexp(x, i)", value="Returns x * (2**i)", inline=False)
		embed.add_field(name="modf(x)", value="Returns the fractional and integer parts of x", inline=False)
		embed.add_field(name="trunc(x)", value="Returns the truncated integer value of x", inline=False)
		embed.add_field(name="exp(x)", value="Returns e**x", inline=False)
		embed.add_field(name="expm1(x)", value="Returns e**x - 1", inline=False)
		embed.add_field(name="log(x[, base])", value="Returns the logarithm of x to the base (defaults to e)", inline=False)
		embed.add_field(name="log1p(x)", value="Returns the natural logarithm of 1+x", inline=False)
		embed.add_field(name="log2(x)", value="Returns the base-2 logarithm of x", inline=False)
		embed.add_field(name="log10(x", value="	Returns the base-10 logarithm of x", inline=False)
		embed.add_field(name="pow(x, y)", value="Returns x raised to the power y", inline=False)
		embed.add_field(name="sqrt(x)", value="Returns the square root of x", inline=False)
		embed.add_field(name="acos(x)", value="Returns the arc cosine of x", inline=False)
		embed.add_field(name="asin(x)", value="Returns the arc sine of x", inline=False)
		embed.add_field(name="atan(x)", value="Returns the arc tangent of x", inline=False)
		embed.add_field(name="atan2(y, x)", value="Returns atan(y / x)", inline=False)
		embed.add_field(name="cos(x)", value="Returns the cosine of x", inline=False)
		embed.add_field(name="hypot(x, y)", value="Returns the Euclidean norm, sqrt(x*x + y*y)", inline=False)
		embed.add_field(name="sin(x)", value="Returns the sine of x", inline=False)
		embed.add_field(name="tan(x)", value="Returns the tangent of x", inline=False)
		embed.add_field(name="degrees(x)", value="Converts angle x from radians to degrees", inline=False)
		embed.add_field(name="radians(x)", value="Converts angle x from degrees to radians", inline=False)
		embed.add_field(name="acosh(x)", value="Returns the inverse hyperbolic cosine of x", inline=False)
		embed.add_field(name="asinh(x)", value="Returns the inverse hyperbolic sine of x", inline=False)
		embed.add_field(name="atanh(x)", value="Returns the inverse hyperbolic tangent of x", inline=False)
		embed.add_field(name="cosh(x)", value="Returns the hyperbolic cosine of x", inline=False)
		embed.add_field(name="sinh(x)", value="Returns the hyperbolic cosine of x", inline=False)
		embed.add_field(name="tanh(x)", value="Returns the hyperbolic tangent of x", inline=False)
		embed.add_field(name="erf(x)", value="Returns the error function at x", inline=False)
		embed.add_field(name="erfc(x)", value="Returns the complementary error function at x", inline=False)
		embed.add_field(name="gamma(x)", value="Returns the Gamma function at x", inline=False)
		embed.add_field(name="lgamma(x)", value="Returns the natural logarithm of the absolute value of the Gamma function at x", inline=False)
		embed.add_field(name="pi", value="Mathematical constant, the ratio of circumference of a circle to it's diameter (3.14159...)", inline=False)
		embed.add_field(name="e", value="mathematical constant e (2.71828...)", inline=False)
		await ctx.send(embed=embed)

	@commands.command()
	@commands.cooldown(1, 60, commands.BucketType.user)
	@commands.check(beta)
	async def fishingmeme(self, ctx, laugh : int):
		if laugh > 1250:
			laugh = 1250
		await ctx.message.delete()
		await ctx.send("Fishing I barely know her!")
		ha = ''
		for x in range(laugh):
			await asyncio.sleep(1)
			ha += "HA"
			await ctx.send(f"**{ha}**", delete_after=10)

	@commands.command()
	async def guns(self, ctx):
		await ctx.send("<:gunforwardr:598954466594783282><:gunforwardl:598954502510477356>")

	@commands.command()
	@commands.cooldown(1, 3, commands.BucketType.user)
	async def dpy(self, ctx):
		await ctx.send("Discord.py > Discord.js")

	@commands.command()
	async def encode(self, ctx, encoding, *, text):
		text = str(text).encode(encoding=str(encoding), errors='namereplace')
		await ctx.send(text)

	@commands.command()
	async def decode(self, ctx, encoding, *, text):
		text1 = text.encode()
		text = text1.decode(str(encoding), errors='namereplace')
		await ctx.send(text)

	@commands.command(aliases=['axolotl'])
	@commands.cooldown(1, 5, commands.BucketType.user)
	async def randomaxolotl(self, ctx):
		pics = 20
		randint = random.randint(1, pics)
		await ctx.send('', file=discord.File(f'C:/Users/Lemon/Desktop/EconomyBot/img/axolotl/axolotl{randint}.jpg'))

	@commands.command(aliases=['italy'])
	@commands.cooldown(1, 5, commands.BucketType.user)
	async def italian(self, ctx):
		try:
			await ctx.message.delete()
			await ctx.send('', file=discord.File(f'C:/Users/Lemon/Desktop/EconomyBot/img/random/italian.png'))
		except:
			await ctx.send("Missing Permissions Use this link to give me correct perms! https://discordapp.com/api/oauth2/authorize?client_id=627932116319076353&permissions=104197185&scope=bot")
		

	@commands.command()
	async def files(self, ctx, path):
		if path == 'home':
			path = f'C:/Users/Lemon/Desktop/EconomyBot'
			files = ''
			for f in listdir(path):
				files += f"{f}\n"
			await ctx.send(f"""```css
Here are the files in {path}
------------------
{files}```""")
		else:
			path = f'C:/Users/Lemon/Desktop/EconomyBot/{path}'
			files = ''
			for f in listdir(path):
				files += f"{f}\n"
			await ctx.send(f"""```css
Here are the files in {path}
------------------
{files}```""")

	@commands.command()
	async def code(self, ctx, start, end, file):
		os.chdir('C:/Users/Lemon/Desktop/EconomyBot')
		read = open(f"{file}", "r").readlines()[int(start)-1:int(end)]
		read = ' '.join(read)
		read = codeblock(read)
		await ctx.send(f'''>>> ```py
 {read}
```''')
		await ctx.send("[+] = ```")
		await ctx.send("[-] = `")
		os.chdir('C:/Users/Lemon/Desktop/EconomyBot')

def codeblock(text):
	codeblockformat = text.replace('```', '[+]').replace('`', '[-]')
	return codeblockformat


def setup(bot):
	print('FunCommands')
	bot.add_cog(fun(bot))