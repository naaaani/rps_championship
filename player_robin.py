from player import Player


class RobinPlayer(Player):
    
    def get_name(self):
        return "Robin"

    def start_match(self):
        Player.start_match(self)
        self.shoot_tracker = 0
        print("Robin around the match!")

    def shoot(self):
        
        options = ("R", "P", "S")
        shoot = options[self.shoot_tracker]
        
        self.shoot_tracker +=1
        if self.shoot_tracker > 2:
            self.shoot_tracker = 0

        return shoot
