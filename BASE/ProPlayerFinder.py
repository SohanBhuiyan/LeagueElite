from urllib.request import urlopen
import json
import os

api_key = "RGAPI-bb691d42-4587-4e19-8abe-b5c303699877"

# returns JSON of different high-tiered players
def get_challenger_players():
    url="https://na1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key=RGAPI-bb691d42-4587-4e19-8abe-b5c303699877"
    html = urlopen(url)
    data = json.load(html)
    return data

def get_grandmaster_players():
    url="https://na1.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5?api_key={}".format(api_key)
    html = urlopen(url)
    data = json.load(html)
    return data


def get_master_players():
    url="https://na1.api.riotgames.com/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5?api_key={}".format(api_key)
    html = urlopen(url)
    data = json.load(html)
    return data

def get_mastery(summoner_id,champion_id):
    url = "https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{}/by-champion/{}?api_key={}".format(summoner_id,champion_id,api_key)
    html = urlopen(url)
    data = json.load(html)
    return data

def find_pro_player():
    #if champ mastery is the highest, then return it
    # parse each tier JSON file, challenger, gm, master and try to find the highest player

    highest_mastery = None
    highest_mastery_user = None

    challenger_json = get_challenger_players()

    for entry in challenger_json["entries"]:
        if entry["wins"] > 350:
            print("Jesus {}, u got {} wins"
                  .format(entry["summonerName"],
                          entry["wins"]))

def create_player_json():

    challenger_json = get_challFunenger_players()
    grandmaster_json = get_grandmaster_players()
    master_json = get_master_players()

    dir = os.path.dirname(__file__)
    filename = os.path.join(dir, 'JSON/challenger.json')

    with open(filename, 'w') as outfile:
        json.dump(challenger_json, outfile)

    filename = os.path.join(dir, 'JSON/grandmaster.json')
    with open(filename, 'w') as outfile:
        json.dump(grandmaster_json, outfile)

    filename = os.path.join(dir, 'JSON/master.json')
    with open(filename, 'w') as outfile:
        json.dump(master_json, outfile)

create_player_json()