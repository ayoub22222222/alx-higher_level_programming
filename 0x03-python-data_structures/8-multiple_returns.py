#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
	return 0
    counter = 0
    for _ in sentence:
        counter += 1
    return counter, sentence[0]
