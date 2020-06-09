# Import modules

import os
import re
import subprocess
from ctypes import windll


# Process list

def List():
 processes = []
 process = subprocess.check_output('@chcp 65001 1> NUL && @TASKLIST /FI \"STATUS eq RUNNING\" | find /V \"Image Name\" | find /V \"=\"',
  shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode(encoding='utf8', errors='strict')
 for processNames in process.split(' '):
  if '.exe' in processNames:
   proc = processNames.replace('K\r\n', '').replace('\r\n', '')
   processes.append(proc)
 return processes


# VirtualBox Detection

def VirtualBox():
 vmware_dll = os.path.join(os.environ['SystemRoot'], 'System32\\vmGuestLib.dll')
 virtualbox_dll = os.path.join(os.environ['SystemRoot'], 'vboxmrxnp.dll')
 if os.path.exists(virtualbox_dll) or os.path.exists(vmware_dll):
  return True

 reg0 = 'REG QUERY HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet001\\Control\\Class\\{4D36E968-E325-11CE-BFC1-08002BE10318}\\0000\\'
 reg1 = os.system(f'{reg0}DriverDesc 2> nul')
 reg2 = os.system(f'{reg0}ProviderName 2> nul')
 if reg1 != 1 and reg2 != 1:    
  return True

 virtualbox_processes = (
     'vboxservice.exe', 'vboxtray.exe',
     'vmtoolsd.exe', 'vmwaretray.exe', 'vmwareuser', 'VGAuthService.exe',
     'vmacthlp.exe', 'vmsrvc.exe', 'vmusrvc.exe',
     'prl_cc.exe', 'prl_tools.exe',
     'xenservice.exe', 'qemu-ga.exe',
        'joeboxcontrol.exe', 'joeboxserver.exe', 'joeboxserver.exe'
 )
 for process in List():
     if process.lower() in virtualbox_processes:
         return True

 x = windll.user32.GetSystemMetrics(0)
 y = windll.user32.GetSystemMetrics(1)
 if x <= 200 or y <= 200:
  return True
 return False