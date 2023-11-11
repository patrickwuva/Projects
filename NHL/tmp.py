import game_request
import requests
import sys
import json
import os

season_data = []



def get_season(year, game):
   
    
    data = 0
    while True:

        
        data = game_request.get(year,game)

        if data == 404 or data["gameState"] == "FUT":
            break
        print(f"current game: {str(game)}")

        season_data.append(data)

        game = game + 1

        print( data["gameState"])
      
    return season_data


get_season(sys.argv[1],400)


with open("data/seasons/2023.json", "w") as file:

    file.write(season_data)
