#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    elif idx == 0 or idx == len(my_list):
        result = my_list[idx]
        return result
