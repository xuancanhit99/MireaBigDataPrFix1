from sklearn.manifold import TSNE
import pandas as pd
import matplotlib

matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn import preprocessing
import umap

zoo_raw_data = pd.read_csv('zoo.csv')
print(zoo_raw_data)

zoo_data = zoo_raw_data.drop(['class_type', 'animal_name'], axis=1)
scaler = preprocessing.MinMaxScaler()
zoo_data = pd.DataFrame(scaler.fit_transform(zoo_data), columns=zoo_data.columns)
print(zoo_data)

# T = TSNE(n_components=2,perplexity=25, random_state=123)
# TSNE_features = T.fit_transform(zoo_data)
#
# print(TSNE_features[1:4,:])
#
Data = zoo_data.copy()
# Data['x'] = TSNE_features[:, 0]
# Data['y'] = TSNE_features[:, 1]

# fig = plt.figure()
# sns.scatterplot(x='x', y='y', hue=zoo_raw_data['class_type'], data=Data, palette='bright')
# plt.show()
#

# UMAP
# n_n = (5, 25, 50)
# m_d = (0.1, 0.6)
#
#
#
# um = dict()
# for i in range(len(n_n)):
#     for j in range(len(m_d)):
#         um[(n_n[i], m_d[j])] = (umap.UMAP(n_neighbors=n_n[i], min_dist=m_d[j], random_state=123).fit_transform(Data))
