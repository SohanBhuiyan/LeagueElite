import json
import os
class User:
    champion_name = None
    summoner_name = None
    summoner_id = None
    api_key = "RGAPI-e3677b02-35f2-4ba7-8fff-ceff7265efe5"

    # constructor
    def __init__(self, summoner_name, champion_name):
        self.summoner_name = summoner_name
        self.champion_name = champion_name

    def convert_champ_id(self,champion_name):
        curr_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
        rel_path = "JSON/championFull.json"
        abs_file_path = os.path.join(curr_dir, rel_path)

        with open(abs_file_path, encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
            return data["data"][champion_name]["key"] #currently this will return a string.


    def get_champion_id(self):
        return self.convert_champ_id(self.champion_name)

#TODO Need to seperate REST calls to a different file. Its going to look messy by manually inserting the same code over again
    def get_summoner_id(self):
        url = "https://na1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key={}".format(
            self.api_key)
        html = urlopen(url)
        data = json.load(html)

    def get_champion_name(self):
        return self.champion_name

    def get_summoner_name(self):
        return self.summoner_name
