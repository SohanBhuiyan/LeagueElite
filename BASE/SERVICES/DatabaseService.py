from BASE.DATABASE.Main import DatabaseService
import json
import os



class DatabaseService:

    databaseService = DatabaseService()

    def populateWithPlayerJSON(self,jsonFile, tier):
        curr_dir = os.path.abspath(os.path.join(__file__, os.pardir))  # able to get parent directory of current module
        rel_path = "JSON/"+jsonFile
        abs_file_path = os.path.join(curr_dir, rel_path)
        with open(abs_file_path, encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
            for entry in data["entries"]:
                summonername = entry["summonerName"]
                rank = tier
                self.databaseService.insertIntoProfile(summonername,rank)
        print("Populated with players in tier:{}".format(tier))


        #todo: Need to work on a method which populates teh champion_mastery table with each pro players mastery.


    def populateChampionMastery(self):
        None

