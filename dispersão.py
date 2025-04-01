# %%
import pandas as pd
import seaborn as sbr
import matplotlib.pyplot as plt

# %%
#Carregando a base
base_disp = pd.read_csv('trees.csv')
print(base_disp.head())

# %%
#Gráfico de dispersão usando o matplotlib
plt.scatter(x=base_disp.Girth, y=base_disp.Volume, color='red', facecolors='none', marker='^')
plt.title('Árvores')
plt.xlabel('Circunferência')
plt.ylabel('Volume')

# %%
#Gráfico com linha ao invés de pontos
plt.plot(base_disp.Girth, base_disp.Volume)
plt.title('Árvores')
plt.xlabel('Circunferência')
plt.ylabel('Volume')

# %%
#Gráfico de dispersão com o Seaborn
sbr.regplot(x=base_disp.Girth, y=base_disp.Volume, data=base_disp, x_jitter=0.3, fit_reg=False)


