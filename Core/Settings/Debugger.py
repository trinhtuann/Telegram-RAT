# Import modules

from ctypes import windll


# Debugger Detection

def Debugger():
 return windll.kernel32.IsDebuggerPresent() != 0