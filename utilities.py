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
    """
    Generally speaking the tables here represent a list of options with a percentile chance of each option.
    Format of {'option': [low_end, high_end]} to be used in a range calculation of
    for x in range('option'[0], 'option'[1] + 1)
    """
    gender = {'male': [1, 50], 'female': [51, 100]}

    race = {'human': [1, 50],
            'elf': [51, 75],
            'half-human': [76, 85],
            'dwarf': [86, 95],
            'other': [96, 100]}

    # called it 'job' instead 'class' because of reserved words in python
    job = {'warrior': [1, 50],
           'wizard': [51, 60],
           'thief': [61, 70],
           'healer': [71, 80],
           'warrior-priest': [81, 85],
           'warrior-wizard': [86, 90],
           'martial artist': [91, 97],
           'priest': [98, 99],
           'special': [100, 100]}

    language = {'human': [1, 20], 'elf': [21, 35], 'dwarf': [36, 45], 'gnome': [46, 50], 'troll': [51, 55],
                'goblin': [56, 60], 'centaur': [61, 63], 'giant': [64, 70], 'chimera': [71, 74], 'sprite': [75, 77],
                'manticora': [78, 80], 'lizard man': [81, 83], 'ogre': [84, 90], 'wyvern': [91, 94],
                'harpy': [95, 97], 'dragon': [98, 100]}

    age = {'13': [1, 1], '14': [2, 3], '15': [4, 5], '16': [6, 8], '17': [9, 14],
           '18': [15, 20], '19': [21, 27], '20': [28, 34], '21': [35, 42], '22': [43, 50],
           '23': [51, 57], '24': [58, 64], '25': [65, 70], '26': [71, 76], '27': [77, 81],
           '28': [82, 86], '29': [87, 90], '30': [91, 94], '31': [95, 97], '32': [98, 99],
           '33': [100, 100]}

    race_multiplier = {'centaur': {'strength': 3, 'knowledge': 1, 'judgement': 1, 'endurance': 3, 'deftness': 1, 'speed': 2, 'personality': 1.5},
                       'chimera': {'strength': 4, 'knowledge': 1.2, 'judgement': 1, 'endurance': 3, 'deftness': '3', 'speed': 1, 'personality': .75},
                       'dragon': {'strength': 25, 'knowledge': 5, 'judgement': 4, 'endurance': 50, 'deftness': '3', 'speed': .75, 'personality': 3},
                       'dwarf': {'strength': 2, 'knowledge': 1, 'judgement': 1, 'endurance': 2, 'deftness': 1, 'speed': .75, 'personality': .75},
                       'elf': {'strength': 1, 'knowledge': 1.5, 'judgement': 1.25, 'endurance': 1, 'deftness': 1, 'speed': 1.5, 'personality': 1},
                       'giant': {'strength': 5, 'knowledge': .5, 'judgement': .5, 'endurance': 5, 'deftness': 1, 'speed': 1, 'personality': 1},
                       'gnome': {'strength': 1.5, 'knowledge': 1, 'judgement': 1, 'endurance': 1.5, 'deftness': 1, 'speed': .75, 'personality': .75},
                       'goblin': {'strength': 2.5, 'knowledge': 1, 'judgement': 1, 'endurance': 1.5, 'deftness': 1, 'speed': 1, 'personality': .75},
                       'harpy': {'strength': 1.5, 'knowledge': .66, 'judgement': .5, 'endurance': 1.5, 'deftness': '3', 'speed': .75, 'personality': .25},
                       'human': {'strength': 1, 'knowledge': 1, 'judgement': 1, 'endurance': 1, 'deftness': 1, 'speed': 1, 'personality': 1},
                       'half-human': {'strength': 1, 'knowledge': 1, 'judgement': 1, 'endurance': 1, 'deftness': 1, 'speed': 1, 'personality': 1},
                       'lizard man': {'strength': 2, 'knowledge': 1, 'judgement': 1, 'endurance': 2, 'deftness': 1, 'speed': 1, 'personality': .8},
                       'manticora': {'strength': 3, 'knowledge': 2, 'judgement': 1.5, 'endurance': 3, 'deftness': '3', 'speed': 1, 'personality': .5},
                       'ogre': {'strength': 3, 'knowledge': 1, 'judgement': 1, 'endurance': 2, 'deftness': .75, 'speed': 1, 'personality': .75},
                       'sprite': {'strength': .25, 'knowledge': 1, 'judgement': 1, 'endurance': .25, 'deftness': 1, 'speed': 2, 'personality': 2},
                       'troll': {'strength': 3.5, 'knowledge': 1, 'judgement': 1, 'endurance': 3, 'deftness': .75, 'speed': 1, 'personality': .75},
                       'wyvern': {'strength': 3, 'knowledge': 3, 'judgement': 2, 'endurance': 5, 'deftness': '3', 'speed': .75, 'personality': .5}}

    # {'number of classes': {[age range from, age range to, chance], [age range from, age range to, chance]}
    past_experience = {'0': [[13, 16, 0]],
                       '1': [[17, 20, 5], [21, 24, 10]],
                       '2': [[25, 28, 15], [29, 32, 20]],
                       '3': [[33, 33, 25]]}

    # Simply a list of possible previous classes
    past_jobs = ['mercenary', 'pirate', 'thief', 'bandit', 'assassin',
                 'spy', 'gladiator', 'priest', 'warrior-priest', 'healer',
                 'martial artist', 'warrior', 'warrior-wizard', 'druid', 'option']

    # These are for generating names
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

    # Score tables are used as a working dict and gets populated by char_gen.py
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

    # Social charts for parentage
    general_groupings = {'common': [1, 40], 'guild': [41, 55], 'merchant': [56, 75],
                         'military': [76, 90], 'gentle': [91, 97], 'noble': [98, 100]}
    # format of {'title': [[chance range], [level range]]}
    noble = {'page': [[1, 30], [1, 3]], 'knight': [[31, 50], [4, 6]], 'thane': [[51, 70], [7, 7]],
             'baron': [[71, 85], [8, 8]], 'minister': [[86, 92], [9, 9]],
             'prince/princess': [[93, 97], [10, 10]], 'king/queen': [[98, 100], [10, 10]]}

    gentle = {'constable': [[1, 45], [1, 3]], 'gentry': [[46, 65], [4, 4]], 'chevalier': [[66, 80], [5, 5]],
              'pretender': [[81, 90], [6, 6]], 'magistrate': [[91, 97], [6, 6]], 'lord mayor': [[98, 100], [6, 6]]}

    military = {'troop': [[1, 50], [1, 1]], 'guard': [[51, 62]], 'lieutenant': [[63, 72], [3, 3]],
                'captain': [[73, 81], [4, 4]], 'major': [[82, 87], [5, 5]], 'colonel': [[88, 92], [6, 6]],
                'general': [[93, 96], [7, 7]], 'army cmdr': [[97, 99], [8, 8]],
                'chief of staff': [[100, 100], [10, 10]]}

    # format of {'title': [[chance range], [level range], skill bonus]}
    merchant = {'huckster': [[1, 30], [1, 3], 10], 'trader': [[31, 49], [4, 6], 15], 'monger': [[50, 66], [7, 9], 20],
                'proprietor': [[67, 81], [10, 12], 25], 'agent': [[82, 91], [13, 15], 30],
                'magnate': [[92, 97], [16, 18], 35], 'high magnate': [[98, 100], [19, 21], 40]}

    guild = {'apprentice': [[1, 45], [1, 4], 15], 'journeyman': [[46, 65], [5, 8], 20],
             'craftsman': [[66, 80], [9, 12], 25], 'expert': [[81, 90], [13, 16], 30],
             'guildmaster': [[91, 97], [17, 20], 35], 'teacher': [[98, 100], [21, 21], 40]}

    common = {'citizen': [[1, 45], [7, 12], 30], 'freeman': [[46, 55], [1, 6], 20], 'serf': [[56, 80], [1, 12], 10],
              'slave': [[81, 90], [0, 0], 0], 'gypsy': [[91, 98], [0, 0], 0], 'adventurer': [[99, 100], [0, 0], 0]}

    # standar format
    merchant_class = {'food stuffs': [1, 6], 'alcoholic beverages': [7, 12], 'rope': [13, 18], 'feed and seed': [19, 24], 'weapons': [24, 28], 'livestock': [29, 31], 'leather goods': [32, 34], 'spices': [35, 37], 'building supplies': [38, 40], 'quarry/mines': [41, 43], 'timber/pitch': [44, 46], 'perfume/soap': [47, 49], 'magic weapons': [50, 50], 'clothing': [51, 56], 'small livestock': [57, 62], 'tools': [63, 68], 'armor': [69, 72], 'foundry': [73, 75], 'shipyard': [76, 78], 'hotelier': [79, 81], 'rugs': [82, 84], 'books/arts': [85, 87], 'gems/metal': [88, 90], 'showman': [91, 93], 'processed foodstuffs': [94, 96], 'magic items': [97, 97], 'shipping': [98, 99], 'other': [100, 100]}

    guild_class = {'accountant': [1, 2], 'alchemist': [3, 4], 'architect': [5, 6], 'armorer': [7, 8], 'artist': [9, 10], 'assassin': [11, 12], 'beggar': [13, 14], 'boatmaker': [15, 16], 'bootmaker': [17, 18], 'botanist': [19, 20], 'bowmaker': [21, 22], 'bricklayer': [23, 24], 'carpenter': [25, 28], 'carpetmaker': [29, 30], 'carver': [31, 32], 'engineer': [33, 34], 'executioner': [35, 36], 'fletcher': [37, 38], 'geologist': [39, 40], 'glassblower': [41, 42], 'goldsmith': [43, 44], 'hatmaker': [45, 46], 'inkmaker': [47, 48], 'interpreter': [49, 50], 'jeweller': [51, 52], 'lampmaker': [53, 54], 'leathercrafts': [55, 56], 'trickster': [57, 60], 'miner': [61, 62], 'metal worker': [63, 64], 'navigator': [65, 66], 'perfumer/dyer': [67, 68], 'pitchmaker': [69, 70], 'potter': [71, 72], 'roofer': [73, 74], 'ropemaker': [75, 76], 'saddlemaker': [77, 78], 'sailmaker': [79, 80], 'sage': [81, 82], 'smith': [83, 84], 'shipbuilder': [85, 86], 'slaver': [87, 88], 'tailor': [89, 92], 'tanner': [93, 94], 'weaver': [95, 98], 'winemaker': [99, 100]}

    common_class = {'moneylender': [1, 2], 'moneychanger': [3, 4], 'court clerk': [5, 6], 'teacher': [7, 8], 'doorman/bouncer': [9, 10], 'barkeep': [11, 12], 'messenger': [13, 14], 'attendant': [15, 16], 'warehouseman': [17, 18], 'cowpoke': [19, 20], 'animal trainer': [21, 22], 'gladiator trainer': [23, 24], 'actor': [25, 26], 'minstrel': [27, 28], 'orator': [29, 30], 'manager -': [31, 32], 'undertaker': [33, 34], 'manager': [35, 36], 'tavernkeeper': [37, 38], 'launderer': [39, 40], 'butcher': [41, 42], 'candlemaker': [43, 44], 'tobacco grower': [45, 46], 'towncrier': [47, 48], 'mountaineer': [49, 50], 'tax collector': [51, 52], 'banker': [53, 54], 'bureaucrat': [55, 56], 'maid/butler': [57, 58], 'porter/bearer': [59, 60], 'wet nurse': [61, 62], 'secretary/aide': [63, 64], 'cook': [65, 66], 'shepherd': [67, 68], 'horse trainer': [69, 70], 'bird trainer': [71, 72], 'dancer': [73 74], 'jester': [75, 76], 'stockboy': [77, 78], 'head clerk': [79, 80], 'physician': [81, 84], 'pawnshopsman': [85, 86], 'innkeeper': [87, 88], 'barber': [89, 90], 'baker': [91, 92], 'hunter': [93, 94], 'wagoneer': [95, 96], 'trapper': [97, 98], 'fisherman': [99, 100]}
