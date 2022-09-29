#!/usr/bin/env python3

if __name__ == '__main__':
    runs = 48426
    innings = 1014
    not_outs = 162

    average = runs / (innings - not_outs)

    print("Sir Geoffrey's Average was", average)
    print("Sir Geoffrey's Average was", round(average, 2))
