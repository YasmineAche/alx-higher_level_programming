#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    for i in range(2):
        if len(tuple_a) < i + 1:
            tuple_a = tuple_a + (0,)
        if len(tuple_b) < i + 1:
            tuple_b = tuple_b + (0,)
    new_tuple = tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1]
    return new_tuple
