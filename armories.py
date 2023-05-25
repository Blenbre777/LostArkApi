import requests
from lostArkApi import Token

class armories:
    headers = {
            'accept': 'application/json',
            'authorization' : Token
        }
    def __init__(self, name):
        self.name = name
    
    #모든 정보
    def characters(self):
        url = f'https://developer-lostark.game.onstove.com/armories/characters/{self.name}'

        response = requests.get(url,headers=self.headers)
        jsonObject = response.json()

        print(response)
        print(jsonObject)

    #프로필
    def profile(self):
        url = f'https://developer-lostark.game.onstove.com/armories/characters/{self.name}/profiles'

        response = requests.get(url,headers=self.headers)
        jsonObject = response.json()

        print(response)
        

        print(jsonObject['CharacterImage'])
        print(jsonObject['ServerName'])
        print(jsonObject['CharacterLevel'])
        print(jsonObject['ItemAvgLevel'])

    #장비
    def equipment(self):
        url = f'https://developer-lostark.game.onstove.com/armories/characters/{self.name}/equipment'

        response = requests.get(url,headers=self.headers)
        jsonObject = response.json()

        print(response)
        print(jsonObject)

    #아바타
    def avatars(self):
        url = f'https://developer-lostark.game.onstove.com/armories/characters/{self.name}/avatars'

        response = requests.get(url,headers=self.headers)
        jsonObject = response.json()

        print(response)
        print(jsonObject)
    
    #스킬 
    def combat_skills(self):
        url = f'https://developer-lostark.game.onstove.com/armories/characters/{self.name}/combat-skills'

        response = requests.get(url,headers=self.headers)
        jsonObject = response.json()

        print(response)
        print(jsonObject)

    #카드
    def card(self):
        url = f'https://developer-lostark.game.onstove.com/armories/characters/{self.name}/cards'

        response = requests.get(url,headers=self.headers)
        jsonObject = response.json()

        print(response)
        print(jsonObject)
    
    #보석 
    def gems(self):
        url = f'https://developer-lostark.game.onstove.com/armories/characters/{self.name}/gems'

        response = requests.get(url,headers=self.headers)
        jsonObject = response.json()

        print(response)
        print(jsonObject)

    #증명의 전장 
    def colosseums(self):
        url = f'https://developer-lostark.game.onstove.com/armories/characters/{self.name}/colosseums'

        response = requests.get(url,headers=self.headers)
        jsonObject = response.json()

        print(response)
        print(jsonObject)
    
    #수집품 요약 
    def collectibles(self):
        url = f'https://developer-lostark.game.onstove.com/armories/characters/{self.name}/collectibles'

        response = requests.get(url,headers=self.headers)
        jsonObject = response.json()

        print(response)
        print(jsonObject)