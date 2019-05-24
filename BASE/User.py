import json
class User:
    champion_name = None
    summoner_name = None

    def __init__(self, summoner_name, champion_name):
        self.summoner_name = summoner_name
        self.champion_name = champion_name

    def convert_champ_id(self,champion_name):
        with open('championFull.json', encoding='utf-8') as data_file:
            data = json.loads(data_file.read())
            return data["data"][champion_name]["key"] #currently this will return a string.


    def get_champion_id(self):
        return self.convert_champ_id(self.champion_name)

    def get_champion_name(self):
        return self.champion_name

    def get_summoner_name(self):
        return self.summoner_name
