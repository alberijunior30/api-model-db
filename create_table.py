from core.settings import DBbaseModel
from core.database import engine



async def create_tables () -> None:
    import models.__all_models
    print("Criando as Tabelas no Banco de Dados...")

    async with engine.begin() as conn:
        await conn.run_sync(DBbaseModel.metadata.drop_all)
        await conn.run_sync(DBbaseModel.metadata.create_all)
    print("Tabelas criadas com Sucesso.")

if __name__ == "__main__":
    import asyncio

    asyncio.run(create_tables())

