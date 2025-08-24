from classes import Alive, NotAlive, NoSecondNameNotAlive, NoSecondNameAlive
def search(people):
    key = input("Enter the letters by what you are going to find the person: (BACK) ").upper()
    if key == "BACK":
        pass
    else:
        found = [person for person in people if key in str(person.name).upper() or key in str(person.surname).upper()
               or key in str(person.second_name).upper()]
        if len(found) == 0:
            print("No coincidence.")
        else:
            for person in found: print(str(person))
