#!/usr/bin/python3


def best_score(a_dictionary):
    if not a_dictionary:
        return
    best_score = max(a_dictionary,
                     key=a_dictionary.get)
    return best_score
