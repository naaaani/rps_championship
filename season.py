from match import Match


class Season:

    def __init__(self, round_count):

        self.table = []
        self.r = round_count

    def add_player(self, player):

        self.table.append([player, 0, 0, 0, 0])

    def dump(self):

        print("Results")

        for entry in sorted(self.table, reverse=True, key=lambda x: x[1]):

            print(" ",
                  entry[0].get_name(),
                  entry[1],
                  "-",
                  entry[2],
                  entry[3],
                  entry[4]
                  )

    def play_match(self, e1, e2):

        p1 = e1[0]
        p2 = e2[0]

        match = Match(p1, p2, self.r)
        (winner, wc1, wc2) = match.play_match()

        if winner == 1:
            e1[1] += 2
            e1[2] += 1
            e2[3] += 1
        elif winner == 2:
            e2[1] += 2
            e2[2] += 1
            e1[3] += 1
        else:
            e1[1] += 1
            e2[1] += 1
            e1[4] += 1
            e2[4] += 1

        print(" ", p1.get_name(), "-", p2.get_name(), ":", wc1, "-", wc2)

    def perform_season(self):

        print("Matches")
        for i1 in range(len(self.table)):
            for i2 in range(i1, len(self.table)):
                if i1 == i2:
                    continue

                self.play_match(self.table[i1], self.table[i2])
