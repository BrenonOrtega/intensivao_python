#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#   Projeto Aula 2 - Análise de Dados
import pandas as pd
import plotly.express as px

tab_clients = pd.read_csv('./aula2/material/ClientesBanco.csv', encoding='latin1')
display(tab_clients)


# In[ ]:


#   Agora será retirado a coluna "CLIENTNUM" visto que ela é pessoal de cada cliente e portanto
#   Irrelevante para nossa análise.
df = tab_clients
df = df.drop('CLIENTNUM', axis=1)

display(df)


# In[ ]:


#   Apenas demonstrando o dataframe após a remoção da coluna desnecessária.
display(df.describe())


# In[58]:


#   Aqui é feita a contagem de clientes que estão ativos e os que estão cancelados
#   foi ""APLICADA"" uma função lambda nomeada como "percent"para transformar a 
#   contagem de clientes normalizada em porcentagem.
percent = lambda x: x * 100

clientes = df.value_counts('Categoria', normalize=True)
clientes = clientes.apply(percent).round(2)

print(clientes)


# In[62]:


#   Após a verificação que realmente há um número alto de cancelamentos, devemos começar
#   a analisar os dados fornecidos, com os dados do dataframe, geraremos histogramas que
#   com uma análise exploratória (visual, empírica) poderá nos trazer algum tipo de 
#   conclusão para a análise.

#   instanciamos nosso óbjeto graph que será do tipo histograma utilizando a biblioteca 
#   plotly e passando a base de dados e indicando a coluna que desejamos "sortir" e com
#   um laço de repetição, geraremos para cada uma das colunas dos nossos dados.
graph = px.histogram(df["Categoria"])
graph.show()

for column in df.columns:
    graph = px.histogram(df[column])
    graph.show()


# In[ ]:




