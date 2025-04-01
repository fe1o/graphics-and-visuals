# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
#Carregando os dados sobre concentração de co2 em plantas
base_dens = pd.read_csv('co2.csv')
print(base_dens.head())

# %%
#Criando duas variáveis para cada atributo contínuo, concentração e uptake
x = base_dens.conc
y = base_dens.uptake
#Atribuindo valores únicos da coluna Treatment a uma variável
unc = list(set(base_dens.Treatment))
#Um for para percorrer cada tipo de tratamento e criar o gráfico de dispersão
for i in range(len(unc)):
    indice = base_dens.Treatment == unc[i]
    plt.scatter(x[indice], y[indice], label = unc[i])
plt.legend(loc='lower right')


