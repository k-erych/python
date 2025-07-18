class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age}"

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        self.record_book = record_book
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age}, Залікова книга: {self.record_book}"

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
            for student in self.group:
                if student.last_name == last_name:
                    self.group.remove(student)
                    break

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        group = ""
        for student in self.group:
            group += str(student) + "\n"
        return f'Number:{self.number}\n{group} '

Student1 = Student("Male", 24, "Andriy", "Grats", "bla")
Student2 = Student("Female", 17, "Anna", "Kovalenko", "123")
my_group = Group("A1")
my_group.add_student(Student1)
my_group.add_student(Student2)


found = my_group.find_student("Grats")
print(my_group)
