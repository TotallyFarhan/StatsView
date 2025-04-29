import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.pro-football-reference.com/years/2024/passing.htm"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
csvFilename = 'quarterbackDataset.csv'

quarterbacks = soup.find_all('tr')[:54]

qbStats = []
last_known_value = None

headers = quarterbacks[0].find_all('th')
header_data = []

for header in headers[1:]:
    header_text = header.text.strip()
        
    if header_text in ['\xa0', '']:
        header_data.append(last_known_value)
    else:
        last_known_value = header_text
        header_data.append(last_known_value)
        
qbStats.append(header_data)
    
#print(quarterbacks[0])

quarterbacks = quarterbacks[1:]

for quarterback in quarterbacks:
    stats = quarterback.find_all('td')
    qb_data = []

    for stat in stats:
        stat_text = stat.text.strip()

        if stat_text in ['\xa0', '']:  
            qb_data.append(last_known_value)
        else:
            last_known_value = stat_text
            qb_data.append(last_known_value)

    qbStats.append(qb_data)

with open(csvFilename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(qbStats)