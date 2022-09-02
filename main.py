import logging
from fast_API_base import app
from animal_methods.the_zoo import Zoo, EnclosureName
from animal_methods.creatures import DietCodes

logger = logging.getLogger()

My_Zoo = Zoo()

My_Zoo.add_animal(enclosure_name=EnclosureName.unnameable_horrors, creature_name='Keith', eyes=16, legs=7, arms=3,
                  holy=True, diet=DietCodes.CARNIVORE)


@app.get("/enclosures/{enclosure_name}")
async def read_enclosure(enclosure_name: str) -> dict[str, str]:
    if enclosure_name in My_Zoo.enclosures.keys():
        relevant_enclosure = My_Zoo.enclosures[enclosure_name]
        return {"enclosure_name": enclosure_name,
                "message": relevant_enclosure.welcome_message + " There are {} creatures here.".format(
                    len(relevant_enclosure.animals_contained))}
    else:
        error_string = "We don't have an enclosure by that name!"
        logger.error(ValueError(error_string))
        return {"enclosure_name": enclosure_name,
                "message": error_string}


@app.get("/enclosures/{enclosure_name}/creatures/{creature_name}")
async def read_creature_by_name(enclosure_name: str, creature_name: str) -> dict[str, str]:
    if enclosure_name in My_Zoo.enclosures.keys():
        relevant_enclosure = My_Zoo.enclosures[enclosure_name]
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


# Access at http://127.0.0.1:8000/enclosures/primates

@app.get("/enclosures/{enclosure_name}/add/")
async def write_creature(enclosure_name: str, creature_name: str, eyes: int = 2, arms: int = 0, legs: int = 4,
                         diet: int = DietCodes.OMNIVORE.value, holy=False):
    return My_Zoo.add_animal(enclosure_name=EnclosureName[enclosure_name], creature_name=creature_name, eyes=eyes,
                             arms=arms,
                             legs=legs, diet=DietCodes(diet), holy=holy)
