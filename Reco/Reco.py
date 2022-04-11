import pandas as pd
import streamlit as st
import numpy as np


# RUN THIS FIRST - streamlit run "C:/Users/TANUL/PycharmProjects/FinalYearProject/Phase - 2/Reco/Reco.py"
# Importing Data -
data = pd.read_excel('Tksrivastava/NLP-Based-Song-Artist-Recommendation-Engine/blob/main/Reco/Final_Recommendation_Data.xlsx')

# Grouping Data -
mbti_data = data.groupby('MBTI')
istj = mbti_data.get_group('istj')
isfj = mbti_data.get_group('isfj')
infj = mbti_data.get_group('infj')
intj = mbti_data.get_group('intj')
istp = mbti_data.get_group('istp')
isfp = mbti_data.get_group('isfp')
infp = mbti_data.get_group('infp')
intp = mbti_data.get_group('intp')
estp = mbti_data.get_group('estp')
esfp = mbti_data.get_group('esfp')
enfp = mbti_data.get_group('enfp')
entp = mbti_data.get_group('entp')
estj = mbti_data.get_group('estj')
esfj = mbti_data.get_group('esfj')
enfj = mbti_data.get_group('enfj')
entj = mbti_data.get_group('entj')


def Reccomendation(type):
    if type == 'istj':
        artist = list(istj['Artist'])
        return artist[0:9]
    if type == 'isfj':
        artist = list(isfj['Artist'])
        return artist[0:9]
    if type == 'infj':
        artist = list(infj['Artist'])
        return artist[0:1]
    if type == 'intj':
        artist = list(intj['Artist'])
        return artist[0:9]
    if type == 'istp':
        artist = list(istp['Artist'])
        return artist[0:9]
    if type == 'isfp':
        artist = list(isfp['Artist'])
        return artist[0:9]
    if type == 'infp':
        artist = list(infp['Artist'])
        return artist[0:9]
    if type == 'intp':
        artist = list(intp['Artist'])
        return artist[0:9]
    if type == 'estp':
        artist = list(estp['Artist'])
        return artist[0:9]
    if type == 'esfp':
        artist = list(esfp['Artist'])
        return artist[0:9]
    if type == 'enfp':
        artist = list(enfp['Artist'])
        return artist[0:9]
    if type == 'entp':
        artist = list(entp['Artist'])
        return artist[0:9]
    if type == 'estj':
        artist = list(estj['Artist'])
        return artist[0:9]
    if type == 'esfj':
        artist = list(esfj['Artist'])
        return artist[0:9]
    if type == 'enfj':
        artist = list(enfj['Artist'])
        return artist[0:9]
    if type == 'entj':
        artist = list(entj['Artist'])
        return artist[0:9]


# Deploying -
st.title('Natural Language Processing based song artist recommendation engine for MBTI personality type')
option = st.selectbox('Enter Your MBTI Personality type', (np.unique(list(data['MBTI']))))
if st.button('Recommend Artist'):
    reco = Reccomendation(option)
    for i in reco:
        st.write(i)
