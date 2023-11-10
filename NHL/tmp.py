import game_request
import requests
import sys
import json
import os

season_data = []



def get_season(data, year, game):
    print(f"current game: {str(game)}")
    data = game_request.get(year,game)

    if data == 404 or game == 5:
        file_path = f"data/seasons/{year}.json"
        print()
        with open(file_path,"w") as file:
            json.dump(season_data, file, indent=4).replace("/","")
        return game, "done"
    
    
    else:
        season_data.append(data)
        return get_season(data,year,game+1)


get_season(0,sys.argv[1],1)

with open("data/seasons/2023.json") as file:
    data = json.load(file)


for game in data:
    print(game)
