import subprocess


# Opens a browser link

def OpenBrowser(URL):
 if not URL.startswith('http'):
     URL = 'http://' + URL
 return subprocess.Popen('start ' + URL, shell=True)