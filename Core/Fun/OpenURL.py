import os


# Opens a browser link

def OpenBrowser(URL):
 if not URL.startswith('http'):
     URL = 'http://' + URL
 return os.system(f'@start {URL} > NUL')