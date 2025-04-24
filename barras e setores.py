# %%
import pandas as pd

# %%
#Carregando a base
base = pd.read_csv('insect.csv')
base.shape

# %%
#dados
base.head()

# %%
#Agrupando os dados da culuna 'spray', contando e somando os registros
gp_spray = base.groupby(['spray'])['count'].sum()
gp_spray

# %%
#Gráfico de barras
gp_spray.plot.bar(color = ['blue', 'yellow', 'red', 'orange', 'green', 'pink'])

# %%
#Gráfico de pizza
gp_spray.plot.pie(legend = True)


