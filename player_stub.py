from player import Player


class StubPlayer(Player):
    
    def __init__(self):
        self.name = "stub"
    
    def get_name(self):
        return self.name

    def shoot(self, round_number):
        return self.forced_shoot
    
    def always_shoot(self, shoot):
        self.forced_shoot = shoot
    
    def set_name(self, name):
        self.name = name
        