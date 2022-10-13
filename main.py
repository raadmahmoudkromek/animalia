import logging

from typing import Dict

from fast_API_base import app
from animal_methods.base_zoo_classes import Enclosure, EnclosureName, Zoo, The_Zoo
from animal_methods.base_zoo_methods import read_enclosure, read_creature_by_name, write_creature
from animal_methods.creatures import BaseCreature, Creature, HolyCreature, DietCodes
from animal_methods.read_write_handling import read_leaflet

logger = logging.getLogger()

The_Zoo.add_animal(enclosure_name=EnclosureName.unnameable_horrors, creature_name='Keith', eyes=16, legs=7, arms=3,
                   holy=True, diet=DietCodes.CARNIVORE)
