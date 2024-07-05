from subidadedatos import data

"""
para esto vamos a instalar 
pip install pandas
pip install matplotlib
pip install scipy
pip install seaborn
"""

#! descriptive stadisctics 

print(data.describe())

#La configuración predeterminada de "describir" omite las variables de tipo objeto. Podemos aplicar el método "describir" sobre las variables de tipo 'objeto' de la siguiente manera: 

print(data.describe(include=["object"]))

#! agrupando datos

data['drive-wheels'].value_counts()

# podemos convertir la serie en un dataframe:
data['drive-wheels'].value_counts().to_frame()

# vamos hacer lo mismo pero lo vamos a guardar en una variable y vamos a cambiar el nombre de la columna
drive_wheels_counts = data['drive-wheels'].value_counts().to_frame()
drive_wheels_counts.rename(columns={'drive-wheels': 'value_counts'}, inplace=True)
print(drive_wheels_counts)

#ahora vamos a colocar nombre al indice
drive_wheels_counts.index.name = 'drive-wheels'

#vamos a sacar los valores unicos de una columna

data['drive-wheels'].unique()


df_test = data[["drive-wheels", "body-style", "price"]]
df_grp = df_test.groupby(["drive-wheels", "body-style"], as_index=False).mean()
print(df_grp)



#tabla dinamica

df_pivot = df_grp.pivot(index="drive-wheels", columns="body-style")
print(df_pivot)

#quitando en la tabla dinamica los valores nan
df_pivot = df_pivot.fillna(0)


#? HACIENDO UN HEATMAP
"""
plt.pcolor(df_pivot, cmap="RdBu")
plt.colorbar()
plt.show()
"""

#! analisis de la variancia ANOVA ALALISIS DE LA VARIANZA 

df_anova = data[["make", "price"]]
grouped_anova = df_anova.groupby([["make"]], anova_results_1 = stats.f_oneway(grouped_anova.get_froup("honda")["price"], grouped_anova.get_group("subaru")["price"]))


#! correlaciones
#encontrar la correlacion
correlacion = data[['bore','stroke','compression-ratio','horsepower']].corr()

sns.regplot(x="engine-size", y="price", data= data)
plt.ylim(0,)

#correlacion de caballos de poder con relacion al precio

pearson_coef, p_value = stats.pearsonr(data["horsepower"], data["price"])

pearson_coef, p_value = stats.pearsonr(data['highway-mpg'], data['price'])
print( "The Pearson Correlation Coefficient is", pearson_coef, " with a P-value of P = ", p_value ) 


df_gptest = data[['drive-wheels','body-style','price']]
grouped_test2= df_gptest[['drive-wheels', 'price']].groupby(['drive-wheels'])
grouped_test2.head(2)
grouped_test2.get_group('4wd')['price']

f_val, p_val = stats.f_oneway(grouped_test2.get_group('fwd')['price'], grouped_test2.get_group('rwd')['price'])  
 
print( "ANOVA results: F=", f_val, ", P =", p_val )

# hacer correlaciones con grafica de velas
sns.boxplot(x="body-style", y="price", data=data)

