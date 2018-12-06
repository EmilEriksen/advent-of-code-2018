import re
import numpy as np

def parse_line(line):
    """
    >>> parse_line('#1 @ 817,273: 26x26')
    (1, (817, 273), (26, 26))
    """
    match = re.search(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)

    return int(match.group(1)), (int(match.group(2)), int(match.group(3))), (int(match.group(4)), int(match.group(5)))


def overlapping(data):
    fabric = np.zeros((1000, 1000))

    for _, (offset_l, offset_t), (width, height) in data:
        fabric[offset_l:offset_l+width, offset_t:offset_t+height] += 1

    return fabric


def find_non_overlapping(data, overlap=None):
    if overlap is None:
        overlap = overlapping(data)

    for iden, (offset_l, offset_t), (width, height) in data:
        if np.all(overlap[offset_l:offset_l+width, offset_t:offset_t+height] == 1):
            return iden


if __name__ == '__main__':
    with open('input.txt', 'r') as input:
        data = list(map(parse_line, input.read().splitlines()))

        overlap = overlapping(data)

        print((overlap >= 2).sum())
        print(find_non_overlapping(data, overlap))
