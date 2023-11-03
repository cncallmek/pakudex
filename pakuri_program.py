from pakuri import Pakuri
from pakudex import Pakudex

if __name__ == "__main__":
    print("Welcome to Pakudex: Tracker Extraordinaire!")
    capacity = int(input("Enter max capacity of the Pakudex: "))
    print(f"The Pakudex can hold {capacity} species of Pakuri")
    my_pakudex = Pakudex(capacity)

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
        if my_pakudex.get_species_array() == None:
            print("No Pakuri in Pakudex yet!")
        else:
            print("Pakuri In Pakudex:")
            for i in range(len(my_pakudex.get_species_array())):
                print(f"{i}: {my_pakudex.get_species_array()[i]}")
    elif user_input == 2:
        print("Incomplete")
    elif user_input == 3:
        print("Incomplete")
    elif user_input == 4:
        print("Incomplete")
    elif user_input == 5:
        print("Incomplete")
    elif user_input == 6:
        print("Thank for using Pakudex! Bye!")
        exit()
    else:
        print("Invalid input!")