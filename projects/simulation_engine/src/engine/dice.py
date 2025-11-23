import random

class Dice:
    def __init__(self, count=1, seed=0, sides=6):
        self._count = count
        self._rng = random.Random(seed)
        self._sides = sides

    def roll(self):
        return [self._rng.randint(1, self._sides) for _ in range(self._count)]