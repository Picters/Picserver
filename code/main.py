from colorama import Fore, init
import time
import os
import sys
init()

# Servers
server_01 = True
server_02 = True
server_03 = True
server_04 = True

# Commands
def clear(): os.system("cls")

def help():
    print("""Commands:
    clear - Clear screen.
    help - Get commands.
    exit - Shutdown machine.
    sv.ping - Ping all servers.
    sv.control - on/off servers.""")

def svping():
    print("Pinging servers...")
    if server_01 == True: print("Server \"01\" ", Fore.GREEN + "Recieved 4/4" + Fore.RESET)
    elif server_01 == False: print("Server \"01\"", Fore.RED + "Recieved 0/4" + Fore.RESET)
    time.sleep(0.5)
    if server_02 == True: print("Server \"02\" ", Fore.GREEN + "Recieved 4/4" + Fore.RESET)
    elif server_02 == False: print("Server \"02\"", Fore.RED + "Recieved 0/4" + Fore.RESET)
    time.sleep(0.5)
    if server_03 == True: print("Server \"03\" ", Fore.GREEN + "Recieved 4/4" + Fore.RESET)
    elif server_03 == False: print("Server \"03\"", Fore.RED + "Recieved 0/4" + Fore.RESET)
    time.sleep(0.5)
    if server_04 == True: print("Server \"04\" ", Fore.GREEN + "Recieved 4/4" + Fore.RESET)
    elif server_04 == False: print("Server \"04\"", Fore.RED + "Recieved 0/4" + Fore.RESET)
    time.sleep(2)
    print(Fore.GREEN + "DONE")
    
# Start
print("Powering on...")
time.sleep(1)
print("Scanning disks...")
time.sleep(2)
print(Fore.GREEN + "DONE" + Fore.RESET)
print()
print("Pinging servers...")
time.sleep(0.5)
print("Server \"01\" ", Fore.GREEN + "Recieved 4/4" + Fore.RESET)
time.sleep(0.5)
print("Server \"02\" ", Fore.GREEN + "Recieved 4/4" + Fore.RESET)
time.sleep(0.5)
print("Server \"03\" ", Fore.GREEN + "Recieved 4/4" + Fore.RESET)
time.sleep(0.5)
print("Server \"04\" ", Fore.GREEN + "Recieved 4/4" + Fore.RESET)
time.sleep(0.5)
print()
print(Fore.GREEN + "All servers pinged sucessfull!" + Fore.RESET)
print()
time.sleep(1)
print("Loading Terminal...")
time.sleep(3)
clear()
print(Fore.GREEN + "DONE")
print()
print("Sent \"help\" for more commands")

while True:
    command = input(Fore.RED + "ROOT@192168 # " + Fore.RESET)
    if command == "clear": clear()
    elif command == "help": help()
    elif command == "sv.ping": svping()
    elif command == "exit": sys.exit()
    elif command == "sv.control": svcontrol()