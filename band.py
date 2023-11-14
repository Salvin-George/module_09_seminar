"""Band class"""


class Band:
    def __init__(self, name=''):
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Adds musician to musicians"""
        return self.musicians.append(musician)

    def play(self):
        for musician in self.musicians:
            musician.play()
