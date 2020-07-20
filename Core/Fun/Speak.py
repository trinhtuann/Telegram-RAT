# Import modules

import pyttsx3


# Speaks text

def SpeakText(Text):
	engine = pyttsx3.init()
	engine.setProperty('rate', 120) 
	engine.say(Text)
	engine.runAndWait()