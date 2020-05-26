import ctypes


# Sets a photo on the desktop wallpaper

def SetWallpapers(Photo, ProgramData):
 ctypes.windll.user32.SystemParametersInfoW(20, 0, ProgramData+'Files\\'+Photo.file_path, 0)