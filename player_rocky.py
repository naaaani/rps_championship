from player import Player


class RockyPlayer(Player):
    
    def get_name(self):
        return "Rocky"

    def start_season(self):
        Player.start_season(self)
    
    def start_match(self):
        Player.start_match(self)

    def shoot(self):
        return "R"
    
    
