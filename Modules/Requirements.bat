echo off

pip3 install PyAudio-0.2.11-cp38-cp38-win_amd64.whl
pip3 install PyAudio-0.2.11-cp38-cp38-win32.whl

pip3 install PyAudio-0.2.11-cp37-cp37m-win_amd64.whl
pip3 install PyAudio-0.2.11-cp37-cp37m-win32.whl

pip3 install pytelegrambotapi
pip3 install opencv-python
pip3 install pycryptodome
pip3 install pyperclip
pip3 install pywin32
pip3 install pillow

pip3 install pyinstaller

pip3 install pysocks
pip3 uninstall -y enum34

:cmd
pause null 