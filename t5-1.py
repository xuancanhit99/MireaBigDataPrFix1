# import time
#
# from sklearn.datasets import load_digits
# from sklearn.manifold import TSNE
# import pandas as pd
# import matplotlib
# import warnings
#
# warnings.filterwarnings("ignore")
#
# matplotlib.use('TkAgg')
# import matplotlib.pyplot as plt
# import numpy as np
# import seaborn as sns
# from sklearn import preprocessing
# import umap
#
# # Смотрим на набор данных цифр
# digits = load_digits()
#
# # Посмотрите на количество предметов и функций:
# # n_samples, n_features = digits.data.shape
# # print((n_samples, n_features))
#
# # plt.gray()
# # plt.matshow(digits.images[0])
# # plt.show()
#
#
# df = pd.DataFrame(digits.data, columns=digits.feature_names)
# # print(df.head())
# #
# # scaler = preprocessing.MinMaxScaler()
# # df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)
# # print(df.head())
#
# T = TSNE(n_components=2, perplexity=50, random_state=123)
# # TSNE_features = T.fit_transform(df)
# # print(TSNE_features[1:4, :])
#
# # data = df.copy()
# # data['x'] = TSNE_features[:, 0]
# # data['y'] = TSNE_features[:, 1]
# # data['target'] = digits.target
#
# # fig = plt.figure(figsize=(10, 10))
# # sns.scatterplot(x='x', y='y', hue=data['target'], data=data, palette='bright')
# # plt.show()
#
# # ---UMAP
# # n_n = (5, 25, 50)  # n_neighbors
# # m_d = (0.1, 0.6)  # min_dist
# #
# # um = dict()
# # for i in range(len(n_n)):
# #     for j in range(len(m_d)):
# #         um[(n_n[i], m_d[j])] = (umap.UMAP(n_neighbors=n_n[i], min_dist=m_d[j], random_state=123).fit_transform(df))
# #
# # data2 = df.copy()
# # data2['target'] = digits.target
# # for i in range(len(n_n)):
# #     for j in range(len(m_d)):
# #         data2['x_{}_{}'.format(i, j)] = um[(n_n[i], m_d[j])][:, 0]
# #         data2['y_{}_{}'.format(i, j)] = um[(n_n[i], m_d[j])][:, 1]
#
# # print(data2.head())
#
# # fig, axs = plt.subplots(len(n_n), len(m_d), figsize=(15, 15))
# # for i in range(len(n_n)):
# #     for j in range(len(m_d)):
# #         sns.scatterplot(ax=axs[i, j],
# #                         x='x_{}_{}'.format(i, j),
# #                         y='y_{}_{}'.format(i, j),
# #                         hue=data2['target'],
# #                         data=data2,
# #                         palette='bright')
# #         axs[i, j].title.set_text('n_neighbors={}, min_dist={}'.format(n_n[i], m_d[j]))
# # plt.show()
#
#
# t_start = time.time()
# TSNE_features = T.fit_transform(df)
# t_end = time.time()
# print("Time for t-SNE: {} second".format(t_end-t_start))
#
# t_start = time.time()
# um = umap.UMAP(n_neighbors=5, min_dist=0.1, random_state=123).fit_transform(df)
# t_end = time.time()
# print("Time for UMAP: {} second".format(t_end-t_start))
