import requests
from lostArkApi import Token

class auctions:
    def __init__(self,options):
        self.options = options
        pass
    
    #경매장 검색 옵션 반환
    def auctions_serch():
        headers = {
            'accept': 'application/json',
            'authorization' : Token
        }
        url = 'https://developer-lostark.game.onstove.com/auctions/{self.options}'

        response = requests.get(url,headers=headers)
        jsonObject = response.json()

        print(response)
        print(jsonObject)