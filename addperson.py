import pickle
import string
from classes import People, Alive, NotAlive, NoSecondNameNotAlive, NoSecondNameAlive
from datetime import datetime
from datetime import date
def add_person(people):
    xyz = True
    while xyz == True:
        def wrong_symbol_in_name(name):
            interference = string.punctuation.replace("-", "")
            x = True
            y = str
            while x == True:
                y = str(input(f"Enter the {name} of the person: ")).title()
                for i in y:
                    if str(i).isdigit():
                        print("This sentence can`t have any numbers. Try again")
                        break
                    elif i in interference:
                        print("This sentence can`t have any punctuation marks except `-`. Try again")
                        break
                    else:
                        x = False
            return y

        def date(date):
            big_year_list = list()
            y = -4
            while y != 2024:
                y += 4
                big_year_list.append(y)
            d = str
            while True:
                try:
                    d = input(f"Enter the date of the {date} of the person: ")
                    for i in string.punctuation:
                        d = d.replace(i, "/")
                    data = datetime.strptime(d, "%d/%m/%Y")
                    break
                except ValueError:
                    print("Wrong date. Try again")
            return d

        def check_right_age(birth, last):
            x = True
            birth = datetime.strptime(birth, "%d/%m/%Y")
            last = datetime.strptime(last, "%d/%m/%Y")
            if birth.year > last.year:
                x = False
            elif birth.year == last.year:
                if birth.month > last.month:
                    x = False
                elif birth.month == last.month:
                    if birth.day > last.day:
                        x = False
            return x
        name = wrong_symbol_in_name("name")
        surname = wrong_symbol_in_name("surname")
        print("If person dose not have second name print `skip`")
        second_name = wrong_symbol_in_name("second name")
        if second_name == "Skip":
            second_name = ""
        date_of_birth = ""
        today = datetime.today().date().strftime("d%/m%/Y%")
        last_day = today
        while True:
            date_of_birth = date("birthday")
            answer = input("Is it needed to add the day of the death of the person? (YES/NO) ").upper()
            if answer == "YES":
                last_day = date("death")
                if check_right_age(date_of_birth, last_day) == False:
                    print("Wrong date. Try again")
                    continue
                else:
                    break
            elif answer == "NO" or answer == "NOT":
                break
            else:
                print("Wrong answer. Try again")
        sex = str
        while True:
            sex = input("Enter the sex of the person: ").title()
            if sex in ("W", "Female", "F", "Woman"):
                sex = "Female"
                break
            elif sex in ("Male", "M", "Man"):
                sex = "Male"
                break
            else: print("Wrong sex. Try again")

        last_day_alive = datetime.strptime(last_day, "%d/%m/%Y")

        if second_name != "":
            if last_day_alive.year == 2025 and last_day_alive.month == 8 and last_day_alive.day == 20:
                person = Alive(name, surname, second_name, date_of_birth, sex)
            else:
                person = NotAlive(name, surname, second_name, date_of_birth, last_day, sex)
        else:
            if last_day_alive.year == 2025 and last_day_alive.month == 8 and last_day_alive.day == 20:
                person = NoSecondNameAlive(name, surname, second_name, date_of_birth, sex)
            else:
                person = NoSecondNameNotAlive(name, surname, second_name, date_of_birth, last_day, sex)
        people.append(person)

        with open("dataforsave.pkl", "wb") as f: pickle.dump(people, f)
        print("Person was successfully added.")
        xyz = False