#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    u = len(sys.argv) - 1
    if u == 0:
        print("{} arguments.".format(u))
    elif u == 1:
        print("{} argument:".format(u))
    else:
        print("{} arguments:".format(u))
        if u >= 1:
            u = 0
            for arg in sys.argv:
                if u != 0:
                    print("{}: {}".format(u, arg))
                    u += 1
