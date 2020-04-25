#!/usr/bin/env python3

import argparse
from utilities import choose
from utilities import get_results
from math import ceil
from pprint import pprint
from utilities import roll_percent
from utilities import roll_score
from utilities import tables
from random import randint

"""
This program will create a character based on the rules as described in
The Game: Fantasy Edition
"""


# Generate Scores
def roll_scores(gender, race):
    for score in tables._req_scores.keys():
        multiplier = tables._race_multiplier[race][score]
        if isinstance(multiplier, str):
            tables._req_scores[score] = int(multiplier)
        else:
            if gender == 'female':
                tables._req_scores[score] = int(ceil(roll_score(3, alt=score, verbose=verbose) * multiplier))
            else:
                tables._req_scores[score] = int(ceil(roll_score(3, verbose=verbose) * multiplier))
    for score in tables._sense_scores.keys():
        tables._sense_scores[score] = roll_score(2, verbose=verbose)
    for score in tables._optional_scores.keys():
        if score == 'beauty':
            tables._optional_scores[score] = roll_score(3, verbose=verbose)
        else:
            tables._optional_scores[score] = roll_score(1, verbose=verbose)
    scores = {'req_scores': tables._req_scores,
              'sense_scores': tables._sense_scores,
              'optional_scores': tables._optional_scores}
    return scores


# Validate Class
def check_class(race, _class):
    limited = ['warrior-priest', 'warrior-wizard', 'martial artist', 'priest', 'special']
    while race != ('human' or 'half-human') and _class.lower() in limited:
        print('{} is not a valid class for {}'.format(_class.title(), race.title()))
        _class = choose(tables._class, 'Class', verbose)
    return _class


# Determine Class(es)
def get_class(race):
    _class = check_class(race, choose(tables._class, 'Class', verbose))
    if _class == 'special':
        _class = []
        for _ in range(randint(2, 5)):
            new_class = get_results(tables._class, roll_percent(), verbose)
            while new_class in character['class']:
                new_class = get_results(tables._class, roll_percent(), verbose)
            _class.append(new_class)
    return _class


# Verbose or not
def get_args():
    parser = argparse.ArgumentParser(description='Generate a Character based on TG:FE rules')
    parser.add_argument('-v', '--verbose', default=False, action='store_true', help='Show rolls')
    return parser.parse_args()


# Make a character
def main():
    global verbose
    args = get_args()
    verbose = args.verbose
    character = {}
    character['gender'] = choose(tables._gender, 'Sex', verbose)
    character['race'] = choose(tables._race, 'Race', verbose)
    if character['race'] == 'other':
        character['race'] = choose(tables._language, 'Extended Races', verbose)
    character['class'] = get_class(character['race'])
    character['scores'] = roll_scores(character['gender'], character['race'])
    character['age'] = get_results(tables._age, roll_percent(), verbose)
    pprint(character)


if __name__ == '__main__':
    main()
