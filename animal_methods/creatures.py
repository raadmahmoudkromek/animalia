from enum import Enum, unique


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


class Creature:
    def __init__(self, name: str, eyes: int, diet: DietCodes, legs: int, arms: int, holy: bool = False):
        if holy:
            self.holy_create(name=name, eyes=eyes, diet=diet, legs=legs, arms=arms)
        else:
            self.create(name=name, eyes=eyes, diet=diet, legs=legs, arms=arms)

    def create(self, name, eyes, diet, legs, arms):
        self.apply_properties(name=name, eyes=eyes, diet=diet, legs=legs, arms=arms)

    @holy_creation
    def holy_create(self, name, eyes, diet, legs, arms):
        self.apply_properties(name=name, eyes=eyes, diet=diet, legs=legs, arms=arms)

    def apply_properties(self, name, eyes, diet, legs, arms):
        self.name = name
        self.eyes = eyes
        self.diet = diet
        self.legs = legs
        self.arms = arms

    @property
    def limbs(self):
        return self.legs + self.arms


class Plant:
    def __init__(self, leaves):
        self.leaves = leaves
