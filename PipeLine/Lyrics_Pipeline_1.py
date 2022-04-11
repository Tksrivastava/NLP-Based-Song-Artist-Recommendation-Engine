import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

# Importing song name Data --
data = pd.read_excel('Song_data_Final.xlsx')
song_name = list(data['Songs'])
Artist = list(data['Artist_Name'])

# Creating URL key --
url_key_artist = []
url_key_song = []
for index in range(len(Artist)):
    url_key_artist.append(''.join(filter(str.isalnum, Artist[index])).lower())
    url_key_song.append(''.join(filter(str.isalnum, song_name[index])).lower().replace('acoustic', '').replace('remix', '')
                        .replace('remake', '').replace('remixes', '').replace('Taylorsversion', ''))
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}

# Creating urls --
url = []
for i in range(len(song_name)):
    link = 'https://www.google.com/search?q=%s+by+%s+lyrics&oq=hello+google&aqs=chrome.' \
           '.69i57j0i512j0i433i512j0i512l7.5855j0j7&sourceid=chrome&ie=UTF-8' % (url_key_song[i], url_key_artist[i])
    url.append(link)
lyrics_url = []
song = []
artist = []
for link in url:
    print(link)
    html_text = requests.get(link, headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')
    for links in soup.find_all('a'):
        link_str = str(links.get('href'))
        if link_str.find('genius.com') != -1:
            lyrics_url.append(links.get('href'))
            song.append(song_name[url.index(link)])
            artist.append(Artist[url.index(link)])

# Creating dictionary --
lyrics_dict = {
    'Artist': artist,
    'Songs': song,
    'Lyrics_links': lyrics_url
}
dataFrame = pd.DataFrame(lyrics_dict)
dataFrame.to_excel('Lyrics_link_data_1.xlsx', index=False)
