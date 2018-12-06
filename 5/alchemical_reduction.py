def react(polymer_str):
    """
    >>> react('dabAcCaCBAcCcaDA')
    'dabCBAcaDA'
    """
    polymer_arr = list(polymer_str)

    i = 1
    while i < len(polymer_arr):
        u1 = polymer_arr[i - 1]
        u2 = polymer_arr[i]

        if u1 != u2 and u1.lower() == u2.lower():
            polymer_arr.pop(i - 1)
            polymer_arr.pop(i - 1) # Since we just popped
            i -= 1
        else:
            i += 1

    return ''.join(polymer_arr)


def p1(polymer_str):
    return len(react(polymer_str))


def p2(polymer_str):
    units = set(polymer_str.lower())

    shortest_length = float('inf')
    for unit in units:
        reacted = react(polymer_str.replace(unit, '').replace(unit.upper(), ''))

        shortest_length = min(shortest_length, len(reacted))

    return shortest_length


if __name__ == '__main__':
    with open('input.txt', 'r') as input:
        polymer_str = input.read()[:-1]

        print(p1(polymer_str))
        print(p2(polymer_str))
