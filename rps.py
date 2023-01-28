#!/usr/bin/python3

from match import Match
from season import Season

from player_robin import RobinPlayer
from player_kevin import KevinPlayer
from player_stub import StubPlayer
from player_carol import CarolPlayer
from player_cool import CoolPlayer
from player_lucy import LucyPlayer
from player_memo import MemoPlayer

def main():
    
    season = Season(100)
    season.add_player(RobinPlayer())
    season.add_player(KevinPlayer())
    season.add_player(CarolPlayer())
    season.add_player(CoolPlayer())
    season.add_player(LucyPlayer())
    season.add_player(MemoPlayer())

    p = StubPlayer()
    p.always_shoot("P")
    p.set_name("Paper Pierre")
    season.add_player(p)

    p = StubPlayer()
    p.always_shoot("R")
    p.set_name("Rocky Rock")
    season.add_player(p)

    p = StubPlayer()
    p.always_shoot("S")
    p.set_name("Scissors Simon")
    season.add_player(p)

    season.perform_season()
    season.dump()

if __name__ == "__main__":
    main()
