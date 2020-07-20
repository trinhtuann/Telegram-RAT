# Import modules

import subprocess


# Opens a browser link

def OpenBrowser(URL):
	if not URL.startswith('http'):
		URL = 'http://' + URL
	subprocess.check_output('start ' + URL, shell=True)