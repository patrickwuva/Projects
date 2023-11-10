import requests
import json


def get(year,game):
    
    game = str(game)

    while len(game) < 4:
        game = "0"+game
    print(game)
    data = []
    response = requests.get(f"https://api-web.nhle.com/v1/gamecenter/{str(year)}02{game}")
    if response.status_code != 200:
        data = 404

    else:

        data = json.loads(response.text)
    return data
