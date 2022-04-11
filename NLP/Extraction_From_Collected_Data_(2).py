import pandas as pd

# Importing Data -
data = pd.read_excel('txt_Address.xlsx')

# Extracting Data -
artist_name = []
genre_perso = []
country_genre = ['istj', 'enfj', 'esfj', 'esfp']
pop_genre = ['istp', 'isfp']
rnb_genre = ['isfj']
rock_genre = ['isfj', 'infp', 'intp', 'estp', 'esfp', 'enfp', 'entp', 'estj']
electronics_genre = ['estp', 'entj', 'istp']
rap_genre = ['isfj', 'infp', 'intp', 'estp', 'esfp', 'enfp', 'entp', 'estj']

for address in list(data['Text_Address']):
    start = 0
    start_1 = 0
    end_1 = 0
    end = 0
    add_str = str(address)
    # song_name.append(add_str[add_str.find('&')+1: add_str.find('@')])
    Genre = add_str[add_str.find('@')+1: add_str.find('.txt')].replace('_', '/')
    if Genre == 'Rap/Hip-Hop':
        for i in range(len(rap_genre)):
            genre_perso.append(rap_genre[i])
            artist_name.append(add_str[0: add_str.find('&')])
    if Genre == 'Rock':
        for i in range(len(rock_genre)):
            genre_perso.append(rock_genre[i])
            artist_name.append(add_str[0: add_str.find('&')])
    if Genre == 'Pop':
        for i in range(len(pop_genre)):
            genre_perso.append(pop_genre[i])
            artist_name.append(add_str[0: add_str.find('&')])
    if Genre == 'R&B/Soul':
        for i in range(len(rnb_genre)):
            genre_perso.append(rnb_genre[i])
            artist_name.append(add_str[0: add_str.find('&')])
    if Genre == 'Electronics':
        for i in range(len(electronics_genre)):
            genre_perso.append(electronics_genre[i])
            artist_name.append(add_str[0: add_str.find('&')])
    if Genre == 'Country':
        for i in range(len(country_genre)):
            genre_perso.append(country_genre[i])
            artist_name.append(add_str[0: add_str.find('&')])

d = {
    'artist_name': artist_name,
    'mbti': genre_perso
}

df = pd.DataFrame(d)
df.to_excel('Personality_From_Genre_Preference.xlsx', index=False)

