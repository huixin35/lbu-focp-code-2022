#!/usr/bin/env python3

if __name__ == '__main__':

    group_size = 24
    students = 175

    labs_needed = students // group_size
    left_over = students % group_size

    print(students, 'students need', labs_needed, 'labs with', left_over, 'left over.')
    print(f'{students} students need {labs_needed} labs with {left_over} left over.')
