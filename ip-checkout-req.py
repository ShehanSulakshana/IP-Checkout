import os
print("\033[32m [+] Installing Requirements...\033[0m")
print()

os.system("pip install --upgrade pip")

#required libraries
os.system("pip install requests")
os.system("pip install socket")
os.system("pip install json")
os.system("pip install pyfiglet")
os.system("pip install colorama")

print("\033[32m [+] Now Run :- \033[34mpython ip-checkout.py \033[32m")
