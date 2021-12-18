class Tekoaly:
    def __init__(self):
        self._siirto = 0

    def anna_siirto(self):
        return "psk"[self._siirto]

    def aseta_siirto(self, siirto):
        self._siirto += 1
        if self._siirto > 2:
            self._siirto -= 3
