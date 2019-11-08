from bs4 import BeautifulSoup
import requests
import urllib3

url = 'https://www.espn.com/college-football/rankings'

response = requests.get(url)
content = BeautifulSoup(response.content, 'html.parser')

rankings = content.find_all('span',class_='pl3 hide-mobile clr-link underline-hover')
stats = content.find_all('td',class_='Table2__td')

print("\nNCAAF RANKINGS:\n")
print(' '.ljust(4) + 'TEAM'.ljust(23) + 'REC'.ljust(8) + 'PTS'.ljust(8) + 'TRND'.ljust(8) + '\n')

for i in range(len(rankings)):
    stat_line = ''
    for j in range(3):
        stat_line = stat_line + '   ' + stats[5*i + j + 2].get_text().ljust(5)
    print(str(i+1).ljust(4) + rankings[i].get_text().ljust(20) + stat_line.ljust(10))
