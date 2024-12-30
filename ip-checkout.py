import requests,json,os ,pyfiglet , socket

#Main fucnction
def Main():
    print(pyfiglet.figlet_format('IP Checkout', font='Standard'))
    print("[+] Script By Shehan Sulakshana")
    print("\n-> Your IP ADDRESS : " + FetchUserIP())
    CheckIP = input("\n# Enter ip address : ")
    FetchData(CheckIP)

#Func for return their own ip
def FetchUserIP():
    UserIp = socket.gethostbyname(socket.gethostname())
    return UserIp

#Fun
def FetchData(ip):
    data = requests.get("http://ip-api.com/json/",ip)
    print("* Response : "+ str(data.status_code))

    if data.status_code == 200:
        data = data.json()
        print()
        for key,value in data.items():
            print(f"{key } : {value}")
    else :
        print ("\n[ERR] Network Error occured ")
        exit



Main()