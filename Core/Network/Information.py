# Import modules

from json import loads
from urllib.request import urlopen
from datetime import datetime, date
from platform import system, release, architecture
from subprocess import check_output, DEVNULL, STDOUT


# Windows Version

def Windows():
	return system() + ' ' + release()


# System Information

def Computer(Win32, Value):
	a = check_output('wmic ' + Win32 + ' get ' + Value, shell=True, stderr=DEVNULL, stdin=DEVNULL)
	b = a.decode('utf-8')
	c = b.split('\n')
	return c[1]


# Computer RAM

def RAM():
	Size = Computer('ComputerSystem', 'TotalPhysicalMemory')
	return int(Size) / 1024 / 1024 / 1024


# Getting the set computer time

def SystemTime():
	SystemTime = str(datetime.today().hour) + ':'+str(datetime.today().minute) + ':' + str(datetime.today().second)
	return SystemTime


# Getting location via IP Address

def Geolocation(Value, Ip=''):
	try:
		result = urlopen(f'http://ip-api.com/json/{Ip}').read().decode('utf-8')
	except:
		return None
	else:
		result = loads(result)
		return result[Value]