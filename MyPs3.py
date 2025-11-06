# %% [markdown]
# # Dimensional Reduction
# 
# Name: Isaac Anderson
# 
# Date: Nov 1st 2025

# %%
# Imports and DataFrames
import pandas as pd
import numpy as np 
import plotly.express as px
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

new_testament = pd.read_pickle("./pickles/tisch.pickle")
old_tesament = pd.read_pickle("./pickles/sept.pickle") 
strongs = pd.read_pickle("./pickles/strongs")

# %% [markdown]
    # 1. Build a matrix where the rows are small analyzable chunks (larger than a word, less than a book). The columns will be the Strong's numbers and the values are the frequency of those lemmas within your chunk.
# %%

# Reading in Old and New Testament
nt = new_testament.groupby(['book','chapter','verse'])[['str','text']].agg(lambda x : " ".join(x))
nt.reset_index().set_index(['book','chapter','verse'])

matthew = new_testament.query("book == 40")


# 
# matrix = pd.DataFrame(columns=matthew['str'].unique())
matthew_by_verse = matthew.groupby(["chapter","verse"])['str'].agg(lambda x : pd.Series(" ".join(x).split()))


new_rows = []
for verse in matthew_by_verse:
    verse_counts = (pd.Series(verse).value_counts())
    new_rows.append(verse_counts)

matrix = pd.DataFrame(data=new_rows).fillna(value=0)
matrix.index = matthew_by_verse.index


# %%
# 2. Apply PCA to this matrix and interpret the results. Interpret top loadings—what terms drive the first three principal components?
scaler = StandardScaler()
pca = PCA(n_components=10)
X_scaled = scaler.fit_transform(matrix)
X_pca = pca.fit_transform(X_scaled)

my_pca = pd.DataFrame(
    X_pca,
    index = matrix.index
)

print("Explained variance ratio", pca.explained_variance_ratio_)
# 3. Create a scree plot and interpret the plot. 

px.line(
    x = np.arange(1, len(pca.explained_variance_)+1),
    y = pca.explained_variance_
)

# 4. Plot results in PCA space and interpret the plot. Use color to plot trends you might expect to see (e.g. author, genre, etc.).
# 
# 5. Quantify separation between clusters. e.g. separation between Pauline books and Johannine books. Do this for 3 different clusters.

# %% [markdown]
# 6. Repeat steps 1-5 but with the parts of speech feature instead of the Strong's numbers.

# %%
7. Use a KNN with a k-fold cross validation for hyper parameter tuning to predict the author of a given pericope (small chunk you must define).

# %% [markdown]
# # Side Quests

# %% [markdown]
# Perform LDA instead of PCA on the matrix in 1.


