import requests
from bs4 import BeautifulSoup

url = "https://www.kabum.com.br/produto/495544/mouse-gamer-sem-fio-logitech-g-pro-x-superlight-2-com-lightspeed-32000-dpi-sensor-hero-2-com-bateria-recarregavel-preto-910-006629"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:149.0) Gecko/20100101 Firefox/149.0'}

response = requests.get(url, headers=headers)

print(f"Status da resposta: {response.status_code}")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    print(f"Titulo da Página: {soup.title.text}")

preco_elemento = soup.find("h4", class_="text-4xl")

if preco_elemento:
    print(f"Produto encontrado, preço: {preco_elemento.get_text()}")
else:
    print("Produto nao encontrado")

preco_bruto = preco_elemento.get_text()

novo_preco = preco_bruto.replace("R$","").strip()

novo_preco = novo_preco.replace(",",".")

preco_final = float(novo_preco)

print(f"Preco formatado: {preco_final}")
print(f"Tipo: {type(preco_final)}")

