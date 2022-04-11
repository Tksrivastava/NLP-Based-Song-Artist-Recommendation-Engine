import pandas as pd
import requests
from bs4 import BeautifulSoup

# Importing Artist Link Data --
data = pd.read_excel('Artist_data_Final.xlsx')
Link = list(data['MusicBrainz_link'])
Artist = list(data['Artist_Name'])
# Scrapping --
song_dict = {
    'Artist_Name': [],
    'Songs': []
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
index = 0
for link in Link:
    html_text = requests.get(link, headers=headers).text
    new_html_text = html_text[html_text.find('<h3>Single</h3>'): html_text.find('<h3>Single + Soundtrack</h3>')]
    soup = BeautifulSoup(new_html_text, 'lxml')
    data = soup.find_all('bdi', text=True)
    song_name = []
    songs = []
    for links in soup.find_all('a'):
        url = 'https://musicbrainz.org/%s' % links.get('href')
        if str(links.get('href')).find('/release-group/') == str(links.get('href')).find('/'):
            name_html = requests.get(url, headers=headers).text
            new_soup = BeautifulSoup(name_html, 'lxml')
            name = new_soup.find('bdi', text=True)
            songs.append(name.text)
    Artist_list = [Artist[index]] * len(songs)
    song_dict['Artist_Name'].extend(Artist_list)
    song_dict['Songs'].extend(songs)
    index += 1
# Saving to excel file --
dataFrame = pd.DataFrame(song_dict)
dataFrame.to_excel('Song_data_Final.xlsx', index=False)



