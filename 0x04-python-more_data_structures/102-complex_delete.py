#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_dic = a_dictionary.copy()
    if value not in a_dictionary.values():
        return a_dictionary
    else:
        for key, val in new_dic.items():
            if value == val:
                del a_dictionary[key]
        return a_dictionary
