from enum import Enum
import logging
from fast_API_base import app

logger = logging.getLogger(__name__)


class EnclosureName(str, Enum):
    small_mammals = 'small_mammals'
    reptiles = 'reptiles'
    primates = 'primates'


class enclosure:
    def __init__(self, enclosure_id, enclosure_size, enclosure_name):
        self.enclosure_id = enclosure_id
        self.enclosure_size = enclosure_size
        self.animals_contained = []
        self.enclosure_name = enclosure_name

    def add_animal(self, animal):
        # add an animal to the enclosure here
        self.animals_contained.append(animal)
        pass


class Zoo:
    def __init__(self, enclosures):
        self.num_enclosures = enclosures


@app.get("/enclosures/{enclosure_name}")
async def get_enclosure(enclosure_name: EnclosureName):
    if enclosure_name == EnclosureName.small_mammals:
        return {"enclosure_name": enclosure_name, "message": "Welcome to the small mammal enclosure. Cute!"}

    if enclosure_name == EnclosureName.reptiles:
        return {"enclosure_name": enclosure_name, "message": "Welcome to the reptile enclosure. Hope you like scales!"}

    if enclosure_name == EnclosureName.primates:
        return {"enclosure_name": enclosure_name,
                "message": "Welcome to the primate enclosure. The Orang-utans are friendly, but mind the macaques!"}

    else:
        error_string = "We don't have an enclosure by that name!"
        logger.error(ValueError())
        raise ValueError(error_string)
