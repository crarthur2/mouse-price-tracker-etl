# Mouse Price Tracker ETL
Pipeline de Dados (ETL) em Python para monitorar o preço de mouses gamers. Usa Web Scrapping para coleta, o banco de dados relacional PostgreSQL para armazenamento e a biblioteca Pandas para a análise de dados.

## Arquitetura do Projeto
O sistema foi implementado usando princípios de modularização e separação de arquivos:

* **Extração (Extract):** Realizada no arquivo 'teste_scrapping.py' usando 'BeautifulSoup' e 'requests'. 
* **Transformação (Transform):** Feita na limpeza e conversão de tipos (string para float) e tratamento de exceções.
* **Carga (Load):** Gerenciada pelo 'SQLAlquemy' (ORM), garantindo que os dados ficassem no **PostgreSQL**.
* **Análise e Visualização:** Processamento de séries temporais com Pandas e geração de gráficos de tendência com Matplotlib.

## Tecnologias Utilizadas

* **Linguagem:** Python 3.12.
* **Banco de Dados:** PostgreSQL 17 (rodando no Windows Host).
* **Bibliotecas Principais:** Pandas, SQLALchemy, Matplolib, BeautifulSoup4, Requests.
* **Ambiente:** WSL2 (Ubuntu) integrado Windows.
* **Automação:** Agendamento via **Crontab** no WSL.

## Funcionalidades Principais

* **Monitoramento Automático:** Execução agendada para capturar variações no mercado sem a necessidade de executar o código todos os dias.
* **Detecção de de Variações:** Algoritmo que identifica e reporta mudanças de preço.
* **Categorização Dinâmica:** Classificação automática de produtos em faixas de preço (Entrada, Intermediário e Premium) via pd.cut.
* **Gráficos Históricos:** Geração automática de imagem .png mostrando a curva de preços de um produto em específico.
* **Log de Erros:** Sistema de rastreamento de falhas de extração para garantir a confiabilidade do pipeline.

## Como executar o projeto

Siga os passos abaixo para configurar e rodar o projeto na sua máquina local.

### 1. Clonar o Repositório
```bash
git clone [https://github.com/seu-usuario/mouse-price-tracker-etl.git](https://github.com/seu-usuario/mouse-price-tracker-etl.git)
cd mouse-price-tracker-etl
```
### 2. Configurar Ambiente Virtual (Python 3.12)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
### 3. Variáveis de Ambiente 
Crie um arquivo .env na raiz do projeto (semelhante ao .env.example) para gerenciar as credenciais do **PostgreSQL** de forma segura.

```bash
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_HOST=localhost
DB_PORT=5432
DB_NAME=seu_nome_do_banco
```

### 4. Inicializar o Banco de Dados

Execute o script para criar a tabela preço_mouses no seu banco de dados.

```bash
python3 test_sql.py
```

### 5. Execução Manual
Para realizar uma coleta e análise imediata.

```bash
python3 main.py     # Executa o Scraping e Carga (Load)
python3 analise.py   # Gera relatórios e o gráfico 'historico_precos.png'
```

### 6. Automação com Crontab (WSL/Linux)
Para monitorar os preços automaticamente todos os dias, adicione a regra ao seu agendador:

1. Abra o editor: crontab -e
2. Adicione a linha (ajuste os caminhos conforme seu usuário):

```bash
00 09 * * * cd /home/arthur/mouse-price-tracker-etl && /home/arthur/mouse-price-tracker-etl/.venv/bin/python3 main.py && /home/arthur/mouse-price-tracker-etl/.venv/bin/python3 analise.py
```


