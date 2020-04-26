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
def get_results(table, roll, verbose):
    item = [item for item, chance in table.items() if roll in range(chance['chance'][0], chance['chance'][1] + 1)]
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
            return choice.lower()
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
    gender = {'male': {'chance': [1, 50]}, 'female': {'chance': [51, 100]}}

    race = {
        'human': {'chance': [1, 50]},
        'elf': {'chance': [51, 75]},
        'half-human': {'chance': [76, 85]},
        'dwarf': {'chance': [86, 95]},
        'other': {'chance': [96, 100]}
    }

    # called it 'job' instead 'class' because of reserved words in python
    job = {
        'warrior': {'chance': [1, 50]},
        'wizard': {'chance': [51, 60]},
        'thief': {'chance': [61, 70]},
        'healer': {'chance': [71, 80]},
        'warrior-priest': {'chance': [81, 85]},
        'warrior-wizard': {'chance': [86, 90]},
        'martial artist': {'chance': [91, 97]},
        'priest': {'chance': [98, 99]},
        'special': {'chance': [100, 100]}
    }

    language = {
        'human': {'chance': [1, 20]}, 'elf': {'chance': [21, 35]}, 'dwarf': {'chance': [36, 45]},
        'gnome': {'chance': [46, 50]}, 'troll': {'chance': [51, 55]}, 'goblin': {'chance': [56, 60]},
        'centaur': {'chance': [61, 63]}, 'giant': {'chance': [64, 70]}, 'chimera': {'chance': [71, 74]},
        'sprite': {'chance': [75, 77]}, 'manticora': {'chance': [78, 80]}, 'lizard man': {'chance': [81, 83]},
        'ogre': {'chance': [84, 90]}, 'wyvern': {'chance': [91, 94]}, 'harpy': {'chance': [95, 97]},
        'dragon': {'chance': [98, 100]}
    }

    age = {
        '13': {'chance': [1, 1]}, '14': {'chance': [2, 3]}, '15': {'chance': [4, 5]}, '16': {'chance': [6, 8]},
        '17': {'chance': [9, 14]}, '18': {'chance': [15, 20]}, '19': {'chance': [21, 27]}, '20': {'chance': [28, 34]},
        '21': {'chance': [35, 42]}, '22': {'chance': [43, 50]}, '23': {'chance': [51, 57]}, '24': {'chance': [58, 64]},
        '25': {'chance': [65, 70]}, '26': {'chance': [71, 76]}, '27': {'chance': [77, 81]}, '28': {'chance': [82, 86]},
        '29': {'chance': [87, 90]}, '30': {'chance': [91, 94]}, '31': {'chance': [95, 97]}, '32': {'chance': [98, 99]},
        '33': {'chance': [100, 100]}
    }

    race_multiplier = {
        'centaur': {'strength': 3, 'knowledge': 1, 'judgement': 1, 'endurance': 3, 'deftness': 1, 'speed': 2, 'personality': 1.5},
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
        'wyvern': {'strength': 3, 'knowledge': 3, 'judgement': 2, 'endurance': 5, 'deftness': '3', 'speed': .75, 'personality': .5}
    }

    # {'number of classes': {[age range from, age range to, chance], [age range from, age range to, chance]}
    past_experience = {
        0: [[13, 16, 0]],
        1: [[17, 20, 5], [21, 24, 10]],
        2: [[25, 28, 15], [29, 32, 20]],
        3: [[33, 33, 25]]
    }

    # Simply a list of possible previous classes
    past_jobs = [
        'mercenary', 'pirate', 'thief', 'bandit', 'assassin',
        'spy', 'gladiator', 'priest', 'warrior-priest', 'healer',
        'martial artist', 'warrior', 'warrior-wizard', 'druid', 'option'
    ]

    # These are for generating names
    vowels = {
        'a': {'chance': [1, 17]},
        'e': {'chance': [18, 41]},
        'i': {'chance': [42, 58]},
        'o': {'chance': [59, 79]},
        'u': {'chance': [80, 92]},
        'y': {'chance': [93, 100]}
    }

    consonants = {
        'b': {'chance': [1, 5]}, 'c': {'chance': [6, 10]}, 'd': {'chance': [11, 15]},
        'f': {'chance': [16, 20]}, 'g': {'chance': [21, 25]}, 'h': {'chance': [26, 30]},
        'j': {'chance': [31, 35]}, 'k': {'chance': [36, 40]}, 'l': {'chance': [41, 45]},
        'm': {'chance': [46, 50]}, 'n': {'chance': [51, 55]}, 'p': {'chance': [56, 60]},
        'q': {'chance': [100, 100]}, 'r': {'chance': [61, 70]}, 's': {'chance': [71, 77]},
        't': {'chance': [78, 84]}, 'v': {'chance': [85, 87]}, 'w': {'chance': [88, 93]},
        'x': {'chance': [94, 95]}, 'z': {'chance': [96, 99]}
    }

    syllables = {
        'vc': {'chance': [1, 30]},
        'vcc': {'chance': [31, 50]},
        'cv': {'chance': [51, 80]},
        'cvv': {'chance': [81, 90]},
        'cvc': {'chance': [91, 99]},
        'cvvc': {'chance': [100, 100]}
    }

    syllable_number = {
        1: {'chance': [1, 30]},
        2: {'chance': [31, 75]},
        3: {'chance': [76, 93]},
        4: {'chance': [94, 97]},
        5: {'chance': [98, 100]}
    }

    # Score tables are used as a working dict and gets populated by char_gen.py
    req_scores = {
        'strength': '',
        'knowledge': '',
        'judgement': '',
        'endurance': '',
        'deftness': '',
        'speed': '',
        'personality': ''
    }

    sense_scores = {
        'sight': '',
        'hearing': '',
        'smell': '',
        'taste': '',
        'touch': '',
        'prescience': ''
    }

    optional_scores = {
        'beauty': '',
        'bravery': '',
        'ego': '',
        'curiousity': '',
        'temper': '',
        'swearing': '',
        'humor': '',
        'stubonrness': '',
        'patience': ''
    }

    # Social charts for parentage
    general_groupings = {
        'common': {'chance': [1, 40]}, 'guild': {'chance': [41, 55]}, 'merchant': {'chance': [56, 75]},
        'military': {'chance': [76, 90]}, 'gentle': {'chance': [91, 97]}, 'noble': {'chance': [98, 100]}
    }

    # format of {'title': {'chance': [chance range], 'level': [level range]}}
    # use for x in range('option'[chance][0], 'option'[chance][1] + 1)
    noble = {
        'page': {'chance': [1, 30], 'level': [1, 3]},
        'knight': {'chance': [31, 50], 'level': [4, 6]},
        'thane': {'chance': [51, 70], 'level': [7, 7]},
        'baron': {'chance': [71, 85], 'level': [8, 8]},
        'minister': {'chance': [86, 92], 'level': [9, 9]},
        'prince/princess': {'chance': [93, 97], 'level': [10, 10]},
        'king/queen': {'chance': [98, 100], 'level': [10, 10]}
    }

    gentle = {
        'constable': {'chance': [1, 45], 'level': [1, 3]},
        'gentry': {'chance': [46, 65], 'level': [4, 4]},
        'chevalier': {'chance': [66, 80], 'level': [5, 5]},
        'pretender': {'chance': [81, 90], 'level': [6, 6]},
        'magistrate': {'chance': [91, 97], 'level': [6, 6]},
        'lord mayor': {'chance': [98, 100], 'level': [6, 6]}
    }

    military = {
        'troop': {'chance': [1, 50], 'level': [1, 1]},
        'guard': {'chance': [51, 62], 'level': [2, 2]},
        'lieutenant': {'chance': [63, 72], 'level': [3, 3]},
        'captain': {'chance': [73, 81], 'level': [4, 4]},
        'major': {'chance': [82, 87], 'level': [5, 5]},
        'colonel': {'chance': [88, 92], 'level': [6, 6]},
        'general': {'chance': [93, 96], 'level': [7, 7]},
        'army cmdr': {'chance': [97, 99], 'level': [8, 8]},
        'chief of staff': {'chance': [100, 100], 'level': [10, 10]}
    }

    # format of {'title': {'chance': [chance range], 'level': [level range], 'bonus': skill bonus]}
    merchant = {
        'huckster': {'chance': [1, 30], 'level': [1, 3], 'bonus': 10},
        'trader': {'chance': [31, 49], 'level': [4, 6], 'bonus': 15},
        'monger': {'chance': [50, 66], 'level': [7, 9], 'bonus': 20},
        'proprietor': {'chance': [67, 81], 'level': [10, 12], 'bonus': 25},
        'agent': {'chance': [82, 91], 'level': [13, 15], 'bonus': 30},
        'magnate': {'chance': [92, 97], 'level': [16, 18], 'bonus': 35},
        'high magnate': {'chance': [98, 100], 'level': [19, 21], 'bonus': 40}
    }

    guild = {
        'apprentice': {'chance': [1, 45], 'level': [1, 4], 'bonus': 15},
        'journeyman': {'chance': [46, 65], 'level': [5, 8], 'bonus': 20},
        'craftsman': {'chance': [66, 80], 'level': [9, 12], 'bonus': 25},
        'expert': {'chance': [81, 90], 'level': [13, 16], 'bonus': 30},
        'guildmaster': {'chance': [91, 97], 'level': [17, 20], 'bonus': 35},
        'teacher': {'chance': [98, 100], 'level': [21, 21], 'bonus': 40}
    }

    common = {
        'citizen': {'chance': [1, 45], 'level': [7, 12], 'bonus': 30},
        'freeman': {'chance': [46, 55], 'level': [1, 6], 'bonus': 20},
        'serf': {'chance': [56, 80], 'level': [1, 12], 'bonus': 10},
        'slave': {'chance': [81, 90], 'level': [0, 0], 'bonus': 0},
        'gypsy': {'chance': [91, 98], 'level': [0, 0], 'bonus': 0},
        'adventurer': {'chance': [99, 100], 'level': [0, 0], 'bonus': 0}
    }

    # standard format
    merchant_class = {
        'food stuffs': {'chance': [1, 6]}, 'alcoholic beverages': {'chance': [7, 12]}, 'rope': {'chance': [13, 18]},
        'feed and seed': {'chance': [19, 24]}, 'weapons': {'chance': [24, 28]}, 'livestock': {'chance': [29, 31]},
        'leather goods': {'chance': [32, 34]}, 'spices': {'chance': [35, 37]},
        'building supplies': {'chance': [38, 40]}, 'quarry/mines': {'chance': [41, 43]},
        'timber/pitch': {'chance': [44, 46]}, 'perfume/soap': {'chance': [47, 49]},
        'magic weapons': {'chance': [50, 50]}, 'clothing': {'chance': [51, 56]},
        'small livestock': {'chance': [57, 62]}, 'tools': {'chance': [63, 68]}, 'armor': {'chance': [69, 72]},
        'foundry': {'chance': [73, 75]}, 'shipyard': {'chance': [76, 78]}, 'hotelier': {'chance': [79, 81]},
        'rugs': {'chance': [82, 84]}, 'books/arts': {'chance': [85, 87]}, 'gems/metal': {'chance': [88, 90]},
        'showman': {'chance': [91, 93]}, 'processed foodstuffs': {'chance': [94, 96]},
        'magic items': {'chance': [97, 97]}, 'shipping': {'chance': [98, 99]}, 'other': {'chance': [100, 100]}
    }

    guild_class = {
        'accountant': {'chance': [1, 2]}, 'alchemist': {'chance': [3, 4]}, 'architect': {'chance': [5, 6]},
        'armorer': {'chance': [7, 8]}, 'artist': {'chance': [9, 10]}, 'assassin': {'chance': [11, 12]},
        'beggar': {'chance': [13, 14]}, 'boatmaker': {'chance': [15, 16]}, 'bootmaker': {'chance': [17, 18]},
        'botanist': {'chance': [19, 20]}, 'bowmaker': {'chance': [21, 22]}, 'bricklayer': {'chance': [23, 24]},
        'carpenter': {'chance': [25, 28]}, 'carpetmaker': {'chance': [29, 30]}, 'carver': {'chance': [31, 32]},
        'engineer': {'chance': [33, 34]}, 'executioner': {'chance': [35, 36]}, 'fletcher': {'chance': [37, 38]},
        'geologist': {'chance': [39, 40]}, 'glassblower': {'chance': [41, 42]}, 'goldsmith': {'chance': [43, 44]},
        'hatmaker': {'chance': [45, 46]}, 'inkmaker': {'chance': [47, 48]}, 'interpreter': {'chance': [49, 50]},
        'jeweller': {'chance': [51, 52]}, 'lampmaker': {'chance': [53, 54]}, 'leathercrafts': {'chance': [55, 56]},
        'trickster': {'chance': [57, 60]}, 'miner': {'chance': [61, 62]}, 'metal worker': {'chance': [63, 64]},
        'navigator': {'chance': [65, 66]}, 'perfumer/dyer': {'chance': [67, 68]}, 'pitchmaker': {'chance': [69, 70]},
        'potter': {'chance': [71, 72]}, 'roofer': {'chance': [73, 74]}, 'ropemaker': {'chance': [75, 76]},
        'saddlemaker': {'chance': [77, 78]}, 'sailmaker': {'chance': [79, 80]}, 'sage': {'chance': [81, 82]},
        'smith': {'chance': [83, 84]}, 'shipbuilder': {'chance': [85, 86]}, 'slaver': {'chance': [87, 88]},
        'tailor': {'chance': [89, 92]}, 'tanner': {'chance': [93, 94]}, 'weaver': {'chance': [95, 98]},
        'winemaker': {'chance': [99, 100]}
    }

    common_class = {
        'moneylender': {'chance': [1, 2]}, 'moneychanger': {'chance': [3, 4]}, 'court clerk': {'chance': [5, 6]},
        'teacher': {'chance': [7, 8]}, 'doorman/bouncer': {'chance': [9, 10]}, 'barkeep': {'chance': [11, 12]},
        'messenger': {'chance': [13, 14]}, 'attendant': {'chance': [15, 16]}, 'warehouseman': {'chance': [17, 18]},
        'cowpoke': {'chance': [19, 20]}, 'animal trainer': {'chance': [21, 22]},
        'gladiator trainer': {'chance': [23, 24]}, 'actor': {'chance': [25, 26]}, 'minstrel': {'chance': [27, 28]},
        'orator': {'chance': [29, 30]}, 'manager -': {'chance': [31, 32]}, 'undertaker': {'chance': [33, 34]},
        'manager': {'chance': [35, 36]}, 'tavernkeeper': {'chance': [37, 38]}, 'launderer': {'chance': [39, 40]},
        'butcher': {'chance': [41, 42]}, 'candlemaker': {'chance': [43, 44]}, 'tobacco grower': {'chance': [45, 46]},
        'towncrier': {'chance': [47, 48]}, 'mountaineer': {'chance': [49, 50]}, 'tax collector': {'chance': [51, 52]},
        'banker': {'chance': [53, 54]}, 'bureaucrat': {'chance': [55, 56]}, 'maid/butler': {'chance': [57, 58]},
        'porter/bearer': {'chance': [59, 60]}, 'wet nurse': {'chance': [61, 62]},
        'secretary/aide': {'chance': [63, 64]}, 'cook': {'chance': [65, 66]}, 'shepherd': {'chance': [67, 68]},
        'horse trainer': {'chance': [69, 70]}, 'bird trainer': {'chance': [71, 72]}, 'dancer': {'chance': [73, 74]},
        'jester': {'chance': [75, 76]}, 'stockboy': {'chance': [77, 78]}, 'head clerk': {'chance': [79, 80]},
        'physician': {'chance': [81, 84]}, 'pawnshopsman': {'chance': [85, 86]}, 'innkeeper': {'chance': [87, 88]},
        'barber': {'chance': [89, 90]}, 'baker': {'chance': [91, 92]}, 'hunter': {'chance': [93, 94]},
        'wagoneer': {'chance': [95, 96]}, 'trapper': {'chance': [97, 98]}, 'fisherman': {'chance': [99, 100]}
    }

    orig_skill_total = {
        1: {'range': [6, 18], 'a': 1, 'b': 0, 'c': 0},
        2: {'range': [19, 36], 'a': 2, 'b': 1, 'c': 0},
        3: {'range': [37, 54], 'a': 3, 'b': 2, 'c': 1},
        4: {'range': [55, 72], 'a': 4, 'b': 3, 'c': 2},
        5: {'range': [73, 90], 'a': 5, 'b': 4, 'c': 3},
        6: {'range': [91, 108], 'a': 6, 'b': 5, 'c': 4},
        7: {'range': [109, 10000], 'a': 7, 'b': 6, 'c': 5},
    }

    table_a = {
        'barber': {'chance': [1, 3], 'stats': ['deftness']},
        'baker': {'chance': [4, 6], 'stats': ['judgement', 'deftness']},
        'beggar': {'chance': [7, 9], 'stats': ['personality']},
        'bootmaker': {'chance': [10, 12], 'stats': ['knowledge', 'deftness']},
        'bricklayer': {'chance': [13, 15], 'stats': ['deftness', 'strength']},
        'butcher': {'chance': [16, 18], 'stats': ['deftness']},
        'carpenter': {'chance': [19, 21], 'stats': ['deftness']},
        'carptemaker': {'chance': [22, 24], 'stats': ['deftness']},
        'carver': {'chance': [25, 27], 'stats': ['deftness']},
        'cook': {'chance': [28, 30], 'stats': ['judgement']},
        'dyer': {'chance': [31, 33], 'stats': ['judgement']},
        'farmer': {'chance': [34, 36], 'stats': ['strength', 'judgement', 'endurance']},
        'fisherman': {'chance': [37, 39], 'stats': ['strength', 'judgement', 'endurance']},
        'glassblower': {'chance': [40, 42], 'stats': ['deftness']},
        'grocer': {'chance': [43, 45], 'stats': ['judgement', 'personality']},
        'hatmaker': {'chance': [46, 48], 'stats': ['judgement', 'deftness']},
        'inkmaker': {'chance': [49, 51], 'stats': ['judgement']},
        'lampmaker': {'chance': [52, 54], 'stats': ['knowledge']},
        'mason': {'chance': [55, 57], 'stats': ['strength', 'deftness']},
        'merchant': {'chance': [58, 61], 'stats': ['knowledge', 'personality']},
        'miner': {'chance': [61, 64], 'stats': ['strength', 'endurance', 'deftness']},
        'papermaker': {'chance': [65, 67], 'stats': ['deftness']},
        'perfumer': {'chance': [68, 70], 'stats': ['judgement', 'deftness']},
        'pitchmaker': {'chance': [71, 73], 'stats': ['knowledge', 'deftness']},
        'potter': {'chance': [74, 76], 'stats': ['knowledge', 'deftness']},
        'roofer': {'chance': [77, 79], 'stats': ['strength', 'deftness']},
        'rope/net maker': {'chance': [80, 82], 'stats': ['judgement', 'deftness']},
        'saddlemaker': {'chance': [83, 85], 'stats': ['judgement', 'deftness']},
        'tailor': {'chance': [86, 91], 'stats': ['deftness']},
        'tanner': {'chance': [92, 94], 'stats': ['judgement', 'deftness']},
        'weaver': {'chance': [95, 97], 'stats': ['deftness']},
        'winemaker': {'chance': [98, 100], 'stats': ['knowledge', 'deftness']}
    }

    table_b = {
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []}
    }

    table_c = {
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []},
        '': {'chance': [], 'stats': []}
    }
