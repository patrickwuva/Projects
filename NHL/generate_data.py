import json

class generate_data:
    def __init__(self,team1, team2, season=2023):
        self.team1 = team1
        self.team2 = team2
        self.season = season

        with open(f'data/seasons/{str(season)}.json', 'r') as file:

            json_data = json.load(file)

        self.json_data = json_data
    

    def get(self):

        data = []
        for game in self.json_data:
            if game["homeTeam"]["abbrev"] == team1.name:

                if team2 != 0 and team2.name == game["awayTeam"]["abbrev"]:
                    data.append(game)    
                
                else:
                    data.append(game)

        if not data:
            return 0
        
        return data

