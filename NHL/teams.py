
class team:

    def __init__(self) -> None:
        pass
        self.teams = ["FLA,", "TBL", "CAR", "BUF","PHI", 
                  "NJD","WPG","NYI","NYR",
                "OTT","TOR","MTL","WSH","BOS",
                  "PIT","COL","EDM","NSH","CGY",
                  "DAL","PHX","CBJ","DET","MIN",
                  "SJS","LAK","STL","VAN","ANA","CHI"]

    
    def get(self, team):
        if team in self.teams:
            return self.teams[self.teams.index(team)]
        
        else:
            return 0
        
    def home_abrv(self):

        return ["home"]["abbrev"]
    
    def away_abrv(self):

        return ["away"]["abbrev"]
    

    def home_total(self):

        return ["boxscore"]["linescore"]["totals"]["home"]

    def away_total(self):
        
        game["boxscore"]["linescore"]["totals"]["away"]
