import os
import urllib.parse
from dotenv import load_dotenv
from sqlalchemy import  create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

os.environ['PGMESSAGES'] = 'en_US.UTF-8'
load_dotenv()

user = os.getenv('DB_USER')
password = urllib.parse.quote_plus(os.getenv('DB_PASSWORD',''))
host = os.getenv('DB_HOST')
port = os.getenv('DB_PORT')
db = os.getenv('DB_NAME', 'mouse_tracker')

DATABASE_URL = f"postgresql://{user}:{password}@{host}:{port}/{db}"
engine = create_engine(DATABASE_URL)

Base = declarative_base()

class MousePreco(Base):
    __tablename__ = 'preco_mouses'

    id = Column(Integer, primary_key=True)
    nome_produto = Column(String, nullable=False)
    loja = Column(String, nullable=False)
    preco = Column(Float, nullable=False)
    data_coleta = Column(DateTime, default=datetime.now)


if __name__ == '__main__':
    try:
        Base.metadata.create_all(engine)
        print(f"Conexão estável e tabela 'precos_mouses' pronta no banco '{db}'!")
    except Exception as e:
        print(f"Erro ao configurar Banco de Dados: {e}")









