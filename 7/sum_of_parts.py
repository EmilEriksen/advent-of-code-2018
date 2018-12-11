from collections import OrderedDict
from ordered_set import OrderedSet


def parse_data(data):
    graph = {}

    for line in data:
        vertex, edge = line[5], line[36]

        if vertex not in graph:
            graph[vertex] = []

        if edge not in graph:
            graph[edge] = []

        graph[vertex].append(edge)

    for vertex, edges in graph.items():
        graph[vertex] = OrderedSet(sorted(edges))

    return OrderedDict(sorted(graph.items(), key=lambda x: x[0]))


def topo_sort(graph):
    queue, path, in_degrees = [], [], dict.fromkeys(graph.keys(), 0)

    for adj in graph.values():
        for v in adj:
            in_degrees[v] += 1

    for v, in_degree in in_degrees.items():
        if in_degree == 0:
            queue.append(v)

    while queue:
        # Obviously not exactly optimal
        queue.sort(reverse=True)

        v = queue.pop()
        path.append(v)

        for a in graph[v]:
            in_degrees[a] -= 1

            if in_degrees[a] == 0:
                queue.append(a)

    return path


def p1(graph):
    return ''.join(topo_sort(graph))


def step_time(step):
    """
    >>> step_time('e')
    5
    """
    return 'abcdefghijklmnopqrstuvwxyz'.index(step.lower()) + 1


def p2(graph):
    queue, time, in_degrees = [], 0, dict.fromkeys(graph.keys(), 0)

    for adj in graph.values():
        for v in adj:
            in_degrees[v] += 1

    for v, in_degree in in_degrees.items():
        if in_degree == 0:
            queue.append([v, 60 + step_time(v)])

    def remove_from_queue(i):
        for a in graph[queue[i][0]]:
            in_degrees[a] -= 1

            if in_degrees[a] == 0:
                queue.append([a, 60 + step_time(a)])

        queue.pop(i)
        queue.sort(key=lambda x: x[0])

    while queue:
        for i in range(len(queue) - 1, -1, -1):
            queue[i][1] -= 1

            if queue[i][1] == 0:
                remove_from_queue(i)

        time += 1

    return time


if __name__ == '__main__':
    with open('input.txt', 'r') as input:
        graph = parse_data(input.read().splitlines())

        print(p1(graph))
        print(p2(graph))
