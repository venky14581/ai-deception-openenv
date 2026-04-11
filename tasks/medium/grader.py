def grade(rewards):
    score = sum(rewards) / len(rewards)

    if score >= 0.5:
        return 1.0
    elif score >= 0.3:
        return 0.6
    else:
        return 0.2