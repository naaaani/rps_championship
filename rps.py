#!/usr/bin/python3

from player_rocky import Rocky

def main():

    rocky = Rocky()
    rocky.start_season()

    rocky.start_match()
    answer = rocky.shoot()
    print(rocky.get_name() + " says: " + answer)

if __name__ == "__main__":
    main()
