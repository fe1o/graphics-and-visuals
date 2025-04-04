# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
#Carregando a base
base = pd.read_csv('trees.csv')
print(base.head())

# %%
#Dispersão de Girth x Volume
plt.scatter(base.Girth, base.Volume)
plt.xlabel('Girth')
plt.ylabel('Volume')

# %%
#Dispersão de Girth x Height
plt.scatter(base.Girth, base.Height)
plt.xlabel('Girth')
plt.ylabel('Height')

# %%
#Dispersão de Height x Volume
plt.scatter(base.Height, base.Volume)
plt.xlabel('Height')
plt.ylabel('Volume')

# %%
#Histograma com o volume
plt.hist(base.Volume)
plt.xlabel('Volume')
plt.ylabel('Frequency')

# %%
#Mostrando os gráficos juntos
#Criando uma figura em que os gráficos serão posicionados
plt.figure(1)
#Espaço vertical entre os gráficos
plt.subplots_adjust(hspace=0.5)
#Espaço horizontal entre os gráficos
plt.subplots_adjust(wspace=0.5)
plt.subplot(2,2,1)
plt.scatter(base.Girth, base.Volume)
plt.xlabel('Girth')
plt.ylabel('Volume')
plt.subplot(2,2,2)
plt.scatter(base.Girth, base.Height)
plt.xlabel('Girth')
plt.ylabel('Height')
plt.subplot(2,2,3)
plt.scatter(base.Height, base.Volume)
plt.xlabel('Height')
plt.ylabel('Volume')
plt.subplot(2,2,4)
plt.hist(base.Volume)
plt.xlabel('Volume')
plt.ylabel('Frequency')


