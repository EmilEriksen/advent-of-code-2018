import re
from functools import reduce
from operator import itemgetter

import dateutil.parser


def parse_data(data):
    datetime_parsed = []
    for line in data:
        match = re.search(r'\[(.+)\](.+)', line)

        datetime = dateutil.parser.parse(match.group(1))
        datetime_parsed.append((datetime, match.group(2)[1:]))

    datetime_parsed = sorted(datetime_parsed, key=itemgetter(0))

    parsed = {}

    guard_id = None
    fell_asleep_at = None
    for datetime, line in datetime_parsed:
        if 'Guard' in line:
            guard_id = int(line.split(' ')[1][1:])
            continue

        if 'falls asleep' in line:
            fell_asleep_at = datetime
            continue

        if 'wakes up' in line:
            if guard_id not in parsed:
                parsed[guard_id] = []

            parsed[guard_id].append((fell_asleep_at, datetime))

    return parsed


def calc_time_asleep(data):
    time_asleep = {}

    for guard_id, asleep_intervals in data.items():
        time_asleep[guard_id] = reduce(lambda total, interval: total + (interval[1].minute - interval[0].minute),
                                       asleep_intervals, 0)

    return time_asleep


def calc_most_asleep(data):
    times_asleep_on = [0] * 60
    for fell_asleep_at, woke_up_at in data:
        for i in range(fell_asleep_at.minute, woke_up_at.minute):
            times_asleep_on[i] += 1

    most_asleep_on = max(enumerate(times_asleep_on), key=itemgetter(1))[0]

    return most_asleep_on, times_asleep_on[most_asleep_on]


def p1(data):
    time_asleep = calc_time_asleep(data)

    guard_id = max(time_asleep.items(), key=itemgetter(1))[0]

    most_asleep_on, _, = calc_most_asleep(data[guard_id])

    return guard_id * most_asleep_on


def p2(data):
    best_guard_id, best_asleep_on, best_times_asleep = -1, -1, -1

    for guard_id, intervals in data.items():
        most_asleep_on, times_asleep = calc_most_asleep(intervals)

        if times_asleep > best_times_asleep:
            best_guard_id, best_asleep_on, best_times_asleep = guard_id, most_asleep_on, times_asleep

    return best_guard_id * best_asleep_on


if __name__ == '__main__':
    with open('input.txt', 'r') as input:
        data = parse_data(input.read().splitlines())

        print(p1(data))
        print(p2(data))
