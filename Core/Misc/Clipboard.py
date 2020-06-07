import pyperclip


# Sets text to clipboard

def SetClipboard(Text):
 pyperclip.copy(Text)


# Get text from clipboard

def GetClipboard():
 return pyperclip.paste()