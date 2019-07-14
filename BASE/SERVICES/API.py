import json
from urllib.request import urlopen

class API:

    API_KEY = "put your API Key Here "

    def get_all_champion_mastery_by_summonerID(self, summonerID):
        url = "https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{}?api_key={}".format(summonerID,self.API_KEY)
        html = urlopen(url)
        data = json.load(html)
        return data

    def get_highest_champion_mastery_by_summonerID(self, summonerID):
        url = "https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{}?api_key={}".format(
            summonerID, self.API_KEY)
        html = urlopen(url)
        data = json.load(html)
        first_entry = data[0]
        return first_entry

    def get_challenger_players():
        url = "https://na1.api.riotgames.com/lol/league/v4/challengerleagues/by-queue/RANKED_SOLO_5x5?api_key={}".format(
            API_KEY)
        html = urlopen(url)
        data = json.load(html)
        return data

    def get_grandmaster_players():
        url = "https://na1.api.riotgames.com/lol/league/v4/grandmasterleagues/by-queue/RANKED_SOLO_5x5?api_key={}".format(
            API_KEY)
        html = urlopen(url)
        data = json.load(html)
        return data

    def get_master_players():
        url = "https://na1.api.riotgames.com/lol/league/v4/masterleagues/by-queue/RANKED_SOLO_5x5?api_key={}".format(
            API_KEY)
        html = urlopen(url)
        data = json.load(html)
        return data

    def get_mastery(summoner_id,champion_id):
        url = "https://na1.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{}/by-champion/{}?api_key={}".format(summoner_id,champion_id,API_KEY)
        html = urlopen(url)
        data = json.load(html)
        return data

