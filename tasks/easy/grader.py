def grade(rewards):
    score = sum(rewards) / len(rewards)

    if score >= 0.4:
        return 1.0
    elif score >= 0.2:
        return 0.5
    else:
        return 0.0