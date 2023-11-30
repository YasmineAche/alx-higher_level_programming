#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sum = 0
    for num, arg in enumerate(sys.argv):
        if num >= 1:
            sum += int(arg)
    print(sum)
