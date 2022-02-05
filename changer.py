
import sys
import os
import time
print('''\033[32m
                                                                        
             ________________________________________________
            |                                                |
           |    _________________________________________     |
           |   |                                         |    |
           |   |  C:\>     Matos MAC Changer             |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |                                         |    |
           |   |_________________________________________|    |
           |                                                  |
            |________________________________________________|
                   \___________________________________/
                ___________________________________________
             _-'    .-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-.  --- `-_
          _-'.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.--.  .-.-.`-_
       _-'.-.-.-. .---.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-`__`. .-.-.-.`-_
    _-'.-.-.-.-. .-----.-.-.-.-.-.-.-.-.-.-.-.-.-.-.-----. .-.-.-.-.`-_
 _-'.-.-.-.-.-. .---.-. .-------------------------. .-.---. .---.-.-.-.`-_
:-------------------------------------------------------------------------:
`---._.-------------------------------------------------------------._.---'
''')
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)
slowprint("[+] Iniciando la herramienta CHANGER  ")
def slowprint(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)
slowprint("[+] Porfavor espere unos segundos...  ")
time.sleep(5)
os.system('clear')
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)
slowprint("\033[91m04/02/22")
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0. / 100)
slowprint('''\033[1;31m \033[32m    
  
                    
 _____ ______   ________  _________  ________  ________      
|\   _ \  _   \|\   __  \|\___   ___\\   __  \|\   ____\     
\ \  \\\__\ \  \ \  \|\  \|___ \  \_\ \  \|\  \ \  \___|_    
 \ \  \\|__| \  \ \   __  \   \ \  \ \ \  \\\  \ \_____  \   
  \ \  \    \ \  \ \  \ \  \   \ \  \ \ \  \\\  \|____|\  \  
   \ \__\    \ \__\ \__\ \__\   \ \__\ \ \_______\____\_\  \ 
    \|__|     \|__|\|__|\|__|    \|__|  \|_______|\_________\
''')
def slowprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(3. / 100)
slowprint("\t\t                                         \033[91mBy :Matitos#9999\033[97m")
print(" ")
print("\033[91m1- \033[32mVer direccion MAC actual")
print("")
print("\033[91m2- \033[32mCambia tu direccion MAC aleatoriamente")
print("")
print("\033[91m3- \033[32mCambia tu direccion MAC personalizable")
print("")
print("\033[91m4- \033[32mResetea tu direccion MAC a la original")
print("")
print("\033[91m5- \033[32mSalir")
print("")
print("")
matos=input("      \033[91m[?] \033[32mElije la opcion ==>")
if matos==('1') :
            print(" ")
            print("\033[94m1 \033[97m- \033[91mwlan0 \033[97m( Conexion WIFI )")
            print("\033[94m2 \033[97m- \033[91meth0 \033[97m( Conexion por cable )")
            print(" ")
            lawla=input("   \033[91m[?] \033[32mElije tu tipo de conexion:")
            if lawla==('1') :
                      slowprint("\033[97m")
                      os.system('macchanger -s wlan0')
                      print(" ")
                      alla=input('Presiona cualquier tecla para continuar')
                      os.system('clear') 
                      os.system('python3 changer.py')
            if lawla==('2') :
                       slowprint("\033[97m")
                       os.system('macchanger -s eth0')
                       print(" ")
                       allah=input('Presiona cualquier tecla para continuar')
                       os.system('clear')
                       os.system('python3 changer.py')

if matos==('2') :
               print(" ")
               print("\033[91m1 - \033[32mwlan0 ( Conexion WIFI )")
               print("\033[91m2 - \033[32meth0 ( Conexion por cable )")
               print(" ")
               deuxs=input("   \033[91m[?] \033[32mElije tu tipo de conexion:")
               if deuxs==('2') :
                        slowprint("")
                        os.system('ifconfig eth0 down')
                        os.system('macchanger -r eth0')
                        os.system('ifconfig eth0 up')
                        print(" ")
                        hoho=input("Presiona cualquier tecla para continuar")
                        os.system('clear')
                        os.system('python3 changer.py')
               if deuxs==('1') :
                        slowprint("")
                        os.system('ifconfig wlan0 down')
                        os.system('macchanger -r wlan0')
                        os.system('ifconfig wlan0 up')
                        print(" ")
                        hoho=input("Pressiona cualquier tecla para continuar")
                        os.system('clear')
                        os.system('python3 changer.py')

if matos==('4'): 
               print(" ")
               print("\033[91m1 - \033[32mwlan0 ( Conexion WIFI )")
               print("\033[91m2 - \033[32meth0 ( Conexion por cable )")
               print(" ")
               talta=input("   \033[91m[?] \033[32mElije tu tipo de conexion:")
               if talta==('2') :
                        print(" ")
                        slowprint("\033[97m")
                        os.system('macchanger -p eth0')
                        print(" ") 
                        lopa=input("Presiona cualquier tecla para continuar")
                        os.system('clear')
                        os.system('python3 changer.py')
               if talta==('1') : 
                        print(" ")
                        slowprint("\033[97m")
                        os.system('ifconfig wlan0 down')
                        os.system('macchanger -p wlan0')
                        os.system('ifconfig wlan0 up')
                        print(" ") 
                        lopa=input("Presiona cualquier tecla para continuar")
                        os.system('clear')
                        os.system('python3 changer.py')




if matos==('3'):
               print(" ")
               print("\033[91m1 - \033[32mwlan0 ( Conexion WIFI )")
               print("\033[91m2 - \033[32meth0 ( Conexion por cable )")
               print(" ")
               rabaa=input("   \033[91m[?] \033[32mElije tu interfaz:")
               if rabaa==('2') :
                        print(" ")
                        os.system('ifconfig eth0 down')
                        dire=input("\033[91m[?] \033[32mIngresa la nueva direccion MAC : ")
                        os.system('ifconfig eth0 down')
                        os.system('macchanger -m'+(dire)+' eth0')
                        os.system('ifconfig eth0 up')
                        print("done")
               if rabaa==('1') : 
                        os.system('ifconfig wlan0 down')
                        print(" ")
                        dire=input("\033[91m[?] \033[32mIngresa la nueva direccion MAC : ")
                        os.system('ifconfig wlan0 down')
                        os.system('macchanger -m'+(dire)+' wlan0')
                        os.system('ifconfig wlan0 up')
                        print("done")



if matos==('5') :
    def slowprint(s):
        for c in s + '\n' :
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(10. / 100)
    slowprint("\033[92m[!] \033[96mSaliendo...")
    os.system('clear')
    os.system('exit')
            




