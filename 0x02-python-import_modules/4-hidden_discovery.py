#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    liste_names = dir(hidden_4)
    for name in liste_names:
        if name[:2] != "__":
            print(name)
