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
            string_list = []
            for species in self.dex:
                string_list.append(species.name)
            return string_list

    def get_stats(self, species):
        for pakuri in self.dex:
            if pakuri.name == species:
                stat_list = [pakuri.attack, pakuri.defense, pakuri.speed]
                return stat_list

    def sort_pakuri(self):
        self.dex = sorted(self.dex, key=lambda x: x.name)

    def add_pakuri(self, species):
        self.dex.append(Pakuri(species))
        self.count += 1

    def evolve_species(self, species):
        for pakuri in self.dex:
            if pakuri.name == species:
                pakuri.evolve()
                return True
        return False
