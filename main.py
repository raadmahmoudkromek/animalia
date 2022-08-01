import logging
from fast_API_base import app
from animal_methods.the_zoo import get_enclosure, Enclosure, EnclosureName
from animal_methods.creatures import Creature, DietCodes
from user_methods import read_user, read_user_me

logger = logging.getLogger()

a_horrifying_creature = Creature(eyes=6, legs=4, arms=10, diet=DietCodes.OMNIVORE)

dummy_enclosures = [Enclosure(enclosure_size=10, enclosure_name=EnclosureName.unnameable_horrors),
                    Enclosure(enclosure_size=20, enclosure_name=EnclosureName.primates)]

dummy_enclosures[0].add_animal(a_horrifying_creature)


@app.get("/enclosures/")
async def read_enclosure(index: int = 0):
    this_enclosure = dummy_enclosures[index]
    return {'enclosure_name': this_enclosure.enclosure_name,
            'message': "Welcome to the {} enclosure! In here there are {} animals out of a maximum of {}.".format(
                this_enclosure.enclosure_name, len(this_enclosure.animals_contained), this_enclosure.enclosure_size)}
