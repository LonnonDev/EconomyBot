import subprocess, shlex, os, psutil
from threading import Thread
import time

clear = lambda: os.system('cls')
clear()

def kill(proc_pid):
	process = psutil.Process(proc_pid)
	for proc in process.children(recursive=True):
		proc.kill()
	process.kill()

def runcode():
	print("\nStarting...\n--------------------------------------")
	sp = subprocess.Popen(["python", "main.py"], shell=True)
	time.sleep(2)
	inputvar = input("[Restart][End]: ")
	if inputvar == 'r' or inputvar == 'restart':
		print("Restarting...")
		kill(sp.pid)
		time.sleep(2)
		clear()
		runcode()
	elif inputvar == 'e' or inputvar == 'end':
		kill(sp.pid)
		print("Ending...")
		time.sleep(2)
		clear()
		quit()

def start():
	pass

if __name__ == '__main__':
	Thread(target = runcode).start()