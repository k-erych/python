import shutil
import os
import pickle
from shutil import copyfile
def save():
    y = True
    while y == True:
        answer = input("Do you want to save to a new file or to old one? NEW/OLD/BACK ").upper()
        x = True
        if answer == "NEW":
            while x == True:
                file_name = input("Create the name of the file: (BACK) ")
                if file_name.upper() == "BACK":
                    x = False
                else:
                    if file_name[-4:] != ".pkl":
                        file_name += ".pkl"
                    try:
                        with open(file_name, "xb") as file:
                            pass
                        shutil.copyfile("dataforsave.pkl", file_name)
                        print("Data where successfully saved to the new file")
                        x = False
                        y = False
                    except FileExistsError:
                        print("File has been already exist")
                        while True:
                            answer = input(
                                "Do you want to rewrite this file or to create another one? (REWRITE/CREATE/BACK) ").upper()
                            if answer == "REWRITE":
                                os.remove(file_name)
                                shutil.copyfile("dataforsave.pkl", file_name)
                                print("Data where successfully rewrote and saved. ")
                                y = False
                                x = False
                                break
                            elif answer == "CREATE" or "BACK":
                                break
        elif answer == "OLD":
            a = True
            while a == True:
                file_name = input("Enter the name of the file: (BACK) " )
                if file_name.upper() == "BACK":
                    a = False
                else:
                    if file_name[-4:] != ".pkl":
                        file_name += ".pkl"
                    if os.path.isfile(file_name):
                        pass
                    else:
                        print("File was not found. Try again")
                        a = False
                    while True:
                        answer = input("Do you want to rewrite or to append the data? (REWRITE/APPEND/BACK) ").upper()
                        if answer == "REWRITE":
                            os.remove(file_name)
                            shutil.copyfile("dataforsave.pkl", file_name)
                            print("Data where successfully rewrote and saved.")
                            y = False
                            a = False
                            break
                        elif answer == "APPEND":
                            from classes import Alive, NotAlive, NoSecondNameNotAlive, NoSecondNameAlive
                            with open(file_name, "rb") as f:
                                old_people = pickle.load(f)
                            with open("dataforsave.pkl", "rb") as f:
                                new_people = pickle.load(f)
                            all_people = list()
                            for _ in old_people:
                                all_people.append(_)
                            for _ in new_people:
                                all_people.append(_)
                            with open(file_name, "wb") as f:
                                pickle.dump(all_people, f)
                            print("Data where successfully appended to the file")
                            a = False
                            y = False
                            break
                        elif answer == "BACK":
                            break
                        else:
                            print("Wrong answer. Try again")
        elif answer == "BACK":
            y = False
        else:
            print("Wrong answer. Try again")