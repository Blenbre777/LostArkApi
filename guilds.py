import requests
from lostArkApi import Token

class guilds:
    headers = {
        'accept': 'application/json',
        'authorization' : Token
        }
    
    def __init__(self,server):
        self.server=server
    
    #길드 랭킹 , 이름 
    def guilds(self):    
        url = f'https://developer-lostark.game.onstove.com/guilds/rankings?serverName={self.server}'

        response = requests.get(url,headers=self.headers)
        jsonObject = response.json()
        
        for list in jsonObject :
            print(list.get("Rank"))
            print(list.get("GuildName"))