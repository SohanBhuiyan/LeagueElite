import os
import time

from BASE.DATABASE.Database import Database
from BASE.SERVICES.API import get_highest_champion_mastery_by_summonerID
from BASE.Utility import *


class DatabaseService:
    ID_INDEX = 0
    database = Database()
    def insert_players_by_rank(self, rank):
        try:
            rank.lower()
            player_list_json = self.get_players_by_rank(rank)
            print("Please wait while populating players....")
            if player_list_json != None:
                for player in player_list_json["entries"]:
                    summonername = player["summonerName"]
                    summonerId = player["summonerId"]
                    self.database.insert_into_profile_table(summonername, summonerId, rank)
                print("Populated with players in tier:{}".format(rank))

        except TypeError:
            print("ERROR: jsonFile format is incorrect. View RIOT's API Response Body for correct format")

    def get_players_by_rank(self, rank):
        try:
            curr_dir = os.getcwd()
            rel_path = "JSON/" + rank + ".json"
            abs_file_path = os.path.join(curr_dir, rel_path)  # eg. BASE/JSON/Challenger.json
            players_json_data = loadJsonFromPath(abs_file_path)
            return players_json_data
        except FileNotFoundError:
            print("Provided rank does not exist, try string Challenger or Master")
            return None


        #todo: Need to work on a method which populates the champion_mastery table with each pro players mastery.


    def update_mastery_table(self):
        api_call_count = 0
        print("Please wait one moment...")
        profile_list = self.database.select("* FROM profiles")
        for profile in profile_list:

            if api_call_count == 100: #my api limit is 200 per 2min, so we will wait it out
                time.sleep(180)
                api_call_count = 0 # reset api_call_count after we waited about two minutes

            summonerID = profile[self.ID_INDEX]
            summonerName = profile[1]

            highest_mastery_entry = get_highest_champion_mastery_by_summonerID(summonerID)
            api_call_count = api_call_count + 1
            mastery_points = highest_mastery_entry["championPoints"]
            champion_id = highest_mastery_entry["championId"]
            self.database.insert_into_champion_mastery_table(summonerName,mastery_points,champion_id)
            time.sleep(.1) # to prevent overdoing api requests in a short period of time
        print("Done populating champion_mastery table")


    def getID(self, summonername):
        self.database.select("From profiles WHERE summonername = {}".format(summonername))


