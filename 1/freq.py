from functools import reduce

if __name__ == '__main__':
    with open('input.txt', 'r') as input:
        print(reduce(lambda x, y: x + int(y), input, 0))
