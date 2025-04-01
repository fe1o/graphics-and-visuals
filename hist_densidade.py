# %%
import pandas as pd
import seaborn as sbr
import matplotlib.pyplot as plt

# %%
#Carregando a base
base_dens = pd.read_csv('trees.csv')

# %%
#dados
print(base_dens.head())

# %%
#Histograma com seis bins para o primeiro atributo da base
plt.hist(base_dens.iloc[:,0], bins=6)

# %%
#Histograma com linha de distribuição de frequência, com 6 bins

sbr.histplot(base_dens.iloc[:,0], kde=False, color="red").set(title='Árvores')

# %%
#Densidade, método kdeplot
sbr.kdeplot(base_dens.iloc[:,0], color="red").set(title='Árvores')

# %%
#Densidade e histograma
sbr.histplot(base_dens.iloc[:,0], kde=True, color="red").set(title='Árvores')


