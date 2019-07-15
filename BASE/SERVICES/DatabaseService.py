import time

from BASE.DATABASE.Database import Database
from BASE.SERVICES.API import API
from BASE.Utility import *


class DatabaseService:
    CHAMP_ID_INDEX = 2
    ID_INDEX = 0
    SUMMONER_INDEX = 1
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
        apiHelper = API()
        print("Please wait one moment...")
        profile_list = self.database.select("* FROM profiles")
        for profile in profile_list:
            # API limitation condition
            if api_call_count == 99: #my api limit is 100 per 2min, so we will wait it out
                print("almost at api limit call, waiting 3 min...")
                time.sleep(180)
                api_call_count = 0 # reset api_call_count after we waited about two minutes
                print("finish waiting, continuing process")

            profileID = profile[self.ID_INDEX] # needed to call certain API methods
            summonerName = profile[self.SUMMONER_INDEX] # what the client sees.

            highest_mastery_entry = apiHelper.get_highest_champion_mastery_by_summonerID(profileID)
            api_call_count = api_call_count + 1

            mastery_points = highest_mastery_entry["championPoints"]
            champion_id = highest_mastery_entry["championId"]

            #check if the player already exist in the db. If so, just update its values
            possible_duplicate = self.database.select("* FROM champion_mastery WHERE summonername=\"{}\"".format(summonerName))

            #if a duplicate exist, same name and champID, we just update score
            if possible_duplicate:
                if possible_duplicate[0][self.CHAMP_ID_INDEX] == champion_id:
                    self.database.update("champion_mastery","score",mastery_points,summonerName)
            else:
                self.database.insert_into_champion_mastery_table(summonerName,mastery_points,champion_id)
            time.sleep(.05) # to prevent overdoing api requests in a short period of time
        print("Done populating champion_mastery table")


    def getID(self, summonername):
        self.database.select("From profiles WHERE summonername = {}".format(summonername))
