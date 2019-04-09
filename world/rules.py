import random


def check(player, trait):
    result = find_stat(player, trait)
    if 'error' in result.keys():
        return result

    stat_roll = roll_stat(result[trait])
    success_msg = '{} rolled a {}. '.format(player.id, stat_roll)
    if stat_roll <= 1:
        success_msg += 'Failure'
    elif stat_roll == 2 and stat_roll <= 5:
        success_msg += 'Very Easy Success.'
    elif stat_roll == 6 and stat_roll <= 10:
        success_msg += 'Easy Success.'
    elif stat_roll == 11 and stat_roll <= 15:
        success_msg += 'Moderate Success'
    elif stat_roll == 16 and stat_roll <= 20:
        success_msg += 'Difficult Success'
    elif stat_roll == 21 and stat_roll <= 30:
        success_msg += 'Very Difficult Success'
    else:
        success_msg += 'Heroic Success'

    return success_msg


def find_stat(player, trait):
    stats = player.db.stats
    value = 0
    if trait in stats.keys():
        value = stats[trait].get('value')
    else:
        for key in stats.keys():
            if trait in stats[key].keys():
                value = stats[key].get(trait)
                value += stats[key].get('value')

    if value == 0:
        return {'error': 'That Trait was not found.'}
    else:
        return {trait: value}


def roll_stat(pips):
    dice = pips / 3
    remainder = pips % 3

    result = 0

    for i in dice:
        result += random.randint(1, 6)

    return result + remainder


def parse_stat(pips):
    dice = pips / 3
    remainder = dice % 3

    if remainder > 0:
        return "{}D+{}".format(dice, remainder)
    else:
        return "{}D".format(dice)
