class IntJoukko:
    def __init__(self, kapasiteetti: int=5, kasvatuskoko: int=5):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")
        else:
            self.kapasiteetti = kapasiteetti

        self.kasvatuskoko = kasvatuskoko

        self.luvut = []

    def kuuluu(self, n):
        return n in self.luvut

    def lisaa(self, n):
        if not self.kuuluu(n):
            self.luvut.append(n)

            return True

        return False

    def poista(self, n):
        if self.kuuluu(n):
            self.luvut.remove(n)
            return True

        return False

    def kopioi_taulukko(self, a, b):
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return len(self.luvut)

    def to_int_list(self):
        return self.luvut

    @staticmethod
    def yhdiste(a, b):
        palautus = IntJoukko()

        for alkio in a.luvut + b.luvut:
            palautus.lisaa(alkio)

        return palautus

    @staticmethod
    def leikkaus(a, b):
        palautus = IntJoukko()

        for alkio in a.luvut:
            if b.kuuluu(alkio):
                palautus.lisaa(alkio)

        return palautus

    @staticmethod
    def erotus(a, b):
        palautus = IntJoukko()

        for alkio in a.luvut:
            if not b.kuuluu(alkio):
                palautus.lisaa(alkio)

        return palautus

    def __str__(self):
        str_lista = "{" + ', '.join(str(alkio) for alkio in self.luvut) + "}"
        return str_lista