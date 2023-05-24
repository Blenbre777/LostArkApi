import requests
from lostArkApi import Token

class markets:
    headers = {
            'accept': 'application/json',
            'authorization' : Token
    }
    def __init__(self,itemId):
        self.itemId=itemId

    #itemID 추출
    def markets():
        headers = {
            'accept': 'application/json',
            'authorization' : Token
    }
        url = 'https://developer-lostark.game.onstove.com/markets/options'

        response = requests.get(url,headers=headers)
        jsonObject = response.json()

        print(jsonObject)

    def markets_search(self):
        url = f'https://developer-lostark.game.onstove.com/markets/items/{self.itemId}'

        response = requests.get(url,headers=self.headers)
        jsonObject = response.json()

        print(jsonObject)