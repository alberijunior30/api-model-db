from pydantic_settings import BaseSettings
from sqlalchemy.orm import declarative_base

# Mudar devido a necessidade
user:str = 'postgres'
password:str = 'Junior32720131%'
host:str = 'localhost'
port:str = '5432'
DB_Name:str = 'faculdade'

class Settings (BaseSettings):

    # configurações gerais usadas na aplicação

    API_V1_STR: str = '/api/v1'
    DB_URL: str = f'postgresql+asyncpg://{user}:{password}@{host}:{port}/{DB_Name}'


    class Config:
        case_sensitive = True

settings = Settings()

DBbaseModel: str = declarative_base()
