#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    liste_names = dir(hidden_4)
    liste = sorted(liste_names)
    for l in liste:
        if not l.startswith("__"):
            print(l)
