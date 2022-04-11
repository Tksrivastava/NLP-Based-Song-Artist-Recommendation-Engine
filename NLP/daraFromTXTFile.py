import pandas as pd
import random

data = pd.read_excel('txt_Address.xlsx')
song_name = []
artist_name = []
Genre = []
word_perso = []
genre_perso = []
istj_word = ['plan', 'schedule', 'compliance', 'compliant', 'organize', 'organization', 'rules', 'regulations',
             'policies', 'procedures', 'protocol', 'actually', 'task', 'error', 'report', 'audit', 'option',
             'advantageous', 'advantage', 'accountable', 'accountability', 'practical', 'responsible', 'responsibility']
isfj_word = ['nice', 'hello', 'hi', 'bye', 'like', 'don’t', 'mean', 'them', 'they', 'us', 'mine', 'my', 'damn',
             'bother', 'bothering', 'alone', 'for', 'make', 'made', 'with', 'okay', 'yes', 'responsible',
             'responsibility', 'work', 'right', 'wrong', 'good', 'bad', 'please', 'happy']
infj_word = ['heal', 'healing', 'healer', 'powerful', 'energy', 'feel', 'things', 'narcissist', 'narcissistic',
             'empath', 'empathy', 'empathic', 'communicate', 'communication', 'negative', 'negativity', 'choice',
             'choose', 'self', 'thank', 'you', 'grow', 'growth', 'pain', 'vibe', 'vibration', 'vibrational',
             'peace', 'space', 'reflect', 'maybe']
intj_word = ['no', 'doesn’t', 'work', 'working', 'evidence', 'myself', 'it', 'that', 'not', 'fact', 'wrong',
             'incompetent', 'idiot', 'efficient', 'inefficient', 'broken', 'annoyed', 'annoying', 'project',
             'alone', 'statistically']
istp_word = ['hey, repair, build, fix, materials, tools', 'parts', 'logic', 'think', 'let', 'allow', 'me', 'common',
             'sense', 'what', 'emotions', 'ugh', 'good']
isfp_word = ['me', 'aesthetic', 'music', 'what', 'huh', 'never', 'get', 'new', 'studio', 'stop', 'cool', 'feel',
             'practice', 'vibe', 'chill']
infp_word = ['okay', 'understand', 'understood', 'me', 'help', 'need', 'create', 'creative', 'creativity', 'art',
             'read', 'reading', 'book', 'story', 'words', 'judge', 'hurt', 'sad', 'cry', 'feelings', 'felt', 'right',
             'mhmm', 'so']
intp_word = ['maths', 'science', 'scientifically', 'data', 'research', 'hypothesis', 'hypothesize', 'posit',
             'advanced', 'advances', 'study', 'exam', 'examine', 'examination', 'criteria', 'error', 'information',
             'theory', 'theoretical', 'interesting', 'fascinating', 'article', 'system', 'systems', 'reasoning',
             'analysis']
estp_word = ['yeah', 'facts', 'fire', 'lit', 'roast', 'roasted', 'lets', 'want', 'play', 'fuck', 'bitch', 'nah',
             'out', 'i', 'm', 'text', 'drive', 'car']
esfp_word = ['fun', 'shop', 'shopping', 'listen', 'listening', 'watch', 'watching', 'go', 'going', 'do', 'doing',
             'talk', 'talking', 'easy', 'busy', 'i', 'starbucks', 'cute', "can’t", 'look', 'party', 'shit',
             'pissed', 'out', 'people', 'uber', 'lyft']
enfp_word = ['love', 'wish', 'time', 'freedom', 'free', 'believe', 'try', 'change', 'soul', 'mind', 'thank', 'you',
             'thanks', 'if', 'then', 'people', 'possible', 'possibly', 'want', 'amazing', 'i', 'feel', 'oops',
             'bored', 'boring', 'control', 'controlling', 'ohhh']
entp_word = ['ram', 'suppose', 'terabyte', 'processor', 'actually', 'if', 'then', 'probably', 'again', 'doubt', 'no',
             'technology', 'program', 'a.i', 'simple', 'hmm', 'memory', 'specs', 'code', 'perhaps', 'possibly',
             'possible']
estj_word = ['metrics', 'performance', 'numbers', 'higher', 'ups', 'coaching', 'develop', 'win', 'weak', 'top',
             'bottom', 'buy', 'sell', 'manage', 'manager', 'management', 'effective', 'ineffective', 'email', 'get',
             'done', 'deliverables', 'action', 'team', 'strategy', 'strategize', 'strategic', 'competitionm',
             'compete', 'competitors', 'win', 'winner']
esfj_word = ['real', 'really', 'family', 'kids', 'people', 'holidays', 'tell', 'told', 'said', 'crazy', 'for', 'hate',
             'my', 'should', "shouldn't", 'lets', 'us', 'asshole', 'omg', 'together', 'heard', 'hear', 'look',
             'whatever', 'call', 'girl', 'boy', 'ill', 'gross']
enfj_word = ['can', 'yourself', 'do', 'motivate', 'we', 'grind', 'confidence', 'determined', 'determination',
             'commitment', 'excuses', 'strong', 'network', 'discipline', 'attitude', 'positive', 'positivity',
             'be', 'win']
entj_word = ['charge', 'effective', 'ineffective', 'cost', 'you', 'profit', 'product', 'productivity', 'work', 'brand',
             'we', 'better', 'money', 'chain', 'secure', 'capital', 'capitalize', 'necessary',
             'opportunity', 'conference', 'absolutely', 'account', 'accountant', 'go']
