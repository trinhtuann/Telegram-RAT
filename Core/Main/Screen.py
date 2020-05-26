from PIL import ImageGrab


# Takes a screenshot

def TakeScreenshot(File):
 Screen = ImageGrab.grab()
 Screen.save(File)