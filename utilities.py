from random import randint


# Simplest roller ever get a number between 1 and 100
def roll_percent():
    return randint(1, 100)


# Return a Score (generally 3d6 x number of times)
def roll_score(times, **kwargs):
    if kwargs.get('alt') == 'str':
        rolls = [randint(1, 8) + randint(1, 6) for _ in range(times)]
    elif kwargs.get('alt') == 'end':
        rolls = [randint(1, 4) + randint(1, 4) + randint(1, 4) + randint(1, 4) for _ in range(times)]
    else:
        rolls = [randint(1, 6) + randint(1, 6) + randint(1, 6) for _ in range(times)]
    if kwargs.get('verbose'):
        print(rolls)
    return sorted(rolls, reverse=True)[0]


# Return the result from a given table
def get_results(group, roll, verbose):
    item = [item for item, chance in group.items() if roll in range(chance[0], chance[1] + 1)]
    if verbose:
        print('{:02d}: {}'.format(roll, item[0]))
    return item[0]


# Choose from list or Roll
def choose(table, table_name, verbose):
    choice = input('Roll or choose your {}: '.format(table_name))
    to_roll = ['', 'r', 'ro', 'rol', 'roll']
    choices = list(table.keys())
    while True:
        if choice.lower() in table.keys():
            return choice
        if choice.lower() in to_roll:
            return get_results(table, roll_percent(), verbose)
        choice = input('Invalid option.  Roll or choose from:\n{}\n'.format(' '.join(list(table.keys())).title()))


# Game tables
class tables:
    _gender = {'male': [1, 50],
               'female': [51, 100]}

    _race = {'human': [1, 50],
             'elf': [51, 75],
             'half-human': [76, 85],
             'dwarf': [86, 95],
             'other': [96, 100]}

    _class = {'warrior': [1, 50],
              'wizard': [51, 60],
              'thief': [61, 70],
              'healer': [71, 80],
              'warrior-priest': [81, 85],
              'warrior-wizard': [86, 90],
              'martial artist': [91, 97],
              'priest': [98, 99],
              'special': [100, 100]}

    _vowels = {'a': [1, 17],
               'e': [18, 41],
               'i': [42, 58],
               'o': [59, 79],
               'u': [80, 92],
               'y': [93, 100]}

    _consonants = {'b': [1, 5], 'c': [6, 10], 'd': [11, 15],
                   'f': [16, 20], 'g': [21, 25], 'h': [26, 30],
                   'j': [31, 35], 'k': [36, 40], 'l': [41, 45],
                   'm': [46, 50], 'n': [51, 55], 'p': [56, 60],
                   'q': [100, 100], 'r': [61, 70], 's': [71, 77],
                   't': [78, 84], 'v': [85, 87], 'w': [88, 93],
                   'x': [94, 95], 'z': [96, 99]}

    _syllables = {'vc': [1, 30],
                  'vcc': [31, 50],
                  'cv': [51, 80],
                  'cvv': [81, 90],
                  'cvc': [91, 99],
                  'cvvc': [100, 100]}

    _syllable_number = {1: [1, 30], 2: [31, 75], 3: [76, 93], 4: [94, 97], 5: [98, 100]}
