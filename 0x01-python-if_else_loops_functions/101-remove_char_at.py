#!/usr/bin/python3
def remove_char_at(str, n):
    pop_str = ""
    str = list(str)
    for i, c in enumerate(str):
        if i != n:
            pop_str = pop_str + c
    return pop_str
