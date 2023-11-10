import game_request
import requests
import sys
import json

game = 1
year = 2023
data = 0
while data != 404:
    data = game_request.get(year,game)
    game += 1
    print(game)
    
