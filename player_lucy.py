from player import Player

class LucyPlayer(Player):
    
    def get_name(self):
        return "Lucy"

    def start_match(self, round_count):
        Player.start_match(self, round_count)

        self.p1 = round_count / 3
        self.p2 = (round_count / 3) * 2

    def shoot(self, round_number):

        if round_number <= self.p1:
            return "R"
        elif round_number > self.p2:
            return "S"
        else:
            return "P"
        
        assert(False)