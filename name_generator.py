#!/usr/bin/env python3

import argparse
from utilities import get_results
from utilities import roll_percent as roll
from utilities import tables

"""
This program will generate a random name based on the rules as described in
The Game: Fantasy Edition
The tables from the book are converted to dictionaries and then iterated over to produce a name
As stated from the book:
It is necessary to remember that in what appears to be an unpronouncable name there could be
such things as silent letters and "'".  Re-roll if name is not liked.
"""


# generate a name (hopefully)
def main():
    global verbose
    args = get_args()
    verbose = args.rolls
    name = []
    if args.syllables:
        syll_num = args.syllables
    else:
        syll_num = get_results(tables._syllable_number, roll(), verbose)
    sylls = []
    for num in range(syll_num):
        sylls.append(get_results(tables._syllables, roll(), verbose))
    for syll in sylls:
        name.append(make_syllable(syll))
    print('Name: ' + ''.join(name).title())
    print('Syllables: ' + '-'.join(name))


# Apply consonants and vowels as determined by the syllable decsription
def make_syllable(syllable):
    letters = []
    for letter in [char for char in syllable]:
        if letter == 'c':
            letters.append(get_results(tables._consonants, roll(), verbose))
        if letter == 'v':
            letters.append(get_results(tables._vowels, roll(), verbose))
    return ''.join(letters)


def get_args():
    parser = argparse.ArgumentParser(description='Generate a name based on TG:FE rules')
    parser.add_argument('-s', '--syllables', default=False, type=int, help='Choose number of syllables, default is random')
    parser.add_argument('-r', '--rolls', default=False, action='store_true', help='Show rolls')
    return parser.parse_args()


if __name__ == '__main__':
    main()
