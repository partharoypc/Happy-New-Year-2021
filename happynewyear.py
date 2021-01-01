import os 
import time
from colorama import Fore, Back
os.system('cls')

filename=["file1.txt","file2.txt", "file3.txt","file4.txt", "file5.txt","file6.txt","file7.txt"]

def animator(filename, delay=3, repeat=20):
	frames=[]
	for name in filename:
		with open(name, "r", encoding="utf-8") as f:
			frames.append(f.readlines())
	for i in range(repeat):
		for frame in frames:
			print(Fore.RED)
			print("".join(frame))
			time.sleep(delay)
			os.system('cls')


animator(filename, delay=0.9, repeat=20)

animator(filename, delay=0.7, repeat=25)

animator(filename, delay=5, repeat=10)