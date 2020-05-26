import subprocess
from ctypes import *


# Ends the selected process

def KillProcess(Process):
 subprocess.Popen('taskkill /f /im '+Process+'.exe')


# Gets the title of the active window

def WindowTitle():
 hWnd = windll.user32.GetForegroundWindow()
 length = windll.user32.GetWindowTextLengthW(hWnd)
 buf = create_unicode_buffer(length + 1)
 windll.user32.GetWindowTextW(hWnd, buf, length + 1)
 if buf.value:
  return buf.value
 else:
  return None


# Stops all processes

def TaskkillAll(Temp):
 with open(os.path.join(Temp, 'taskkill.bat'), 'w') as OPATH:
   OPATH.writelines([
     'if "%~1"=="" (set "x=%~f0"& start "" /min "%comspec%" /v/c "!x!" any_word & exit /b)\n', 
     'taskkill /f /fi "USERNAME eq %username%" /fi "IMAGENAME ne explorer.exe USERNAME eq %username%" /fi "IMAGENAME ne "'+CurrentName+'"'])
 os.startfile(Temp+'taskkill.bat')