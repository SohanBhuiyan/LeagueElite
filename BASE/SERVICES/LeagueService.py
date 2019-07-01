from urllib.request import urlopen
from BASE.SERVICES.API import get_challenger_players
from BASE.SERVICES.API import get_grandmaster_players
from BASE.SERVICES.API import get_master_players
from BASE.DATABASE.Database import Database
import json

import os



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

    challenger_json = get_challenger_players()
    grandmaster_json = get_grandmaster_players()
    master_json = get_master_players()

    #return dir of the file that called this method, not nessecarily the directory this file is under.
    dir = os.getcwd()

    filename = os.path.join(dir, 'JSON/challenger.json')

    with open(filename, 'w') as outfile:
        json.dump(challenger_json, outfile)

    filename = os.path.join(dir, 'JSON/grandmaster.json')
    with open(filename, 'w') as outfile:
        json.dump(grandmaster_json, outfile)

    filename = os.path.join(dir, 'JSON/master.json')
    with open(filename, 'w') as outfile:
        json.dump(master_json, outfile)


"""
@param: 
jsonData: JSON data of different tiered players
champId: the id that is associated with a champion name. Method in user class can convert champname to id
"""
def get_highest_mastery_entry_for(champId):
    db = Database()
    max_entry = db.select("SELECT * FROM champion_mastery WHERE score=(SELECT MAX(score) FROM champion_mastery WHERE champId = {})".format(champId))
    return max_entry

