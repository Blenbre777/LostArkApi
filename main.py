import requests
import json
from lostArkApi import Token


headers = {
    'accept': 'application/json',
    'authorization' : Token
}

url = 'https://developer-lostark.game.onstove.com/news/notices'

response = requests.get(url,headers=headers)
jsonObject = response.json()

print(response)
print(jsonObject)
