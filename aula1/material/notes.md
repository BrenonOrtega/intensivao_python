# Aula 1 - Intensivão Python - Automação de tarefas

[Material de Estudo](https://drive.google.com/drive/folders/1VYhdSpPCTNjwlVclDUl9EK8GBVOK6Y2j)

<div>
    <p>pandas trabalha nativamente com leitura do excel</p>
    <code> 
    import pandas as pd
    dataset = pd.read_excel(*insira caminho do arquivo a ser lido aqui*)
    display(dataset) 
    </code>
    <p>comando "display(args)" do pandas exibe o conjunto de dados importada do arquivo.</p>

</div>

[Documentação Pandas](https://pandas.pydata.org/docs/)
<ul>
    <p>pandas possui funções para organizar dados como:</p>
        <li> .groupby(*nome da coluna da tabela*) - agrupa os valores de acordo com a coluna indicada no campo</li>
        <li>.sum() executa a soma de valores agrupados.</li>
        <li>Ao pegar colunas de uma tabela, devemos usar [] para campos simples e [[]] para mais de um campo.</li>
        <li>metodo join(*tabela a ser unida*) une duas tabelas diferentes através de seus index na tabela, podendo fazer isso sequencialmente de uma vez só em uma unica linha.</li>
        <li>metodo 'loc()' pega as linhas e colunas que desejamos</li>
        <li>metodo list[].unique() retorna os valores das colunas sem duplicatas.</li>
    <p>Toda tabela no python é um dataframe e posso transformar um conjunto de dados em tabela utilizando a built in function "to_frame()" </p>
        <li>tabela.to_html() formata uma tabela para html</li>
</ul>

### Resultado final da aula: Atingido :rocket:
<div>  
    <p> Foi possível desenvolver a automação do processo da geração de relatórios e gerar os emails</p>
    <p> 
        subject: Resumo de Vendas - loja Iguatemi Esplanada
        From: brenon.ortega@gmail.com
        To: teste123@hotmail.com
        contenty-type: text/html


                <h1>Este é o resumo da loja Iguatemi Esplanada</h1>
                <table border="1" class="dataframe">
        <thead>
            <tr style="text-align: right;">
            <th></th>
            <th>Quantidade</th>
            <th>Valor Final</th>
            <th>Ticket Médio</th>
            </tr>
            <tr>
            <th>ID Loja</th>
            <th></th>
            <th></th>
            <th></th>
            </tr>
        </thead>
        <tbody>
            <tr>
            <th>Iguatemi Esplanada</th>
            <td>8580</td>
            <td>1699681</td>
            <td>198.098019</td>
            </tr>
        </tbody>
        </table>
                <p>Estou a disposição em caso de dúvidas</p>
    </p>
</div>
