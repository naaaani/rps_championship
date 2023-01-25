from player import Player


class RockyPlayer(Player):
    
    def get_name(self):
        return "Rocky"

    def start_season(self):
        Player.start_season(self)
        print("Rocky rocks the season!")

    def start_match(self):
        Player.start_match(self)
        print("Rocky rocks the match!")

    def shoot(self):
        return "R"
    
    
