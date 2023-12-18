def solution(E, L):
    duration = in_minute(L) - in_minute(E)
    if duration == 0:
        return 2
    elif duration <= 60:
        return 5
    else:
        after_first = duration - 60
        return 5 - (after_first // -60) * 4


def in_minute(string):
    hour_string, minute_string = string.split(":")
    return int(hour_string) * 60 + int(minute_string)
