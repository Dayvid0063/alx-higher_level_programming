#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    n = len(sys.argv)
    if n == 1:
        print("0 arguments.")
    else:
        print("{:d} argument".format(n - 1), end="")
        if n > 2:
            print("s", end="")
        print(":")
        for i in range(1, n):
            print("{:d}: {:s}".format(i, sys.argv[i]))
