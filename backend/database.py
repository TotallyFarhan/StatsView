import requests
from bs4 import BeautifulSoup
import csv

# Gives the url to be webscraped to BeautifulSoup for parsing
url = "https://www.pro-football-reference.com/years/2024/passing.htm"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
csvFilename = 'backend/quarterbackDataset.csv' # File name where data will be stored

# Finds the first 53 rows in the table of quarterbacks stats
quarterbacks = soup.find_all('tr')[:54]

qbStats = [] # Array to hold all the data from the quarterback rows which will be converted to the CSV file
last_known_value = None

# Finds all the header data in the table
headers = quarterbacks[0].find_all('th')
header_data = []

# Goes through each table and extracts the text from it, then adds it to the qbStats array
for header in headers[1:]:
    header_text = header.text.strip()
        
    if header_text in ['\xa0', '']:
        header_data.append(last_known_value)
    else:
        last_known_value = header_text
        header_data.append(last_known_value)
# Adds the header data to the array
qbStats.append(header_data)
    
quarterbacks = quarterbacks[1:] # Removes the header row from the rows array

# Goes through all the rest of the rows of quarterback data and extracts the text from it, then adds it to the qbStats array
for quarterback in quarterbacks:
    stats = quarterback.find_all('td') # Extracts each data point from a row
    qb_data = []

    for stat in stats:
        stat_text = stat.text.strip()

        if stat_text in ['\xa0', '']:  
            qb_data.append(last_known_value)
        else:
            last_known_value = stat_text
            qb_data.append(last_known_value)
    # Adds the array of QB data to the array
    qbStats.append(qb_data)

# Creates a CSV file and fills its content with the array of QB data created in the loops above
with open(csvFilename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerows(qbStats)