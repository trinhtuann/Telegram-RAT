import time
from ctypes import windll


# Blocks mouse and keyboard movements

def Block(Seconds):
 windll.user32.BlockInput(True)
 time.sleep(Seconds)
 windll.user32.BlockInput(False)
