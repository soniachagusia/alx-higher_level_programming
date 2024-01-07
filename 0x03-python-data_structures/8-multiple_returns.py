#!/usr/bin/python3
def multiple_returns(sentence):

    length = len(sentence)

    if sentence:
        first_letter = sentence[0]
    else:
        first_letter = None
    return (length, first_letter)
