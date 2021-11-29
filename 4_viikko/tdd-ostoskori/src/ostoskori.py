from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.kori = []

    def tavaroita_korissa(self):
        return len(self.kori) 

    def hinta(self):
        return sum(ostos.hinta() for ostos in self.kori)

    def lisaa_tuote(self, lisattava: Tuote):
        self.kori.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.kori
