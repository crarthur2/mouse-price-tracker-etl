import os
import pandas as pd
import matplotlib.pyplot as plt
from test_sql import engine

caminho_projeto = os.path.dirname(os.path.abspath(__file__))

# Carregamento e limpeza
query = "SELECT * FROM preco_mouses"
df = pd.read_sql(query, engine, index_col='id')

# Verificacao de variacao nos precos
historico = df.sort_values(['nome_produto', 'data_coleta'])
df['variacao'] = df.groupby('nome_produto')['preco'].diff()

# Relatorios especificos 
mudancas = df[df['variacao']!=0].dropna(subset=['variacao'])
print("--- Produtos que sofreram alteração no preço ---")
print(mudancas[['nome_produto', 'preco', 'variacao']])

prod = df[df['preco'] <= 500].sort_values(by='preco',ascending=False)
print("\n--- Produtos de até 500 reais ---")
print(prod)

mouses_logitech = df[df['nome_produto'].str.contains('Logitech', case=False, na=False)]
print("\n--- Mouses da marca LOGITECH ---")
print(mouses_logitech)

mouses_red = df[(df['nome_produto'].str.contains("Redragon", case=False)) & (df['preco'] <= 100)].sort_values(by='preco', ascending=False)
print("\n--- Mouses da REDRAGON de até 100 reais")
print(mouses_red)

df['categoria'] = pd.cut(df['preco'], bins=[0, 150, 400, 2000], labels=['Entrada', 'Intermediario', 'Premium'])
mouses_categ = df['categoria'].value_counts()
print("\n--- Mouses por categoria ---")
print(mouses_categ)

idx_min = df['preco'].idxmin()
mais_barato = df.loc[idx_min, 'nome_produto']
print("\n--- Mouse mais barato da loja ---")
print(mais_barato)

idx_max = df['preco'].idxmax()
mais_caro = df.loc[idx_max, 'nome_produto']
print("\n--- Mouse mais caro da loja ---")
print(mais_caro)

media_precos = df['preco'].mean()
print("\n--- Media de precos da loja ---")
print(media_precos)


if not df.empty:
    mouse_graf = df['nome_produto'].iloc[0]
    dados_plot = df[df['nome_produto'] == mouse_graf].sort_values('data_coleta')

    plt.figure(figsize=(12,6))
    plt.plot(dados_plot['data_coleta'], dados_plot['preco'], marker='o', linestyle='-', color='forestgreen', linewidth=2)

    plt.title(f"Histórico de preço: {mouse_graf[:50]}...", fontsize=14)
    plt.xlabel('Data da Coleta', fontsize=12)
    plt.ylabel('Preço (R$)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig(os.path.join(caminho_projeto, 'historico_precos.png'))
    print("\nGráfico gerado com sucesso: 'histórico_precos.png'")


