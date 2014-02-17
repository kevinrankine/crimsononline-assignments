from random import random as r

def random_direction():
    v = r()
    if v <= 0.2:
        return "U"
    elif v <= 0.4:
        return "D"
    elif v <= 0.6:
        return "L"
    elif v <= 0.8:
        return "R"
    else:
        return "F"
"""
luigi() is the actual function that performs "trials" trials.
"""
def luigi(trials):
    experiment = []
    num_wins = 0.0
    for i in range(trials):
        for i in range(3):
            experiment.append(random_direction())
        if not "F" in experiment:
            num_wins += 1
        experiment = []
    return num_wins / trials
