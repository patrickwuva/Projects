import sys
import args
from nhl_data import nhl_data


#args = args(sys.argv)

#commands = commands(args)

nhl = nhl_data()

data = nhl_data.get(sys.argv[1])

print("hello")
print(data)


