from urllib.request import urlopen
import json
api_key = "RGAPI-e3677b02-35f2-4ba7-8fff-ceff7265efe5"

def get_challenger_players():
    url="https://na1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key={}".format(api_key)
    html = urlopen(url)
    data = json.load(html)
    print(data)

def get_grandmaster_players():
    url="https://na1.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5?api_key={}".format(api_key)
    html = urlopen(url)
    data = json.load(html)
    print(data)

def get_master_players():
    url="https://na1.api.riotgames.com/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5?api_key={}".format(api_key)
    html = urlopen(url)
    data = json.load(html)
    print(data)
