#!/usr/bin/env python3

from statistics import mean


if __name__ == '__main__':
    mark_1 = int(input('Enter mark #1: '))
    mark_2 = int(input('Enter mark #2: '))
    mark_3 = int(input('Enter mark #3: '))
    mark_4 = int(input('Enter mark #4: '))
    mark_5 = int(input('Enter mark #5: '))

    max_mark = max(mark_1, mark_2, mark_3, mark_4, mark_5)
    min_mark = min(mark_1, mark_2, mark_3, mark_4, mark_5)
    avg_mark = mean([mark_1, mark_2, mark_3, mark_4, mark_5])

    print()

    print('Highest Mark:  ', max_mark)
    print('Lowest Mark:   ', min_mark)
    print('Average Mark:  ', avg_mark)

    print()

    print('Highest Mark:  ', max(mark_1, mark_2, mark_3, mark_4, mark_5))
    print('Lowest Mark:   ', min(mark_1, mark_2, mark_3, mark_4, mark_5))
    print('Average Mark:  ', mean([mark_1, mark_2, mark_3, mark_4, mark_5]))