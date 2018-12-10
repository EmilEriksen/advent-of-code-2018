import numpy as np
from ordered_set import OrderedSet


def parse_line(line):
    return tuple(map(int, line.split(', ')))


def get_bounds(points):
    min_x, min_y, max_x, max_y = float('inf'), float('inf'), -float('inf'), -float('inf')

    for x, y in points:
        min_x = min(min_x, x)
        min_y = min(min_y, y)
        
        max_x = max(max_x, x)
        max_y = max(max_y, y)

    return (min_x, min_y), (max_x, max_y)


def draw_points(points):
    (min_x, min_y), (max_x, max_y) = get_bounds(points)

    drawing = ''
    for j in range(min_y, max_y + 1):
        drawing += "\n"
        for i in range(min_x, max_x + 1):
            drawing += '.' if (i, j) not in points else str(points.index((i, j)))

    return drawing


def manhattan_dist(p1, p2):
    (x1, y1) = p1
    (x2, y2) = p2

    return abs(x1 - x2) + abs(y1 - y2)


def find_nearest(point, points):
    equal = False
    best_i = None
    best_dist = float('inf')
    for i, p in enumerate(points):
        dist = manhattan_dist(point, p)
        if dist == best_dist:
            equal = True

        if dist < best_dist:
            best_i = i
            best_dist = dist
            equal = False

    return best_i if not equal else None


def p1(points):
    (min_x, min_y), (max_x, max_y) = get_bounds(points)
    grid = np.zeros((max_x, max_y), dtype='int')
    for i in range(min_x, max_x):
        for j in range(min_y, max_y):
            nearest = find_nearest((i, j), points)
            grid[i - min_x, j - min_y] = -1 if nearest is None else nearest

    unique, counts = np.unique(grid, return_counts=True)
    best = -float('inf')
    for pi, count in zip(unique, counts):
        if pi == -1:
            continue

        x, y = points[pi]

        if grid[0, y - min_y] == pi or grid[x - min_x, 0] == pi or grid[-1, y - min_y] == pi or grid[x - min_x,
                                                                                                     -1] == pi:
            continue

        if count > best:
            best = count

    return best


def within_region(point, points):
    x, y = point
    total_distance = 0

    for i, p in enumerate(points):
        total_distance += manhattan_dist(point, p)

        if total_distance >= 10000:
            return False

    return True


def p2(points):
    (min_x, min_y), (max_x, max_y) = get_bounds(points)
    size = 0

    for i in range(min_x, max_x):
        for j in range(min_y, max_y):
            if within_region((i, j), points):
                size += 1

    return size


if __name__ == '__main__':
    with open('input.txt', 'r') as input:
        points = OrderedSet(map(parse_line, input.read().splitlines()))

        #print(p1(points))
        print(p2(points))
