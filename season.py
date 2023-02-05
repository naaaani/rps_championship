from match import Match

class Entry:
    pass

class Season:

    def __init__(self, round_count):

        self.table = []
        self.r = round_count

    def add_player(self, player):

        entry = Entry()
        entry.player = player
        entry.pts = 0
        entry.win = 0
        entry.draw = 0
        entry.lose = 0

        self.table.append(entry)

    def dump(self):

        print("Results")

        for entry in sorted(self.table, reverse=True, key=lambda x: x.pts):

            print(" ",
                  entry.player.get_name(),
                  entry.pts,
                  "-",
                  entry.win,
                  entry.draw,
                  entry.lose
                  )

    def play_match(self, e1, e2):

        p1 = e1.player
        p2 = e2.player

        match = Match(p1, p2, self.r)
        (winner, wc1, wc2) = match.play_match()

        if winner == 1:
            e1.pts += 2
            e1.win += 1
            e2.lose += 1
        elif winner == 2:
            e2.pts += 2
            e2.win += 1
            e1.lose += 1
        else:
            e1.pts += 1
            e1.draw += 1
            e2.pts += 1
            e2.draw += 1

        print(" ", p1.get_name(), "-", p2.get_name(), ":", wc1, "-", wc2)

    def perform_season(self):

        print("Matches")
        for i1 in range(len(self.table)):
            for i2 in range(i1, len(self.table)):
                if i1 == i2:
                    continue

                self.play_match(self.table[i1], self.table[i2])
