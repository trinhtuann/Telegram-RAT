# Import modules

from ctypes import WinDLL, wintypes


# SandBox Detection

def SandBox():
 sandbox_dll_list = (
     'SbieDll',
     'SxIn',
     'Sf2',
     'snxhk',
     'cmdvrt32'
 )
 kernel32 = WinDLL('kernel32', use_last_error=True)
 kernel32.GetModuleHandleW.restype = wintypes.HMODULE
 kernel32.GetModuleHandleW.argtypes = [wintypes.LPCWSTR]
 for dll in sandbox_dll_list:
  hMod = kernel32.GetModuleHandleW(dll + '.dll')
  if hMod == None:
   continue
  else:
   del(kernel32)
   return True

 del(kernel32)
 return False