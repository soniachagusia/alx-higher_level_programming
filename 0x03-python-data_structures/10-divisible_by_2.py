#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    store = []

    for digit in my_list:
        if digit % 2 == 0:
            store.append(True)
        else:
            store.append(False)
    return store
