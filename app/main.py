from contextlib import asynccontextmanager

from bson import ObjectId
from bson.errors import InvalidId
from fastapi import FastAPI, HTTPException
from motor.motor_asyncio import AsyncIOMotorCollection

from app.db import mongodb
from app.models.user_model import UserCreate, UserResponse, UserUpdate


# Eventos de startup e shutdown
@asynccontextmanager
async def lifespan(api: FastAPI):
    await mongodb.connect()
    yield
    mongodb.close()


app = FastAPI(
    title="User Registration API",
    description="API simples para cadastro de usuários com MongoDB",
    version="0.1.0",
    lifespan=lifespan
)


def get_users_collection() -> AsyncIOMotorCollection:
    return mongodb.database.users


@app.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate):
    collection = get_users_collection()

    # Verifica se o e-mail já existe
    if await collection.find_one({"email": user.email}):
        raise HTTPException(status_code=400, detail="Email já cadastrado")

    user_dict = user.model_dump()
    result = await collection.insert_one(user_dict)
    return {**user_dict, "id": str(result.inserted_id)}


@app.get("/users/", response_model=list[UserResponse])
async def get_all_users():
    collection = get_users_collection()
    users = await collection.find().to_list(1000)

    # Converte ObjectId para string
    for user in users:
        user["id"] = str(user["_id"])
        del user["_id"]

    return users


@app.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: str, user_data: UserUpdate):
    # Obter usuário existente
    existing_user = await get_user_or_404(user_id)
    collection = get_users_collection()

    update_data = user_data.model_dump(exclude_unset=True)

    # Verificar se o novo email já está em uso
    if "email" in update_data:
        email_exists = await collection.find_one({
            "email": update_data["email"],
            "_id": {"$ne": ObjectId(user_id)}
        })
        if email_exists:
            raise HTTPException(status_code=400, detail="Email já está em uso")

    # Atualizar no banco de dados
    await collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": update_data}
    )

    # Retornar usuário atualizado
    updated_user = await collection.find_one({"_id": ObjectId(user_id)})
    return convert_user(updated_user)


@app.delete("/users/{user_id}")
async def delete_user(user_id: str):
    # Verificar existência do usuário
    await get_user_or_404(user_id)
    collection = get_users_collection()

    # Excluir do banco de dados
    await collection.delete_one({"_id": ObjectId(user_id)})

    return {"message": "Usuário excluído com sucesso"}


def convert_user(user) -> dict:
    user["id"] = str(user["_id"])
    del user["_id"]
    return user


async def get_user_or_404(user_id: str):
    try:
        obj_id = ObjectId(user_id)
    except InvalidId:
        raise HTTPException(status_code=400, detail="ID inválido")

    collection = get_users_collection()
    user = await collection.find_one({"_id": obj_id})

    if not user:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return user
