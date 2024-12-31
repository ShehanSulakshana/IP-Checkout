# SCRIPT CODED BY SHEHAN SULAKSHANA
# FOLLOW ME ON GITHUB & IF YOU ARE SATISFIED STAR MY REPOSITORIES ❤️

import requests,json,os ,pyfiglet , socket ,os
from colorama import Fore ,Style ,Back

#Main fucnction
def Main():
    print(Fore.RED + pyfiglet.figlet_format('IP Checkout', font='Standard'))
    print(f"{Fore.BLUE}{Style.BRIGHT}{Back.RED}[+] Script By Shehan Sulakshana {Style.RESET_ALL} ")
    print(f"{Style.NORMAL}\033[0m\n-> Your PUBLIC IP ADDRESS : " + FetchUserIP())

    print(f"\n\t{Fore.BLUE}[1]~\033[0m Public IP Checkout \n\t{Fore.BLUE}[2]~\033[0m WEB IP Checkout ")

    #input : option selection
    try :
        Opt = int(input("\n\033[0m# Choice :: "))
    except Exception:
        print (f"\n{Fore.RED}[ERR] Wrong input Detected")
        Opt = int(input("\n# Choice : "))

    if Opt==1:
        CheckIP = str(input("\n\033[0m# Enter ip address :: "))
        FetchData(CheckIP)

    elif Opt==2:
        WebIpCheckout()
    else:
        print(f"\n{Fore.RED}[ERR] Wrong input Detected")
        os.system("exit")

#Func for return their own ip
def FetchUserIP():
    UserIp = socket.gethostbyname(socket.gethostname())
    return UserIp

#Func for fetching ip data using API
def FetchData(ip):
    data = requests.get("http://ip-api.com/json/"+ip)
    print("\n* Response : "+ str(data.status_code))

    if data.status_code == 200:
        data = data.json()
        print()

        if 'status' in data:
            print(Fore.GREEN + " Status       : " + Fore.WHITE +  data['status'])
        if 'query' in data:
            print(Fore.GREEN + " Ip           : " + Fore.WHITE +  data['query'])
        if 'country' in data:
            print(Fore.GREEN + " Country      : " + Fore.WHITE +  data['country'])
        if 'countryCode' in data:
            print(Fore.GREEN + " Country Code : " + Fore.WHITE +  data['countryCode'])
        if 'region' in data:
            print(Fore.GREEN + " Region Code  : " + Fore.WHITE +  data['region'])
        if 'regionName' in data:
            print(Fore.GREEN + " Region Name  : " + Fore.WHITE +  data['regionName'])
        if 'city' in data:
            print(Fore.GREEN + " City         : " + Fore.WHITE +  data['city'])
        if 'zip' in data:
            print(Fore.GREEN + " Zip Code     : " + Fore.WHITE +  data['zip'])
        if 'timezone' in data:
            print(Fore.GREEN + " Tome Zone    : " + Fore.WHITE +  data['timezone'])
        if 'isp' in data:
            print(Fore.GREEN + " Isp          : " + Fore.WHITE +  data['isp'])
        if 'org' in data:
            print(Fore.GREEN + " Organization : " + Fore.WHITE +  data['org'])
        if 'lat' in data:
            print(Fore.GREEN + " Latitude     : " + Fore.WHITE +  str(data['lat']))
        if 'lon' in data:
            print(Fore.GREEN + ""
                               " Longitude    : " + Fore.WHITE +  str(data['lon']))
        if 'lon' in data and 'lat' in data:
            print(Fore.YELLOW + "\n Approximate location    : " + Fore.WHITE +  str(data['lat']) + "," + str(data['lon']))

        RestartFunc()

    else :
        print (f"\n{Fore.RED}[ERR] Network Error occured ")
        exit


def WebIpCheckout():
    web = str(input("\n# Web Domain :: "))
    WebIp = socket.gethostbyname(web)
    print(f"\n{Fore.GREEN} Website Ip Address :\033[0m {WebIp}")

    RestartFunc()


# ASK user if needed to restart the script
def RestartFunc():
    Restart = input("\n# Do you need to restart programme (y/n)? : ")
    Restart == Restart.lower().strip()
    if Restart=="y" or Restart== "Y":
        Main()
    else:
        os.system("exit")


Main()