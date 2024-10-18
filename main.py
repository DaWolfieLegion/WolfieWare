import pyfiglet
from time import sleep
import os
import sys
import socket
from datetime import datetime
import time
import subprocess
import platform
import re
from colorama import *
import nmap
print("IF THIS IS UR FIRST BOOT PLEASE USE THE FOLLOWING COMMAND FROM WITHIN THE AREA U HAVE INSTALLED THIS PROGRAM OR U WILL GET ERRRORS\n\npip install -r requirements.txt")
sleep(5)
global logo
global logo1
global logo2
global target_ip
global openL
global networks
global Runnable
target_ip="[NULL]"
openL="[NULL]"
networks="[NULL]"
closedL="[NULL]"
logo1=pyfiglet.figlet_format("PortGooner")
logo= pyfiglet.figlet_format("Wolfieware.exe")
logo2=pyfiglet.figlet_format("netwank")
logo3=pyfiglet.figlet_format("DaWolfieLegion")
logo3a=pyfiglet.figlet_format("Da\nWolfie\nLegion")
logo4=pyfiglet.figlet_format("pip cheecker")
MEOW=pyfiglet.figlet_format("MEOW MEOW")
MEOW2=pyfiglet.figlet_format("WE GONNA GET CHU!")
networks=[]
Runnable=False
menu1=False
def clear():
    os.system('cls')
def checker():
    global Runnable
    Runnable=False
    require=[]
    programss=[]
    add=[]
    print(logo,"\n",logo4)
    sleep(2)
    clear()
    qboot()
    clear()
    pippy="pip freeze"
    checky=subprocess.check_output(pippy, text=True)
    print(logo,"\n",logo4)
    print("now listin wah nweeded :3:")
    sleep(3)
    for line in checky.splitlines():
        version=line.split("==")[1].strip()
        program=line.split("==")[0].strip()
        print(program,"is running version-",version)
        sleep(0.125)
    for line in checky.splitlines():
        programss.append(line)
    clear()
    print("installed programs:\n")
    print(programss)
    sleep(4)
    clear()
    file=open("import.txt", "r")
    with file as f:
        require= f.read().splitlines() 
    file.close()
    print("requirements:\n")
    print(require)
    sleep(4)
    clear()
    print(logo,"\n\n")
    print("sortin da wists...")
    programss.sort()
    require.sort()
    sleep(2)
    clear()
    sleep(3)
    print (programss)
    print(require)
    print("sworted!")
    sleep(3)
    clear()
    print("we compware da fings..")
    sleep(3)
    clear()
    print(logo)
    for required_program in require:
        if required_program not in programss:
            add.append(required_program)
            print(required_program," ish nu instwalled ans wills be added to da wist")
            sleep(0.15)
        else:
            print(required_program," ish instwalled!")
            sleep(0.15)
    sleep(4)
    string=", ".join(map(str,add))
    loopy4=False
    clear()
    if len(add)>0:
        print(logo,"\nda pwogwams: ",string," awre nweeded")
        sleep(5)
        clear()
        loopy4=True
    else:
        print("all da pwogwams nweeded awre instwalled!")
        Runnable=True
        loopy4=False
        sleep(3)
        clear()
    while loopy4==True:
        print(logo,"\n")
        numby=len(add)
        print("install da ",numby," pwogwams nweeeded?\n(y/n)\n\n")
        choosyy=input(":")
        if choosyy=="y":
            numm=0
            while numm<numby:
                commannnd=("pip install ")
                commannnd+=str(add[numm])
                print(commannnd)
                os.system(commannnd)
                numm+=1
            Runnable=True
            loopy4=False
        elif choosyy=="n":
            print("DaWolfieLegion have all dese pwogwams instwalled for a weason pwease instwall to use owr pwogwam :3")
            sleep(4)
            Runnable=False
            loopy4=False
        else:
            print("dat nu a option UwU")
