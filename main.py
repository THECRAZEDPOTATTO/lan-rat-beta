import time 
import sys 
import os 
import threading 
import psutil
import platform
from datetime import datetime

acc = '''

	
                            _________
                           /         /.
    .-------------.       /_________/ |
   /             / |      |         | |
  /+============+\ |      | |====|  | |
  ||C:\>        || |      |         | |
  ||            || |      | |====|  | |
  ||            || |      |   ___   | |
  ||            || |      |  |166|  | |
  ||            ||/@@@    |   ---   | |
  \+============+/    @   |_________|./.
                     @          ..  ....'
  ..................@     __.'.'  ''
 /oooooooooooooooo//     ///
/................//     /_/
------------------

'''

print(acc)
print("")
print("")
print("Welcome to LAN 22-exploiter")
print("scanning LAN for defult requirement...")
print("="*40, "Network Information", "="*40)
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        print(f"=== Interface: {interface_name} ===")
        if str(address.family) == 'AddressFamily.AF_INET':
            print(f"  IP Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast IP: {address.broadcast}")
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            print(f"  MAC Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast MAC: {address.broadcast}")
net_io = psutil.net_io_counters()
print("")
print("")
print("requirement met")
print("------info------")
print("not suported on: chrome os, or MAC os")
print("----------------")
print("starting..")
time.sleep(4)
print("gathing packets")
#Gatherpackets here
time.sleep(4)
print("done")
print("donwloading online software")
#download online software
print("done")
print("ready to go")
print(".1 scan net work for divs recomended first 2. wifi rat 3. die[exit]")
i = input(">>>  ")
#adding if error happends in school not done so there just the print stuff rn
#add if then esif else while true stuff later today
x = -1

if x < 0:
  raise Exception("error on divs make sure you have a wifi attapter to do attacks")