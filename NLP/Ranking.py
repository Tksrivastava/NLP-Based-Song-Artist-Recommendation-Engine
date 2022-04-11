import pandas as pd

# Importing Data -
data = pd.read_excel('Personality_From_Word_Preference.xlsx')
artist = list(data['artist_name'])
mbti = list(data['mbti'])

# Matrix -
istj = []
isfj = []
infj = []
intj = []
istp = []
isfp = []
infp = []
intp = []
estp = []
esfp = []
enfp = []
entp = []
estj = []
esfj = []
enfj = []
entj = []

for perso in mbti:
    if perso == 'istj':
        istj.append(1)
        isfj.append(0)
        infj.append(0)
        intj.append(0)
        istp.append(0)
        isfp.append(0)
        infp.append(0)
        intp.append(0)
        estp.append(0)
        esfp.append(0)
        enfp.append(0)
        entp.append(0)
        estj.append(0)
        esfj.append(0)
        enfj.append(0)
        entj.append(0)

    if perso == 'isfj':
        istj.append(0)
        isfj.append(1)
        infj.append(0)
        intj.append(0)
        istp.append(0)
        isfp.append(0)
        infp.append(0)
        intp.append(0)
        estp.append(0)
        esfp.append(0)
        enfp.append(0)
        entp.append(0)
        estj.append(0)
        esfj.append(0)
        enfj.append(0)
        entj.append(0)

    if perso == 'infj':
        istj.append(0)
        isfj.append(0)
        infj.append(1)
        intj.append(0)
        istp.append(0)
        isfp.append(0)
        infp.append(0)
        intp.append(0)
        estp.append(0)
        esfp.append(0)
        enfp.append(0)
        entp.append(0)
        estj.append(0)
        esfj.append(0)
        enfj.append(0)
        entj.append(0)

    if perso == 'intj':
        istj.append(0)
        isfj.append(0)
        infj.append(0)
        intj.append(1)
        istp.append(0)
        isfp.append(0)
        infp.append(0)
        intp.append(0)
        estp.append(0)
        esfp.append(0)
        enfp.append(0)
        entp.append(0)
        estj.append(0)
        esfj.append(0)
        enfj.append(0)
        entj.append(0)

    if perso == 'istp':
        istj.append(0)
        isfj.append(0)
        infj.append(0)
        intj.append(0)
        istp.append(1)
        isfp.append(0)
        infp.append(0)
        intp.append(0)
        estp.append(0)
        esfp.append(0)
        enfp.append(0)
        entp.append(0)
        estj.append(0)
        esfj.append(0)
        enfj.append(0)
        entj.append(0)

    if perso == 'isfp':
        istj.append(0)
        isfj.append(0)
        infj.append(0)
        intj.append(0)
        istp.append(0)
        isfp.append(1)
        infp.append(0)
        intp.append(0)
        estp.append(0)
        esfp.append(0)
        enfp.append(0)
        entp.append(0)
        estj.append(0)
        esfj.append(0)
        enfj.append(0)
        entj.append(0)

    if perso == 'infp':
        istj.append(0)
        isfj.append(0)
        infj.append(0)
        intj.append(0)
        istp.append(0)
        isfp.append(0)
        infp.append(1)
        intp.append(0)
        estp.append(0)
        esfp.append(0)
        enfp.append(0)
        entp.append(0)
        estj.append(0)
        esfj.append(0)
        enfj.append(0)
        entj.append(0)

    if perso == 'intp':
        istj.append(1)
        isfj.append(0)
        infj.append(0)
        intj.append(0)
        istp.append(0)
        isfp.append(0)
        infp.append(0)
        intp.append(1)
        estp.append(0)
        esfp.append(0)
        enfp.append(0)
        entp.append(0)
        estj.append(0)
        esfj.append(0)
        enfj.append(0)
        entj.append(0)

    if perso == 'estp':
        istj.append(0)
        isfj.append(0)
        infj.append(0)
        intj.append(0)
        istp.append(0)
        isfp.append(0)
        infp.append(0)
        intp.append(0)
        estp.append(1)
        esfp.append(0)
        enfp.append(0)
        entp.append(0)
        estj.append(0)
        esfj.append(0)
        enfj.append(0)
        entj.append(0)

    if perso == 'esfp':
        istj.append(0)
        isfj.append(0)
        infj.append(0)
        intj.append(0)
        istp.append(0)
        isfp.append(0)
        infp.append(0)
        intp.append(0)
        estp.append(0)
        esfp.append(1)
        enfp.append(0)
        entp.append(0)
        estj.append(0)
        esfj.append(0)
        enfj.append(0)
        entj.append(0)

    if perso == 'enfp':
        istj.append(0)
        isfj.append(0)
        infj.append(0)
        intj.append(0)
        istp.append(0)
        isfp.append(0)
        infp.append(0)
        intp.append(0)
        estp.append(0)
        esfp.append(0)
        enfp.append(1)
        entp.append(0)
        estj.append(0)
        esfj.append(0)
        enfj.append(0)
        entj.append(0)

    if perso == 'entp':
        istj.append(0)
        isfj.append(0)
        infj.append(0)
        intj.append(0)
        istp.append(0)
        isfp.append(0)
        infp.append(0)
        intp.append(0)
        estp.append(0)
        esfp.append(0)
        enfp.append(0)
        entp.append(1)
        estj.append(0)
        esfj.append(0)
        enfj.append(0)
        entj.append(0)

    if perso == 'estj':
        istj.append(0)
        isfj.append(0)
        infj.append(0)
        intj.append(0)
        istp.append(0)
        isfp.append(0)
        infp.append(0)
        intp.append(0)
        estp.append(0)
        esfp.append(0)
        enfp.append(0)
        entp.append(0)
        estj.append(1)
        esfj.append(0)
        enfj.append(0)
        entj.append(0)

    if perso == 'esfj':
        istj.append(0)
        isfj.append(0)
        infj.append(0)
        intj.append(0)
        istp.append(0)
        isfp.append(0)
        infp.append(0)
        intp.append(0)
        estp.append(0)
        esfp.append(0)
        enfp.append(0)
        entp.append(0)
        estj.append(0)
        esfj.append(1)
        enfj.append(0)
        entj.append(0)

    if perso == 'enfj':
        istj.append(0)
        isfj.append(0)
        infj.append(0)
        intj.append(0)
        istp.append(0)
        isfp.append(0)
        infp.append(0)
        intp.append(0)
        estp.append(0)
        esfp.append(0)
        enfp.append(0)
        entp.append(0)
        estj.append(0)
        esfj.append(0)
        enfj.append(1)
        entj.append(0)

    if perso == 'entj':
        istj.append(0)
        isfj.append(0)
        infj.append(0)
        intj.append(0)
        istp.append(0)
        isfp.append(0)
        infp.append(0)
        intp.append(0)
        estp.append(0)
        esfp.append(0)
        enfp.append(0)
        entp.append(0)
        estj.append(0)
        esfj.append(0)
        enfj.append(0)
        entj.append(1)

d = {
    'artist': artist,
    'istj': istj,
    'isfj': isfj,
    'infj': infj,
    'intj': intj,
    'istp': istp,
    'isfp': isfp,
    'infp': infp,
    'intp': intp,
    'estp': estp,
    'esfp': esfp,
    'enfp': enfp,
    'entp': entp,
    'estj': estj,
    'esfj': esfj,
    'enfj': enfj,
    'entj': entj
}

df = pd.DataFrame(d)
df.to_excel('Word_Ranking.xlsx', index=False)
