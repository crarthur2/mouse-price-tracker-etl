import pandas as pd
from test_sql import engine


query = "SELECT * FROM preco_mouses"
df = pd.read_sql(query, engine, index_col='id')
df = df.drop(columns='data_coleta')

# media de precos da loja
media_precos = df['preco'].mean()

# mouses de até 500 reais
prod = df[df['preco'] <= 500].sort_values(by='preco',ascending=False)

# mouse mais caro
mais_caro = df[['nome_produto', 'preco']].max()

# mouse mais barato
mais_barato = df[['nome_produto', 'preco']].min()

# mouses da marca logitech
mouses_logitech = df[df['nome_produto'].str.contains('Logitech', case=False, na=False)]

# media mouses logitech
media_logi = mouses_logitech['preco'].mean()

# mouse mais caro logitech 
caro_logi = mouses_logitech[['nome_produto', 'preco']].max()

# mouse mais barato logitech 
barato_logi = mouses_logitech[['nome_produto', 'preco']].min()

# soma de todos os mouses da loja
soma = df['preco'].sum()

# mouses da redragon ate 100 reais
mouses_red = df[(df['nome_produto'].str.contains("Redragon", case=False)) & (df['preco'] <= 100)].sort_values(by='preco', ascending=False)

# categoria de mouses
df['categoria'] = pd.cut(df['preco'], bins=[0, 150, 400, 2000], labels=['Entrada', 'Intermediario', 'Premium'])

# quantos mouses por categoria
mouses_categ = df['categoria'].value_counts()


