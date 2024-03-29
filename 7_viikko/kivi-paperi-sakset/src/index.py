from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        pelit = {
                'a': KPSPelaajaVsPelaaja(),
                'b': KPSTekoaly(),
                'c': KPSTekoaly(parempi=True)
                }
        try:
            peli = pelit[vastaus]
            peli.pelaa()
        except Exception:
            break


if __name__ == "__main__":
    main()
