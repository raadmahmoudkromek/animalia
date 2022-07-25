from fastapi import FastAPI
from animal_methods.creatures import holy_creation, DietCodes, Creature, Plant
from animal_methods.the_zoo import EnclosureName
import logging

app = FastAPI()

logger = logging.getLogger()


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


@app.get("/enclosures/{enclosure_name}")
async def get_enclosure(enclosure_name: EnclosureName):
    if enclosure_name == EnclosureName.small_mammals:
        return {"enclosure_name": enclosure_name, "message": "Welcome to the small mammal enclosure. Cute!"}

    if enclosure_name == EnclosureName.reptiles:
        return {"enclosure_name": enclosure_name, "message": "Welcome to the reptile enclosure. Hope you like scales!"}

    if enclosure_name == EnclosureName.primates:
        return {"enclosure_name": enclosure_name, "message": "Welcome to the primate enclosure. The Orang-utans are friendly, but mind the macaques!"}

    else:
        error_string = "We don't have an enclosure by that name!"
        logger.error(ValueError())
        raise ValueError(error_string)
