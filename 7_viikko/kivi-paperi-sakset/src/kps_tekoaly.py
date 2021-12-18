from tekoaly import Tekoaly
from tekoaly_parannettu import TekoalyParannettu
from kps import KPS

class KPSTekoaly(KPS):
    def __init__(self, parempi: bool=False):
        if parempi:
            self._tekoaly = TekoalyParannettu(10)
        else:
            self._tekoaly = Tekoaly()

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        self._tekoaly.aseta_siirto(ensimmaisen_siirto)
        return tokan_siirto
