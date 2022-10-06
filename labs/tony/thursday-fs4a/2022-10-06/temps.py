#!/usr/bin/env python3

from statistics import mean


if __name__ == '__main__':
    temp_1 = float(input('Enter temperature at 08:00: ')[:-1])
    temp_2 = float(input('Enter temperature at 11:00: ')[:-1])
    temp_3 = float(input('Enter temperature at 14:00 ')[:-1])
    temp_4 = float(input('Enter temperature at 17:00: ')[:-1])
    temp_5 = float(input('Enter temperature at 20:00: ')[:-1])

    max_temp = max(temp_1, temp_2, temp_3, temp_4, temp_5)
    min_temp = min(temp_1, temp_2, temp_3, temp_4, temp_5)
    avg_temp = mean([temp_1, temp_2, temp_3, temp_4, temp_5])

    print()

    print('Highest Temp:  ', max_temp, 'C', sep='')
    print('Lowest Temp:   ', min_temp, 'C', sep='')
    print('Average Temp:  ', avg_temp, 'C', sep='')

    print()

    print('Highest Temp:  ', max(temp_1, temp_2, temp_3, temp_4, temp_5), 'C', sep='')
    print('Lowest Temp:   ', min(temp_1, temp_2, temp_3, temp_4, temp_5), 'C', sep='')
    print('Average Temp:  ', mean([temp_1, temp_2, temp_3, temp_4, temp_5]), 'C', sep='')

    print()

    print(f'Highest Temp: {max_temp:>7.1f}C')
    print(f'Lowest Temp:  {min_temp:>7.1f}C')
    print(f'Average Temp: {avg_temp:>7.1f}C')
