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
def roll_scores(gender, race, verbose):
    req_scores = {'strength': '',
                  'knowledge': '',
                  'judgement': '',
                  'endurance': '',
                  'deftness': '',
                  'speed': '',
                  'personality': ''}
    sense_scores = {'sight': '',
                    'hearing': '',
                    'smell': '',
                    'taste': '',
                    'touch': '',
                    'prescience': ''}
    optional_scores = {'beauty': '',
                       'bravery': '',
                       'ego': '',
                       'curiousity': '',
                       'temper': '',
                       'swearing': '',
                       'humor': '',
                       'stubonrness': '',
                       'patience': ''}
    for score in req_scores.keys():
        multiplier = tables._race_multiplier[race][score]
        if isinstance(multiplier, str):
            req_scores[score] = int(multiplier)
        else:
            if gender == 'female':
                req_scores[score] = int(ceil(roll_score(3, alt=score, verbose=verbose) * multiplier))
            else:
                req_scores[score] = int(ceil(roll_score(3, verbose=verbose) * multiplier))
    for score in sense_scores.keys():
        sense_scores[score] = roll_score(2, verbose=verbose)
    for score in optional_scores.keys():
        if score == 'beauty':
            optional_scores[score] = roll_score(3, verbose=verbose)
        else:
            optional_scores[score] = roll_score(1, verbose=verbose)
    scores = {'req_scores': req_scores, 'sense_scores': sense_scores, 'optional_scores': optional_scores}
    return scores


# Validate Class
def check_class(race, _class):
    limited = ['warrior-priest', 'warrior-wizard', 'martial artist', 'priest', 'special']
    while race != ('human' or 'half-human') and _class.lower() in limited:
        print('{} is not a valid class for {}'.format(_class.title(), race.title()))
        _class = choose(tables._class, 'Class', verbose)
    return _class


# Determine Class(es)
def get_class(race, verbose):
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


def main():
    args = get_args()
    verbose = args.verbose
    character = {}
    character['gender'] = choose(tables._gender, 'Sex', verbose)
    character['race'] = choose(tables._race, 'Race', verbose)
    if character['race'] == 'other':
        character['race'] = choose(tables._language, 'Extended Races', verbose)
    character['class'] = get_class(character['race'], verbose)
    character['scores'] = roll_scores(character['gender'], character['race'], verbose)
    character['age'] = get_results(tables._age, roll_percent(), verbose)
    pprint(character)


if __name__ == '__main__':
    main()
