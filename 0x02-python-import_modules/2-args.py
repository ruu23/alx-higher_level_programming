#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1

    if count == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(count, 's' if count != 1 else ''))
        for i in range(count):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
