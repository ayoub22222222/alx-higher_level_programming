#!/usr/bin/python3
def multiple_returns(sentence):
    var = ()
    if len(sentence) == 0:
	var = 0, "None"
    else:
        var =  len(sentence), sentence[0]
    return var
