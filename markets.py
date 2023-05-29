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
        code_list=[]
        headers = {
            'accept': 'application/json',
            'authorization' : Token
    }
        url = 'https://developer-lostark.game.onstove.com/markets/options'

        response = requests.get(url,headers=headers)
        jsonObject = response.json()
        
        data =  (jsonObject.get('Categories'))
        for item in data:
            code = item['Code']
            code_name = item['CodeName']
            code_list.append((code,code_name))
        return code_list

    #itemID 기반 검색 
    def markets_search(self):
        url = f'https://developer-lostark.game.onstove.com/markets/items/{self.itemId}'

        response = requests.get(url,headers=self.headers)
        jsonObject = response.json()

        print(jsonObject)