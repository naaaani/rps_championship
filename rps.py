#!/usr/bin/python3

from player_robin import RobinPlayer
from player_kevin import KevinPlayer
from player_stub import StubPlayer
from match import Match
from season import Season

def main():
 
    season = Season()
    season.add_player(RobinPlayer())
    season.add_player(KevinPlayer())

    p = StubPlayer()
    p.always_shoot("P")
    p.set_name("Pierre")
    season.add_player(p)

    p = StubPlayer()
    p.always_shoot("R")
    p.set_name("Rocky")
    season.add_player(p)

    p = StubPlayer()
    p.always_shoot("S")
    p.set_name("Simon")
    season.add_player(p)

    season.perform_season()

    season.dump()

if __name__ == "__main__":
    main()
