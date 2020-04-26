#!/usr/bin/env python3

import argparse
from utilities import choose
from utilities import get_results
from math import ceil
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


# Determine past experience
def past_exp(age):
    num_jobs = 0
    for exp in tables.past_experience.keys():
        for _ in tables.past_experience[exp]:
            if int(age) in range(_[0], _[1] + 1):
                num_jobs = int(exp)
                chance = _[2]
                print('num_jobs: {}\nchance: {}'.format(num_jobs, chance))
    past_jobs = []
    counter = 0
    while counter < num_jobs:
        for job in tables.past_jobs:
            if roll_percent() <= chance and job not in past_jobs:
                past_jobs.append({job: randint(1, 6) + randint(1, 6)})
                break
        counter = counter + 1
    return past_jobs


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
    character['previous experience'] = past_exp(character['age'])
    pprint(character)


if __name__ == '__main__':
    main()
