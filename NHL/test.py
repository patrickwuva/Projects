import json

with open('data/seasons/2023.json', 'r') as file:
    json_data = json.load(file)

print(json_data["id"])