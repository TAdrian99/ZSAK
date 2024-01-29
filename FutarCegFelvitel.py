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
class Futar(Szemely):
    def __init__(self, nev, cim, telefon, futar_nev):
        super().__init__(nev, cim, telefon)
        self.futar_nev = futar_nev

    @property
    def futar_nev(self):
        return self._futar_nev

    @futar_nev.setter
    def futar_nev(self, value):
        if value == "":
            raise ValueError("A futár cég neve nem lehet üres!")
        self._futar_nev = value
def futar_felvitel():
    try:
        nev = input("Adja meg a futár cég nevét (vagy 0 a kilépéshez): ")
        if nev == '0':
            print("Visszatérés a főmenübe.")
            return

        cim = input("Adja meg a címet: ")
        telefon = input("Adja meg a telefonszámot: ")
        futar_nev = input("Adja meg a futár cég nevét: ")

        futar = Futar(nev, cim, telefon, futar_nev)

        # Az adatokat egy szövegfájlba írjuk
        with open("futarok.txt", "a", encoding='utf-8') as f:
            f.write(f"Futár név: {futar_nev}\n")
            f.write(f"Név: {nev}\nCím: {cim}\nTelefon: {telefon}\n")
            f.write("-------------------------\n")

        print("A futár cég felvéve az adatbázisba.")
        input("Nyomja meg az entert a főmenübe való visszatéréshez...")

    except Exception as e:
        print(f"Hiba történt: {e}")

