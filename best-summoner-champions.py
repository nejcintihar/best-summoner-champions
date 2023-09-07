import json
import requests

api_key = 'YOUR_API_KEY'

champion_Ids = []

username = input('Enter your League of Legends username: ')

json_champion_url = "http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json"

url = f'https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{username}'

headers = {
    'X-Riot-Token': api_key,
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    puuid = data['puuid']
else:
    print(f'Error: {response.status_code}')
    print(response.text)

url = f'https://euw1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}/top?count=3'

headers = {
    'X-Riot-Token': api_key,
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    for item in data:
        champion_Ids.append(item['championId'])
else:
    print(f'Error: {response.status_code}')
    print(response.text)

response = requests.get(json_champion_url, headers=headers)

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
