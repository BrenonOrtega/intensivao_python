# Intensivao Piton - Projeto Aula 2: Análise de dados

## Notas de Aula

### Estudo de Caso

Você trabalha em uma grande empresa de cartão de crédito e o diretor da empresa percebeu que o número de cleintes que cancelam cartões tem aumentado significativamente, causando prejuízos enormes para a empresa.

O que fazer para evitar isso? Como saber as pessoas que tem a maior tendencia para cancelar o cartão?

### Ferramentas

* Base de dados com cadastro dos clientes e suas informações, quais cancelaram, quais não e etc.

* Python

* Plotly

#### Passo a passo

Sempre ao fazer uma análise de dados:

1. É necessário fazer a importação da base de dados
2. É necessário fazer tratamentos na base de dados para assegurar a integridade do dataframe.
        - Rodar o DataFrame.info() para verificar se há campos nulos ou vazios, a partir daí podemos decidir como tratar os dados.
        - Tratamentos comuns: Exclusão e correção de linhas e colunas vazias
        - Corrigir colunas importadas (nomes com caracteres invalidos, erros de importação e etc).
        - Eliminar dados inuteis para análise (apagar as colunas desnecessárias).
3. Análisar os dados.
    - Objetivo: Descobrir os principais motivos do cancelamento de cartões de crédito.

##### A análise de dados

1. Devemos ter uma noção da nossa situação, olhar para o panorama do problema, inicialmente no nosso estudo de caso, na coluna "categoria" podemos verificar quantos clientes estão ativos e quantos cancelaram.

2. Após fazer a contagem da quantidade de clientes ativos e a quantidade de clientes cancelados, descobrimos que 16% dos clientes cancelaram suas contas.

3. Análise 80/20 - REGRA DE PARETO: Verificar todas as características dos clientes e buscar os principais motivos de cancelamento.
    * Quais são os 20% dos problemas que impactam em 80% dos seus resultados, neste caso, 20% dos problemas podem estar causando 80% dos cancelamentos, encontrar problemas em comum dentro desses cancelamentos, corrigi-lo terá um impacto grande nos resultados da empresa.
    Existem diversos problemas que podem impactar, mas sempre 20% deles são responsáveis pela maior parte dos problemas.

    * Utilizando o plotly.express geraremos um histograma (pegar novamente explicação do motivo do histograma em 1:17:00 da aula.) histogramas para cada uma das colunas que nos dão informações a cerca dos clientes, para encontrar o nosso "20%" que é onde nosso maior problema se concentra.

#### Analisando os gráficos gerados

* análise exploratória, para encontrar algo que salta os olhos de maneira clara, se não é necessário entrar mais a fundo, durante esta análise a maior parte dos gráficos pode não dar nenhuma resolução, a idéia é encontrar aquela discrepância gritante que seja os "20%" da regra de pareto.

* Categoria do cliente: 16% dos clientes cancelaram, como queremos saber o motivo dos cancelamentos.

* Idade dos clientes: A maioria dos clientes que cancelou está dentro da faixa dos 35 a 57 anos, mas a maioria dos clientes também está nessa faixa.

* Sexo dos clientes: maioria dos clientes femininos, maioria dos cancelamentos femininos, poucas informações relevantes.
* quantidade de dependentes: Sem informações.

* Faixa Salarial: seguindo a tendência da quantiade de clientes x cancelamentos, pouco conclusiva.

* Categoria do Cartão - Quase todos os clientes que cancelaram são da categoria Blue de cartão de crédito.

* Tempo de Inatividade: tempo de inatividade tem uma taxa alta de cancelamento.

* Contatos em 12m - Quanto mais um cliente tentou contato com a empresa, maior a taxa de cancelamentos, INVESTIGAR MOTIVOS PRINCIPAIS DO CONTATO EM OUTRAS BASES DE DADOS. AÇÃO: Tratar os clientes que mais entraram em contato com a empresa para que eles não precisem ligar outras vezes, evitando assim a cancelar o cartão.

* Limite do cartão consumido: Parece que metade dos clientes que não utilizaram o cartão, cancelaram o cartão.

* Qtd de transações em 12m: Clientes com mais de 80 transações ao ano, não cancelam o cartão e clientes que fazem menos de 55 transações ao ano, tem alta taxa de cancelamento. CLIENTES COM MENOS DE 60 TRANSAÇÕES É ALTAMENTE CRÍTICO.

* RELAÇÃO, CLIENTES QUE USAM POUCO O CARTÃO E TENTAM MUITO ENTRAR EM CONTATO COM A EMPRESA, CANCELAM O CARTÃO.

### Funções importantes

Leitura das bases de dados para ler arquivos e salvar em uma variável do tipo dataframe.

* possibilidade de informar o tipo de encoding para poder lidar com caractéres especiais

* Hosting jupyter no vscode não acusa erro de importação, porém acontece no google collab.

```python
df  = pandas.read_excel(file)

df2 = pandas.read_csv(file_path, encoding = 'latin1')
```

#### Método drop():

Para apagar uma coluna ou linha do dataframe utilizamos o método DataFrame.drop(field, axis) sendo field o nome da coluna ou o index da linha e o eixo, sendo axis=0 para apagar linha e axis=1 para deletar coluna.

```python
df = df.drop("coluna1", "coluna2", "coluna...", axis=int)
```

É possível apagar várias linhas ou colunas, só é necessário especificar na função.

```python
df = df.drop("coluna1", "coluna2", "coluna...", axis=int)

df2 = df2.drop(linha1, linha2, linha3, axis=int)
```

#### Método info()

built-in do python, mostra informações acerca de um objeto. no nosso caso, pode ser usado pra mostrar informações acerca de todo o dataframe.

```python
df.info()
```

#### Método dropna()

Método do pandas que exclui todas as linhas que tem itens vazios em uma série.

```python
df.dropna()
```

#### Metodo pandas.describe():

Método do pandas que descreve o dataframe, demonstra contagem de dados, distribuições, média, desvio padrão, valores min, maximo, distribuição normal dos valores de cada campo.

```python
df.describe()
```

#### Método value_counts():

Faz a contagem de todos os valores de toda a coluna passada no index do dataframe.

```python
df['column'].value_counts()
```

parametros opcionais da função:

value_counts(normalize = Bool)
Retorna a contagem dos valores em percentual.

```python
df['column'].value_counts(normalize=True) #Retorna em porcentagem

df['column'].value_counts(normalize=False) #Retorna em número inteiro
```

#### Método apply()

Método da classe pandas.Series que aplica uma função a cada um dos valores de uma série, conforme exemplo a seguir:

```python
df = pd.Series([20, 21, 12],
              index=['London', 'New York', 'Helsinki'])
```

```cmd
df
London      20
New York    21
Helsinki    12
dtype: int64
```

```python
def square(x):
    return x ** 2

df.apply(square)

London      400
New York    441
Helsinki    144
dtype: int64
```

### Plotly

Utilizado para pegar os dados do dataframe e o utiliza para gerar gráficos que dentro do notebook são interativos.
Necessário passar o dataframe, a coluna que será utilizada no eixo x (no caso do histograma, verificar outras tabelas) e color utilizará algum outro campo como parametro para diferenciar os dados.

```python
import ploty.express as px

graph = px.histogram(dataframe, x=x_axis, color)

graph.show()
```

### Libs

[plotly.express](https://plotly.com/python)

[plotly documentation](https://plotly.com/graphing-libraries/)

### Referências

[Kaggle](https://www.kaggle.com/)

* O Kaggle é um portal que fornece desafíos relacionados a análise de dados e machine learning.
