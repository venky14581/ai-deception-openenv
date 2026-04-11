def grade(reward):

    if reward >= 0.8:
        return 1.0

    elif reward >= 0.5:
        return 0.7

    elif reward >= 0.3:
        return 0.4

    return 0.0
