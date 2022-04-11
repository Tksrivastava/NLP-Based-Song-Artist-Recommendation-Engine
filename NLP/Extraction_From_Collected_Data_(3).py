import pandas as pd
import re
import nltk
# nltk.download('stopwords')
# nltk.download('brown')
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
all_stopword = stopwords.words('english')
all_stopword.remove('not')

# Importing Data -
neg = []
neu = []
pos = []
compound = []
data = pd.read_excel('txt_Address.xlsx')
for address in list(data['Text_Address']):
    loc = 'C:/Users/TANUL/PycharmProjects/FinalYearProject/Phase - 2/PipeLine/Lyrics_Data/%s' % address
    file = open(loc, 'r', encoding="utf8")
    d = file.read().lower()
    d = d.replace("n'", 'ng')
    d = re.sub('[^A-Za-z]+', ' ', d)
    d_list = d.split()
    copy_d = d_list.copy()
    for ele in d_list:
        for ele2 in all_stopword:
            if ele == ele2:
                copy_d.remove(ele)

    new_d = ' '.join(copy_d)
    score = SentimentIntensityAnalyzer().polarity_scores(new_d)
    neg.append(score['neg'])
    neu.append(score['neu'])
    pos.append(score['pos'])
    compound.append(score['compound'])

s = {
    'text_File': list(data['Text_Address']),
    'neg': neg,
    'neu': neu,
    'pos': pos,
    'compound': compound
}

sdf = pd.DataFrame(s)

sdf.to_excel('Sentiment.xlsx', index=False)








