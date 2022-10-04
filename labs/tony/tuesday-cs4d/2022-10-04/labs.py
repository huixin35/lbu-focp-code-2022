#!/usr/bin/env python3

if __name__ == '__main__':

    students = int(input('How many students? '))
    labs_size = int(input('Required lab size? '))

    groups = students // labs_size
    left_over = students % labs_size

    print(f'There will be {groups} group{"" if groups == 1 else "s"} with '
          f'{left_over} student{"" if left_over == 1 else "s"} left over.')
