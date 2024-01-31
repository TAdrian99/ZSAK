# Tesztelési Jegyzőkönyv - 0.1.2

## 1. Bevezetés

### 1.1. Cél és Háttér
- A tesztelési jegyzőkönyv célja a raktárkezelő program funkcióinak és teljesítményének ellenőrzése.

### 1.2. Projekt Téma
- Raktárkezelő rendszer tesztelése és értékelése.

## 2. Tesztelési Célok

### 2.1. Funkcionális Tesztek
   - Árukezelés (hozzáadás, szerkesztés, törlés)
   - Készletmozgások rögzítése
   - Készletellenőrzési folyamatok
   - Kiszállítási dátum módosítása (7-es pont)
   - Futár cég felvitel (8-as pont)
   - Fuvarozó hozzárendelése (9-es pont)
   - Adott futárcéghez tartozó terméklista (10-es pont)

### 2.2. Teljesítménytesztek
   - Rendszer válaszidők ellenőrzése nagy adatmennyiség esetén.
   - Terheléses tesztek a szerver stabilitásának vizsgálatára.

## 3. Tesztelési Környezet

### 3.1. Hardver
   - Szerver: 4 magos, 2.5 GHz, 16 GB RAM
   - Kliens: Böngésző (Chrome, Firefox, Safari)

### 3.2. Szoftver
   - Operációs rendszer: Linux (szerver), Windows
   - Böngészők: Chrome v90, Firefox v87, Safari v14
   - Python v3.x, Flask, SQLAlchemy

## 4. Tesztesetek és Eredmények

### 4.1. Funkcionális Tesztek

#### 4.1.1. Árukezelés
   - Teszteset: Új áru hozzáadása
     - Eredmény: Az áru sikeresen hozzá lett adva.
    
     - ![image](https://github.com/TAdrian99/ZSAK/assets/150531076/fd7fbe65-21a9-4563-95a8-3ede8e411584)


#### 4.1.2. Készletmozgások
   - Teszteset: Bevétel rögzítése
     - Eredmény: A bevétel rögzítése sikeres volt.

#### 4.1.3. Készletellenőrzés
   - Teszteset: Ellenőrzési folyamat indítása
     - Eredmény: Az ellenőrzés sikeresen elindult.

#### 4.1.4. Kiszállítási Dátum Módosítása
   - Teszteset: Kiszállítási dátum módosítása
     - Eredmény: A kiszállítási dátum sikeresen módosult.

#### 4.1.5. Futár Cég Felvitel
   - Teszteset: Új futár cég felvitele
     - Eredmény: A futár cég sikeresen fel lett véve.

#### 4.1.6. Fuvarozó Hozzárendelése
   - Teszteset: Fuvarozó hozzárendelése
     - Eredmény: A fuvarozó sikeresen hozzá lett rendelve a megfelelő futár céghez.


#### 4.1.7. Adott Futárcéghez Tartozó Terméklista
   - Teszteset: Futárcéghez tartozó terméklista lekérése
     - Eredmény: A terméklista megfelelően vissza lett adva.

### 4.2. Teljesítménytesztek

#### 4.2.1. Terheléses Teszt
   - Teszteset: Nagy adatmennyiségű kérés kezelése
     - Eredmény: A rendszer stabil marad nagy terhelés esetén is.


# 5. Hibajelentések

### 5.1. Felületi Hibák

#### 5.1.1. Menü Hibái
  - A menü kiválasztásánál elírás történt. Az utolsó menüpont a "10. Adott futárcéghez tartozó terméklista", de a a kiválasztásnál csak 0-9-ig szerepelnek a lehetőségek. Javaslom a kijavítását az egyértelműség érdekében.

### 5.2. Funkcionális Hibák
#### 5.2.1. Adatkezelési Funkciók Nem Működnek

Az alábbi funkciók jelenleg nem működnek:

  - Kiszállítási dátum módosítása (7. pont)
  - Futár cég felvitel (8. pont)
  - Fuvarozó hozzárendelése (9. pont)
  - Adott futárcéghez tartozó terméklista (10. pont)

# 6. Összegzés

A tesztelés során néhány hiba és hiányosság került azonosításra:

- Felületi Hibák: A menü egy részénél az elírások okozhatnak félreértéseket a felhasználók számára. Ezt javasolt kijavítani az egyértelműség és a felhasználói élmény javítása érdekében.

- Funkcionális Hibák: Több funkció nem működik megfelelően, beleértve a kiszállítási dátum módosítását, futár cég felvitelét, fuvarozó hozzárendelését és az adott futárcéghez tartozó terméklista lekérdezését. Ezeket a funkciókat szükséges javítani a program teljes funkcionalitásának biztosítása érdekében.

Az összegzés alapján szükséges további fejlesztések és javítások a program teljes funkcionalitásának és felhasználói élményének biztosítása érdekében. A fejlesztőcsapatnak ajánlott ezeket a hibákat prioritással kezelni és frissítéseket szállítani a stabil működés érdekében.







