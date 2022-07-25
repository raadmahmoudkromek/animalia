from enum import Enum


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
