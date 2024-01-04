#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    numargs = len(sys.argv) - 1
    if numargs == 0:
        print("0 arguments.")

    elif numargs == 1:
        print("1 argument:")

    else:
        print(numargs, "arguments:")

    for idx in range(1, numargs + 1):
        print("{}: {}".format(idx, sys.argv[idx]))
