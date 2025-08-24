from datetime import datetime
from itertools import count
today = "15/08/2025"

class People:

    def __init__(self, name, surname, second_name, date_of_birth, sex):
        self.name = str(name).title()
        self.surname = str(surname).title()
        self.second_name = str(second_name).title()
        self.date_of_birth = date_of_birth
        self.sex = str(sex).title()

    def count_age(self, last_date):
        birthday = datetime.strptime(self.date_of_birth, "%d/%m/%Y")
        last_day = datetime.strptime(last_date, "%d/%m/%Y")
        age = last_day.year - birthday.year
        if (last_day.month, last_day.day) < (birthday.month, birthday.day):
            age -= 1
        return age



class Alive(People):
    def __init__(self, name, surname, second_name, date_of_birth, sex):
        super().__init__(name, surname, second_name, date_of_birth, sex)
    def __str__(self):
        return f"{self.name} {self.second_name} {self.surname}, {self.count_age(today)} years old, {self.sex}. Born on: {self.date_of_birth}."

    
class NotAlive(People):
    def __init__(self, name, surname, second_name, date_of_birth, date_of_death, sex):
        super().__init__(name, surname, second_name, date_of_birth, sex)
        self.date_of_death = date_of_death
    def __str__(self):
        return f"{self.name} {self.second_name} {self.surname}, {self.count_age(self.date_of_death)} years old, {self.sex}. Born on: {self.date_of_birth}. Died on: {self.date_of_death}."

class NoSecondNameAlive(Alive):
    def __init__(self, name, surname, second_name, date_of_birth, sex):
        super().__init__(name, surname, second_name, date_of_birth, sex)
    def __str__(self):
        return f"{self.name} {self.surname}, {self.count_age(today)} years old, {self.sex}. Born on: {self.date_of_birth}."

class NoSecondNameNotAlive(NotAlive):
    def __init__(self, name, surname, second_name, date_of_birth, date_of_death, sex):
        super().__init__(name, surname, second_name, date_of_birth, date_of_death, sex)
    def __str__(self):
        return f"{self.name} {self.surname}, {self.count_age(self.date_of_death)} years old, {self.sex}. Born on: {self.date_of_birth}.  Died on: {self.date_of_death}."


