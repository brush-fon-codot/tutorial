#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys, subprocess
from time import sleep
os.system("clear")
reload(sys)
sys.setdefaultencoding("utf-8")

host = " "
port = " "
output = " "

def logo():
 print("""

b = '\033[34;1m'
g = '\033[32;1m'
p = '\033[35;1m'
c = '\033[36;1m'
r = '\033[31;1m'
w = '\033[37;1m'
y = '\033[33;1m'
os.system('clear') 
print y+"                               _.._"
print y+"                             .'    '."
print y+"                            (____/`\ \\ "
print y+"                           (  |' ' )  ) .    "
print y+"                           )  _\= _/  (     "
print y+"                 __..---.(`_.'  ` \\    )   "
print y+"                `;-''-._(_( .      `; (     "
print y+"                /       `-`'--'     ; )"
print y+"               /    /  .    ( .  ,| |("
print y+"_.-`'---...__,'    /-,..___.-'--'_| |_)"
print y+"'-'``'-.._       ,'  |   / .........'"
print y+"       ``;--'`;   |   `-`"
print y+"             `'..__.'\n"                                       
                          


\t [*] Author : an brush fon
\t [*] Coded By :20k19™
\t [*] AndroSec1337 indonesian darknet public
  """)

def help():
 print("""
  Commands :
       set HOST       : Set Your Host (e.g set HOST 127.0.0.1)
       set PORT       : Set Your Port (e.g set PORT 1337)
       set OUTPUT     : Set Your Output Name And Path (e.g set OUTPUT /home/payload)
       show values    : Show Host, Port And Output Value
       start listener : Start Your Conection Server

  Please Report This bug To My Kontak
  WHATSAPP : https://api.whatsapp.com/send?phone=6289637763566
  TELEGRAM : https://t.me/cdt28

def main():
    global host, port, output

    while True:
        cmd = raw_input("[*] root@localhost:~# ").lower()

        if cmd == "help":
            help()

        elif cmd == 'banner':
            os.system("clear")
            logo()
            main()

        elif "clear" in cmd:
            os.system("clear")

        elif "set host" in cmd:
            host = cmd.split()[-1]

        elif "set port" in cmd:
            port = int(cmd.split()[-1])

        elif "set output" in cmd:
            output = cmd.split()[-1]

        elif cmd == "show values":
            print "\n[+] HOST   : %s\n[+] PORT   : %s\n[+] OUTPUT : %s\n"%(host, port,output)

        elif cmd == "generate payload" or cmd == "generate":
            if host != " " and port != " " and output != " ":
                print("[+] Generating Payload . . .")
                sleep(1)
                print("[*] Using Configuration . . .\n |_ HOST   : "+host+"\n |_ PORT   : "+str(port)+"\n |_ OUTPUT : "+output)
                sleep(3)
                os.system("sh modules/gen.sh "+host+" "+str(port)+" "+output)
                print("[+] Generating Success . . .")
                sleep(1)
                main()
            else:
                print "\n[!] HOST   : %s\n[!] PORT   : %s\n[!] OUTPUT : %s\n"%(host,port,output)

        elif cmd == "start" or cmd == "run" or cmd == "start listener":
            if host != " " and port != " ":
                if os.name == "nt":
                    subprocess.Popen([sys.executable, 'modules/listener.py', host, str(port)], creationflags=subprocess.CREATE_NEW_CONSOLE)
                else:
                    os.system(sys.executable + " modules/listener.py %s %s"%(host, str(port)))
            else:
                print "\n[!] Host : %s\n[!] Port : %s\n"%(host,port)
        else:
            print("[!] Check Your Command . . .")
            main()

def contol():
    try:
        logo()
        main()
    except KeyboardInterrupt:
        print("\n[!] CTRL+C Detect Exiting Tools . . .")
        sleep(2)
        sys.exit()
if __name__ == "__main__":
    contol()
