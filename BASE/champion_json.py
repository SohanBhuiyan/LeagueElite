import json

with open('championFull.json', encoding='utf-8') as data_file:
    data = json.loads(data_file.read())

print(data["data"]["Aatrox"]["key"])

def get_champion_id(champion_name):
    with open('championFull.json', encoding='utf-8') as data_file:
     data = json.loads(data_file.read())
     return data["data"][champion_name]["key"]
