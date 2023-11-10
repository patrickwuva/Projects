import game_request
import requests
import sys
import json

def get_season(data, year, game):
    print(f"current game: {str(game)}")
    data = game_request.get(year,game)

    if data == 404:
        return game, "done"
    
    
    else:
        print(f"Finishing game: {str(year)} {data['homeTeam']['abbrev']} played {data['awayTeam']['abbrev']} with a final score of {data['boxscore']['linescore']['totals']['home']} - {data['boxscore']['linescore']['totals']['away']}")
        return get_season(data,year,game+1)


get_season(0,2023,1)
