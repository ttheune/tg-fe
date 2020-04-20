from random import randint


def roll_percent():
    return randint(1, 100)


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


class name_tables:
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
