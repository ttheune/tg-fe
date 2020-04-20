#!/usr/bin/env python3

import argparse
from random import randint
from utilities import name_tables
from utilities import roll_percent as roll

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
    global rolls
    args = get_args()
    rolls = args.rolls
    name = []
    if args.syllables:
        syll_num = args.syllables
    else:
        syll_num = get_results(name_tables.syllable_number, roll())
    sylls = []
    for num in range(syll_num):
        sylls.append(get_results(name_tables.syllables, roll()))
    for syll in sylls:
        name.append(make_syllable(syll))
    print('-'.join(name))
    print(''.join(name))


# Return the result from a given table
def get_results(group, roll):
    item = [item for item, chance in group.items() if roll in range(chance[0], chance[1] + 1)]
    if rolls:
        print('{:02d}: {}'.format(roll, item[0]))
    return item[0]


# Apply consonants and vowels as determined by the syllable decsription
def make_syllable(syllable):
    letters = []
    for letter in [char for char in syllable]:
        if letter == 'c':
            letters.append(get_results(name_tables.consonants, roll()))
        if letter == 'v':
            letters.append(get_results(name_tables.vowels, roll()))
    return ''.join(letters)


def get_args():
    parser = argparse.ArgumentParser(description='Generate a name based on TG:FE rules')
    parser.add_argument('-s', '--syllables', default=False, type=int, help='Choose number of syllables, default is random')
    parser.add_argument('-r', '--rolls', default=False, action='store_true', help='Show rolls')
    return parser.parse_args()


if __name__ == '__main__':
    main()
