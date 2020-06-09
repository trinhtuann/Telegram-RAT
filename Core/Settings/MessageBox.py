# Import modules

from ctypes import windll


# MessageBox Output

def MessageBox(MessageTitle, Message):
 windll.user32.MessageBoxW(0, Message, u'' + MessageTitle, 0x10)