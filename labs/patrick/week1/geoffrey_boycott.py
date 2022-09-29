#!/usr/bin/env python3

if __name__ == '__main__':
    player = "Geoffrey Boycott"
    games = 609
    batted = 1014
    not_out = 162
    total_score = 48426

    print("Player:", player, sep=" ")
    print("Played " + str(games) + " Matches")
    print(f'Average score  {total_score/(batted-not_out):.2f}')
