# Mouse Price Tracker ETL
Pipeline de Dados (ETL) em Python para monitorar o preço de mouses gamers. Usa Web Scrapping para coleta, o banco de dados relacional PostgreSQL para armazenamento e a biblioteca Pandas para a análise de dados.

## Arquitetura do Projeto
O sistema foi implementado usando princípios de modularização e separação de arquivos:

* **Extração (Extract):** Realizada no arquivo 'teste_scrapping.py' usando 'BeautifulSoup' e 'requests'. 
* **Transformação (Transform):** Feita na limpeza e conversão de tipos (string para float) e tratamento de exceções.
* **Carga (Load):** Gerenciada pelo 'SQLAlquemy' (ORM), garantindo que os dados ficassem no **PostgreSQL**.

## Tecnologias Utilizadas

* **Linguagem:** Python 3.12
* **Banco de Dados:** PostgreSQL 17 (rodando no Windows Host)
* **ORM:** SQLAlquemy
* **Ambiente:** WSL2 (Ubuntu) integrado Windows
