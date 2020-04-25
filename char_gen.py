#!/usr/bin/env python3

import argparse
from utilities import choose
from utilities import get_results
from utilities import roll_score
from utilities import tables

"""
This program will create a character based on the rules as described in
The Game: Fantasy Edition
"""


# Generate Requisit Scores
def req_scores(gender, verbose):
    scores = {'str': '', 'kno': '', 'jud': '', 'end': '', 'def': '', 'spe': '', 'per': ''}
    for score in scores.keys():
        if gender == 'female':
            scores[score] = roll_score(3, alt=score, verbose=verbose)
        scores[score] = roll_score(3, verbose=verbose)
    return scores


def main():
    verbose = False
    character = {}
    character['gender'] = choose(tables._gender, 'Sex', verbose)
    character['race'] = choose(tables._race, 'Race', verbose)
    character['class'] = choose(tables._class, 'Class', verbose)
    character['req_scores'] = req_scores(character['gender'], verbose)
    print(character)


if __name__ == '__main__':
    main()
