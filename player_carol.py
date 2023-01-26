from player import Player


class CarolPlayer(Player):
    
    def get_name(self):
        return "Carol"

    def start_match(self, round_count):
        Player.start_match(self, round_count)
        self.next_shot = "R"

    def feedback(self, result, opp_shot):
        
        if opp_shot == "R":
            self.next_shot = "P"
        elif opp_shot == "P":
            self.next_shot = "S"
        else:
            self.next_shot = "R"

    def shoot(self, round_number):
        return self.next_shot