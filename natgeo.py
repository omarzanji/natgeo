# Scrapes NatGeo pic of the day and puts in folder.

# Author: Omar Barazanji
# Date: 8/20/20
# Python Version: 2.7

import requests
import urllib
from bs4 import BeautifulSoup

url = 'https://www.nationalgeographic.com/photography/photo-of-the-day'

# Fetch content
page = requests.get(url)

# Extracting HTML code
soup = BeautifulSoup(page.text, 'lxml')

image_loc = soup.findAll('div', {'class' : 'parsys iparsys content'})

image_json = str(image_loc[0])

if len(image_json) > 0:
    print('Data fetched, downloading...')

img_json = ''
for ndx, x in enumerate(image_json):
    if 'endpoint' in image_json[ndx: ndx+8]:
        img_json = image_json[ndx+11:]
        break

json_link = ''
for ndx, x in enumerate(img_json):
    if x == ',':
        json_link = img_json[:ndx-1]
        break

# Fetch json content
page2 = requests.get(json_link)

json_data = page2.json()

for x in json_data['items']:
    urllib.urlretrieve(x['originalUrl'], 'DailyPhoto.jpg')
    break

print('Image saved in program directory')
