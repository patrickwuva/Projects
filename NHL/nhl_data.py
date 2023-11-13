from generate_data import generate_data

class nhl_data:

    def __init__(self):
        self.teams = ["FLA,", "TBL", "CAR", "BUF","PHI", 
                  "NJD","WPG","NYI","NYR",
                "OTT","TOR","MTL","WSH","BOS",
                  "PIT","COL","EDM","NSH","CGY",
                  "DAL","PHX","CBJ","DET","MIN",
                  "SJS","LAK","STL","VAN","ANA","CHI"]
        
    def home_abrv(self):

        return (["home"],["abbrev"])
    
    def away_abrv(self):

        return (["away"],["abbrev"])
    

    def home_total(self):

        return (["boxscore"],["linescore"],["totals"],["home"])

    def away_total(self):
        
        return (["boxscore"],["linescore"],["totals"],["away"])

    
    def get(team1, team2=-1, w=0, l=0, season = 2023):
       
      
        #if team1.get(team1) == 0:
        #    return "team 1 not found"
        #
        #if team2 != -1:
        #    if team.get(team2) == 0:
        #        return "team 2 not found"
        
     
        data = generate_data(team1, team2, season).get()
        #data = data.get(team1)
        
        return_data = []
        for game in data:



            if team2 != -1:


                if team1 == game["homeTeam"]["abbrev"] and team2 == game["awayTeam"]["abbrev"]:
                    return_data.append((game["boxscore"]["linescore"]["totals"]["home"], game["boxscore"]["linescore"]["totals"]["away"]))


                elif team2 == game["homeTeam"]["abbrev"] and team1 == game["awayTeam"]["abbrev"]:
                    return_data.append((game["boxscore"]["linescore"]["totals"]["away"], game["boxscore"]["linescore"]["totals"]["home"]))

            else:

                if team1 == game["homeTeam"]["abbrev"]:
                    return_data.append((game["boxscore"]["linescore"]["totals"]["home"], game["boxscore"]["linescore"]["totals"]["away"]))


                elif team1 == game["awayTeam"]["abbrev"]:
                    return_data.append((game["boxscore"]["linescore"]["totals"]["away"], game["boxscore"]["linescore"]["totals"]["home"]))


               
        h_t = 0
        a_t = 0
        for score in return_data:
            if  score[0] > score[1]:
                h_t += 1
            else:
                a_t += 1  

        return (h_t,a_t)





