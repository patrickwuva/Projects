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

        if data == 404 or data["clock"]["timeRemaining"] == "20:00":
            break

        print(f"current game: {str(game)}")

        season_data.append(data)

        game = game + 1
      
    return season_data


get_season(sys.argv[1],int(sys.argv[2]))

if season_data:

    with open("data/seasons/2023.json", "w") as file:

        file.write(json.dumps(season_data))



else:
    print("No data")