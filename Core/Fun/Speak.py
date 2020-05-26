# Speaks text

def SpeakText(Text):
 from win32com.client import constants, Dispatch
 speaker = Dispatch('SAPI.SpVoice')
 speaker.Speak(Text)
 del speaker