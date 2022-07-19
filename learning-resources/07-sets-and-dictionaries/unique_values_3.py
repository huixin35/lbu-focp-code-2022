#!/usr/bin/env python3

if __name__ == '__main__':

    values = set()

    while True:
        next_value = input('--> ')

        if not next_value:
            break

        values.add(int(next_value))

    print(list(values))
