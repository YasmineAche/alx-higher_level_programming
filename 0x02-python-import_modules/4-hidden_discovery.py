#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    liste = dir(hidden_4)
    for l in liste:
        if not l[:2] != "__":
            print(l)
