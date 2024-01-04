#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    numargs = len(sys.argv)
    sum = 0

    for arg in range(1, numargs):
        num = int(sys.argv[arg])
        sum = sum + num
    print(sum)
