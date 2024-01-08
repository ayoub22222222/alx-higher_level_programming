#!/usr/bin/python3
"""
this module is dividing a the number 
by all the element of a matrix and return a new one 
by rounding every single eleme of the matrix to two decimal
...
"""
def matrix_divided(matrix, div):
    """ this functin is divide a the element of a matrix
    by the a number
    args:
        param1: (list): the first parameter
        param2: (int): the secne parameter
    raise TypeError:
        raise error if 
    Return:
        divide al the element of a matrix and retrun
        a new matrix
    """
    type_error = "matrix must be a matrix (list of lists) of integers/floats"
    if type(div) not in (int, float):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    if type(matrix) is not list or len(matrix) == 0 or len(matrix[0]) == 0:
    	raise TypeError(type_error)

    for i in matrix:
    	if type(matrix) is not list:
    		raise TypeError(type_error)
        for j in i:
            if not isinstance(j, int):
                raise TypeError(type_error)

    len_of_matrix = len(matrix[0])
    for lists in matrix:
    	if type(lists) is not list:
    		raise TypeError(msg)
    	if len(lists) != samelen:
            raise TypeError("Each row of the matrix must have the sam")

    new_matrix = [[round(j / div, 2) for j in i] for i in matrix]
    return new_matrix
