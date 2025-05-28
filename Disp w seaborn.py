# %%
import pandas as pd
import seaborn as sbr
import matplotlib.pyplot as plt

# %%
#Carregando a base de dados
base = pd.read_csv('co2.csv')
base.head()

# %%
#Gráfico de dispersão utilizando os atributos conc e uptake, agrupando pelo type
sbr.scatterplot(x = base.conc, y = base.uptake, hue = base.Type)

# %%
#Seleção de registros especificos de cada região (Quebec e Mississippi)
q = base.loc[base['Type'] == 'Quebec']
m = base.loc[base['Type'] == 'Mississippi']

# %%
#Com os registros selecionados, plot de um subgráfico mostrando os gráficos de cada região

plt.figure()
plt.subplot(1,2,1)
sbr.scatterplot(x = q.conc, y = q.uptake).set_title('Quebec')
plt.subplot(1,2,2)
sbr.scatterplot(x = m.conc, y = m.uptake).set_title('Mississippi')
plt.tight_layout()

# %%
#Para os refrigerados e não refrigerados
ch = base.loc[base['Treatment'] == 'chilled']
nc = base.loc[base['Treatment'] == 'nonchilled']

# %%
#Gráficos, para a comparação das mesmas variáveis categóricas
plt.figure()
plt.subplot(1,2,1)
sbr.scatterplot(x = ch.conc, y = ch.uptake).set_title('Chilled')
plt.subplot(1,2,2)
sbr.scatterplot(x = nc.conc, y = nc.uptake).set_title('Non chilled')
plt.tight_layout()

# %%
#Usando outra técnica de agrupamendo do Seaborn com outra basse de dados
base2 = pd.read_csv('esoph.csv')
base2.head()

# %%
#Gráfico com os atributos 'alcgp'(consumo de álcool) e 'ncontrols'(número de controles)
sbr.catplot(x = 'alcgp', y = 'ncontrols', data = base2, jitter = False)

# %%
#Gráficos entre os mesmos atributos mas dessa vez com agrupamento
sbr.catplot(x = 'alcgp', y = 'ncontrols', data = base2, col = 'tobgp')


