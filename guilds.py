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
        rank = []
        guildName =[]

        url = f'https://developer-lostark.game.onstove.com/guilds/rankings?serverName={self.server}'

        response = requests.get(url,headers=self.headers)
        jsonObject = response.json()
        
        for list in jsonObject :
            rank.append(list.get("Rank"))
            guildName.append(list.get("GuildName"))
        
        return rank , guildName