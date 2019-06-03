from BASE.DATABASE.Main import Database
import json
import os



class DatabaseService:

    databaseService = Database()


    # The file should have .json extension.
    def populateWithPlayerJSON(self,jsonFile, tier):
        try:
            # curr_dir, rel_path, abs_file_path are just file path setup to find the JSON file.
            curr_dir = os.getcwd()
            rel_path = "JSON/"+jsonFile
            abs_file_path = os.path.join(curr_dir, rel_path) # eg. BASE/JSON/Challenger.jso
            with open(abs_file_path, encoding='utf-8') as data_file:
                data = json.loads(data_file.read())
            for entry in data["entries"]:
                summonername = entry["summonerName"]
                rank = tier
                self.databaseService.insertIntoProfile(summonername,rank)
            print("Populated with players in tier:{}".format(tier))
        except FileNotFoundError:
            print("ERROR: File name does not exist inside of JSON dir")
        except TypeError:
            print("ERROR: jsonFile format is incorrect. View RIOT's API Response Body for correct format")




        #todo: Need to work on a method which populates the champion_mastery table with each pro players mastery.

    def populateMasteryTable(self):
        cursor = self.databaseService.select("* FROM profiles")
        for data in cursor:
            print(data)

    def getID(self, summonername):
        self.databaseService.select("From profiles WHERE summonername = {}".format(summonername))

    def find(name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)