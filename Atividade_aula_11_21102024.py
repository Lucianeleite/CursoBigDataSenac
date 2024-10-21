#Atividade Prática:
#Através do Kaggle, procurem outros datasets e apliquem os comandos trabalhados anteriormente.

#Novo arquivo baixado do kaggle  1980sClassics

import pandas as pd
df_disco = pd.read_csv('1980sClassics.csv')  #Baixar o arquivo do link acima e colocar ele na pasta do PY, o nome escrito no código tem que ser igual ao do arquivo baixado
print(df_disco.head())  # Exibe as primeiras linhas
print(df_disco.tail())  # Exibe as cinco últimas linhas

print(df_disco.to_string())

pd.set_option('display.max_rows',4)

df_filtrado = df_disco[df_disco['Year'] == 1978]
print(df_filtrado)

df_disco['Duration_Seconds'] = df_disco['Acousticness'] / 60