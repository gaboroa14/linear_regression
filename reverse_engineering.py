import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols
import statsmodels.formula.api as smf
from scipy import stats as sci

data = pd.read_csv('datos2.csv')
print("\n 1) EXPLORACION DE LOS DATOS:")
print("\nCategorización por sexo: (0 = Mujeres, 1 = Hombres): ")
print(data['sex'].value_counts())
objects = ('Mujeres', 'Hombres')
regiones = ('Sureste', 'Noreste', 'Suroeste', 'Noroeste')
hijos = (0,1,2,3,4,5)
y_pos = np.arange(len(objects))
y_pos1 = np.arange(len(regiones))
y_pos2 = np.arange(len(hijos))
performance = data['sex'].value_counts()
figure, axes = plt.subplots(ncols=2,nrows=2)
axes[0,0].bar(y_pos, performance, align='center', alpha=0.5)
axes[0,0].set_xticks(y_pos, objects)
axes[0,0].set_ylabel('Cantidad')
axes[0,0].set_title('Cantidad de hombres y mujeres')
axes[0,0].set_xticklabels(['','Mujeres','' ,'Hombres'])
print("\nCategorización por fumadores: (0 = No, 1 = Sí): ")
print(data['smoker'].value_counts())
performance = data['smoker'].value_counts()
axes[0,1].bar(y_pos, performance, align='center', alpha=0.5)
axes[0,1].set_xticks(y_pos, objects)
axes[0,1].set_ylabel('Cantidad')
axes[0,1].set_title('Cantidad de fumadores')
axes[0,1].set_xticklabels(['','No','' ,'Sí'])
print("\nCategorización por región: 0 NE, 1 NW, 2 SE, 3 SW: ")
print(data['region'].value_counts())
performance = data['region'].value_counts()
axes[1,0].bar(y_pos1, performance, align='center', alpha=0.5)
axes[1,0].set_xticks(y_pos, objects)
axes[1,0].set_ylabel('Cantidad')
axes[1,0].set_title('Cantidad por región')
axes[1,0].set_xticklabels(['','SE', 'NE', 'SO', 'NO'])
print("\nCategorización por cantidad de hijos: ")
print(data['children'].value_counts())
performance = data['children'].value_counts()
axes[1,1].bar(y_pos2, performance, align='center', alpha=0.5)
axes[1,1].set_xticks(y_pos, objects)
axes[1,1].set_ylabel('Cantidad')
axes[1,1].set_title('Cantidad de hijos')
print("\nExploración descriptiva de los datos cuantitativos: ")
print(data.describe())

print("\n 2) MATRIZ DE CORRELACION")
print("\n\n Correlación lineal de los datos: ")
print(round(data.corr(),3))

#GRAFICOS
fig, ax = plt.subplots()
im = ax.imshow(data.corr(),cmap=plt.get_cmap("RdBu"))
correlacion = data.corr()
cabeceras = ["Edad", "Sexo", "BMI", "Hijos", "Fumador", "Región", "Cargos"]
ax.set_xticks(np.arange(len(cabeceras)))
ax.set_yticks(np.arange(len(cabeceras)))
ax.set_xticklabels(cabeceras)
ax.set_yticklabels(cabeceras)
plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")
ax.set_title("Gráfico de correlación de las variables")
cabeceras_panda = ["age","sex","bmi","children","smoker","region","charges"]
for i in range(len(cabeceras_panda)):
    for j in range(len(cabeceras_panda)):
        text = ax.text(j,i,round(correlacion[cabeceras_panda[i]][cabeceras_panda[j]],2), ha="center", va="center", color="k" if i != j else "w")
fig.tight_layout()
figure.tight_layout()
#plt.show()

print("\nANOVA:\n")
f = sci.f_oneway(data["bmi"],data["region"])
print(f)


print("\n Modelo Lineal:\n")
mod = smf.ols('charges ~ age + sex + bmi + children + smoker + region', data=data).fit()
print(mod.summary())
print(mod.params)
print('Coeficiente de determinación:', mod.rsquared)

print("\n\n Modelo Lineal por región:\n")
for region, df_region in data.groupby('region'):
    if region == 0:
        ne = df_region
    elif region == 1:
        nw = df_region
    elif region == 2:
        se = df_region
    else:
        sw = df_region
print("\nRegión Noreste:")
mod = smf.ols('charges ~ age + sex + bmi + children + smoker', data=ne).fit()
print(mod.summary())
print(mod.params)
print('Coeficiente de determinación:', mod.rsquared)
print("\nRegión Noroeste:")
mod = smf.ols('charges ~ age + sex + bmi + children + smoker', data=nw).fit()
print(mod.summary())
print(mod.params)
print('Coeficiente de determinación:', mod.rsquared)
print("\nRegión Sureste:")
mod = smf.ols('charges ~ age + sex + bmi + children + smoker', data=se).fit()
print(mod.summary())
print(mod.params)
print('Coeficiente de determinación:', mod.rsquared)
print("\nRegión Suroeste:")
mod = smf.ols('charges ~ age + sex + bmi + children + smoker', data=sw).fit()
print(mod.summary())
print(mod.params)
print('Coeficiente de determinación:', mod.rsquared)
