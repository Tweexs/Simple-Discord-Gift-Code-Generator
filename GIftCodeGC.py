import random
import requests
import string
from bs4 import BeautifulSoup
import time


webhookurl = input('Paste Your Webhook here: ')

def createStr():
    randomS = (random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=16))
    randomSD = ''.join(map(str, randomS))
    return(randomSD)


def CheckGiftToken():

    source = 'https://discord.com/api/v8/entitlements/gift-codes/' + createStr()
    page = requests.get(source)
    check = BeautifulSoup(page.content, 'html.parser')
    print(check)


    if check.find('"Unknown Gift Code"') != True:
        print('Invalid GiftCode')

    else:
        GiftCodestr = {
            "content": 'http://discord.gift/' + createStr()
        }
        give = requests.post(webhookurl, json=GiftCodestr)
        print('This Code is valid!')

        try:
            give.raise_for_status()
        except requests.exceptions.HTTPError as err:
            print(err)
        else:
            print("Payload delivered successfully, code {}.".format(give.status_code))


i = float(input('How may Tokens do you want to generate and check?: '))
sec = float(input('How many second do you want to wait after each check? (must be at least 10s): '))
if sec < 10:
    quit('Waiting time must be over 10s')
else:
    while i > 1:
        CheckGiftToken()
        i -= 1
        time.sleep(10)

