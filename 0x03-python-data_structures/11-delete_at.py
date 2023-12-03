#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
	return my_list
    elif idx >= 0 and idx < len(my_list):
        new_list = []
	for i in my_list:
	    if i != my_list[idx]:
	        new_list.append(i)
        return new_list
