import pandas as pd


# Importing Data set --
data = pd.read_excel('Lyrics_link_data_1.xlsx')
artist = list(data['Artist'])
song = list(data['Songs'])
link = list(data['Lyrics_links'])

# Removing extra links --
for index in range(0, len(link) - 1):
    if str(link[index+1]).find('translate.google.com') != -1:
        artist[index] = ''
        song[index] = ''
        link[index] = ''
        artist[index + 1] = ''
        song[index + 1] = ''
        link[index + 1] = ''

artist_new_1 = [e for e in artist if e != '']
song_new_1 = [e for e in song if e != '']
link_new_1 = [e for e in link if e != '']

for index in range(len(link_new_1)):
    if song_new_1[index] == song_new_1[index-1] and link_new_1[index] != link_new_1[index-1]:
        artist_new_1[index-1] = ''
        song_new_1[index-1] = ''
        link_new_1[index-1] = ''

artist_new = [e for e in artist_new_1 if e != '']
song_new = [e for e in song_new_1 if e != '']
link_new = [e for e in link_new_1 if e != '']

song_new_2 = [song_name.replace('/', '_').replace(' ', '_').replace('#', '_').replace('•', '_').replace('?', '_')
              .replace('*', '_').replace('"', '').replace("'", '').replace('/', '_').replace('<', '')
              .replace('>', '').replace(')', '').replace('(', '') for song_name in song_new]
artist_new_2 = [artist_name.replace(' ', '_').replace('/', '_') for artist_name in artist_new]

# Creating dictionary --
lyrics_dict = {
    'Artist': artist_new_2,
    'Songs': song_new_2,
    'Lyrics_links': link_new
}
dataFrame = pd.DataFrame(lyrics_dict)
dataFrame.to_excel('Lyrics_link_data_Final.xlsx', index=False)

