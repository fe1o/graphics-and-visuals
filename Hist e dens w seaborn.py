# %%
#Histograma com densidade utilizando o seaborn

# %%
import pandas as pd
import seaborn as sbr
import matplotlib.pyplot as plt

# %%
#Carregando os dados
base = pd.read_csv('trees.csv')
base.head()

# %%
#Histograma com 7 bins e com gráfico de densidade
sbr.histplot(base.Volume, color='red', kde=True, stat='density', bins=7).set(title='Volume')

# %%
#Carregando outra base de dados
base_2 = pd.read_csv('chicken.csv')
base_2.head()

# %%
#Agrupando o atributo feed e fazendo a sua frequência
gp_chicken = base_2.groupby(['feed'])['weight'].sum()
gp_chicken

# %%
#Histograma considerando o valor 'horsebean' com densidade

sbr.kdeplot(base_2.loc[base_2['feed'] == 'horsebean'].weight).set(title='horsebean', xlabel = 'Peso', ylabel = 'Densidade')

# %%
#Histograma considerando apenas o valor 'casein'
sbr.histplot(base_2.loc[base_2['feed'] == 'casein'].weight, kde=True).set(title='casein', xlabel = 'Peso', ylabel = 'Densidade')

# %%
#Histograma considerando apenas o valor 'linseed'
sbr.histplot(base_2.loc[base_2['feed'] == 'linseed'].weight, kde=True).set(title='linseed', xlabel = 'Peso', ylabel = 'Densidade')

# %%
#Histograma considerando apenas o valor 'meatmeal'
sbr.histplot(base_2.loc[base_2['feed'] == 'meatmeal'].weight, kde=True).set(title='meatmeal', xlabel = 'Peso', ylabel = 'Densidade')

# %%
#Histograma considerando apenas o valor 'soybean'
sbr.histplot(base_2.loc[base_2['feed'] == 'soybean'].weight, kde=True).set(title='soybean', xlabel = 'Peso', ylabel = 'Densidade')

# %%
#Histograma considerando apenas o valor 'sunflower'
sbr.histplot(base_2.loc[base_2['feed'] == 'sunflower'].weight, kde=True).set(title='sunflower', xlabel = 'Peso', ylabel = 'Densidade')

# %%
#Gerando um painel com 3 linhas e duas colunas contendo os gráficos para comparação
plt.figure()
plt.subplot(3,2,1)
sbr.histplot(base_2.loc[base_2['feed'] == 'horsebean'].weight).set(title='horsebean', xlabel = 'Peso', ylabel = 'Densidade')
plt.subplot(3,2,2)
sbr.histplot(base_2.loc[base_2['feed'] == 'casein'].weight, kde=True).set(title='casein', xlabel = 'Peso', ylabel = 'Densidade')
plt.subplot(3,2,3)
sbr.histplot(base_2.loc[base_2['feed'] == 'linseed'].weight, kde=True).set(title='linseed', xlabel = 'Peso', ylabel = 'Densidade')
plt.subplot(3,2,4)
sbr.histplot(base_2.loc[base_2['feed'] == 'meatmeal'].weight, kde=True).set(title='meatmeal', xlabel = 'Peso', ylabel = 'Densidade')
plt.subplot(3,2,5)
sbr.histplot(base_2.loc[base_2['feed'] == 'soybean'].weight, kde=True).set(title='soybean', xlabel = 'Peso', ylabel = 'Densidade')
plt.subplot(3,2,6)
sbr.histplot(base_2.loc[base_2['feed'] == 'sunflower'].weight, kde=True).set(title='sunflower', xlabel = 'Peso', ylabel = 'Densidade')
#Ajustando layout para não ter sobreposição
plt.tight_layout()


