import requests
import json
import sys


def get(year,game):
    
    game = str(game)

    for i in range(len(game),4):
        game = "0"+game


    data = []
    response = requests.get(f"https://api-web.nhle.com/v1/gamecenter/{str(year)}02{game}/boxscore")
    
    if response.status_code != 200:
        data = 404

    else:

        data = json.loads(response.text)
    return data
