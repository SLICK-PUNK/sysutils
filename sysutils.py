#!/usr/bin/env python3
import os
import sys
import time 
import subprocess
from colorama import Fore
from colorama import Style
import colorama
colorama.init()
def  clean():
    os.system("cls")
    print(Fore.LIGHTCYAN_EX)
    subprocess.run("cleanmgr")
    print(Style.RESET_ALL)
    os.system("cls")
    menu()
    


def ping(): 
    os.system("cls")
    site = input(f"{Fore.LIGHTYELLOW_EX}Type Website URL/IP to ping: {Fore.LIGHTGREEN_EX}")
    print(Fore.LIGHTCYAN_EX)
    subprocess.run(['ping', site])  
    print(Style.RESET_ALL)
    input(f"{Fore.LIGHTYELLOW_EX}Press enter to return to menu{Style.RESET_ALL}")
    os.system("cls")
    menu()
    


def netstat():
    os.system("cls")
    print(Fore.LIGHTCYAN_EX)
    subprocess.run("netstat") 
    print(Style.RESET_ALL)
    input(f"{Fore.LIGHTYELLOW_EX}Press enter to return to menu{Style.RESET_ALL}")
    os.system("cls")
    menu()
    


def tracert():
    os.system("cls")
    site = input(f"{Fore.LIGHTYELLOW_EX} Type Website URL/IP to trace packets to: {Fore.LIGHTGREEN_EX}")
    print(Fore.LIGHTCYAN_EX)
    subprocess.run(["tracert", site])  
    print(Style.RESET_ALL)
    input(f"{Fore.LIGHTYELLOW_EX}Press enter to return to menu{Style.RESET_ALL}")
    os.system("cls")
    menu()
    


def powercfg():
    os.system("cls")
    print(Fore.LIGHTCYAN_EX)
    subprocess.run(["powercfg", "-energy"])
    print(Style.RESET_ALL)
    input(f"{Fore.LIGHTYELLOW_EX}Press enter to return to menu{Style.RESET_ALL}")
    os.system("cls")
    menu()
    


def sysinfo():
    os.system("cls")
    print(f"{Fore.LIGHTCYAN_EX}")
    subprocess.run("systeminfo")
    print(Style.RESET_ALL) 
    input(f"{Fore.LIGHTYELLOW_EX}Press enter to return to menu{Style.RESET_ALL}")
    os.system("cls")
    menu() 
    


def sfcscan():
    os.system("cls")
    print(Fore.LIGHTCYAN_EX)
    subprocess.run(['sfc', '/scannow'])
    print(Style.RESET_ALL)
    input(f"{Fore.LIGHTYELLOW_EX}Press enter to return to menu{Style.RESET_ALL}")
    os.system("cls")
    menu()
    


def chkdsk():
    os.system("cls")
    #cfpbs = check for physically bad sectors
    cfpds = ''
    a = input(f"{Fore.LIGHTYELLOW_EX} Do you also want to check for physically bad sectors? y/n?: {Fore.LIGHTGREEN_EX}")
    if a == "y":
        cfpds = "/r"


    print(Fore.LIGHTCYAN_EX)
    subprocess.run(['chkdsk', '/f', cfpds])
    print(Style.RESET_ALL)
    input(f"{Fore.LIGHTYELLOW_EX}Press enter to return to menu{Style.RESET_ALL}")
    os.system("cls")
    menu()
    


def utilman():
    os.system("cls")
    print(Fore.LIGHTCYAN_EX)
    subprocess.run("utilman")
    print(Style.RESET_ALL)
    input(f"{Fore.LIGHTYELLOW_EX}Press enter to return to menu{Style.RESET_ALL}")
    os.system("cls")
    menu()
    


def control():
    os.system("cls")
    print(Fore.LIGHTCYAN_EX)
    subprocess.run("control")
    print(Style.RESET_ALL)
    input(f"{Fore.LIGHTYELLOW_EX}Press enter to return to menu{Style.RESET_ALL}")
    os.system("cls")
    menu()


