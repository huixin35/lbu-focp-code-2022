#!/usr/bin/env python3

if __name__ == '__main__':

    values = []

    while True:
        next_value = input('--> ')

        if not next_value:
            break

        values.append(int(next_value))

    unique = []
    for v in values:
        if v not in unique:
            unique.append(v)

    print(unique)
