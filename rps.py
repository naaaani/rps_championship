#!/usr/bin/python3

from player_robin import RobinPlayer
from player_rocky import RockyPlayer
from match import Match
from season import Season

def main():

    m = Match(RockyPlayer(), RobinPlayer())
    #m.play_match()
    m.perform_round()


    quit()
    season = Season()
    season.add(RockyPlayer)



if __name__ == "__main__":
    main()
