import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.cluster import KMeans
import plotly.graph_objects as go

# Data -
data1 = pd.read_excel('Sentiment.xlsx')
data = data1.drop('text_File', axis=1)

# Plotting 3d Sctter -
fig2 = px.scatter_3d(data, x="neg", y="neu", z="pos")
fig2.update_layout(title="5 Features Representation")
fig2.show()

# Finding Clusters -
X = data
inertia = []
for i in range(1, 11):
    kmeans = KMeans(
        n_clusters=i, init="k-means++",
        n_init=10,
        tol=1e-04, random_state=42
    )
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)
fig = go.Figure(data=go.Scatter(x=np.arange(1, 11), y=inertia))
fig.update_layout(title="Inertia vs Cluster Number", xaxis=dict(range=[0, 11], title="Cluster Number"),
                  yaxis={'title': 'Inertia'})
fig.show()
#
kmeans = KMeans(
    n_clusters=3, init="k-means++",
    n_init=10,
    tol=1e-04, random_state=42
)
kmeans.fit(X)
clusters = pd.DataFrame(X, columns=data.columns)
clusters['label'] = kmeans.labels_
clusters['artist'] = data1['text_File']
new = clusters.drop(['neg', 'pos', 'neu', 'compound'], axis=1)
new.to_excel('Sentiment_clustered.xlsx', index=False)
polar = clusters.groupby("label").mean().reset_index()
polar = pd.melt(polar, id_vars=["label"])
fig4 = px.line_polar(polar, r="value", theta="variable", color="label", line_close=True, height=800, width=1400)
fig4.show()

pie = clusters.groupby('label').size().reset_index()
pie.columns = ['label', 'value']
fig5 = px.pie(pie, values='value', names='label', color=['blue', 'red', 'green'])
fig5.show()
