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

    def get_nev(self):
        return self.nev

    def set_nev(self, value):
        if not value or not isinstance(value,str):
            raise ValueError("A név mező nem lehet null vagy üres!")
        else:
            cleaned_value = value.strip().title()
            self.nev = cleaned_value
        
    def get_cim(self):
        return self.cim

    def set_cim(self, value):
        if not value or not isinstance(value,str):
            raise ValueError("A cím mező nem lehet null vagy üres!")
        else:
            cleaned_value = value.strip().title()
            self.nev = cleaned_value    

    def get_telefonszam(self):
        return self.telefon

    def set_cim(self, value):
        if not value or not isinstance(value,str):
            raise ValueError("A telefon nem lehet null vagy üres!")
        if not value.startswith("+"):
            raise ValueError("Csak nemzetközi telefonszám adható meg, így a kezdőkarakter mindenféleképpen +")
        if len(value) <= 8 or len(value) > 20:
            raise ValueError("A telefonszám legalább 8 karakter hosszú vagy 20 karakternél rövidebbnek kell lennie!")
        else:
            cleaned_telefon = value.strip()
            self.telefon = cleaned_telefon


