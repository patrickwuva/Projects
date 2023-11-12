import json

class generate_data:
    def __init__(self,team1, team2=0,season):
        self.team1 = team1
        self.team2 = team2
        self.season = season

        with open('data/seasons/{str(season)}.json', 'r') as file:

            json_data = json.load(file)

        self.json_data = json_data
    

    def get(self):

        data = []
        for game in self.json_data:
            if game["homeTeam"]["abbrev"] == self.team1:

                if self.team2 != 0 and self.team2 = game["awayTeam"]["abbrev"]:
                    data.append(game)    
                
                else:
                    data.append(game)

        if not data:
            return 0

        return data

