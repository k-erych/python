set_1 = {0}
set_2 = {0}
def common_elements():
    for i in range(3, 100, 3):
        set_1.add(i)
    for a in range(5, 100, 5):
        set_2.add(a)
    print(set_1.intersection(set_2))
common_elements()