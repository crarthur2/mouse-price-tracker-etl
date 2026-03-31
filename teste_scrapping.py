import requests
from bs4 import BeautifulSoup

def extrai_dados_mouse(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:149.0) Gecko/20100101 Firefox/149.0"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        preco_elemento = soup.find('h4', class_='text-secondary-500')
        preco_texto = preco_elemento.text
        preco_limpo = float(preco_texto.replace("R$",'').replace(".",'').replace(",",'.').strip())

        titulo_elemento = soup.find('h1', class_='text-black-800')
        nome_mouse = titulo_elemento.text.strip()

        return {'Nome': nome_mouse, 'Preco': preco_limpo}
    
    except Exception as e:
        print(f"Erro ao extrair preco mouse {e}")
        return None

