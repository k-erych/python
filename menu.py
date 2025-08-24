from classes import Alive, NotAlive, NoSecondNameNotAlive, NoSecondNameAlive
def menu():
    people = list()
    while True:
        print("============================")
        print("Choose option: ")
        print("1. Import data from the file")
        print("2. Print list of a people")
        print("3. Add person by yourself")
        print("4. Do a search")
        print("5. Delete person")
        print("6. Save data to the file")
        print("9. Exit")
        print("============================")
        answer = str(input())
        if answer[0].isdigit():
            if len(answer) != 1:
                if len(answer) == 2:
                    if not answer[1].isdigit():
                        answer = answer[0]
                    else:
                        print("You have chosen wrong symbol. Try again")
                        continue
                else:
                    print("You have chosen wrong symbol. Try again")
                    continue
            if answer == "1":
                from importdata import import_data
                people = import_data(people)
            elif answer == "2":
                for person in people:
                    print(str(person))
            elif answer == "3":
                from addperson import add_person
                add_person(people)
            elif answer == "4":
                from search import search
                search(people)
            elif answer == "5":
                from delete import delete
                delete(people)
            elif answer == "6":
                from save import save
                save()
            elif answer == "9":
                with open("saves.txt", "w") as f:
                    f.write("")
                    f.close()
                break
            else:
                print("You have chosen wrong symbol. Try again")
                continue
            x = 0
            if x == 0:
                continue
            else:
                break

        else:
            print("You have chosen wrong symbol. Try again")
            continue
menu()