def OwO():
    print('''
    ⢰⠶⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠶⠲⣄⠀
⠀⠀⣠⡟⠀⠈⠙⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⡶⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠾⠋⠁⠀⠀⢽⡄
⠀⠀⡿⠀⠀⠀⠀⠀⠉⠷⣄⣀⣤⠤⠤⠤⠤⢤⣷⡀⠙⢷⡄⠀⠀⠀⠀⣠⠞⠉⠀⠀⠀⠀⠀⠈⡇
⠀⢰⡇⠀⠀⠀⠀⠀⠀⠀⠉⠳⣄⠀⠀⠀⠀⠀⠈⠁⠀⠀⠹⣦⠀⣠⡞⠁⠀⠀⠀⠀⠀⠀⠀⠀⡗
⠀⣾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣻⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣏
⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇
⠀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠂
⠀⢿⠀⠀⠀⠀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣤⣤⡀⠀⠀⠀⠀⠀⣸⠇⠀
⠀⠘⣇⠀⠀⠀⠀⠉⠉⠛⠛⢿⣶⣦⠀⠀⠀⠀⠀⠀⢴⣾⣟⣛⡋⠋⠉⠉⠁⠀⠀⠀⠀⣴⠏⠀⠀
⢀⣀⠙⢷⡄⠀⠀⣀⣤⣶⣾⠿⠋⠁⠀⢴⠶⠶⠄⠀⠀⠉⠙⠻⠿⣿⣷⣶⡄⠀⠀⡴⠾⠛⠛⣹⠇
⢸⡍⠉⠉⠉⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⣬⠷⣆⣠⡤⠄⢀⣤⠞⠁⠀
⠈⠻⣆⡀⠶⢻⣇⡴⠖⠀⠀⠀⣴⡀⣀⡴⠚⠳⠦⣤⣤⠾⠀⠀⠀⠀⠀⠘⠟⠋⠀⠀⠀⢻⣄⠀⠀
⠀⠀⣼⠃⠀⠀⠉⠁⠀⠀⠀⠀⠈⠉⢻⡆⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⠀⠀
⠀⢠⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⣀⡿⠧⠿⠿⠟⠀⠀
⠀⣾⡴⠖⠛⠳⢦⣿⣶⣄⣀⠀⠀⠀⠀⠘⢷⣀⠀⣸⠃⠀⠀⠀⣀⣀⣤⠶⠚⠉⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢷⡀⠈⠻⠦⠀⠀⠀⠀⠉⠉⠁⠀⠀⠀⠀⠹⣆⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡴⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⡄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⢲⡗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠋⠀⠀⠀⠀⠀⠀⠀
          ''')
def UwU():
        #https://emojicombos.com/boykisser-ascii-art
        print('''
    ⣿⡇⣽⣿⣿⣿⣧⠘⣿⣿⠠⣤⣍⡛⢿⣿⣿⠏⣰⣿⣿⣿⣿⣿⡆⢿
    ⣿⢀⣿⣿⣿⣿⣿⣷⡈⢿⡄⢿⣿⣿⣦⡙⠏⣰⣿⣿⣿⣿⣿⣿⡇⣿
    ⣿⢸⣿⣿⣿⣿⣿⣿⡿⠄⣡⣤⣿⣿⣿⣿⣄⣿⣿⣿⣿⣿⣿⣿⡇⣿
    ⣿⢸⣿⣿⣿⣿⣿⣿⣤⣬⣭⣬⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿
    ⣿⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⣿
    ⣿⡀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠿⠿⣿⣿⡿⢠⣿
    ⣿⣧⠸⣿⣧⠀⣴⡆⣤⠀⢸⣿⣿⣿⣿⠀⠀⢸⣿⡌⣶⣿⠟⢁⣾⣿
    ⠙⠛⠂⠹⡿⢸⣿⡇⢸⠁⢸⣿⣿⣿⣿⠀⠀⢈⣿⡇⢸⣯⣤⣤⠀⣿
    ⣆⠙⣿⣿⣇⢸⣿⣇⠀⢀⣾⡿⢿⣿⣿⣀⣀⣼⣿⡇⣸⣿⡿⢁⣾⣿
    ⣿⣷⢀⡟⡉⠞⢻⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⠋⠘⣹⣿⡄⢻⣿⣿
    ⣿⡇⣼⣿⣧⣶⣿⣿⣿⣟⠻⢋⣍⣉⣋⣼⣿⣿⣿⣶⢿⣿⣿⡄⢻⣿
    ⣿⣧⣭⣭⣄⡙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⣡⣤⣭⣤⣴⣾⣿
    ⣿⣿⣿⣿⣿⣿⣇⠠⣬⣭⣽⣿⣿⣿⣿⣿⣷⡈⢿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣦⠙⣿⣿⣿⣿⣿⣿⣿⣿⣷⡈⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⠃⠼⢿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠹⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣶⠆⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢹⣿⣿⣿⣿⣿
    ''')
