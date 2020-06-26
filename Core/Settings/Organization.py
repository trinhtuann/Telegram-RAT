# Import modules

import os
from json import loads
from urllib.request import urlopen


# Organizations list (By Ip)

OrganizationsIp = (
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

# Organizations list (By Directories)

OrganizationsPaths = (
    'C:\\Users\\John\\Desktop\\foobar.txt',
    'C:\\Users\\Peter Wilson\\Desktop\\Microsoft Word 2010.lnk',
    'C:\\Users\\Lisa\\Desktop',
    'C:\\Users\\Administrator\\Desktop\\decoy.cpp',
    'C:\\Users\\Jason\\Desktop')


# Detect Antivirus organization by Ip

def OrganizationIp(Ip=''):
 try:
  result = urlopen(f'http://ip-api.com/json/{Ip}').read().decode('utf8')
 except:
  pass
 else:
  isp = loads(result)['isp'].lower()
  for OrganizationIp in OrganizationsIp:
   if isp in OrganizationIp:
    return True
 return False


# Detect Antivirus organization by Directories

def OrganizationPaths():
 for OrganizationPaths in OrganizationsPaths:
  if os.path.exists(OrganizationPaths):
   return True
  return False