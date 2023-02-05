from player import Player


class RobinPlayer(Player):
    
    def __init__(self, first_shoot="R"):
        super().__init__()

        if first_shoot == "R":
            self.init_shoot = 0
            self.name_postfix = "Rock"

        elif first_shoot == "P":
            self.init_shoot = 1
            self.name_postfix = "Paper"
            
        else:
            self.init_shoot = 2
            self.name_postfix = "Scissors"

    def get_name(self):
        return "Round Robin " + self.name_postfix
 
    def start_match(self, round_count):
        Player.start_match(self, round_count)
        self.shoot_tracker = self.init_shoot

    def shoot(self, round_number):
    
        options = ("R", "P", "S")
        shoot = options[self.shoot_tracker]
        
        self.shoot_tracker += 1
        if self.shoot_tracker > 2:
            self.shoot_tracker = 0

        return shoot
