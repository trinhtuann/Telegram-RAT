from win32api import EnumDisplayDevices, EnumDisplaySettings, ChangeDisplaySettingsEx
from win32con import ENUM_CURRENT_SETTINGS, DMDO_DEFAULT, DMDO_90, DMDO_180, DMDO_270


# Variables

rotations = {
    "0": DMDO_DEFAULT,
    "90": DMDO_90,
    "180": DMDO_180,
    "270": DMDO_270
}


# Monitor position control

def DisplayRotate(degrees="0"):
 try:
  rotation_value = rotations[degrees]
 except KeyError:
  rotation_value = DMDO_DEFAULT
 device = EnumDisplayDevices(None, 0)
 dm = EnumDisplaySettings(device.DeviceName, ENUM_CURRENT_SETTINGS)
 if (dm.DisplayOrientation + rotation_value) % 2 == 1:
  dm.PelsWidth, dm.PelsHeight = dm.PelsHeight, dm.PelsWidth   
 dm.DisplayOrientation = rotation_value
 ChangeDisplaySettingsEx(device.DeviceName,dm)
