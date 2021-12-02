LOVE = 0
POINT = 1
THREE_POINTS = 3

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.players = {player1_name: LOVE, player2_name: LOVE}

    def won_point(self, player_name):
        self.players[player_name] += POINT

    def get_score(self):
        player1_score, player2_score = self.players.values()
        score = ""
        points = ["Love", "Fifteen", "Thirty", "Forty"]

        if player1_score == player2_score:
            if player1_score > THREE_POINTS:
                score = "Deuce"
            else:
                score = f"{points[player1_score]}-All"

        elif max(player1_score, player2_score) > THREE_POINTS:
            difference = abs(player1_score - player2_score)

            leading_player = max(self.players, key = self.players.get)

            if difference == POINT:
                score = f"Advantage {leading_player}"
            else:
                score = f"Win for {leading_player}"

        else:
            score = f"{points[player1_score]}-{points[player2_score]}"

        return score
