from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

#    Esimerkki matcher
#    matcher = And(
#        HasAtLeast(5, "goals"),
#        HasAtLeast(5, "assists"),
#        PlaysIn("PHI")
#    )

#    Tehtävä 2 matcher testaus
    matcher = And(
        Not(HasAtLeast(1, "goals")),
        PlaysIn("NYR")
    )


    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
