import time

import pandas as pd
import umap
from sklearn.datasets import load_digits
from sklearn.manifold import TSNE

digits = load_digits()
df = pd.DataFrame(digits.data, columns=digits.feature_names)

T = TSNE(n_components=2, perplexity=25, random_state=123)
t_start = time.time()
TSNE_features = T.fit_transform(df)
t_end = time.time()
print("Time for t-SNE: {} second".format(t_end-t_start))

t_start = time.time()
um = umap.UMAP(n_neighbors=5, min_dist=0.1, random_state=123).fit_transform(df)
t_end = time.time()
print("Time for UMAP: {} second".format(t_end-t_start))
