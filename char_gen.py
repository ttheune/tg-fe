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


# Generate Scores
def roll_scores(gender, verbose):
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
        if gender == 'female':
            req_scores[score] = roll_score(3, alt=score, verbose=verbose)
        req_scores[score] = roll_score(3, verbose=verbose)
    for score in sense_scores.keys():
        sense_scores[score] = roll_score(2, verbose=verbose)
    for score in optional_scores.keys():
        if score == 'beauty':
            optional_scores[score] = roll_score(3, verbose=verbose)
        else:
            optional_scores[score] = roll_score(1, verbose=verbose)
    scores = {'req_scores': req_scores, 'sense_scores': sense_scores, 'optional_scores': optional_scores}
    return scores


# Modify Scores
def main():
    verbose = False
    character = {}
    character['gender'] = choose(tables._gender, 'Sex', verbose)
    character['race'] = choose(tables._race, 'Race', verbose)
    character['class'] = choose(tables._class, 'Class', verbose)
    character['scores'] = roll_scores(character['gender'], verbose)
    pprint(character)


if __name__ == '__main__':
    main()
