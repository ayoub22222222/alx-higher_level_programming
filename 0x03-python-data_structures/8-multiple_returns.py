#!/usr/bin/python3
def multiple_returns(sentence):
    var = ()
    if len(sentence) == 0:
	var = 0, "None"
    counter = 0
    else:
        for _ in sentence:
            counter += 1
    return counter, sentence[0]
