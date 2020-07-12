# Import modules

from subprocess import call


# Opens a browser link

def OpenBrowser(URL):
	if not URL.startswith('http'):
		URL = 'http://' + URL
	call('start ' + URL, shell=True)