from playerreader import PlayerReader
from player import Player

class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality: str):
        players = list(filter(lambda player: player.nationality == nationality, self.reader.get_players()))
        players.sort(key=lambda player: player.goals+player.assists, reverse=True)

        return players
