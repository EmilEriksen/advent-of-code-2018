import sys
from collections import deque
from functools import reduce


class Node:
    def __init__(self, child_nodes, metadata_entries):
        self.metadata_entries = metadata_entries
        self.child_nodes = child_nodes

    def get_child_nodes_qty(self):
        return len(self.child_nodes)

    def get_metadata_entries_qty(self):
        return len(self.metadata_entries)


def parse_data(data):
    def parse(data):
        child_nodes_qty, metadata_entries_qty = data[0], data[1]
        child_nodes = []

        if child_nodes_qty == 0:
            return Node(child_nodes, data[2:2+metadata_entries_qty]), 2 + metadata_entries_qty

        child_nodes_size = 0
        while child_nodes_qty != 0:
            n, size = parse(data[2:])
            data = data[:2] + data[2 + size:]
            child_nodes_size += size
            child_nodes.append(n)
            child_nodes_qty -= 1

        return Node(child_nodes, data[2:2+metadata_entries_qty]), 2 + child_nodes_size + metadata_entries_qty

    parsed, _ = parse(data)

    return parsed


def walk(tree):
    queue = deque([tree])

    while queue:
        n = queue.popleft()

        yield n

        queue.extend(n.child_nodes)


def p1(tree):
    return reduce(lambda a, x: a + sum(x.metadata_entries), walk(tree), 0)


def calc_value(tree):
    if tree.get_child_nodes_qty() == 0:
        return sum(tree.metadata_entries)

    s = 0
    for entry in tree.metadata_entries:
        if 1 <= entry <= tree.get_child_nodes_qty():
            s += calc_value(tree.child_nodes[entry - 1])

    return s




def p2(tree):
    return calc_value(tree)


if __name__ == '__main__':
    sys.setrecursionlimit(10000)

    with open('input.txt', 'r') as input:
        tree = parse_data(list(map(int, input.read()[:-1].split(' '))))

        print(p1(tree))
        print(p2(tree))
