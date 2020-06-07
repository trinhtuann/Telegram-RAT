import ctypes


# Debugger Detection

def Debugger():
 return ctypes.windll.kernel32.IsDebuggerPresent() != 0