import pandas as pd
import requests
from bs4 import BeautifulSoup
import shutil
import os

#get url and parse
url = input('Enter a URL: ')
result = requests.get(url)
doc = BeautifulSoup(result.text, "html.parser")

#extract plain text
summary = doc.find_all('tr')
list_text= [x.get_text()for x in summary]

#place text to pandas and csv
df = pd.DataFrame(list_text)
csv = input('Enter name of csv: ')
df.to_csv(csv) 

#move file to folder
source = "C:\\Users\\user\\Desktop\\Nairaland_Scraper"
destination = "C:\\Users\\user\\Desktop\\Nairaland_Scraper\\Nairaland_csv"

try:
    for file in os.listdir(source):
        if file.endswith('_csv'):
            shutil.move(source + f'\\{file}', destination)
            print('file moved')
            print(f"{file}")

except Exception as error:
    print(error)
