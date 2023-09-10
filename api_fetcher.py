import os

import requests
from dotenv import load_dotenv

BASE_URL = "https://{region}.api.riotgames.com"

SUMMONER_NAME = f'{BASE_URL}/lol/summoner/v4/summoners/by-name/'
CHAMPION_MASTERY_URL = f'{BASE_URL}/lol/champion-mastery/v4/champion-masteries/by-puuid/'

load_dotenv()
api_key = os.environ.get("X-Riot-Token")
headers = {
    'X-Riot-Token': api_key,
}


def get_puuid(username, region):
    url = SUMMONER_NAME.format(region=region) + username

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['puuid']
    else:
        print(f'Error: {response.status_code}')
        print(response.text)


def get_champions_ids(puuid, count, region):
    champion_ids = []

    url = CHAMPION_MASTERY_URL.format(region=region) + puuid + '/top?count=' + count

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        for item in data:
            champion_ids.append(item['championId'])
    else:
        print(f'Error: {response.status_code}')
        print(response.text)

    return champion_ids


def get_region():
    while True:
        print("What region is your account located in?")
        print("BR, EUNE, EUW, LAN, LAS, NA, OCE, RU, TR, JP, KR, PH, SG, TW, TH, VN?")
        region = input("Region: ").strip().upper()

        if region == "BR":
            return "BR1"
        elif region == "EUNE":
            return "EUN1"
        elif region == "EUW":
            return "EUW1"
        elif region == "LAN":
            return "LA1"
        elif region == "LAS":
            return "LA2"
        elif region == "NA":
            return "NA1"
        elif region == "OCE":
            return "OC1"
        elif region == "RU":
            return "RU1"
        elif region == "TR":
            return "TR1"
        elif region == "JP":
            return "JP1"
        elif region == "KR":
            return "KR1"
        elif region == "PH":
            return "PH1"
        elif region == "SG":
            return "SG2"
        elif region == "TW":
            return "TW2"
        elif region == "TH":
            return "TH2"
        elif region == "VN":
            return "VN2"
        else:
            print("Invalid region. Please enter a valid region.")
