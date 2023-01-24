#!/usr/bin/python3

from player_rocky import Rocky
from match import Match

def main():

    rocky1 = Rocky()
    rocky2 = Rocky()
    
    print("Starting season")
    rocky1.start_season()
    rocky2.start_season()
    
    match = Match(rocky1, rocky2)
    match.perform_round()    

if __name__ == "__main__":
    main()
