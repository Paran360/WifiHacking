import os
print('''\033[1;36;40mWifi_Hacking Installer By PARAN360
Your Device Must Be Rooted
If Any Question,
Contact Me On Telegram
Tg_User:@paran360 \n''')
os.system("pkg update && pkg upgrade")
os.system("pkg install git python")
os.system("pkg install -y root-repo")
os.system("pkg install -y git tsu python wpa-supplicant pixiewps iw")
os.system("cd WifiHacking")
os.system("chmod +x wifihack.py")

print("\033[1;34;40mThanks.\nInstallation Done.\n Enter This Command : \nsudo python wifihack.py -i wlan0 -K")
