from playerreader import PlayerReader
from playerstats import PlayerStats
import datetime

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    print(f"Players from FIN {datetime.datetime.now()}")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()
