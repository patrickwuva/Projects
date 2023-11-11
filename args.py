class args:

    def __init__(self,args) -> list:
        self.args = args 
        self.len = len(args)

    def get(self, i=0):
        
        if i != 0 and i <= self.len:
            return self.args[i]

    def index(self,i):
        
        if i not in self.args:
            return -1
        else:
            return self.args[i]
        