from typing import Dict

from animal_methods.base_zoo_classes import Zoo, The_Zoo, logger, Enclosure, EnclosureName
from animal_methods.creatures import DietCodes
from fast_API_base import app


@app.post("/Zoos/The_Zoo/enclosures/")
async def create_item(enclosure: Enclosure):
    The_Zoo.__add_enclosure__(enclosure_name=enclosure.enclosure_name, enclosure_size=enclosure.enclosure_size,
                              welcome_message=enclosure.welcome_message)
    return enclosure


@app.post("/Zoos/")
async def create_item(zoo: Zoo):
    return zoo


@app.post("/Zoos/The_Zoo/enclosures/{enclosure_name}/add/")
async def write_creature(enclosure_name: str, creature_name: str, eyes: int = 2, arms: int = 0, legs: int = 4,
                         diet: int = DietCodes.OMNIVORE.value, holy: bool = False):
    return The_Zoo.add_animal(enclosure_name=EnclosureName[enclosure_name], creature_name=creature_name, eyes=eyes,
                              arms=arms, legs=legs, diet=DietCodes(diet), holy=holy)


@app.get("/Zoos/The_Zoo/enclosures/{enclosure_name}")
async def read_enclosure(enclosure_name: str) -> Dict[str, str]:
    if enclosure_name in The_Zoo.enclosures.keys():
        relevant_enclosure = The_Zoo.enclosures[enclosure_name]
        return {"enclosure_name": enclosure_name,
                "message": relevant_enclosure.welcome_message + " There are {} creatures here.".format(
                    len(relevant_enclosure.animals_contained))}
    else:
        error_string = "We don't have an enclosure by that name!"
        logger.error(ValueError(error_string))
        return {"enclosure_name": enclosure_name,
                "message": error_string}


@app.get("/Zoos/The_Zoo/enclosures/{enclosure_name}/creatures/{creature_name}")
async def read_creature_by_name(enclosure_name: str, creature_name: str) -> Dict[str, str]:
    if enclosure_name in The_Zoo.enclosures.keys():
        relevant_enclosure = The_Zoo.enclosures[enclosure_name]
    else:
        error_string = "We don't have an enclosure by that name!"
        logger.error(ValueError(error_string))
        return {"enclosure_name": enclosure_name,
                "message": error_string}
    for animal in relevant_enclosure.animals_contained:
        if animal.name == creature_name:
            return {"enclosure_name": enclosure_name,
                    "creature_name": creature_name,
                    "eyes": animal.eyes,
                    "arms": animal.arms,
                    "legs": animal.legs,
                    "diet": animal.diet.name,
                    "message": "This is {}, give them a cuddle!".format(animal.name)}
    return {"enclosure_name": enclosure_name,
            "creature_name": creature_name,
            "message": "We have no animal by the name of {} in this enclosure. Sorry.".format(creature_name)}
