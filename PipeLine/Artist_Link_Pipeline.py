import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

# Method for extracting url --
def Find(string):
    # findall() has been used
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]" \
            r"+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url_find = re.findall(regex, string)
    return [x[0] for x in url_find]


# Importing artist data --
artist_data = pd.read_excel('Artist_data.xlsx')
artist_data_list = list(artist_data['Artist_Name'])
# Creating URL key --
url_key = []
for index in range(len(artist_data_list)):
    artist = artist_data_list[index]
    artist_list = list(artist)
    for i in range(len(artist_list)):
        if artist_list[i] == ' ':
            artist_list[i] = '+'
    key = ''.join(artist_list)
    url_key.append(key)
# Creating URL address -
url_address = []
for key in range(len(url_key)):
    url = 'https://www.google.com/search?q=musicbrainz+%s&rlz=1C1JZAP_enIN993IN993&oq=musicbrainz+alec+benjaim&aqs=' \
          'chrome..69i57j69i64.18661j0j7&sourceid=chrome&ie=UTF-8' % artist_data_list[key]
    url_address.append(url)
# Scrapping URL --
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
artist_singles_link_list = []
for url in url_address:
    html_text = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')
    artist = soup.find('div', class_='yuRUbf', attrs='href')
    artist_string = str(artist)
    links = Find(artist_string)
    valid_link = '%s' % links[0]
    artist_singles_link_list.append(valid_link)

# Creating a new csv file which will contain the link of musicbrainz for every artist
artist_dict = {
    'Artist_Name': artist_data_list,
    'MusicBrainz_link': artist_singles_link_list
}
dataFrame = pd.DataFrame(artist_dict)
dataFrame.to_excel('Artist_data_Final.xlsx', index=False)
