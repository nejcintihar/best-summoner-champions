import json
import requests
import os
from dotenv import load_dotenv
from api_fetcher import getPuuid
from api_fetcher import getChampionsIds

JSON_CHAMPION_URL = "http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json"

load_dotenv()
api_key = os.environ.get("X-Riot-Token")
headers = {
    'X-Riot-Token': api_key,
}

username = input('Enter your League of Legends username: ')
count = input('Enter how many champions would you like to see: ')

puuid = getPuuid(username)

champion_Ids = getChampionsIds(puuid, count)

response = requests.get(JSON_CHAMPION_URL, headers=headers)

if response.status_code == 200:
    data = json.loads(response.text)

    champion_data = data['data']
    champion_id_name_map = {champion_data[champion]['key'].lower(): champion for champion in champion_data}

    def get_champion_name(champion_id):
        return champion_id_name_map.get(str(champion_id).lower(), "Champion not found")

    champion_names = [get_champion_name(champion_id) for champion_id in champion_Ids]
    print(f"{username}'s most played champions:", champion_names)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
