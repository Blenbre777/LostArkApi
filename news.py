import requests
from lostArkApi import Token

class news:
    
    def __init__(self):
        pass

    #공지사항 
    def notice():
        headers = {
            'accept': 'application/json',
            'authorization' : Token
        }
        url = 'https://developer-lostark.game.onstove.com/news/notices'

        response = requests.get(url,headers=headers)
        jsonObject = response.json()

        for list in jsonObject[:10]:
            print(list.get("Title"))