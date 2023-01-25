from player import Player


class StubPlayer(Player):
    
    def get_name(self):
        return "stub"

    def shoot(self):
        return self.forced_shoot
    
    def always_shoot(self, shoot):
        self.forced_shoot = shoot
        