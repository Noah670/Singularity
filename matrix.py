# Noah Pohl
# Singularity: Enter your name and age to enter the singularity

import os

# pip install pyfiglet to display banner images
import pyfiglet 
from pyfiglet import Figlet

custom_font = Figlet(font='larry3d')
print(custom_font.renderText('noah670'))

print('Welcome to the matrix')
username = input('Please enter your name: ')
print('Hello', username)

age = int(input('Now tell me how old you are ' + username + ':'))
print('So you are', age ,' years old?')

if age >= 18:
    print('You are technically considered an adult')
if age >= 18 and age <= 19:
    print('However you are still a teenager')
elif age >= 20 and age <= 29:
    print('You are in your 20\'s')
elif age >= 30 and age <= 39:
     print('You are in your 30\'s')
elif age >= 40 and age <= 49:
     print('You are in your 40\'s')
elif age >= 50 and age <= 59:
     print('You are in your 50\'s')
elif age >= 60 and age <= 69:
     print('You are in your 60\'s')
elif age >= 70 and age <= 79:
     print('You are in your 70\'s')
elif age >= 80 and age <= 89:
     print('You are in your 80\'s')
elif age >= 90 and age <= 99:
     print('You are in your 90\'s')
elif age >= 100 and age <= 999:
     print('You are a Centenarian Congragts!')
elif age >= 1000:
    print('You are also basically immortal')                                                
else:
    print('You are really young')

input("Press any key to enter the Matrix using your confirmed user settings...")

print('Now approaching the singularity...!')


ascii_image =pyfiglet.figlet_format("Welcome to the Singularity!")
print(ascii_image)