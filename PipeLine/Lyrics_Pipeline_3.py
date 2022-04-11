import pandas as pd
import requests
from bs4 import BeautifulSoup
import unidecode
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry




# Importing Data set --
data = pd.read_excel('Lyrics_link_data_Final.xlsx')
artist = list(data['Artist'])
song = list(data['Songs'])
link = list(data['Lyrics_links'])
genre = list(data['Genre'])

# Scraping lyrics --
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
lyrics = ''
for url_index in range(len(link)):
    file_address = 'C:/Users/TANUL/PycharmProjects/FinalYearProject/Phase - 2/PipeLine/Lyrics_Data' \
                   '/%s&%s@%s.txt' % (artist[url_index], unidecode.unidecode(song[url_index]), str(genre[url_index]).
                                      replace('/', '_'))
    print('%s&%s@%s.txt' % (artist[url_index], unidecode.unidecode(song[url_index]), str(genre[url_index]).
                            replace('/', '_')))
    # html_text = requests.get(link[url_index], headers=headers).text
    session = requests.Session()
    retry = Retry(connect=3, backoff_factor=1)
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    html_text = session.get(link[url_index], headers=headers).text
    soup = BeautifulSoup(html_text, 'lxml')
    lyrics = soup.find_all('div', class_='Lyrics__Container-sc-1ynbvzw-6 jYfhrf')
    lyrics_text = []
    for text in lyrics:
        lyrics_text.append(text.get_text())
    text = ' '.join(lyrics_text)
    file = open(file_address, 'w', encoding="utf-8")
    file.write(text)
    file.close()

