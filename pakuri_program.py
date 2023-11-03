from pakudex import Pakudex

if __name__ == "__main__":
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    capacity = int(input("Enter max capacity of the Pakudex: "))
    print(f"The Pakudex can hold {capacity} species of Pakuri")
    my_pakudex = Pakudex(capacity)

    while True:
        print("\nPakudex Main Menu")
        print("-----------------")
        print("1. List Pakuri")
        print("2. Show Pakuri")
        print("3. Add Pakuri")
        print("4. Evolve Pakuri")
        print("5. Sort Pakuri")
        print("6. Exit")

        user_input = int(input("\nWhat would you like to do? "))

        if user_input == 1:
            if my_pakudex.get_species_array() is None:
                print("No Pakuri in Pakudex yet!")
            else:
                print("Pakuri In Pakudex:")
                for i in range(len(my_pakudex.get_species_array())):
                    print(f"{i+1}: {my_pakudex.dex[i].name}")

        elif user_input == 2:
            pakuri = input("Enter the name of the species to display: ")
            success = False
            stats = []
            for species in my_pakudex.dex:
                if species.name == pakuri:
                    success, stats = my_pakudex.get_stats(species)
            if success:
                print(f"\nSpecies: {pakuri}")
                print(f"Attack: {stats[0]}")
                print(f"Defense: {stats[1]}")
                print(f"Speed: {stats[2]}")
            else:
                print("Error: No such Pakuri!")

        elif user_input == 3:
            pakuri = input("Enter the name of the species to add: ")
            duplicate = False
            for species in my_pakudex.dex:
                if species.name == pakuri:
                    duplicate = True
            if my_pakudex.get_size() == my_pakudex.capacity:
                print("Error: Pakudex is full!")
            elif not duplicate:
                my_pakudex.add_pakuri(pakuri)
                print(f"Pakuri species {pakuri} successfully added!\n")
            elif duplicate:
                print("Error: Pakudex already contains this species!")

        elif user_input == 4:
            exists = False
            pakuri = input("Enter the name of the species to evolve: ")
            for species in my_pakudex.dex:
                if species.name == pakuri:
                    my_pakudex.evolve_species(species)
                    exists = True
            if not exists:
                print("Error: No such Pakuri!")
        elif user_input == 5:
            my_pakudex.sort_pakuri()
            print("Pakuri have been sorted!")
        elif user_input == 6:
            print("Thank for using Pakudex! Bye!")
            exit()
        else:
            print("Invalid input!")