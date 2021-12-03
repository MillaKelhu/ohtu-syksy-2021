class Summa:
    def __init__(self, sovellus, syotteen_luku, historia):
        self._sovellus = sovellus
        self._syotteen_luku = syotteen_luku
        self._historia = historia
        self._syotteet = []

    def _uusi_syote(self):
        syote = self._syotteen_luku()
        self._syotteet.append(syote)
        return syote

    def suorita(self):
        self._sovellus.plus(self._uusi_syote())
        self._historia.append(self.kumoa)
    
    def kumoa(self):
        edellinen_syote = self._syotteet.pop()
        self._sovellus.miinus(edellinen_syote)

class Erotus:
    def __init__(self, sovellus, syotteen_luku, historia):
        self._sovellus = sovellus
        self._syotteen_luku = syotteen_luku
        self._historia = historia
        self._syotteet = []

    def _uusi_syote(self):
        syote = self._syotteen_luku()
        self._syotteet.append(syote)
        return syote

    def suorita(self):
        self._sovellus.miinus(self._uusi_syote())
        self._historia.append(self.kumoa)
    
    def kumoa(self):
        edellinen_syote = self._syotteet.pop()
        self._sovellus.plus(edellinen_syote)

class Nollaus:
    def __init__(self, sovellus, tuloksen_luku, historia):
        self._sovellus = sovellus
        self._tuloksen_luku = tuloksen_luku
        self._historia = historia
        self._tulokset = []

    def _tallenna_vanha_tulos(self):
        tulos = self._tuloksen_luku()
        self._tulokset.append(tulos)

    def suorita(self):
        self._tallenna_vanha_tulos()
        self._sovellus.nollaa()
        self._historia.append(self.kumoa)
    
    def kumoa(self):
        edellinen_tulos = self._tulokset.pop()
        self._sovellus.plus(edellinen_tulos)

class Kumoa:
    def __init__(self, sovellus, historia):
        self._sovellus = sovellus
        self._historia = historia

    def suorita(self):
        try:
            komento = self._historia.pop()
            komento()
        except Exception:
            pass
