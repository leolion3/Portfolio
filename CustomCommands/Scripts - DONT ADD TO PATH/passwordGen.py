#!/usr/bin/env python3
import pyperclip
import random
import string

alphabet = string.ascii_letters + string.digits + string.punctuation + string.digits

user_alphabet = input("Select custom alphabet or leave empty for default: ")

hidden = False

hidepass = input("Do you want to hide the password? Y/N: ")

if 'y' in hidepass.lower():
    hidden = True

if len(user_alphabet):
    alphabet = user_alphabet

password_length = int(input("Please select password length: "))

password = ''

for i in range(0,password_length):
    password = password + alphabet[random.randint(0,len(alphabet)-1)]

pyperclip.copy(password)

if not hidden:
    print("Your random password is " + password)
else:
    print("Password copied to clipboard!")
