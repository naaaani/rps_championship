from player import Player


class CoolPlayer(Player):
    
    def get_name(self):
        return "Cool"

    def start_match(self, round_count):
        Player.start_match(self, round_count)
        self.next_shot = "R"

    def feedback(self, result, opp_shot):
        
        if result == 1:
            return
        
        if self.next_shot == "R":
            self.next_shot = "P"
        elif self.next_shot == "P":
            self.next_shot = "S"
        else:
            self.next_shot = "R"

    def shoot(self, round_number):
        return self.next_shot