def boot():
    count=0
    while count<12:
        clear()
        print(pyfiglet.figlet_format("booting program"))
        UwU()
        print(logo3a)
        sleep(1)
        clear()
        print(pyfiglet.figlet_format("booting program."))
        UwU()
        print(logo3a)
        sleep(0.5)
        clear()
        print(pyfiglet.figlet_format("booting program.."))
        UwU()
        print(logo3a)
        sleep(0.5)
        clear()
        print(pyfiglet.figlet_format("booting program..."))
        UwU()
        print(logo3a)
        sleep(0.5)
        count+=1
    clear()
    print("program loaded")
    OwO()
    sleep(5)
    clear()
def qboot():
    count=0
    while count<4:
        clear()
        print(pyfiglet.figlet_format("booting program"))
        UwU()
        print(logo3a)
        sleep(0.5)
        clear()
        print(pyfiglet.figlet_format("booting program."))
        UwU()
        print(logo3a)
        sleep(0.5)
        clear()
        print(pyfiglet.figlet_format("booting program.."))
        UwU()
        print(logo3a)
        sleep(0.5)
        clear()
        print(pyfiglet.figlet_format("booting program..."))
        UwU()
        print(logo3a)
        sleep(0.5)
        count+=1
    clear()
    print("program loaded")
    OwO()
    sleep(3)
    clear()
def help():
    clear()
    print(logo3)
    print("\nexit:-2\nglobalised things:-1\nhelp:0\nport scanner: 1\nlocal network scan: 2\n")
