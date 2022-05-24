import cProfile
import subprocess

def calc():
	subprocess.run(["python3","39.py"])

cProfile.run('calc()')