import unittest
from creatures import Creature, DietCodes


class TestCreatures(unittest.TestCase):
    def testCreate(self, eyes=2, arms=0, legs=4, diet=DietCodes.OMNIVORE):
        dog = Creature(eyes=eyes, arms=arms, legs=legs, diet=diet)
        self.assertEqual(dog.limbs, arms+legs)


if __name__ == '__main__':
    unittest.main()
