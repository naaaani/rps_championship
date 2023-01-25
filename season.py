from match import Match

class Season:

    def __init__(self):

        self.table = []

    def add_player(self, player):
        
        self.table.append([player, 0])

    def dump(self):
        
        print("Dump:")

        for entry in self.table:

            print(entry[0].get_name(), entry[1]) 

    def perform_season(self):

        for i1 in range(len(self.table)):
            for i2 in range(i1, len(self.table)):
                if i1 == i2:
                    continue

                self.play_match(self.table[i1], self.table[i2])
    
    def play_match(self, e1, e2):

        p1 = e1[0]
        p2 = e2[0]

        match = Match(p1, p2)
        winner = match.play_match()
        