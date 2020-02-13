import subprocess, shlex, os, psutil
from threading import Thread
import time
import asyncio
from colorama import init
from termcolor import colored
init()

clear = lambda: os.system('cls')
clear()

def kill(proc_pid):
	process = psutil.Process(proc_pid)
	for proc in process.children(recursive=True):
		proc.kill()
	process.kill()

def runcode(run):
	run = run
	print(colored("\nUpdating...\n--------------------------------------", 'cyan'))
	update()
	time.sleep(15)
	clear()
	print(colored("\nStarting...\n--------------------------------------", 'green'))
	sp = subprocess.Popen(run, shell=True)
	inputvar = input("")
	if inputvar == 'r' or inputvar == 'restart':
		try:
			print("Restarting...")
			kill(sp.pid)
			time.sleep(2)
			clear()
			runcode(run)
		except:
			time.sleep(2)
			clear()
			runcode(run)
	elif inputvar == 'e' or inputvar == 'end':
		try:
			kill(sp.pid)
			print("Ending...")
			time.sleep(2)
			clear()
			quit()
		except:
			time.sleep(2)
			clear()
			quit()

def update():
	pp = subprocess.Popen(["pip", "install", "--upgrade", "youtube_dl"], shell=True)
	pp = subprocess.Popen(["pip", "install", "--upgrade", "discord.py"], shell=True)
	pp = subprocess.Popen(["pip", "install", "--upgrade", "lavalink"], shell=True)
	pp = subprocess.Popen(["python", "-m", "pip", "install", "--upgrade", "pip"], shell=True)
	# python -m pip install --upgrade pip

if __name__ == '__main__':
	inputvar = input("[r/b]")
	print(inputvar)
	if inputvar == 'b':
		run = ["python", "main.py", "b"]
		runcode(run)
	else:
		run = ["python", "main.py", "r"]
		runcode(run)