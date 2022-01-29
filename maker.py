import time

import random
from colorama import Fore,init
init()
import os
import pyfiglet


elysia_banner = pyfiglet.figlet_format('ELYSIA PASSWORD MAKER')

print(Fore.GREEN,elysia_banner)
print('')

print(Fore.LIGHTGREEN_EX,'Password Length')

length = input('>')

length = int(length)

chars = 'abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+QWERTYUIOP}{ASDFGHJKLZXCVBNM,./;~`'

dosya = open('pass.txt','a')

for i in range(length) :    
    
    char = random.choice(chars)

    print(char)

    dosya.write(char)

dosya.close()

dosya = open('pass.txt','r')

password = dosya.read()

dosya.close()

os.remove('pass.txt')

os.system('cls')

print(Fore.RED,'Here is your password =>',password)

input('')