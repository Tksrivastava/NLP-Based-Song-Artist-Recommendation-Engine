import pandas as pd

data1 = pd.read_excel('Theme_Ranking.xlsx')
data2 = pd.read_excel('Genre_Ranking.xlsx')
data3 = pd.read_excel('Word_ranking.xlsx')

concat = pd.concat([data1, data2, data3], axis=0)

concat.to_excel('Final_Ranking.xlsx', index=False)