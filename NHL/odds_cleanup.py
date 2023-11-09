from bs4 import BeautifulSoup
import requests

season = "2007-08"

url = "https://www.sportsbookreviewsonline.com/scoresoddsarchives/nhl-odds-2007-08/"
response = requests.get(url)
print(response.status_code)
html = response.text
soup = BeautifulSoup(html, "lxml")

test = soup.find("div")
print(test)
table = soup.find("table")
print(table)
if table:
    rows = table.find("tr")
    for row in rows:
            columns = row.find_all("td")
            for column in columns:
                print(column.text)
