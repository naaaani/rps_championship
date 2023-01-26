class Match():

    def __init__(self, player1, player2):

        self.player1 = player1
        self.player2 = player2

        player1.start_match()
        player2.start_match()


    def play_match(self):
       
        self.win_count_p1 = 0
        self.win_count_p2 = 0
        self.draw_count = 0

        for i in range(5):

            winner = self.perform_round()

            if winner == 1:
                self.win_count_p1 += 1
            elif winner == 2:
                self.win_count_p2 += 1
            else:
                self.draw_count += 1
        
        if self.win_count_p1 > self.win_count_p2:
            result = 1    
        elif self.win_count_p1 < self.win_count_p2:
            result = 2
        else:
            result = 3
        
        return (result, self.win_count_p1, self.win_count_p2)

    def perform_round(self):

        shoot1 = self.player1.shoot()
        shoot2 = self.player2.shoot()
        winner = self.get_winner(shoot1, shoot2)
        
        return winner

    def get_winner(self, shoot1, shoot2):

        assert(shoot1 == "R" or shoot1 == "S" or shoot1 == "P")
        assert(shoot2 == "R" or shoot2 == "S" or shoot2 == "P")

        if shoot1 == shoot2:
            return 3
        
        if shoot1 == "R" and shoot2 == "S": return 1
        if shoot1 == "R" and shoot2 == "P": return 2
        if shoot1 == "P" and shoot2 == "S": return 2
        if shoot1 == "P" and shoot2 == "R": return 1
        if shoot1 == "S" and shoot2 == "R": return 2
        if shoot1 == "S" and shoot2 == "P": return 1

    