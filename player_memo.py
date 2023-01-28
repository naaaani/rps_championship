from player import Player


class MemoPlayer(Player):

    def get_name(self):
        return "Memo"

    def start_match(self, round_count):
        Player.start_match(self, round_count)
        
        self.mem = {"R": 0, "P": 0, "S": 0}
        self.round_count = round_count
        self.last_shot = "R"

    def feedback(self, result, opp_shot):
        
        if result == 1:
            self.mem[self.last_shot] += 6
        elif result == 2:
            self.mem[opp_shot] += 3
        else:
            self.mem[self.last_shot] += 2
        
    def shoot(self, round_number):

        if round_number < (self.round_count * 0.6):
            self.last_shot = self.shot_inc(self.last_shot)
        
        else:            
            best = 0
            self.last_shot = "R"
            
            for shot in ("R", "P", "S"):                           
                if best >= self.mem[shot]:
                    continue                
                best = self.mem[shot]
                self.last_shot = shot
            
        return self.last_shot
                