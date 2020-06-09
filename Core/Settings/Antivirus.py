# Import modules

import os


# Variables

ProgramFiles = os.environ['ProgramW6432'] + '\\'
ProgramFiles86 = os.environ['ProgramFiles(x86)'] + '\\'


# Detect installed antivirus software

if os.path.exists(ProgramFiles + 'Windows Defender'):
   av = 'Windows Defender'
if os.path.exists(ProgramFiles + 'AVAST Software\\Avast'):
   av = 'Avast'
if os.path.exists(ProgramFiles + 'AVG\\Antivirus'):
   av = 'AVG'
if os.path.exists(ProgramFiles86 + 'Avira\\Launcher'):
   av = 'Avira'
if os.path.exists(ProgramFiles86 + 'IObit\\Advanced SystemCare'):
   av = 'Advanced SystemCare'
if os.path.exists(ProgramFiles + 'Bitdefender Antivirus Free'):
   av = 'Bitdefender'
if os.path.exists(ProgramFiles + 'DrWeb'):
   av = 'Dr.Web'
if os.path.exists(ProgramFiles + 'ESET\\ESET Security'):
   av = 'ESET'
if os.path.exists(ProgramFiles86 + 'Kaspersky Lab'):
   av = 'Kaspersky'
if os.path.exists(ProgramFiles86 + '360\\Total Security'):
   av = '360 Total Security'