for address in list(data['Text_Address']):
    start = 0
    start_1 = 0
    end_1 = 0
    end = 0
    add_str = str(address)
    artist_name.append(add_str[0: add_str.find('&')])
    song_name.append(add_str[add_str.find('&')+1: add_str.find('@')])
    Genre.append(add_str[add_str.find('@')+1: add_str.find('.txt')].replace('_', '/'))
    loc = 'C:/Users/TANUL/PycharmProjects/FinalYearProject/Phase - 2/PipeLine/Lyrics_Data/%s' % address
    file = open(loc, 'r', encoding="utf8")
    d = file.read()
    istj_word_count = 0
    for element in istj_word:
        if element in d:
            istj_word_count += 1
    isfj_word_count = 0
    for element in isfj_word:
        if element in d:
            isfj_word_count += 1
    infj_word_count = 0
    for element in infj_word:
        if element in d:
            infj_word_count += 1
    intj_word_count = 0
    for element in intj_word:
        if element in d:
            intj_word_count += 1
    istp_word_count = 0
    for element in istp_word:
        if element in d:
            istp_word_count += 1
    isfp_word_count = 0
    for element in isfp_word:
        if element in d:
            isfp_word_count += 1
    infp_word_count = 0
    for element in infp_word:
        if element in d:
            infp_word_count += 1
    intp_word_count = 0
    for element in intp_word:
        if element in d:
            intp_word_count += 1
    estp_word_count = 0
    for element in estp_word:
        if element in d:
            estp_word_count += 1
    esfp_word_count = 0
    for element in esfp_word:
        if element in d:
            esfp_word_count += 1
    enfp_word_count = 0
    for element in enfp_word:
        if element in d:
            enfp_word_count += 1
    entp_word_count = 0
    for element in entp_word:
        if element in d:
            entp_word_count += 1
    estj_word_count = 0
    for element in estj_word:
        if element in d:
            estj_word_count += 1
    esfj_word_count = 0
    for element in esfj_word:
        if element in d:
            esfj_word_count += 1
    enfj_word_count = 0
    for element in enfj_word:
        if element in d:
            enfj_word_count += 1
    entj_word_count = 0
    for element in entj_word:
        if element in d:
            entj_word_count += 1

    Word_Count_list = [istj_word_count, isfj_word_count, infj_word_count, intj_word_count, istp_word_count,
                       isfp_word_count,
                       infp_word_count, intp_word_count, estp_word_count, esfp_word_count, enfp_word_count,
                       entp_word_count,
                       estj_word_count, esfj_word_count, enfj_word_count, entj_word_count]

    if Word_Count_list.index(max(Word_Count_list)) == 0:
        word_perso.append('istj')
    elif Word_Count_list.index(max(Word_Count_list)) == 1:
        word_perso.append('isfj')
    elif Word_Count_list.index(max(Word_Count_list)) == 2:
        word_perso.append('infj')
    elif Word_Count_list.index(max(Word_Count_list)) == 3:
        word_perso.append('intj')
    elif Word_Count_list.index(max(Word_Count_list)) == 4:
        word_perso.append('istp')
    elif Word_Count_list.index(max(Word_Count_list)) == 5:
        word_perso.append('isfp')
    elif Word_Count_list.index(max(Word_Count_list)) == 6:
        word_perso.append('infp')
    elif Word_Count_list.index(max(Word_Count_list)) == 7:
        word_perso.append('intp')
    elif Word_Count_list.index(max(Word_Count_list)) == 8:
        word_perso.append('estp')
    elif Word_Count_list.index(max(Word_Count_list)) == 9:
        word_perso.append('esfp')
    elif Word_Count_list.index(max(Word_Count_list)) == 10:
        word_perso.append('enfp')
    elif Word_Count_list.index(max(Word_Count_list)) == 11:
        word_perso.append('entp')
    elif Word_Count_list.index(max(Word_Count_list)) == 12:
        word_perso.append('estj')
    elif Word_Count_list.index(max(Word_Count_list)) == 13:
        word_perso.append('esfj')
    elif Word_Count_list.index(max(Word_Count_list)) == 14:
        word_perso.append('enfj')
    else:
        word_perso.append('entj')

for genre in Genre:
    if genre == 'Country':
        g = ['istj', 'enfj', 'esfj', 'esfp']
        genre_perso.append(random.choice(g))
    if genre == 'Pop':
        g = ['istp', 'isfp']
        genre_perso.append(random.choice(g))
    if genre == 'R&B/Soul':
        genre_perso.append('isfj')
    if genre == 'Rock':
        g = ['isfj', 'infp', 'intp', 'estp', 'esfp', 'enfp', 'entp', 'estj']
        genre_perso.append(random.choice(g))
    if genre == 'Electronics':
        g = ['estp', 'entj', 'istp']
        genre_perso.append(random.choice(g))
    if genre == 'Rap/Hip-Hop':
        g = ['isfj', 'infp', 'intp', 'estp', 'esfp', 'enfp', 'entp', 'estj']
        genre_perso.append(random.choice(g))

d = {
    'artist_name': artist_name,
    'song_name': song_name,
    'Genre': Genre,
    'Personality_by_word': word_perso,
    'Personality_by_genre': genre_perso
}

e = pd.DataFrame(d)
e.to_excel('Data_Extracted.xlsx', index=False)
