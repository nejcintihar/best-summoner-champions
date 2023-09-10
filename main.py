import json
import requests
import os
from dotenv import load_dotenv
from api_fetcher import get_puuid
from api_fetcher import get_champions_ids
from api_fetcher import get_region

JSON_CHAMPION_URL = "http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json"

load_dotenv()
api_key = os.environ.get("X-Riot-Token")
headers = {
    'X-Riot-Token': api_key,
}
api_region = get_region()

username = input('Enter your League of Legends username: ')
count = input('Enter how many champions would you like to see: ')

puuid = get_puuid(username, api_region)

champion_Ids = get_champions_ids(puuid, count, api_region)

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
