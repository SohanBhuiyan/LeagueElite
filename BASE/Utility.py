import json
import os

def loadJsonFromPath(abs_file_path):
    with open(abs_file_path, encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
        return data;



def convert_champName_to_id(champion_name):
    curr_dir = os.path.dirname(__file__)  # <-- absolute dir the script is in
    rel_path = "JSON/championFull.json"
    abs_file_path = os.path.join(curr_dir, rel_path)

    with open(abs_file_path, encoding='utf-8') as data_file:
        data = json.loads(data_file.read())
        return data["data"][champion_name]["key"] #currently this will return a string.