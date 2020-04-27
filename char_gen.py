#!/usr/bin/env python3

import argparse
from math import ceil
from utilities import choose
from utilities import get_results
from pprint import pprint
from utilities import roll_percent
from utilities import roll_score
from utilities import tables
from random import randint

"""
This program will create a character based on the rules as described in
The Game: Fantasy Edition
"""


# Generate Scores
def roll_scores(gender, race):
    for score in tables.req_scores.keys():
        multiplier = tables.race_multiplier[race][score]
        if isinstance(multiplier, str):
            tables.req_scores[score] = int(multiplier)
        else:
            if gender == 'female':
                tables.req_scores[score] = int(ceil(roll_score(3, alt=score, verbose=verbose) * multiplier))
            else:
                tables.req_scores[score] = int(ceil(roll_score(3, verbose=verbose) * multiplier))
    for score in tables.sense_scores.keys():
        tables.sense_scores[score] = roll_score(2, verbose=verbose)
    for score in tables.optional_scores.keys():
        if score == 'beauty':
            tables.optional_scores[score] = roll_score(3, verbose=verbose)
        else:
            tables.optional_scores[score] = roll_score(1, verbose=verbose)
    scores = {'req_scores': tables.req_scores,
              'sense_scores': tables.sense_scores,
              'optional_scores': tables.optional_scores}
    return scores


# Validate Class
def check_class(race, job):
    limited = ['warrior-priest', 'warrior-wizard', 'martial artist', 'priest', 'special']
    while race != ('human' or 'half-human') and job.lower() in limited:
        print('{} is not a valid class for {}'.format(job.title(), race.title()))
        job = choose(tables.job, 'Class', verbose)
    return job


# Determine Class(es)
def get_class(race):
    job = check_class(race, choose(tables.job, 'Class', verbose))
    if job == 'special':
        job = []
        for _ in range(randint(2, 5)):
            new_class = get_results(tables.job, roll_percent(), verbose)
            while new_class in character['class']:
                new_class = get_results(tables.job, roll_percent(), verbose)
            job.append(new_class)
    return job


# Determine possiblity of past experience
def possible_past_exp(age):
    num_jobs = 0
    for exp in tables.past_experience.keys():
        for _ in tables.past_experience[exp]:
            if int(age) in range(_[0], _[1] + 1):
                num_jobs = int(exp)
                chance = _[2]
    possibilities = {'num_jobs': num_jobs, 'chance': chance}
    return possibilities


# Generate past experience
def past_exp(possibilities):
    past_jobs = []
    counter = 0
    while counter < possibilities['num_jobs']:
        for job in tables.past_jobs:
            if roll_percent() <= possibilities['chance']:
                if job not in past_jobs:
                    past_jobs.append({job: randint(1, 6) + randint(1, 6)})
                break
        counter = counter + 1
    return past_jobs


# Parental Social level
def define_parent(parent_type):
    parent = {}
    if parent_type == 'mother':
        roll = roll_percent()
        if roll <= 70:
            return homemaker(parent)
    parent['social_group'] = choose(tables.general_groupings, '{}\'s Social Group'.format(parent_type), verbose)
    parent['group_rank'] = choose(getattr(tables, parent['social_group'], None), '{}\'s Rank'.format(parent_type), verbose)
    level_range = getattr(tables, parent['social_group'], None)[parent['group_rank']]['level']
    parent['level'] = randint(level_range[0], level_range[1])
    if parent['social_group'] in tables.lower:
        if parent['group_rank'] not in tables.exempt:
            parent['job_spec'] = choose(getattr(tables, parent['social_group'] + '_class', None), '{}\'s Job Description'.format(parent_type), verbose)
            parent['skill_bonus'] = getattr(tables, parent['social_group'], None)[parent['group_rank']]['bonus']
        elif parent['group_rank'] == 'serf':
            parent['job_spec'] = 'farmer'
        else:
            parent['job_spec'] = None
    else:
        parent['job_spec'] = None
    return parent


# moms get shafted in this game
def homemaker(parent):
    parent['social_group'] = 'homemaker'
    parent['group_rank'] = 'homemaker'
    parent['level'] = 0
    parent['job_spec'] = None
    return parent


# Calculate number of original skills
def calc_skills():
    total = 0
    total = sum([total + value for score, value in tables.req_scores.items() if score != 'speed'])
    for row in tables.orig_skill_total.keys():
        low = tables.orig_skill_total[row]['chance'][0]
        high = tables.orig_skill_total[row]['chance'][1]
        if total in range(low, high + 1):
            return tables.orig_skill_total[row]


# Determine originial skills
def get_skills(skill_table):
    orig_skills = {}
    for table in ['a', 'b', 'c']:
        table_name = 'table_' + table
        counter = 0
        while counter < skill_table[table]:
            skill = choose(getattr(tables, table_name, None), 'skill from Table {}'.format(table.title()), verbose)
            if skill not in orig_skills.keys():
                orig_skills[skill] = skill_value(getattr(tables, 'table_' + table, None)[skill]['stats'])
                counter = counter + 1
    return orig_skills


# Calculate skill value
def skill_value(stats):
    ranks = []
    for stat in stats:
        if stat in tables.optional_scores.keys():
            ranks.append(tables.optional_scores[stat])
        if stat in tables.sense_scores.keys():
            ranks.append(tables.sense_scores[stat])
        if stat in tables.req_scores.keys():
            ranks.append(tables.req_scores[stat])
    ranks = sorted(ranks, reverse=True)
    if len(stats) == 1:
        return ranks[0] * 2
    if len(stats) > 1:
        return ranks[0] + ranks[1]


# Create a Name
def name():
    name = []
    sylls = []
    syll_num = choose(tables.syllable_number, 'number of syllables in your name', verbose)
    for num in range(syll_num):
        sylls.append(choose(tables.syllables, 'syllable', verbose))
    for syll in sylls:
        name.append(make_syllable(syll))
    return ''.join(name).title()


# Apply consonants and vowels as determined by the syllable decsription
def make_syllable(syllable):
    letters = []
    for letter in [char for char in syllable]:
        if letter == 'c':
            letters.append(get_results(tables.consonants, roll_percent(), verbose))
        if letter == 'v':
            letters.append(get_results(tables.vowels, roll_percent(), verbose))
    return ''.join(letters)


# Verbose or not
def get_args():
    parser = argparse.ArgumentParser(description='Generate a Character based on TG:FE rules')
    parser.add_argument('-v', '--verbose', default=False, action='store_true', help='Show rolls')
    return parser.parse_args()


# Make a character
def main():
    global verbose
    args = get_args()
    verbose = args.verbose
    character = {}
    character['gender'] = choose(tables.gender, 'Sex', verbose)
    character['race'] = choose(tables.race, 'Race', verbose)
    if character['race'] == 'other':
        character['race'] = choose(tables.language, 'Extended Races', verbose)
    character['class'] = get_class(character['race'])
    character['scores'] = roll_scores(character['gender'], character['race'])
    character['age'] = get_results(tables.age, roll_percent(), verbose)
    character['previous experience'] = past_exp(possible_past_exp(character['age']))
    character['father'] = define_parent('father')
    character['mother'] = define_parent('mother')
    character['original_skills'] = get_skills(calc_skills())
    character['name'] = name()
    pprint(character)


if __name__ == '__main__':
    main()
