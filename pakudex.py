from pakuri import Pakuri

class Pakudex(Pakuri):

    def __init__(self, capacity=20):
        self.count = 0
        self.capacity = capacity
        self.dex = []

    def get_size(self):
        return self.count

    def get_capacity(self):
        return self.capacity

    def get_species_array(self):
        if len(self.dex) == 0:
            return None
        else:
            return self.dex

    def get_stats(self, species):
        return None

    def sort_pakuri(self):
        self.dex.append(Pakuri)

    def add_pakuri(self, species):
        print()

    def evolve_species(self, species):
        species.evolve