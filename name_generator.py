#!/usr/bin/env python3

import argparse
from random import randint

"""
This program will generate a random name based on the rules as described in
The Game: Fantasy Edition
The tables from the book are converted to dictionaries and then iterated over to produce a name
As stated from the book:
It is necessary to remember that in what appears to be an unpronouncable name there could be
such things as silent letters and "'".  Re-roll if name is not liked.
"""

vowels = {'a': [1, 17],
          'e': [18, 41],
          'i': [42, 58],
          'o': [59, 79],
          'u': [80, 92],
          'y': [93, 100]}

consonants = {'b': [1, 5], 'c': [6, 10], 'd': [11, 15],
              'f': [16, 20], 'g': [21, 25], 'h': [26, 30],
              'j': [31, 35], 'k': [36, 40], 'l': [41, 45],
              'm': [46, 50], 'n': [51, 55], 'p': [56, 60],
              'q': [100, 100], 'r': [61, 70], 's': [71, 77],
              't': [78, 84], 'v': [85, 87], 'w': [88, 93],
              'x': [94, 95], 'z': [96, 99]}

syllables = {'vc': [1, 30],
             'vcc': [31, 50],
             'cv': [51, 80],
             'cvv': [81, 90],
             'cvc': [91, 99],
             'cvvc': [100, 100]}


syllable_number = {1: [1, 30], 2: [31, 75], 3: [76, 93], 4: [94, 97], 5: [98, 100]}


# generate a name (hopefully)
def main():
    global rolls
    args = get_args()
    rolls = args.rolls
    name = []
    if args.syllables:
        syll_num = args.syllables
    else:
        syll_num = get_results(syllable_number, roll())
    sylls = []
    for num in range(syll_num):
        sylls.append(get_results(syllables, roll()))
    for syll in sylls:
        name.append(make_syllable(syll))
    print('-'.join(name))
    print(''.join(name))


# Simplest roller function ever
def roll():
    return randint(1, 100)


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
            letters.append(get_results(consonants, roll()))
        if letter == 'v':
            letters.append(get_results(vowels, roll()))
    return ''.join(letters)


def get_args():
    parser = argparse.ArgumentParser(description='Generate a name based on TG:FE rules')
    parser.add_argument('-s', '--syllables', default=False, type=int, help='Choose number of syllables, default is random')
    parser.add_argument('-r', '--rolls', default=False, action='store_true', help='Show rolls')
    return parser.parse_args()


if __name__ == '__main__':
    main()
