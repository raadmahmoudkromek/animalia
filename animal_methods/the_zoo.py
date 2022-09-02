from enum import Enum
from animal_methods.creatures import Creature, DietCodes
from typing import Dict, List
import logging

logger = logging.getLogger(__name__)


class EnclosureName(Enum):
    small_mammals = 1
    reptiles = 2
    primates = 3
    unnameable_horrors = 4


class Enclosure:
    def __init__(self, enclosure_size: int, enclosure_name: EnclosureName, welcome_message: str):
        try:
            assert type(enclosure_name) is EnclosureName
        except AssertionError as e:
            logger.error(e)
        self.enclosure_size = enclosure_size
        self.animals_contained: List[Creature] = []
        self.enclosure_name = enclosure_name
        self.welcome_message = welcome_message

    def add_animal(self, animal: Creature):
        try:
            assert len(self.animals_contained) <= self.enclosure_size - 1
        except AssertionError:
            logger.error(AssertionError)
            return {"enclosure_name": self.enclosure_name.name,
                    "creature_name": animal.name,
                    "message": "We can't fit any more creatures in this enclosure! There are {} animals out of a possible {} in this enclosure.".format(
                        len(self.animals_contained), self.enclosure_size)}

        self.animals_contained.append(animal)
        return {"enclosure_name": self.enclosure_name.name,
                "creature_name": animal.name,
                "message": "You have added {} to the {} enclosure. There are now {} animals out of a possible {} in this enclosure.".format(
                    animal.name, self.enclosure_name.name, len(self.animals_contained), self.enclosure_size)}


class Zoo:
    def __init__(self):
        self.enclosures: Dict[str, Enclosure] = {}
        self.__add_enclosure__(enclosure_name=EnclosureName.small_mammals, enclosure_size=10,
                               welcome_message="Welcome to the small mammal enclosure. Cute!")
        self.__add_enclosure__(enclosure_name=EnclosureName.primates, enclosure_size=10,
                               welcome_message="Welcome to the primate enclosure. The Orang-utans are friendly, but mind the macaques!")
        self.__add_enclosure__(enclosure_name=EnclosureName.reptiles, enclosure_size=10,
                               welcome_message="Welcome to the reptile enclosure. Hope you like scales!")
        self.__add_enclosure__(enclosure_name=EnclosureName.unnameable_horrors, enclosure_size=2,
                               welcome_message="Welcome to the enclosure for the horrifying otherworldly monsters. Please keep children under control, they frighten the beings.")

    def __add_enclosure__(self, enclosure_name: EnclosureName, enclosure_size: int, welcome_message: str):
        self.enclosures[enclosure_name.name] = Enclosure(enclosure_size=enclosure_size, enclosure_name=enclosure_name,
                                                         welcome_message=welcome_message)

    def add_animal(self, enclosure_name: EnclosureName, creature_name: str, eyes: int, diet: DietCodes, legs: int,
                   arms: int, holy: bool):
        new_creature = Creature(name=creature_name, eyes=eyes, diet=diet, legs=legs, arms=arms, holy=holy)
        try:
            assert new_creature not in [creature.name for enc in self.enclosures.values() for creature in
                                        enc.animals_contained]
        except AssertionError:
            logger.error(AssertionError)
            return {"enclosure_name": enclosure_name,
                    "creature_name": creature_name,
                    "message": "There is already a creature by the name of {} in the zoo!".format(creature_name)}

        return self.enclosures[enclosure_name.name].add_animal(new_creature)
