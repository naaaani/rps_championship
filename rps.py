#!/usr/bin/python3

from player_robin import RobinPlayer
from player_rocky import RockyPlayer
from player_stub import StubPlayer
from match import Match
from season import Season

def main():
 
    season = Season()
    season.add_player(RockyPlayer())
    season.add_player(RobinPlayer())
    p3 = StubPlayer()
    p3.always_shoot("P")
    season.add_player(p3)

    season.perform_season()

    season.dump()

if __name__ == "__main__":
    main()
