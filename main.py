from fastapi import FastAPI
from animal_methods.creatures import holy_creation, DietCodes, Creature, Plant
from animal_methods import the_zoo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the Zoo!"}


@app.get("/users/me")
async def read_user_me():
    return {"user_id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
