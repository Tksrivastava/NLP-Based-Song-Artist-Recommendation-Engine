import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup

# Importing artist data --
artist_data = pd.read_excel('Song_data_Final.xlsx')
artist = list(artist_data['Artist_Name'])
artist = np.unique(artist)
# Creating URL key --
url_key = []
for index in range(len(artist)):
    artist_name = artist[index]
    artist_list = list(artist_name)
    for i in range(len(artist_list)):
        if artist_list[i] == ' ':
            artist_list[i] = '+'
    key = ''.join(artist_list)
    url_key.append(key)

# Creating URL address -
url_address = []
for key in range(len(url_key)):
    url = 'https://www.google.com/search?q=%s+genre&rlz=1C1JZAP_enIN993IN993&oq=musicbrainz+alec+benjaim&aqs=' \
          'chrome..69i57j69i64.18661j0j7&sourceid=chrome&ie=UTF-8' % url_key[key]
    url_address.append(url)

# Scrapping URL --
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
genre_list = []
for url in url_address:
    print(url)
    html_text = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')
    data = soup.find_all('div', class_=['bVj5Zb FozYP', 'Z0LcW'])
    for div in data:
        print(div.get_text())
        if len(div.get_text()) != 0:
            genre_list.append(div.get_text())
        else:
            print('')
            genre_list.append('')
        break


# Creating a new csv file which will contain the link of musicbrainz for every artist
artist_dict = {
    'Artist_Name': artist,
    'Genre': genre_list
}
dataFrame = pd.DataFrame(artist_dict)
dataFrame.to_excel('Genre_data_Final.xlsx', index=False)
