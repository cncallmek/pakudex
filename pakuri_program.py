from pakudex import Pakudex

if __name__ == "__main__":
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    capacity = None
    while type(capacity) != int:
        try:
            capacity = int(input("Enter max capacity of the Pakudex: "))
            if capacity < 0:
                capacity = ('')
                raise TypeError
        except:
            print("Please enter a valid size.")
    print(f"The Pakudex can hold {capacity} species of Pakuri.")
    my_pakudex = Pakudex(capacity)

    while True:
        user_input = None
        while not type(user_input) == int:
            try:
                print("\nPakudex Main Menu")
                print("-----------------")
                print("1. List Pakuri")
                print("2. Show Pakuri")
                print("3. Add Pakuri")
                print("4. Evolve Pakuri")
                print("5. Sort Pakuri")
                print("6. Exit")
                user_input = input("\nWhat would you like to do? ")
                if 0 > int(user_input):
                    raise TypeError
                else:
                    user_input = int(user_input)
            except:
                print("Unrecognized menu selection!")

        if user_input == 1:
            if my_pakudex.get_species_array() is None:
                print("No Pakuri in Pakudex yet!")
            else:
                print("Pakuri In Pakudex:")
                for i in range(len(my_pakudex.get_species_array())):
                    print(f"{i+1}. {my_pakudex.dex[i].name}")

        elif user_input == 2:
            pakuri = input("Enter the name of the species to display: ")
            try:
                stats = my_pakudex.get_stats(pakuri)
                if stats is not None:
                    print(f"\nSpecies: {pakuri}")
                    print(f"Attack: {stats[0]}")
                    print(f"Defense: {stats[1]}")
                    print(f"Speed: {stats[2]}")
                else:
                    raise TypeError
            except:
                print("Error: No such Pakuri!")

        elif user_input == 3:
            try:
                if my_pakudex.get_size() == my_pakudex.capacity:
                    raise TypeError
                pakuri = input("Enter the name of the species to add: ")
                success = my_pakudex.add_pakuri(pakuri)
                if success:
                    print(f"Pakuri species {pakuri} successfully added!")
                else:
                    raise AttributeError
            except TypeError:
                print("Error: Pakudex is full!")
            except AttributeError:
                print("Error: Pakudex already contains this species!")

        elif user_input == 4:
            pakuri = input("Enter the name of the species to evolve: ")
            success = my_pakudex.evolve_species(pakuri)
            if success:
                print(f"{pakuri} has evolved!")
            else:
                print("Error: No such Pakuri!")
        elif user_input == 5:
            my_pakudex.sort_pakuri()
            print("Pakuri have been sorted!")
        elif user_input == 6:
            print("Thanks for using Pakudex! Bye!")
            exit()
        else:
            print("Unrecognized menu selection!")
