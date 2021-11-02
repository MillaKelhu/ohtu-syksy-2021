import unittest
from statistics import sort_by_points, Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_sort_by_points_returns_points(self):
        points = sort_by_points(Player("Semenko", "EDM", 4, 12))

        self.assertEqual(points, 16)

    def test_search_works_with_valid_input(self):
        player = self.statistics.search("Semenko").__str__()

        self.assertEqual(player, "Semenko EDM 4 + 12 = 16")

    def test_search_returns_None_with_invalid_input(self):
        player = self.statistics.search("Smith")

        self.assertEqual(player, None)

    def test_team_works_with_valid_input(self):
        team = self.statistics.team("EDM")
        team_str = []
        for player in team:
            team_str.append(player.__str__())

        self.assertEqual(team_str, [
            "Semenko EDM 4 + 12 = 16",
            "Kurri EDM 37 + 53 = 90",
            "Gretzky EDM 35 + 89 = 124"
        ])

    def test_top_scorers_works(self):
        players = self.statistics.top_scorers(2)
        players_str = []
        for player in players:
            players_str.append(player.__str__())

        self.assertEqual(players_str, [
            "Gretzky EDM 35 + 89 = 124",
            "Lemieux PIT 45 + 54 = 99",
            "Yzerman DET 42 + 56 = 98"
        ])
