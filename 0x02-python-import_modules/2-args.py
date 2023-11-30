#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    len = len(sys.argv)
    if len == 1:
        print("0 arguments.")
    else:
        if len == 2:
            print("1 argument:")
        else:
            print("{} arguments:".format(len - 1))
        for num, arg in enumerate(sys.argv):
            if num >= 1:
                print("{}: {}".format(num, arg))
