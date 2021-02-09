import pandas as pd

tabela_vendas = pd.read_excel("./aula1/material/Vendas.xlsx")
print(tabela_vendas)

tabela_faturamento = tabela_vendas[["ID Loja", "Valor Final"]].groupby("ID Loja").sum()

print(tabela_faturamento)
