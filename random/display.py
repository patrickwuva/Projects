from node import node

class display:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[]]
        self._create()

    def _create(self):
        for y in range(self.height):
            self.board.append([])
            for x in range(self.width):
                self.board[y].append(node((x,y)," "))

    def print(self):
        for y in range(self.height):
            for x in range(self.width):
                print(self.board[y][x].val, end="\r")
            print("")


