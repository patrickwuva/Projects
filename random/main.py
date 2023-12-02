import time
from display import display

display = display(10,10)

for x in range(10):
    node = display.board[x][x]

    node.val = str(x)
    display.print()
    node.val = " "
    time.sleep(1)

display.print()
