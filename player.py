class Player:

    def get_name(self):
        return None

    def start_match(self, round_count):
        pass

    def shoot(self, round_number):
        assert(False)

    def feedback(self, result, opp_shot):
        pass

    def shot_inc(self, shot):
        
        if shot == "R":
            return "P"
        elif shot == "P":
            return "S"
        elif shot == "S":
            return "R"
        
        assert(False)
        
    def shot_dec(self, shot):

        if shot == "R":
            return "S"
        elif shot == "P":
            return "R"
        elif shot == "S":
            return "P"
        
        assert(False)
