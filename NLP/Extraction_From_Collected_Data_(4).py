import pandas as pd

# Importing Data -
data = pd.read_excel('Sentiment_clustered.xlsx')

# Extracting Data -
artist_name = []
theme_perso = []
reb = ['isfj', 'infp', 'intp', 'estp', 'esfp', 'enfp', 'entp', 'estj', 'isfj']
lov = ['istp', 'isfp', 'estp', 'entj']
hd = ['istj', 'enfj', 'esfj', 'esfp']
artist = list(data['artist'])
label = list(data['label'])
for address in list(data['artist']):
    start = 0
    start_1 = 0
    end_1 = 0
    end = 0
    add_str = str(address)
    # song_name.append(add_str[add_str.find('&')+1: add_str.find('@')])
    index = artist.index(address)
    if label[index] == 0:
        for i in range(len(reb)):
            theme_perso.append(reb[i])
            artist_name.append(add_str[0: add_str.find('&')])
    if label[index] == 1:
        for i in range(len(hd)):
            theme_perso.append(hd[i])
            artist_name.append(add_str[0: add_str.find('&')])
    if label[index] == 2:
        for i in range(len(lov)):
            theme_perso.append(lov[i])
            artist_name.append(add_str[0: add_str.find('&')])

d = {
    'artist_name': artist_name,
    'mbti': theme_perso
}

df = pd.DataFrame(d)
df.to_excel('Personality_From_Theme_Preference.xlsx', index=False)

