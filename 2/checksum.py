def contains_two_or_three(str):
    counts = {}

    for l in str:
        if l not in counts: counts[l] = 0

        counts[l] += 1

    contains_two, contains_three = False, False
    for count in counts.values():
        if count == 2: contains_two = True
        if count == 3: contains_three = True

    return contains_two, contains_three


if __name__ == '__main__':
    with open('input.txt', 'r') as input:
        data = input.read().splitlines()

        two_count = 0
        three_count = 0

        for str in data:
            contains_two, contains_three = contains_two_or_three(str)

            two_count += int(contains_two)
            three_count += int(contains_three)

        print(two_count * three_count)

        done = False
        for str1 in data:
            if done:
                break

            for str2 in data:
                if str1 == str2:
                    continue

                count = 0
                for l1, l2 in zip(str1, str2):
                    if l1 != l2:
                        count += 1
                    if count > 1:
                        break

                if count <= 1:
                    str = ''
                    for l1, l2 in zip(str1, str2):
                        if l1 == l2:
                            str += l1

                    print(str)
                    done = True
                    break