def dism():
    os.system("cls")
    print(Fore.LIGHTCYAN_EX)
    subprocess.run(["DISM", "/Online", "/Cleanup-Image", "/RestoreHealth" ])
    print(Style.RESET_ALL)
    input(f"{Fore.LIGHTYELLOW_EX}Press enter to return to menu{Style.RESET_ALL}")
    os.system("cls")
    menu()


def tree():
    os.system("cls")
    input(f"{Fore.LIGHTRED_EX}Does NOT work!!. Press enter to continue")
    os.system("cls")
    menu()



def menu():
    choice = input(f'\n\n {Fore.LIGHTYELLOW_EX}[1]{Fore.LIGHTBLUE_EX} Clean up unneeded system files to free up space (Can be run regularly) \n\n {Style.RESET_ALL}{Fore.LIGHTYELLOW_EX}[2]{Fore.LIGHTBLUE_EX} Ping a website of your choice to see if your wifi works/website is up and measure latency of the connection {Style.RESET_ALL}\n\n {Fore.LIGHTYELLOW_EX}[3]{Fore.LIGHTBLUE_EX} Get a list of all active TCP connections from your computer.{Style.RESET_ALL}\n\n {Fore.LIGHTYELLOW_EX}[4]{Fore.LIGHTBLUE_EX} Show path your internet traffic takes to get from your browser to a remote system like Google servers{Style.RESET_ALL}\n\n {Fore.LIGHTYELLOW_EX}[5]{Fore.LIGHTBLUE_EX} Check power configuration to diagnose battery drain/generates warnings and/or to help you improve battery life{Style.RESET_ALL}\n\n {Fore.LIGHTYELLOW_EX}[6] {Fore.LIGHTBLUE_EX}Get info about you system {Style.RESET_ALL}\n\n {Fore.LIGHTYELLOW_EX}[7] {Fore.LIGHTBLUE_EX}Check for corruption of core system files (caused by viruses or other means). Fixes system irregularites{Style.RESET_ALL}\n\n {Fore.LIGHTYELLOW_EX}[8] {Fore.LIGHTBLUE_EX}Check disk/storage for errors and bad sectors{Style.RESET_ALL}\n\n {Fore.LIGHTYELLOW_EX}[9] {Fore.LIGHTBLUE_EX}Open Ease of Access settings{Style.RESET_ALL}\n\n {Fore.LIGHTYELLOW_EX}[10]{Fore.LIGHTBLUE_EX} Open Control Panel\n\n {Fore.LIGHTYELLOW_EX}[11] {Fore.LIGHTBLUE_EX} Scan and repair for problems in the windows image using DISM. Use if opt 7 does not work\n\n{Fore.LIGHTYELLOW_EX} [12] {Fore.LIGHTBLUE_EX}List all folders and files in your system in a specific drive \n\n {Fore.LIGHTYELLOW_EX}[*] {Fore.LIGHTBLUE_EX}Exit\n\n {Fore.LIGHTMAGENTA_EX}{name}@sys>{Style.RESET_ALL} ')
    if choice == "1":
        clean()
    if choice == "2":
        ping()
    if choice == "3":
        netstat()
    if choice == "4":
        tracert()
    if choice == "5":
        powercfg()
    if choice == "6":
        sysinfo()
    if choice == "7":
        sfcscan()
    if choice == "8":
        chkdsk()        
    if choice == "9":
        utilman()
    if input == "10":
        control()    
    if choice == "11":
        dism()
    if  choice == "12":
        tree()  
    if choice == "*":
        sys.exit(0)  

os.system("cls")          
print("\n" + Fore.LIGHTYELLOW_EX + "Starting Tool...")
os.system('echo|set /p="Welcome " ') 
os.system("echo %username%!")
name = subprocess.run(["echo", "%username%"], stdout=subprocess.PIPE, shell=True)
name = (name.stdout.decode("utf-8"))
name = str.rstrip(name)
menu()

