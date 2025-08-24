import os
import pickle
from classes import Alive, NotAlive, NoSecondNameNotAlive, NoSecondNameAlive
people = list()
def import_data(people):
    x = True
    while x:
        while True:
            answer = input("Do you want to clean the list that you have made? (YES/NO/BACK) ").upper()
            if answer == "YES":
                people = list()
                break
            elif answer == "NO" or answer == "NOT":
                break
            elif answer == "BACK":
                x = False
                break
            else:
                print("Wrong answer. Try again")
        if x == False: break
        file_name = input("Enter the name of the file: ")
        if file_name[-4:] != ".pkl":
            file_name += ".pkl"
        if os.path.isfile(file_name):
            with open(file_name, "rb") as f:
                old_people = pickle.load(f)
        for person in old_people:
            people.append(person)
        print("Data were successfully imported")
        break
    return people




