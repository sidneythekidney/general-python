from bs4 import BeautifulSoup
import requests
import urllib3

url = 'https://www.espn.com/nba/standings'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

teams = soup.find_all('span',class_='hide-mobile')
for i in range(len(teams)):
    teams[i] = teams[i].get_text()

stats = soup.find_all('span',class_='stat-cell')
for i in range(len(stats)):
    stats[i] = stats[i].get_text()

stat_elements = ["NAME" , "W" , "L" , "AVG" , "GB" , "HOME" , "AWAY" , "DIV" , "CONF" , "PPG" , "OPP PPG" , "DIFF" , "STREAK" , "L10"]

print('\nEastern Conference: \n')

stat_line = ''
for i in range(len(stat_elements)):
    if i == 0:
        stat_line = stat_line + '   ' + stat_elements[i].ljust(26)
    if i > 0:
        stat_line = stat_line + '   ' + stat_elements[i].ljust(7)
stat_line = stat_line + '\n'
print(stat_line)

for i in range(len(teams)):
    team = teams[i]
    stat = ''

    if i == 15:
        print('\n\nWestern Conference: \n')
        print(stat_line)

    for j in range(13):
        stat = stat + '   ' + stats[13*i + j].ljust(7)
    if i < 15:
        print(str(i+1).ljust(4) + team.ljust(25) + stat)
    if i >= 15:
        print(str(i-14).ljust(4) + team.ljust(25) + stat)