def SCANNYTHING():
    global openL, target_ip, closedL
    print(logo1)
    print("\nBy DaWolfieLegion")
    sleep(4)
    clear()
    UwU()
    sleep(2)
    print("hwak da pwanet\nThatCamdenFurry\n")
    sleep(4)
    clear()
    print("dis pwogwam was mwade by DaWolfieLegion don stweal")
    sleep(3)
    print("\n\n\nMeow meow mwoferfwuker we ish gonna gwoon on chor pworts\n-ThatCamdenFurry\n")
    sleep(5)
    clear()
    target=input('wha chu wan scwan\n\n: ')
    clear()
    customhelper=True
    while customhelper==True:
        custom=input("chu wan do custom amownts of pworts?\ny/n\n:")
        clear()
        if custom=="y":
            menuports=True
            customhelper=False
            clear()
        elif custom=="n":
            menuports=False
            customhelper=False
            clear()
        else:
            customhelper=True
            print("DAS NU A GUD INPWUT ONLY y or n")
            sleep(1)
            clear()
    if menuports==True:
        ports=int(input("how mwenny chu wan to be gwooned\n(if chu wan do dem all put 0)\n:"))
    sleep(0.01)
    print("OTAY DEN WETS DO DIS!")
    sleep(0.5)
    clear()
    target_ip = socket.gethostbyname(target)
    print("-" * 50)
    global uwu
    uwu=pyfiglet.figlet_format("UwU")
    print(uwu)
    print("-" * 50)
    sleep(3)
    clear()
    print("\n\n")
    #funny banner
    print("-" * 50)
    print("Scwannin da twarget: " + target)
    print("Dis ish happenin at:" + str(datetime.now()))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("-" * 50)
    sleep(5)
    clear()
    start = time.time()

    #the actual scanner
    def port_scan(port):
        try:
            s.connect((target_ip, port))
            return True
        except:
            return False

    open=0
    closed=0
    openL=[]
    closedL=[]
    #the thing that has the logic for the scanning
    try: 
        start = time.time()
        print('stwartin gooinin on hwost:', target_ip)
        print("dis will twake a wile")
        #if defult it scans ports 1-65535
        if menuports==False:
            ports=65535
        counter2=0
        for port in range(1,ports):
            if counter2>11:
                 clear()
                 counter2=0
            else:
                 counter2+=1
            if port_scan(port):
                print(f'port {port} is open')
                openL.append(port)
                open+=1

            else:
                print(f'port {port} is closed')
                closedL.append(port)
                closed+=1
    except KeyboardInterrupt:
            print("\n STWOPPIN CUZ CHU SWAID SO !!!!")
            sleep(3)
            boot()
            clear()
    except socket.gaierror:
            print("\n NU HOWST CWOULD BE WESOLVED  !!!!")
            sleep(1)
            boot()
            clear()
            
    except socket.error:
            print("\n DA SWERVER NU WESPOND !!!!")
            sleep(1)
            boot()
            clear()
    
    end = time.time()
    print("-" * 50)
    print("\n")
    global wolf
    wolf=pyfiglet.figlet_format("DaWolfieLegion")
    print(wolf)
    print("\n")
    print("-" * 50)
    print("\ngwooned chor pworts")
    sleep(2)
    clear()
    print(open, " -open ports\n\n",closed," -closed ports\n\n")
    print("ports dat are open:", openL)
    print(f'dis twook {end-start:.2f} seconds')
    closedlist=False
    loopy1=True
    while loopy1==True:
        clist=input("wold chu wike to see da cwosed ports?\n(y/n)\n:")
        if clist=="y":
            sleep(0.1)
            clear()
            print(closedL)
            sleep(3)
            clear()
            boot()
            loopy1=False
        elif clist=="n":
            print("otay :3")
            sleep(0.3)
            clear()
            loopy1=False
        else:
            print("dats nu a option ;3")
            sleep(2)
            clear()
    globalise=input("to keep da open pworts an wah ip day came fwom pwease entwer 1 if chu don wan dis den entwer 0\n\n:")
    int(globalise)
    sleep(0.2)
    clear()
    if globalise==0:
         print(logo1)
         sleep(2)
         clear()
    elif globalise==1:
         clear()
         boot()
         clear()
         print(logo1)
         sleep(2)
         return openL, target_ip, closedL
    clear()
def localWiFi():
    print("we gon purr on da nwetworcs UwU")
    UwU()
    sleep(2)
    clear()
    # Command to list Wi-Fi networks on Windows.
    list_networks_command = 'netsh wlan show networks'
    count1=0
    try:
        # Execute the command and capture the output.
        print("WE GOT DEM NOWS!")
        sleep(3)
        clear()
        output = subprocess.check_output(list_networks_command, text=True)
        networks = []
        # Use the output to find open Wi-Fi networks.
        print(output)
        sleep(6)
        print("bwakin da data down UwU")
        sleep(3)
        boot()
        for line in output.splitlines():
            if "SSID" in line:
                # Extract the SSID (Wi-Fi network name).
                ssid = line.split(":")[1].strip()
            elif "Authentication" in line and "Open" in line:
                # Check if the Wi-Fi network has open authentication.
                networks.append(ssid)
        # Check if any open networks were found.
        if len(networks) > 0:
            # Print a message for open networks with colored output.
            print(f'{Fore.LIGHTMAGENTA_EX}[+] owpn Wifi networks in wange: \n')
            for each_network in networks:
                print(f"{Fore.GREEN}[+] {each_network}")
                count1+=1
            sleep(3)
            clear()
        else:
            # Print a message if no open networks were found.
            print(f"{Fore.RED}[-] Nu owpun wifi networks in wange")
    except subprocess.CalledProcessError as e:
        # Handle any errors that occur during the execution of the command.
        print(f"{Fore.RED}Error: {e}")
        # Return an empty list to indicate that no networks were found.
        return []
    for each_network in networks:
        print(f"{Fore.GREEN}[+] {each_network}")
    print(count1, "-nwetworcs fownd UwU")
    sleep(4)
    loopy2=True
    while loopy2==True:
        clist=input("wold chu wike to go to mwenu?\n(y/n)\n:")
        if clist=="y":
            print("otay :3")
            sleep(3)
            clear()
            loopy2=False
        elif clist=="n":
            clear()
            for each_network in networks:
                print(f"{Fore.GREEN}[+] {each_network}")
            print(count1, "-nwetworcs fownd UwU")
            loopy2=True
        else:
            print("dats nu a option ;3")
            sleep(2)
            clear()
