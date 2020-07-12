# Import modules

from win32api import keybd_event
from win32con import VK_VOLUME_UP


# Audio volume control

def VolumeControl(Level):
	for i in range(int(Level)):
		keybd_event(VK_VOLUME_UP, 0)