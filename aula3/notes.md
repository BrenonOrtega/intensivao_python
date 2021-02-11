# Projeto Aula 3: Data Science e Machine Learning

## Notas de Aula

### Estudo de Caso

No Airbnb, qualquer pessoa que tenha um quarto ou imóvel de qualquer tipo disponível para alugar e você pode ofertar o seu imóvel para ser alugado por diária.

#### Objetivo

Construir um modelo de previsão que indique para essa pessoa qual o melhor valor para aluguel do seu imovel.

##### Ciência de Dados

* Ciência de dados -> Resolver desafio com dados.

* Ciência de dados x Business Inteligence.

* Ciência de dados e Machine Learning(Inteligência Artificial)

* Onde podemos aplicar Ciência de Dados?

### Ferramentas

* Python

* Projeto pronto com machine learning

* DataSet com dados

#### Passo a passo de um projeto de ciência de dados

Todo projeto de ciência de dados possui 8 tapas, sendo estas:
**Importante notar que a partir do passo 3 é onde se ínicia o trabalho com o python, tratando os dados.

1. Entendimento do Desafio

2. Entendimento da Empresa/Área de Aplicação

3. Extração/Obtenção de Dados

4. Ajustes de Dados (Limpeza e tratamento dos dados)

5. Análise Exploratória

6. Modelagem + Algoritmos

7. Interpretação dos Resultados

8. Deploy/Produção.

#### Analise

Importamos nossa base de dados, consolidamos todos os dados em uma única base de dados.

A partir daí tiramos uma amostra do nosso modelo e eliminamos campos que são desnecessários para  análise como campos de texto livre, dados irrelevantes ou que não são analisaveis, dados que são repetitivos como data de entrada x mês da consulta, retiramos valores que são identicos ou tem pouquissima variação.

A partir daí temos que lidar com campos vazios
NENHUM MODELO DE INTELIGÊNCIA ARTIFICIAL PODE LIDAR COM CAMPOS VAZIOS.

Regra que o instrutor utilizou, em caso de mais de 300_000 itens, a coluna foi apagada. (Eu pessoalmente popularia elas com as médias das linhas validas. # Instrutor disse que no caso de inserir médias é necessário verificar se aquilo não pode gerar um resultado falso.)
Tudo que não te ajuda, te atrapalha, portanto deve ser eliminado.

Depois disso, apagar apenas as linhas que possuem valores vazios, no caso de ser uma porcentagem pequena de todo o database onde não influênciaria.

Executar ajustes na base de dados, por exemplo transformar colunas que aparecem como "texto" mas são número em tipos numéricos de dados. (ex: Valor do imóvel aparecendo como coluna de texto.)

Executar a análise exploratória e verificar a correlação das colunas entre si, qualquer valor que seja 1, -1 ou muito próximo disso deve ser eliminado visto que sua correlação é muito grande.

Na tabela de correlação, números negativos são inversamente proporcionais, correlação positiva é quando os valores das colunas são diretamente proporcionais.

OUTLIERS: São pontos fora da curva, eles atrapalham a análise de dados, portanto é necessário análisar se é possível ou não excluir este dados.

Após plotar os gráficos para cada uma das features (colunas) do gráfico, verificamos através do histograma e do gráfico de caixa que é possível no nosso caso de excluir os outliers, devido a ter análisado que esses outliers são realmente fora da realidade de uma pessoa comum, porém essa análise deve ser feita para cada uma das features da database.
No caso da feature "number of reviews" não é possível retirar os outliers devido a que no nosso caso, os imoveis que tem o maior número de reviews são imoveis que alugam muito, portanto estamos retirando um imóvel que está sendo muito procurado, portanto é um grande parâmetro pra precificar os imóveis, mas foi removido da análise visto que a idéia é para uma pessoa inserir um novo imovel, ele não teria nenhum review.

Qualquer programa de inteligência artificial só pode utilizar números, nunca texto, portanto devemos mapear as linhas de texto como uma matriz identidade.

Devemos transformar o texto em "variáveis dummies", linhas de texto se transformam em colunas que relacionadas a estas mesmas linhas, geram uma matriz identidade, quando o "texto" dessa linha for relacionada a coluna que foi criada, ela recebe o valor 1(verdadeiro, True) para que a AI possa entender os dados.

após gerar todos estes dados, poderemos entregar isso para a AI para que ela possa aprender

ETAPAS A SEGUIR SEMPRE QUE FOR UTILIZAR INTELIGÊNCIA ARTIFICIAL:

1. Necesário identificar como avaliar os resultados do modelo.

* Nesse caso foi utilizado a métrica do R², quanto mais próximo de 100% o valor melhor, a partir de 80% já pode ser dito confiável.

2. Escolher a inteligência artificial que será utilizada, existem muitas disponíveis.

* Neste projeto serão utilizados modelos de regressão estatística, visto que desejamos descobrir o preço do imóvel, ou seja cálcular um valor numérico é utilizado a regressão.

* Modelos mais comuns para regressão: RandomForest, LinearRegression, Extra Tree.

São extremamente confiáveis e geram resultados númericos de maneira eficiente.

3. Treinar os modelos utilizando a base de dados.

* Você passa 90% da base de dados, ele vai análisar o conjunto de características e ver o valor correspondente e a partir disso ele terá "aprendido" com sua base de dados, passando um "set" com os 10% de características restantes como testes, poderemos validar se o modelo é bem sucedido.

* Após o treinamento, verificar os resultados e decidir qual é o melhor modelo para o case study, fazer ajustes no modelo, retirando o que for desnecessário, coisas que não tem impacto no nosso modelo e refazer o treinamento do

### Comandos Importantes

#### Atributo pandas.DataFrame.dtypes

Demonstra o tipo de dado (datatype) de cada coluna inserida em um dataframe.

```python
df = pandas.DataFrame()
df.dtypes
```

#### Método to_csv()

Metodo do pandas para criação de um arquivo '.csv' a partir de um dataframe, uso básico é inserindo como parametro o nome do novo arquivo seguido de .csv
[referencia de uso](https://www.datacourses.com/write-a-pandas-dataframe-to-a-csv-file-218/)
```python
df = pandas.DataFrame()
df.to_csv('new_file_name.csv')
```

Parametros Opcionais:

chunksize is an extremely useful when the size of the DataFrame is very large (think 100k+ rows). It can be easily added to the to_csv() function:

```python
df.to_csv('new_file_name.csv', mode='a', header=False, index=False, chunksize=10000)
```
#### Método ()

```python
 ------------------
```

#### Método ()

```python
 ------------------
```

#### Método ()

```python
 ------------------
```

#### Método ()

```python
 ------------------
```

#### Método ()

```python
 ------------------
```

### Libs

[pandas](https://pandas.pydata.org/pandas-docs/stable/#)

[pathlib](https://pathlib.readthedocs.io/en/0.5/)

[numpy](https://numpy.org/)

[seaborn](https://seaborn.pydata.org/)

[matplolib(pyplot)](https://matplotlib.org/api/pyplot_api.html)

[plotly](https://plotly.com/python/plotly-express/)

[sklearn (metrics, linear_model, ensemble, model_selection)](https://sklearn.org/)

### Referências
[Case Study - AirBnb Rio de janeiro](https://www.kaggle.com/allanbruno/airbnb-riode-janeiro)

[Solução do caso](https://www.kaggle.com/allanbruno/helping-regular-people-price-listingson-airbnb)
