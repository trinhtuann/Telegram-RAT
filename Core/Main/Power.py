import subprocess
from ctypes import *
from ctypes.wintypes import *


# Puts the computer to sleep 

def Hibernate():
 subprocess.Popen('shutdown -h /f')

# Turns off the computer

def Shutdown():
 subprocess.Popen('shutdown -s /t 0 /f')


# Restarts computer

def Restart():
 subprocess.Popen('shutdown -r /t 0 /f')

# Ends user session

def Logoff():
 subprocess.Popen('shutdown -l /f')


# Blue screen of death

def BSoD():
 ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, byref(c_bool()))
 ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, byref(DWORD()))
