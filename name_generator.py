#!/usr/bin/env python3

from random import randint

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


def main():
    name = []
    syll_num = get_results(syllable_number, roll())
    sylls = []
    for num in range(syll_num):
        sylls.append(get_results(syllables, roll()))
    for syll in sylls:
        name.append(make_syllable(syll))
    print('-'.join(name))
    print(''.join(name))


def roll():
    return randint(1, 100)


def get_results(group, roll):
    item = [item for item, chance in group.items() if roll in range(chance[0], chance[1] + 1)]
    return item[0]


def make_syllable(syllable):
    letters = []
    for letter in [char for char in syllable]:
        if letter == 'c':
            letters.append(get_results(consonants, roll()))
        if letter == 'v':
            letters.append(get_results(vowels, roll()))
    return ''.join(letters)


if __name__ == '__main__':
    main()
