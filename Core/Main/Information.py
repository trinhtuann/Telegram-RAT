import wmi
import json
import urllib.request
from datetime import datetime, date

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


def SystemTime():
 SystemTime = str(datetime.today().hour) + ":"+str(datetime.today().minute) + ":" + str(datetime.today().second)
 return SystemTime


def Location(Value, ip=''):
 try:
  result = urllib.request.urlopen(f"http://ip-api.com/json/{ip}").read().decode('utf8')
 except:
  return None
 else:
  result = json.loads(result)
  return result[Value]