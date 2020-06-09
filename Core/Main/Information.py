# Import modules

import json
import urllib.request
from datetime import datetime, date
try:
 import wmi
except ImportError:
 raise SystemExit(('Please run: pip install wmi'))


# Variables

c = wmi.WMI()    
systeminfo = c.Win32_ComputerSystem()[0]
os_info = c.Win32_OperatingSystem()[0]
proc_info = c.Win32_Processor()[0]
gpu_info = c.Win32_VideoController()[0]

os_version = ' '.join([os_info.Version, os_info.BuildNumber])
system_ram = float(os_info.TotalVisibleMemorySize) / 1048576


SystemVersion = os_info.Caption
Manufacturer = systeminfo.Manufacturer
Model = systeminfo.Model
CPU = proc_info.Name
GPU = gpu_info.Name
RAM = system_ram
ARM = os_info.osarchitecture


# Getting the version of Windows

def Windows():
 if SystemVersion.find('7') != -1 :
  return 'Windows 7'

 if SystemVersion.find('8') != -1 :
  return 'Windows 8'

 if SystemVersion.find('10') != -1 :
  return 'Windows 10'


# Getting the set computer time

def SystemTime():
 SystemTime = str(datetime.today().hour) + ':'+str(datetime.today().minute) + ':' + str(datetime.today().second)
 return SystemTime


# Getting location via IP Address

def Location(Value, ip=''):
 try:
  result = urllib.request.urlopen(f'http://ip-api.com/json/{ip}').read().decode('utf-8')
 except:
  return None
 else:
  result = json.loads(result)
  return result[Value]