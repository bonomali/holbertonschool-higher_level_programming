#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list"""
    i = 0
    if my_list:
        for j in range(x):
            try:
                print("{}".format(my_list[i]), end="")
            except IndexError:
                break
            i += 1
        print()
    return i
