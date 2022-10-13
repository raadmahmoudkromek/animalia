from enum import Enum, unique
from pydantic import BaseModel
from dataclasses import dataclass


def holy_creation(func):
    def wrapper(*args, **kwargs):
        print('I am creating a living thing!')
        created_thing = func(*args, **kwargs)
        print('I have... CREATED!!')
        return created_thing

    return wrapper


@unique
class DietCodes(Enum):
    OMNIVORE = 0
    CARNIVORE = 1
    VEGETARIAN = 2


class BaseCreature(BaseModel):
    name: str
    eyes: int
    diet: DietCodes
    legs: int
    arms: int

    @property
    def limbs(self):
        return self.legs + self.arms


class Creature(BaseCreature):
    def __init__(self, name: str, eyes: int, diet: DietCodes, legs: int, arms: int):
        super().__init__(name=name, eyes=eyes, diet=diet, legs=legs, arms=arms)


class HolyCreature(BaseCreature):
    @holy_creation
    def __init__(self, name: str, eyes: int, diet: DietCodes, legs: int, arms: int):
        super().__init__(name=name, eyes=eyes, diet=diet, legs=legs, arms=arms)


class Plant:
    def __init__(self, leaves):
        self.leaves = leaves
