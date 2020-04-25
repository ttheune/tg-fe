from random import randint


# Simplest roller ever get a number between 1 and 100
def roll_percent():
    return randint(1, 100)


# Return a Score (generally 3d6 x number of times)
def roll_score(times, **kwargs):
    if kwargs.get('alt') == 'strength':
        rolls = [randint(1, 8) + randint(1, 6) for _ in range(times)]
    elif kwargs.get('alt') == 'endurance':
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

    _language = {'human': [1, 20], 'elf': [21, 35], 'dwarf': [36, 45], 'gnome': [46, 50], 'troll': [51, 55],
                 'goblin': [56, 60], 'centaur': [61, 63], 'giant': [64, 70], 'chimera': [71, 74], 'sprite': [75, 77],
                 'manticora': [78, 80], 'lizard man': [81, 83], 'ogre': [84, 90], 'wyvern': [91, 94],
                 'harpy': [95, 97], 'dragon': [98, 100]}

    _age = {'13': [1, 1], '14': [2, 3], '15': [4, 5], '16': [6, 8], '17': [9, 14],
            '18': [15, 20], '19': [21, 27], '20': [28, 34], '21': [35, 42], '22': [43, 50],
            '23': [51, 57], '24': [58, 64], '25': [65, 70], '26': [71, 76], '27': [77, 81],
            '28': [82, 86], '29': [87, 90], '30': [91, 94], '31': [95, 97], '32': [98, 99],
            '33': [100, 100]}

    _race_multiplier = {'centaur': {'strength': 3, 'knowledge': 1, 'judgement': 1, 'endurance': 3, 'deftness': 1, 'speed': 2, 'personality': 1.5},
                        'chimera': {'strength': 4, 'knowledge': 1.2, 'judgement': 1, 'endurance': 3, 'deftness': '3', 'speed': 1, 'personality': .75},
                        'dragon': {'strength': 25, 'knowledge': 5, 'judgement': 4, 'endurance': 50, 'deftness': '3', 'speed': .75, 'personality': 3},
                        'dwarf': {'strength': 2, 'knowledge': 1, 'judgement': 1, 'endurance': 2, 'deftness': 1, 'speed': .75, 'personality': .75},
                        'elf': {'strength': 1, 'knowledge': 1.5, 'judgement': 1.25, 'endurance': 1, 'deftness': 1, 'speed': 1.5, 'personality': 1},
                        'giant': {'strength': 5, 'knowledge': .5, 'judgement': .5, 'endurance': 5, 'deftness': 1, 'speed': 1, 'personality': 1},
                        'gnome': {'strength': 1.5, 'knowledge': 1, 'judgement': 1, 'endurance': 1.5, 'deftness': 1, 'speed': .75, 'personality': .75},
                        'goblin': {'strength': 2.5, 'knowledge': 1, 'judgement': 1, 'endurance': 1.5, 'deftness': 1, 'speed': 1, 'personality': .75},
                        'harpy': {'strength': 1.5, 'knowledge': .66, 'judgement': .5, 'endurance': 1.5, 'deftness': '3', 'speed': .75, 'personality': .25},
                        'human': {'strength': 1, 'knowledge': 1, 'judgement': 1, 'endurance': 1, 'deftness': 1, 'speed': 1, 'personality': 1},
                        'lizard man': {'strength': 2, 'knowledge': 1, 'judgement': 1, 'endurance': 2, 'deftness': 1, 'speed': 1, 'personality': .8},
                        'manticora': {'strength': 3, 'knowledge': 2, 'judgement': 1.5, 'endurance': 3, 'deftness': '3', 'speed': 1, 'personality': .5},
                        'ogre': {'strength': 3, 'knowledge': 1, 'judgement': 1, 'endurance': 2, 'deftness': .75, 'speed': 1, 'personality': .75},
                        'sprite': {'strength': .25, 'knowledge': 1, 'judgement': 1, 'endurance': .25, 'deftness': 1, 'speed': 2, 'personality': 2},
                        'troll': {'strength': 3.5, 'knowledge': 1, 'judgement': 1, 'endurance': 3, 'deftness': .75, 'speed': 1, 'personality': .75},
                        'wyvern': {'strength': 3, 'knowledge': 3, 'judgement': 2, 'endurance': 5, 'deftness': '3', 'speed': .75, 'personality': .5}}

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

    _req_scores = {'strength': '',
                   'knowledge': '',
                   'judgement': '',
                   'endurance': '',
                   'deftness': '',
                   'speed': '',
                   'personality': ''}
    _sense_scores = {'sight': '',
                     'hearing': '',
                     'smell': '',
                     'taste': '',
                     'touch': '',
                     'prescience': ''}
    _optional_scores = {'beauty': '',
                        'bravery': '',
                        'ego': '',
                        'curiousity': '',
                        'temper': '',
                        'swearing': '',
                        'humor': '',
                        'stubonrness': '',
                        'patience': ''}
