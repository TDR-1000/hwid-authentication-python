import requests
import os
from time import sleep

apikey = ""


class Authentication:


    def remove(hwid):
        check = requests.get(f'http://yourip:5000/api/v1/hwid?type=remove&hwid={hwid}&apikey={apikey}').text
        if 'success' in check:
            print(f'[\033[32m+\033[39m] Removed [\033[91m{hwid}\033[39m] From The Database.')
            sleep(2)
            Main()
        elif 'invalid_apikey' in check:
            print(f'[\033[91m-\033[39m] Invalid API Key\033[91m:\033[39m {apikey}')
            sleep(2)
            Main()

def Main():
    os.system('cls & title [Authentication]')
    print(f'''
                                        \033[97m╔═╗╦ ╦╔╦╗╦ ╦╔═╗╔╗╔╔╦╗╦╔═╗╔═╗╔╦╗╦╔═╗╔╗╔\033[39m
                                        \033[37m╠═╣║ ║ ║ ╠═╣║╣ ║║║ ║ ║║  ╠═╣ ║ ║║ ║║║║\033[39m
                                        \033[91m╩ ╩╚═╝ ╩ ╩ ╩╚═╝╝╚╝ ╩ ╩╚═╝╩ ╩ ╩ ╩╚═╝╝╚╝\033[39m
''')
    hwid = input('[\033[91m?\033[39m] HWID\033[91m:\033[39m ')
    Authentication.remove(hwid)


if __name__ == "__main__":
    Main()