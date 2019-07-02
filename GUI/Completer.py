import json
import os


def create_autocomplete_list():
    temp_list = []

    par_dir = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
    rel_path = "BASE/JSON/championFull.json"
    abs_file_path = os.path.join(par_dir, rel_path)

    with open(abs_file_path, encoding='utf-8') as data_file:
        data = json.loads(data_file.read())

        for champion in data["data"]:
            temp_list.append(champion)
        return temp_list


def get_autocomplete_list():
    ac_list = create_autocomplete_list()
    return ac_list


get_autocomplete_list()