# Funkcionális Specifikáció 

## 1. Bevezetés

### 1.1. Cél és Háttér
- A raktárkezelő program célja a raktárkészlet hatékony kezelése és áttekinthető nyilvántartása.

### 1.2. Projekt Téma
- A projekt célja egy olyan raktárkezelő rendszer létrehozása, amely lehetővé teszi az áruk követését, be- és kivitelezését, valamint az aktuális készlet állapotának megjelenítését.

## 2. Felhasználói Szerepek

### 2.1. Adminisztrátor
   - Felhasználók és raktárak kezelése.
   - Készletmozgások felügyelete.

### 2.2. Raktárkezelő
   - Áruk hozzáadása, szerkesztése, törlése.
   - Készletmozgások rögzítése.

### 2.3. Ellenőrzési Személyzet
   - Készletellenőrzés indítása és lezárása.
   - Raktári készlet állapotának ellenőrzése.

## 3. Funkcionális Követelmények

### 3.1. Felhasználói Bejelentkezés
   - A felhasználóknak be kell tudniuk jelentkezni a rendszerbe.

### 3.2. Raktárkezelés
   - Áru hozzáadása, szerkesztése és törlése.
   - Készletmozgások rögzítése (bevétel, kivétel).

### 3.3. Készlet Ellenőrzés
   - Ellenőrzési folyamat indítása és lezárása.
   - Készletellenőrzési eredmények rögzítése.

### 3.4. Riportok
   - Készítsen riportokat a készletállapotokról, készletmozgásokról és készletellenőrzésekről.

### 3.5. Jogosultságok
   - Különböző szintű jogosultságok biztosítása az egyes felhasználói szerepkörök számára.

## 4. Felülettel Szemben Támasztott Követelmények

### 4.1. Felhasználói Felület
   - Egyszerű és felhasználóbarát felhasználói felület készítése.

### 4.2. Mobil Kompatibilitás
   - A felhasználók számára biztosítsunk egy mobilbarát felületet.

### 4.3. Kereső Funkciók
   - Az áruk és tranzakciók könnyű keresését biztosítsuk.

## 5. Tesztelési Követelmények

### 5.1. Egységtesztek
   - Ellenőrizzük az egyes modulok helyes működését.

### 5.2. Rendszertesztek
   - Biztosítsuk, hogy az összekapcsolt modulok együtt megfelelően működjenek.

## 6. Adatvédelem és Biztonság

### 6.1. Felhasználói Adatok
   - Biztosítsuk a felhasználók személyes adatainak védelmét.

### 6.2. Tranzakciós Biztonság
   - Az adatbázis tranzakciók biztonságos kezelése.

## 7. Rendszerintegrációk

### 7.1. Külső Rendszerek
   - Az integráció más vállalati rendszerekkel.

## 8. Rendszerkorlátozások

### 8.1. Teljesítmény
   - Az alkalmazásnak hatékonyan kell kezelnie a nagy adatmennyiséget.

### 8.2. Keresztfunkcionalitás
   - A rendszernek kompatibilisnek kell lennie különböző böngészőkkel és operációs rendszerekkel.

