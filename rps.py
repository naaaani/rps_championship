#!/usr/bin/python3

from player_rocky import Rocky

def main():

    rocky = Rocky()
    rocky.start_season()

    rocky.start_match()
    answer = rocky.shoot()


if __name__ == "__main":
    main()
