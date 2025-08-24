from classes import Alive,NotAlive,NoSecondNameNotAlive,NoSecondNameAlive, People
def delete(people):
    x = 0
    while x == 0:
        key = input("Enter the key word by what you want to delete the person: (BACK) ").upper()
        if key == "BACK":
            break
        else:
            found = dict()
            i = 1
            for person in people:
                if key in str(person.name).upper() or key in str(person.surname).upper() or key in str(
                        person.second_name).upper():
                    found[i] = person
                    i += 1
            if len(found) == 0:
                print("No coincidence.")
            else:
                for key, value in found.items():
                    print("Choose person that you want delete: (BACK)")
                    print(f"{key}. {str(value)}")
                answer = ""
                y = 0
                while y == 0:
                    answer = input("Your choose: ")
                    if answer.upper() == "BACK":
                        break
                    if answer[0].isdigit():
                        if len(answer) != 1:
                            if len(answer) == 2:
                                if not answer[1].isdigit():
                                    answer = answer[0]
                                    break
                                else:
                                    print("You have chosen wrong symbol. Try again")
                                    continue
                            else:
                                print("You have chosen wrong symbol. Try again")
                                continue
                        else:
                            break
                    while True:
                        if key in found:
                            removed = found.pop(key)
                            people.remove(removed)
                            del removed
                            answer = input(
                                "Operation is successful. Do you want to make another removal? (YES/NO) ").upper()
                            if answer == "YES":
                                break
                            elif answer == "NO" or "NOT":
                                x += 1
                                y += 1
                                break
                            else:
                                print("Wrong answer. Try again")




