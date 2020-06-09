# Import modules

try:
 from PIL import ImageGrab
except ImportError:
 raise SystemExit('Please run: pip install pillow')


# Takes a screenshot

def TakeScreenshot(File):
 Screen = ImageGrab.grab()
 Screen.save(File)