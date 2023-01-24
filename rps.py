#!/usr/bin/python3

from player_robin import Robin
from player_rocky import Rocky
from match import Match
from season import Season

def main():

    m = Match(Rocky(), Robin())
    m.play_match()


    quit()
    season = Season()
    season.add(Rocky)



if __name__ == "__main__":
    main()
