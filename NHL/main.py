import sys

from nhl_data import nhl_data


nhl = nhl_data()


if len(sys.argv) == 2:
    
    data = nhl_data.get(sys.argv[1])

    print(f"{sys.argv[1]} is {data[0]}-{data[1]}  on the season")

    
    sys.exit


elif len(sys.argv) == 3:

    data = nhl_data.get(sys.argv[1],sys.argv[2])

    print(f"{sys.argv[1]} is {data[0]}-{data[1]} against {sys.argv[2]}")
    
    sys.exit
else:
    print("error")