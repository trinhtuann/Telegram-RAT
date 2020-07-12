# Import modules

from ctypes import windll


# Open cdrom

def OpenCD():
	return windll.WINMM.mciSendStringW(u'set cdaudio door open', None, 0, None)


# Close cdrom

def CloseCD():
	return windll.WINMM.mciSendStringW(u'set cdaudio door closed', None, 0, None)