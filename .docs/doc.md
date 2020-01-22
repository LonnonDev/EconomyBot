<!DOCTYPE html>
<html>
	<head>
		<link rel="stylesheet" href="stylesheet.css">
		<link rel="stylesheet" href="monokai-sublime.css">
		<script src="highlight.pack.js"></script>
		<script>hljs.initHighlightingOnLoad();</script>
	</head>
		<!-- General Commands Heading -->
<div>
<body>
<h1>General Commands</h1>
<h2>Class</h2><pre>
<code>class general(commands.Cog, name='General Commands'):
	def __init__(self, bot):
		self.bot = bot</code></pre>
<pre>This is the class section for the General commands, where it defines the bot arg, so it can be used later in the code for certain things.</pre>
</body></div>
<h2>Commands</h2>
<pre><code class="language-python">
	@commands.command(name="start")
	async def start(self, ctx):
			easylog(ctx) # logs the command used
			person = str(ctx.author.id) # defins the person using the commands
			c.execute("SELECT * from people WHERE name=?", (person,)) #gets the persons table if exists or not exists
			conn.commit() # commits that
			fetch = c.fetchone() # fetchs the data
			if fetch == None: # if it's none than it registers the person using the command
				personhandler(person) # runs the personhandeler function
				await ctx.send(f"{ctx.author.mention} You just got registed!") # sends a message saying that you registered
			else: # else statement
				await ctx.send(f"{ctx.author.mention} You're already registered") # sends a message if the person is already registered
				await ctx.send("Do `f!help` for help!") # tells them to do "f!help" for help, aka telling them all commands</code>
This is the the start command, his command starts the users game, if they haven't ran any other game command before,
if they have started the game already it will send "{user} You're already registered"</pre>
</html>