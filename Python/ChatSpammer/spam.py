#!/usr/bin/env python3
import pyautogui
import time
import keyboard
import sys
import os
import pyperclip

spam = ''
for a in sys.argv:
	if not (os.path.basename(__file__) in a): 
		spam += a + ' '

print('[BOOT] Starting spammer in 3 seconds...')
print('[INFO] Press "q" anytime to quit')
time.sleep(3)
print('[INFO] Spamming...')
pyperclip.copy(spam)

while(True):
	pyautogui.hotkey('ctrl','v')
	pyautogui.press('enter')
	try:
		if keyboard.is_pressed('q'):
			break
	except:
		continue

print('[EXIT] Exiting...')
