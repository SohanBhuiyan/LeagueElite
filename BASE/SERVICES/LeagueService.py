from BASE.SERVICES.API import API
from BASE.DATABASE.Database import Database
import json

import os

API = API()
def update_rosters():
    challenger_json = API.get_challenger_players()
    grandmaster_json = API.get_grandmaster_players()
    master_json = API.get_master_players()

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


def get_highest_mastery_entry_for(champId):
    db = Database()
    max_entry = db.select(" * FROM champion_mastery WHERE score=(SELECT MAX(score) FROM champion_mastery WHERE champId = {})".format(champId))
    return max_entry[0] # the first and only element in the list
