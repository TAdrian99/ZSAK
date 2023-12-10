class Futarceg:
    def __init__(self, nev, cim, telefon):
        if not nev or not isinstance(nev,str):
            raise ValueError("A név nem lehet null vagy üres!")
        else:
            cleaned_nev = nev.strip().title()
            self.nev = cleaned_nev
        if not cim or not isinstance(cim,str):
            raise ValueError("A cím nem lehet null vagy üres!")
        else:
            cleaned_cim = cim.strip().title()
            self.cim = cleaned_cim
        if not telefon or not isinstance(telefon,str):
            raise ValueError("A telefon nem lehet null vagy üres!")
        if not telefon.startswith("+"):
            raise ValueError("Csak nemzetközi telefonszám adható meg, így a kezdőkarakter mindenféleképpen +")
        if len(telefon) <= 8 or len(telefon) > 20:
            raise ValueError("A telefonszám legalább 8 karakter hosszú vagy 20 karakternél rövidebbnek kell lennie!")
        else:
            cleaned_telefon = telefon.strip()
            self.telefon = cleaned_telefon
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



