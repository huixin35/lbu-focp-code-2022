#!/usr/bin/env python3

if __name__ == '__main__':
    marks = []
    for i in range(5):
        marks.append(int(input(f'Enter mark #{i+1}: ')))

    max_mark = max(marks)
    min_mark = min(marks)
    avg_mark = sum(marks)/len(marks)

    print(f'Highest Mark: {max_mark}')
    print(f'Lowest Mark:  {min_mark}')
    print(f'Average Mark: {avg_mark:.2f}')
