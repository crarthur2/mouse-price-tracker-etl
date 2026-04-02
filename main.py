import os
import logging
from sqlalchemy.orm import sessionmaker
from test_sql import engine, MousePreco
from teste_scrapping import extrai_dados_mouse

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

logging.basicConfig(
    filename='erro_tracker.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'  
)

urls = [
    'https://www.kabum.com.br/produto/988975/mouse-gamer-razer-deathadder-v3-30-000dpi-preto-rz01-04640100',
    'https://www.kabum.com.br/produto/476952/mouse-gamer-razer-basilisk-v3-rgb-chroma-26000-dpi-optical-switch-11-botoes-preto-rz01-04000100-r3u1',
    'https://www.kabum.com.br/produto/988976/mouse-gamer-sem-fio-razer-viper-v3-hyperspeed-30000-dpi-preto-rz01-04910100',
    'https://www.kabum.com.br/produto/715915/mouse-gamer-razer-deathadder-v3-30-000dpi-preto-rz0104640100',
    'https://www.kabum.com.br/produto/752836/mouse-gamer-rise-mode-laser-pro-black-rgb-16000-dpi-10-botoes-preto-rm-mg-lp-b',
    'https://www.kabum.com.br/produto/94555/mouse-gamer-redragon-cobra-chroma-rgb-12400-dpi-8-botoes-preto-m711',
    'https://www.kabum.com.br/produto/97092/mouse-gamer-sem-fio-logitech-g305-lightspeed-12000-dpi-6-botoes-preto-910-005281',
    'https://www.kabum.com.br/produto/610298/mouse-gamer-sem-fio-redragon-invader-pro-rgb-10000-dpi-8-botoes-wireless-preto-m719rgb-pro',
    'https://www.kabum.com.br/produto/269638/mouse-gamer-sem-fio-logitech-g305-lightspeed-12-000-dpi-6-botoes-programaveis-branco-910-005290',
    'https://www.kabum.com.br/produto/495544/mouse-gamer-sem-fio-logitech-g-pro-x-superlight-2-com-lightspeed-32000-dpi-sensor-hero-2-com-bateria-recarregavel-preto-910-006629',
    'https://www.kabum.com.br/produto/149990/mouse-sem-fio-gamer-logitech-g-pro-x-superlight-lightspeed-25000-dpi-5-botoes-branco-910-005941',
    'https://www.kabum.com.br/produto/652884/mouse-gamer-sem-fio-logitech-g-pro-2-com-lightspeed-rgb-lightsync-ambidestro-4-botoes-programaveis-dpi-de-32k-preto-910-007294',
    'https://www.kabum.com.br/produto/874688/mouse-gamer-redragon-k1ng-1k-m724-12400-dpi-ambidestro-1000hz-usb-tipo-c-preto-m724',
    'https://www.kabum.com.br/produto/154304/mouse-gamer-razer-deathadder-essential-com-fio-6400-dpi-5-botoes-preto',
    'https://www.kabum.com.br/produto/988975/mouse-gamer-razer-deathadder-v3-30-000dpi-preto-rz01-04640100',
    'https://www.kabum.com.br/produto/904360/mouse-gamer-sem-fio-attack-shark-x3-tri-mode-26-000-dpi-sensor-optico-paw3395-6-botoes-programaveis-vermelho',
    'https://www.kabum.com.br/produto/677447/mouse-gamer-sem-fio-logitech-g-pro-x-superlight-2-dex-lightspeed-44-000-dpi-design-assimetrico-para-destros-branco-910-007364',
    'https://www.kabum.com.br/produto/174167/mouse-gamer-logitech-g502-hero-rgb-16000-dpi-11-botoes-lightsync-ajuste-de-peso-910-005550',
    'https://www.kabum.com.br/produto/904361/mouse-gamer-sem-fio-attack-shark-x3-tri-mode-26-000-dpi-sensor-optico-paw3395-6-botoes-programaveis-lilas',
    'https://www.kabum.com.br/produto/499329/mouse-gamer-machenike-m7-pro-com-fio-12800-dpi-6-botoes-preto-jj02gp006',
    'https://www.kabum.com.br/produto/112947/mouse-gamer-logitech-g203-lightsync-rgb-efeito-de-ondas-de-cores-6-botoes-programaveis-e-ate-8-000-dpi-branco-910-005794',
    'https://www.kabum.com.br/produto/519395/mouse-gamer-hyperx-pulsefire-haste-2-rgb-26000dpi-6-botoes-wireless-preto-6n0b0aa',
    'https://www.kabum.com.br/produto/904359/mouse-gamer-sem-fio-attack-shark-x3-tri-mode-26-000-dpi-sensor-optico-paw3395-6-botoes-programaveis-branco',
    'https://www.kabum.com.br/produto/597062/mouse-gamer-sem-fio-redragon-st4r-pro-26000-dpi-6-botoes-bluetooth-preto-m917gb-pro',
    'https://www.kabum.com.br/produto/903640/mouse-gamer-sem-fio-attack-shark-r1-18000-dpi-55g-tri-mode-sensor-paw3311-preto',
    'https://www.kabum.com.br/produto/134253/mouse-gamer-sem-fio-logitech-g305-lightspeed-6-botoes-12-000-dpi-lilas-910-006021',
    'https://www.kabum.com.br/produto/938638/mouse-gamer-sem-fio-attack-shark-x2-transparente-tri-mode-rgb-2400-dpi-sensor-pixart-3212-branco',
    'https://www.kabum.com.br/produto/631570/mouse-gamer-redragon-office-1200-dpi-com-fio-bm-4049-preto',
    'https://www.kabum.com.br/produto/312917/mouse-gamer-sem-fio-logitech-g-pro-x-superlight-lightspeed-25-600-dpi-5-botoes-programaveis-sensor-hero-25k-magenta-910-005955',
    'https://www.kabum.com.br/produto/518744/mouse-gamer-husky-arrow-rgb-16000-dpi-7-botoes-preto-hms300pt',
    'https://www.kabum.com.br/produto/904362/mouse-gamer-sem-fio-attack-shark-x3-tri-mode-26-000-dpi-sensor-optico-paw3395-6-botoes-programaveis-laranja',
    'https://www.kabum.com.br/produto/724692/mouse-gamer-xt-racer-ultimate-xtm-230-rgb-16000dpi-1ms-profissional-preto-xtm-230',
    'https://www.kabum.com.br/produto/108985/mouse-gamer-redragon-invader-m719-rgb-7-botoes-10000dpi-rgb-m719-rgb',
    'https://www.kabum.com.br/produto/732611/mouse-gamer-sem-fio-hyperx-pulsefire-haste-2-core-wireless-rgb-12000-dpi-bluetooth-dongle-de-2-4-ghz-branco-8r2e7aa',
    'https://www.kabum.com.br/produto/948296/mouse-gamer-sem-fio-logitech-g-pro-x-superlight-2c-5-botoes-sensor-44k-dpi-atualizacao-de-ate-8-khz-pc-e-mac-branco-910-007537',
    'https://www.kabum.com.br/produto/388060/mouse-gamer-sem-fio-logitech-g705-colecao-aurora-rgb-bluetooth-usb-6-botoes-branco-910-006366',
    'https://www.kabum.com.br/produto/652883/mouse-gamer-sem-fio-logitech-g-pro-2-com-lightspeed-rgb-lightsync-ambidestro-4-botoes-programaveis-dpi-de-32k-branco-910-007301',
    'https://www.kabum.com.br/produto/641963/mouse-sem-fio-gamer-hyperx-pulsefire-haste-2-mini-rgb-led-650-ips-bluetooth-5-1-wireless-preto-7d388aa',
    'https://www.kabum.com.br/produto/948297/mouse-gamer-sem-fio-logitech-g-pro-x-superlight-2c-5-botoes-44000-dpi-atualizacao-de-ate-8-khz-pc-e-mac-magenta-910-007544',
    'https://www.kabum.com.br/produto/220599/mouse-gamer-razer-deathadder-essential-6400dpi-5-botoes-branco'
]

Session = sessionmaker(bind=engine)
session = Session()

urls = list(set(urls))

try:
    for url in urls:
        print(f"Extraindo dados de {url}")
        dados = extrai_dados_mouse(url)

        if dados:
            novo_mouse = MousePreco(
                nome_produto=dados['Nome'],
                loja="Kabum",
                preco=dados['Preco']
            )
            session.add(novo_mouse)
        else:
            logging.warning(f"Falha na extração da URL: {url}")

    session.commit()
    print("Sucesso!")

except Exception as e:
    session.rollback()
    logging.error(f"Erro no processo: {e}", exc_info=True)
    print(f"Erro registrado no log: {e}")

finally:
    session.close()