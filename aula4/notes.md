# Projeto Aula 4: Web Scrapping com python

## Notas de Aula

### Estudo de Caso

Numa empresa que possui um produto de alto valor agregado, a cada compra o cliente tem 30 dias pra fazer o pagamento, caso não ocorra o mesmo, ele se torna inadimplente e a equipe do setor financeiro aciona a área de cobrança que deve verificar os clientes, gerar o boleto e enviar o mesmo.

#### Objetivo

Automatizar este processo manual e repetitivo de verificar a planilha de clientes, identificar quem está inadimplente e quem não está, entrar no portal de cobrança (no caso, pagseguro), gera o boleto, envia o boleto e repete para o próximo, de modo a facilitar a vida da área de cobrança.

#### Passo a passo

1. Importar a base de dados

2. Visualizar a base de dados

3. Mapear manualmente todo o processo

4. Transformar o processo manual em código python, para apenas um cliente.

* Com o selenium

5. Automatizar o processo para todas as pessoas.

6. Revisar código e fazer ajustes.

##### Web Scrapping


#### A automação

* Dica: Para testar envios automáticos de email, qualquer email, que antes do '@' tenha um parametro "+1, +2, +3" ex: meu_email+1@hotmail.com sempre receberá o email na mesma caixa de entrada.
disparar email para meu_email@hotmail.com, meu_email+1@hotmail.com, meu_email+2@hotmail.com sempre enviará para a mesma caixa de entrada.

* No caso de dados de cobrança é sempre interessante verificar a forma que o campo de valor a cobrar, pagar e etc, pois se ele receber valores escrevendo primeiro os centavos, depois passando este valor pra reais, é necessário entregar já o valor formatado para aquele campo, podemos utilizar o template string formatando para float com a quantidade de casas desejadas no campo


```python
valor = 500
texto_valor = f"{valor:.2f}"
texto_valor
'500.00'

```



Método manual:

* Identificar o cliente inadimplente

* Abrir o site do pagseguro

* Fazer login no PagSeguro.

* Ir para a página de cobrança de pagamento
 
* Preencher as informações do cliente.

* Calcular o valor devido pelo cliente

* inserir o valor cálculado em valor unitário

* Inserir uma mensagem para o cliente

* Clicar em revisar as informações

* Clicar em enviar cobrança. 


#### O Selenium

### Comandos Importantes

#### Método pandas.read_excel("file_path", sheet_name = "sheet name", dtype={Coluna : (object || str || int ||float64)})

Parametros adicionais do pandas.read_excel, sheet_name permite selecionar qual a folha da planilha que desejamos utilizar.
dtype pode alterar o tipo de dado de uma coluna para qualquer tipo valido do python.

```python
------------------

```

#### Método webdriver.get(url)

Acessa o site específicado em url

```python
a = webdriver.Chrome()
a.get(url)
#Abre o chrome na página específicada
```

#### Método webdriver.find_element_by_id("id").send_keys("string")
Encontra na página o elemento com o "id" específicado e o ".send_keys(string) envia a string como parametro para o id do elemento.

```python
a = webdriver.Chrome()
a.get('https://www.youtube.com/watch?v=N9CfV5xtvCQ')
a.find_element_by_id(id="input").send_keys("hello world")
#escreverá "hello world" no elemento que tiver o id == input.
```

#### Método webdriver.find_element_by_xpath('').click()
Caso o elemento não possua um id, podemos utilizar o xpath, inspecionando o elemento, clicando com o botão direito em "copiar" será copiado o xpath do elemento e podemos passar isso como parametro para encontrar este elemento e com o ".click" clicaremos no elemento


```python
a = webdriver.Chrome()
a.get ('https://www.youtube.com/watch?v=N9CfV5xtvCQ')
a.find_element_by_id('/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/button').click()
#clicará no botão de buscar barra de busca do youtube.
```

#### Import de dados de outros elementos

Podemos declarar dados com variáveis dentro de um arquivo de texto como se fosse um arquivo de código e importar para dentro do python.

```senha.txt
senha_email = abcd123
```

```python
from senha import senha_email

a = senha
print(a)
```

#### time.sleep()

Importando a biblioteca time, podemos utilizar a função sleep(time) para avisar ao python esperar x tempo antes de ir para o próximo comando do script

```python
import time
a = "hello
print(a)
time.sleep(5)
a = "world"
print(a)
'hello'
'world'
#depois de 5 segundos foi printado o "world'
```

### Ferramentas

* Python

* Selenium

* DataSet com dados

### Libs

[Selenium](https://www.selenium.dev/)

### Referências
[Case Study]()

[Solução do caso]()
