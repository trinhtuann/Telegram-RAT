import time

# Emulator Detection

def Emulator():
 ticks = time.time()
 time.sleep(0.1)
 if (time.time() - ticks) < 0.1:
  return True
 return False