def localNet():
    full_results = [re.findall('^[\w\?\.]+|(?<=\s)\([\d\.]+\)|(?<=at\s)[\w\:]+', i) for i in os.popen('arp -a')]
    final_results = [dict(zip(['IP', 'LAN_IP', 'MAC_ADDRESS'], i)) for i in full_results]
    final_results = [{**i, **{'LAN_IP':i['LAN_IP'][1:-1]}} for i in final_results]
def MeNu():
    print(logo3)
    print("WELCOM TO DAWOLFIELEGION GOOIN PWATFORM FOR ALL CHOR HWAKIN NEEDS UwU")
    sleep(2)
    OwO()
    sleep(3)
    clear()
    help()
    choise=int(input("\n\n:"))
    if choise==-1:
        print("last scanned ip", target_ip ,"OPEN PORTS:\n", openL, "nearby wifis", networks)
        sleep(2)
        chooser=True
        while chooser==True:
            thing1=input("wold chu wike to see da cwosed pworts aswel?\n(y/n)\n\n:")
            if thing1=="y":
                print("last scanned ip: ", target_ip ,"\nOPEN PORTS:\n", openL, "\nCLSOED PORTS:\n", closedL)
                wait=True
                while wait==True:
                    wait1=input("when chu wan weave jus entwer a 0\n\n:")
                    if wait1=="0":
                        wait=False
                    else:
                        print("error das nu gud inpwut")
                        clear()
                clear()
    elif choise==-2:
        clear()
        UwU()
        print(logo3)
        sleep(4)
        clear()
        count3=0
        exitt=pyfiglet.figlet_format("HAK DE PWANET")
        while count3<7:
            print(exitt)
            sleep(0.5)
            count3+=1
        sleep(1)
        clear()
        exit()

    elif choise==0:
        clear()
        help()
    elif choise==1:
        clear()
        print(logo1)
        UwU()
        sleep(3)
        clear()
        boot()
        print("TIME TO SCWAN DEM PWORTS")
        sleep(1)
        SCANNYTHING()
    elif choise==2:
        clear()
        print(logo2)
        OwO()
        sleep(4)
        clear()
        boot()
        clear()
        sleep(1)
        localWiFi()
    else:
        print("chu stoopid das nu somfin i undwerstand")
        clear()
def startup():
    clear()
    print(logo)
    sleep(2)
    OwO()
    sleep(4)
    clear()
    OwO()
    print(MEOW)
    print(MEOW2)
    sleep(3)
    clear()
    boot()
    print(logo3)
    sleep(3)
    clear()
    checker()
def fincheck():
    global Runnable
    global menu1
    if Runnable==True:
        menu1=True
    else:
        print(logo)
        print("CHU DON MWEET OWR WECQUIREMENTS PWEASE WAIT WILE WE WUN DA INSTWALLER...")
        sleep(5)
        clear()
        checker()
clear()
startup()
fincheck()
while Runnable==False:
    fincheck()
while menu1==True:
    print(pyfiglet.figlet_format("ACCESS GRANTED"))
    MeNu()