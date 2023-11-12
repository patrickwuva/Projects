from generate_data import generate_data


class nhl_data:

    def __init__(self):
       self.name = "name" 
        

    
    def get(team1, team2=0, w=0, l=0, season = 2023):
        
        data = generate_data.get(team1, team2, season)
        
        return_data = []
        print(data)
        for game in data:
            if team2 != 0:
                if game["awayTeam"]["abbrev"] == team2:

                    return_data.append((game["boxscore"]["linescore"]["totals"]["home"], game["boxscore"]["linescore"]["totals"]["away"]))

            else:
                return_data.append((game["boxscore"]["linescore"]["totals"]["home"], game["boxscore"]["linescore"]["totals"]["away"]))
    
        h_t = 0
        a_t = 0
        
        for h, a in return_data:
            if h > a:
                h_t += 1
            else:
                a_t += 1  

        return (h_t,a_t)





