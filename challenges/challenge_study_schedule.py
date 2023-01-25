def study_schedule(permanence_period, target_time):
    if not target_time:
        return None

    count = 0

    try:
        for period in permanence_period:
            if period[0] <= target_time <= period[1]:
                count += 1

    except TypeError:
        return None

    return count
