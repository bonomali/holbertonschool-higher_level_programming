#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if len(argv) is 1:
        print("0 arguments.")
    if len(argv) is 2:
        print("1 argument:\n1: {}".format(argv[1]))
    if len(argv) > 2:
        print("{} arguments:".format(len(argv) - 1))
        for i in range(len(argv) - 1):
            print("{:d}: {:s}".format(i + 1, argv[i + 1]))
