#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return None
    elif idx > len(my_list):
        return None
    else:
        result = my_list[idx]
        print("Element at index {} is {}".format(idx, result))
