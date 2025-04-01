# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
#Carregamento da base
base_hist = pd.read_csv('trees.csv')
base_hist.shape

# %%
#dados
print(base_hist.head())

# %%
#Criação do histograma, considerando apenas o segundo atributo e com seis bins
#A variável h armazena os valores da coluna Height
h = np.histogram(base_hist.iloc[:,1], bins=6)
h

# %%
#Visualização do histograma com 6 bins
plt.hist(base_hist.iloc[:,1], bins=6)
plt.title("Árvores")
plt.ylabel("Frequência")
plt.xlabel("Altura")


