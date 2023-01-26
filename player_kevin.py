from player import Player


class KevinPlayer(Player):
    
    def get_name(self):
        return "Kevin"

    def start_match(self):
        Player.start_match(self)
        self.prev_shot = "R"

    def feedback(self, result, opp_shot):
        self.prev_shot = opp_shot

    def shoot(self):
        return self.prev_shot
        
        
