import pandas as pd
import numpy as np

# Importar o conjunto de dados presentes na pasta **"bases"**
df_1 = pd.read_csv("airbnb_ny_2019.csv", encoding= "UTF-8", delimiter= "," )
df_2 = pd.read_csv("mapeamento_vizinhanca.csv", encoding= "UTF-8", delimiter= ";")

# Remover linhas duplicadas
df_airbnb = df_1.drop_duplicates()
df_map = df_2.drop_duplicates()

#Verificando nulos
print(df_airbnb.isnull().sum())
print(df_airbnb.shape)

print(df_map.isnull().sum())
print(df_map.shape)

# Remover linhas com valores nulos
df_airbnb_na = df_airbnb.dropna(how='any')
df_map_na = df_map.dropna(how='any')

#Verificando nulos
print(df_airbnb_na.isnull().sum())
print(df_airbnb_na.shape)

print(df_map_na.isnull().sum())
print(df_map_na.shape)


# Juntar as **bases airbnb_ny_2019** e **mapeamento_vizinhanca** através de um join (**neighbourhood** <-> **vizinhanca**)
df_juntar = df_airbnb_na.merge(df_map_na, how="inner", left_on= "neighbourhood", right_on="vizinhanca")

# Remover a coluna **vizinhanca** após o join
df_juntar_sv = df_juntar.drop("vizinhanca", 1)
 
# Trocar o nome da coluna de **vizinhanca_grupo** para **neighbourhood_group**
df_juntar_tn = df_juntar_sv.rename(columns={"vizinhanca_grupo":"neighbourhood_group"})

# Filtre a coluna neighbourhood_group e mantenha apenas os valores 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island'
bairros = ["Brooklyn", "Manhattan", "Queens", "Staten Island"]
df_filtrado = df_juntar_tn.query(f"neighbourhood_group in {bairros}")

# Após todos os filtros mencionados acima, gere uma base chamada residencias.csv
df_filtrado.to_csv('residencias.csv', index=False)
df_filtrado.to_json('residencias.json')

# A partir da base **residencias.csv**, gere também uma base **media_preco.csv** com a média de preços por tipo de quarto (coluna room_type) e grupo do bairro (coluna neighbourhood_group)
df_mp = pd.read_csv("residencias.csv", encoding= "UTF-8", delimiter= ",")

df_media_preco = df_mp[["room_type", "neighbourhood_group", "price"]].groupby(["room_type", "neighbourhood_group"]).mean()
df_media_preco.to_csv('media_preco.csv', index=False)
df_media_preco.to_json('media_preco.json')