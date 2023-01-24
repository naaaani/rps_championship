class Player:

    def get_name(self):
        return None

    def start_season(self):
        self.match_count = 0
        self.point = 0

    def start_match(self):
        self.match_count += 1

    def add_point(self, amount):
        self.point += amount

    def get_point(self):
        return self.point

