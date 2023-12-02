class Szemely:
    def __init__(self, nev, cim, telefon):
        self.nev = nev
        self.cim = cim
        self.telefon = telefon

    @property
    def nev(self):
        return self._nev

    @nev.setter
    def nev(self, value):
        if value == "":
            raise ValueError("A név nem lehet üres!")
        self._nev = value

    @property
    def telefon(self):
        return self._telefon

    @telefon.setter
    def telefon(self, value):
        if not value.startswith("+36"):
            raise ValueError("A telefonszám +36-tal kell kezdődjön!")
        self._telefon = value



