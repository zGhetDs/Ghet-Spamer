import requests, threading, pystyle, colorama, os, json
from colorama import Fore
from pystyle import Colorate, Colors

webhooks = input("[ + ] URL Del Webhook: ")

header = {
        "content-type": "application/json"
    }

data = {
    "content": input("[ + ] Mensaje de spam: "),
    "username": input("[ + ] Nombre del bot:"),
    "avatar_url": input("[ + ] Avatar del bot:")
  }

print("""
░██████╗░██╗░░██╗███████╗████████╗  ░██████╗██████╗░░█████╗░███╗░░░███╗███╗░░░███╗███████╗██████╗░
██╔════╝░██║░░██║██╔════╝╚══██╔══╝  ██╔════╝██╔══██╗██╔══██╗████╗░████║████╗░████║██╔════╝██╔══██╗
██║░░██╗░███████║█████╗░░░░░██║░░░  ╚█████╗░██████╔╝███████║██╔████╔██║██╔████╔██║█████╗░░██████╔╝
██║░░╚██╗██╔══██║██╔══╝░░░░░██║░░░  ░╚═══██╗██╔═══╝░██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝░░██╔══██╗
╚██████╔╝██║░░██║███████╗░░░██║░░░  ██████╔╝██║░░░░░██║░░██║██║░╚═╝░██║██║░╚═╝░██║███████╗██║░░██║
░╚═════╝░╚═╝░░╚═╝╚══════╝░░░╚═╝░░░  ╚═════╝░╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚═╝
""")

print("[ + ] Herramienta Desarrollada por zGhet")

def main(webhook):
  os.system('cls' if os.name=='nt' else 'clear')


while True:
  requests.post(webhooks, headers = header, json = data)
  print(f"[ + ] ¡El mensaje ha sido enviado!")

if __name__ == "__main__":
  for webhook in webhooks:
    threading.Thread(target=main, args=(webhook,)).start()
