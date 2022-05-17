import random
import requests
import string
from bs4 import BeautifulSoup
import time


webhookurl = 'YOUR WEBHOOK HERE'

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


i = 0
while i < 100:
    CheckGiftToken()
    i += 1
    time.sleep(10)
