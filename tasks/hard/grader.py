def grade(rewards):
    score = sum(rewards) / len(rewards)

    if score >= 0.6:
        return 1.0
    elif score >= 0.4:
        return 0.7
    else:
        return 0.3