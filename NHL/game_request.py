import sys
import requests
import json

id = sys.argv[1].strip() 
url = f"https://api-web.nhle.com/v1/gamecenter/{id}/boxscore"
data = []
try:
    response = requests.get(url)
    data = json.loads(response.text)
        
except Exception as e:
    print(f"Error: {str(e)}")
    print(data["awayTeam"]["abbrev"])
