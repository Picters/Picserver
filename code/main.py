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

# Server status
status_01 = Fore.GREEN + "Working" + Fore.RESET
status_02 = Fore.GREEN + "Working" + Fore.RESET
status_03 = Fore.GREEN + "Working" + Fore.RESET
status_04 = Fore.GREEN + "Working" + Fore.RESET

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

def svcontrol():
    global server_01, server_02, server_03, server_04
    global status_01, status_02, status_03, status_04
    
    print("server_01 = ", status_01)
    print("server_02 = ", status_02)
    print("server_03 = ", status_03)
    print("server_04 = ", status_04)

    sel = input("Enter the name of the server: ")
    if sel == "server_01" and server_01 == True:
        turn = input("Turn off the server? (y/n): ")
        if turn == "y":
             server_01 = False
             status_01 = Fore.RED + "Not working" + Fore.RESET
             print(Fore.GREEN + "DONE" + Fore.RESET)
        else: return
    elif sel == "server_01" and server_01 == False:
        turn = input("Turn on the server? (y/n): ")
        if turn == "y":
            server_01 = True
            status_01 = Fore.GREEN + "Working" + Fore.RESET
            print(Fore.GREEN + "DONE" + Fore.RESET)
        else: return
    elif sel == "server_02" and server_02 == True:
        turn = input("Turn off the server? (y/n): ")
        if turn == "y":
            server_02 = False
            status_02 = Fore.RED + "Not working" + Fore.RESET
            print(Fore.GREEN + "DONE" + Fore.RESET)
        else: return
    elif sel == "server_02" and server_02 == False:
        turn = input("Turn on the server? (y/n): ")
        if turn == "y":
            server_02 = True
            status_02 = Fore.GREEN + "Working" + Fore.RESET
            print(Fore.GREEN + "DONE" + Fore.RESET)
        else: return
    elif sel == "server_03" and server_03 == True:
        turn = input("Turn off the server? (y/n): ")
        if turn == "y":
            server_03 = False
            status_03 = Fore.RED + "Not working" + Fore.RESET
            print(Fore.GREEN + "DONE" + Fore.RESET)
        else: return
    elif sel == "server_03" and server_03 == False:
        turn = input("Turn on the server? (y/n): ")
        if turn == "y":
            server_03 = True
            status_03 = Fore.GREEN + "Working" + Fore.RESET
            print(Fore.GREEN + "DONE" + Fore.RESET)
        else: return
    elif sel == "server_04" and server_04 == True:
        turn = input("Turn off the server? (y/n): ")
        if turn == "y":
            server_04 = False
            status_04 = Fore.RED + "Not working" + Fore.RESET
            print(Fore.GREEN + "DONE" + Fore.RESET)
        else: return
    elif sel == "server_04" and server_04 == False:
        turn = input("Turn on the server? (y/n): ")
        if turn == "y":
            server_04 = True
            status_04 = Fore.GREEN + "Working" + Fore.RESET
            print(Fore.GREEN + "DONE" + Fore.RESET)
        else: return

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
    else: print(Fore.RED + "Unknown" + Fore.RESET)