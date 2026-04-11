def grade(reward):

    if reward >= 0.6:
        return 1.0

    elif reward >= 0.3:
        return 0.5

    return 0.0
