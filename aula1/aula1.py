#!/usr/bin/env python
# coding: utf-8

# In[ ]:



#Problema: Com a tabela "Vendas.xlsx" devemos criar relatórios de cada uma das lojas no dataframe, enviar para os seus respectivos gerentes e então, enviar um relatório geral para a diretoria.

#Devemos automatizar este processo utilizando python.


# In[ ]:


#Aqui é feita a importação da lib pandas como pd e utilizada sua 
#função para ler o excel e display para mostrar a tabela e seu conteúdo.
#lembrete:necessário instalação das libs corretas para executar a leitura.
import pandas as pd

tabela_vendas = pd.read_excel("./Vendas.xlsx")
display(tabela_vendas.columns)


# In[ ]:


#aqui é criada a tabela_faturamento recebendo apenas as colunas "ID Loja" e "Valor final"
#subsquentemente jáfoi feito o agrupamento das linhas usando como parametro o "ID Loja" e a 
#soma dos valores com função "Sum()" possívelmente existem as funções das outras operações.
faturamento = tabela_vendas[["ID Loja", "Valor Final"]].groupby(by="ID Loja", sort=False).sum()

#É possível selecionar como ordernar a tabela utilizando a função ".sort_value()" ou ".sort_index()"
#importante ressaltar que sort_index() não recebe um parametro "by", enquanto sort_values() recebe.
#o parametro ascending=bool que dita se o index ou os valores será apresentado de maneira crescente ou decrescente.
faturamento = faturamento.sort_index(ascending=True)
print(tabela_faturamento)


# In[ ]:


#   Criação da tabela total_vendas, onde será possível averiguar quantas 
#   vendas foram feitas por cada loja, também já sendo agrupadas de acordo com o ID
#   e somando os valores da quantidade de vendas.
total_vendas = tabela_vendas[["ID Loja", "Quantidade"]].groupby("ID Loja").sum()

#   Listando de acordo com a quantidade de vendas
total_vendas = total_vendas.sort_index()
print(total_vendas)


# In[ ]:





# In[ ]:


#   Agora com a tabela de total de vendas e total faturamento, podemos calcular o 
#   "ticket médio" das vendas que é o valor médio de cada venda feita por aquela loja.
#   IMPORTANTE: PARA TRANSFORMAR ticket_medio EM UM DATAFRAME É NECESSÁRIO USAR A FUNÇÃO ".to_frame()"
ticket_medio = (faturamento["Valor Final"] / total_vendas["Quantidade"]).to_frame()

#Renomeando  o campo vazio para "ticket médio" utilizando o comando rename({'oldName1': 'newName1'})
#A coluna vem por padrão definida como 0, portanto renomeamos 0 com "Ticket Medio"
#Então organizamos de acordo com o maior valor utilizando novamente o sort_values()
ticket_medio = ticket_medio.rename(columns={0: "Ticket Medio"}).sort_index()

print(ticket_medio)


# In[ ]:


#   Agora para gerar um relatório customizado para cada loja, primeiramente é necessário gerar 
#   uma lista com todas as lojasnosso dataframe tabela_vendas possuí todos os nome de loja, 
#   porém com repetições, se passarmos diretamente para a variável lojas, teremos todas as 
#   10mil linhas apresentadasPara resolver isso, existe o método de dataframe "unique()" que
#   retornará cada uma das chaves de ID Loja sem repetições.
lojas = tabela_vendas['ID Loja'].unique()

fatur_qtd = tabela_vendas[['ID Loja', 'Quantidade', 'Valor Final']].groupby('ID Loja').sum()
fatur_qtd = fatur_qtd.sort_index()

print(fatur_qtd)


# In[ ]:


#   Criação da função que gera e dispara os emails automaticamente. 
#   Teste de geração de email: OK
#   Teste de envio de email: Pendente

import smtplib
import email.message
secrets = 'teste'
def enviar_email(resumo_loja, loja, destinatario="teste123@hotmail.com"):
    remetente = "brenon.ortega@gmail.com"
    servidor = smtplib.SMTP("smtp.gmail.com:587")
    conteudo_email = f"""
        <h1>Este é o resumo da loja {loja}</h1>
        {resumo_loja.to_html()}
        <p>Estou a disposição em caso de dúvidas</p> 
    """

    mail = email.message.Message()

    mail['subject'] = f'Resumo de Vendas - loja {loja}' 
    mail['From'] = remetente
    mail['To'] = destinatario
    password = secrets

    mail.add_header('contenty-type', 'text/html')
    mail.set_payload(conteudo_email)

    #server.starttls()
    #server.login(remetente, password)
    #s.sendmail(remetente, destinatario, email.as_string().encode('utf-8'))
    print(mail)


# In[ ]:



#   Agora a maneira para conseguir gerar um resumo do faturamente e da quantidade de vendas, é 
#   necessário criar um laço for que executará duas operações, primeiro gerar uma tabela com
#   todas as vendas de uma loja específica,agrupar estes dadogits e fazer a somatória, gerar o ticket médio de cada loja.
#   ***O atributo "loc[]" tem muitas peculiaridades, ler e entender bem a documentação para utilizá-lo.
for loja in lojas:
    tabela_loja = tabela_vendas.loc[(tabela_vendas["ID Loja"] == loja), ['ID Loja', 'Quantidade', 'Valor Final']]
    tabela_loja = tabela_loja.groupby('ID Loja').sum()
    tabela_loja["Ticket Médio"] = tabela_loja["Valor Final"] / tabela_loja["Quantidade"]
    enviar_email(tabela_loja, loja)




# In[ ]:




