# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
#Carregando a base
base_box = pd.read_csv('trees.csv')
print(base_box.head())

# %%
#Gerando o boxplot
plt.boxplot(base_box.Volume, vert=False, showfliers=False, notch=True, patch_artist=True)
plt.title('Árvores')
plt.xlabel('Volume')

# %%
#Gerando o boxplot por linha (não ideal)
plt.boxplot(base_box)
plt.title('Árvores')
plt.xlabel('Dados')


