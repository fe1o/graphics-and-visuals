# %%
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d

# %%
#Carregando os dados
base = pd.read_csv('orchard.csv')
base

# %%
#Criação do gráfico 3d, para possibilitar a visualização de 3 variáveis numéricas
#Indicando três atributos(decrease, rowpos e colpos)
graph = plt.figure()
eixo = graph.add_subplot(1, 1, 1, projection = '3d')
eixo.scatter(base.decrease, base.rowpos, base.colpos)
eixo.set_xlabel('decrease')
eixo.set_ylabel('rowpos')
eixo.set_zlabel('colpos')


