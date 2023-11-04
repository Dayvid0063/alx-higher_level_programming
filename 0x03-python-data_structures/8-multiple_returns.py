#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        sentence = None
        if sentence:
            size = len(sentence)
        else:
            size = 0
        return size, sentence if not sentence else sentence[:1]
