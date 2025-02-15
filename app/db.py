from dotenv import dotenv_values
from motor.motor_asyncio import AsyncIOMotorClient

# Carrega variáveis de ambiente do arquivo .env
config = dotenv_values(".env")


class MongoDB:
    def __init__(self):
        self.client = None
        self.database = None

    async def connect(self):
        self.client = AsyncIOMotorClient(config["MONGODB_URL"])
        self.database = self.client[config["DB_NAME"]]
        print("Conectado ao MongoDB!")

    def close(self):
        self.client.close()
        print("Conexão com MongoDB fechada!")


# Instância única do banco de dados
mongodb = MongoDB()
