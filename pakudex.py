from pakuri import Pakuri


class Pakudex:

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

    @staticmethod
    def get_stats(species):
        stat_list = [species.attack, species.defense, species.speed]
        return True, stat_list

    def sort_pakuri(self):
        self.dex.append(Pakuri)

    def add_pakuri(self, species):
        new_species = Pakuri(species)
        self.dex.append(new_species)
        self.count += 1

    @staticmethod
    def evolve_species(species):
        species.evolve()
