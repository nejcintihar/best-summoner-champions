import json
import requests
import os
from dotenv import load_dotenv

SUMMONER_NAME = 'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/'
CHAMPION_MASTERY_URL = "https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/"

load_dotenv()
api_key = os.environ.get("X-Riot-Token")
headers = {
    'X-Riot-Token': api_key,
}

def getPuuid(username):
    url = f'{SUMMONER_NAME}{username}'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['puuid']
    else:
        print(f'Error: {response.status_code}')
        print(response.text)

def getChampionsIds(puuid, count):
    champion_Ids = []

    url = f'{CHAMPION_MASTERY_URL}{puuid}/top?count={count}'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for item in data:
            champion_Ids.append(item['championId'])
    else:
        print(f'Error: {response.status_code}')
        print(response.text)

    return champion_Ids
