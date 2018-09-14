#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    a = 0
    for count, ag in enumerate((argv[1:]), 1):
        a += int(ag)
    print("{}".format(a))
