from IPython.display import display  # para usar display
import pandas as pd


# CRIANDO UM DATAFRAME A PARTIR DE UM DICIONARIO

# dataframe = pd.DataFrame() - PARA FAZER UM DATAFRAME VAZIO

venda = {'data': ['15/02/2021', '16/02/2021'],
         'valor': [500, 300],
         'produto': ['feijao', 'arroz'],
         'qtde': [50, 70],
         }
vendas_df = pd.DataFrame(venda)

# VISUALIZACAO DE DADOS
# display, print
display(vendas_df)

# IMPORTANDO ARQUIVOS E BASES DE DADOS

vendas_df = pd.read_excel("Vendas.xlsx")
display(vendas_df)

# RESUMOS DE VISUALIZACAO DE DADOS SIMPLES E UTEIS
# head, shape, describe

display(vendas_df.head(10))

print(vendas_df.shape)  # mostra quantidade de linha e colunas

display(vendas_df.describe())  # para fazer resumo da tabela

# PEGAR 1 COLUNA (E OS PD.SERIES)

# se for mais de 1 coluna tem que haver 2 > [] < vendas_df[['produto', 'vendas']]
produtos = vendas_df['Produto']
display(produtos)

# .LOC UM METODO MUITO IMPORTANTE:
# pegar 1 linha,
display(vendas_df.loc[1])

# pegar linhas de acordo com alguma condicao,
vendas_norteshopping_df = display(
    vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping'])

# pegar linhas e colunas especificas,
vendas_norteshopping_df = vendas_df.loc[vendas_df['ID Loja'] == 'Norte Shopping', ["ID Loja, "Produto", "Quantidade" ]]
display(vendas_norteshopping_df)

# pegar 1 valor especifico
print(vendas_df.loc[1, 'Produto'])

#ADICIONAR 1 COLUNA
#a partir de uma coluna que existe
vendas_df['Comissao'] = vendas_df['Valor Final'] * 0.05

#criar uma coluna com valor padrao
vendas_df.loc[:,"Imposto"] = 0