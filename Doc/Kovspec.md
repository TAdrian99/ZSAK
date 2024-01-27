# Jelenlegi helyzet leírása:

A raktárkezelő program célja a raktárak hatékony és pontos kezelése, valamint a készletnyilvántartás optimalizálása. A programnak lehetőséget kell biztosítania a raktárkészlet nyomon követésére, a beérkező és kimenő áruk kezelésére, valamint különböző riportok és elemzések generálására.
**Az adminisztrációs idő nagy mértékben csökkenthető, ha egy jól megtervezett programban kezeljük papir forma helyett.**
**A raktárban dolgozó adminsztratív kollegák, ma már szívesebben rögzítenek digitálisan, mint papir alapon, hiszen jobban lekövethető és nyomonkövethető a leltározás.**




# Megrendelői igényspecifikáció (megrendelő által megfogalmazott igények, célok, követelmények):

## Megrendelői vízió (Vágyálom)
Cégünk egy dinamikusan fejlődő vállalat, amely folyamatosan bővíti termékpalettáját és piaci részesedését. A vágyunk, hogy a raktári folyamatainkat modern és hatékony rendszerrel optimalizáljuk, amely támogatja a gyors üzleti döntéseket, minimalizálja az emberi hibákat és növeli a készletek hatékony kihasználását.

## Megrendelői cél: 

1. Valós idejű Készletnyilvántartás: Az ideális rendszerünk valós idejű információkat szolgáltat a készleteinkről. Szeretnénk látni a pontos mennyiségeket, mozgásokat és készletváltozásokat minden pillanatban.

2. Gyors és Egyszerű Árukezelés: Az áruk beérkezése és kimenete könnyedén kezelhető legyen a rendszeren keresztül. Az egyszerű és intuitív interfész segítse a felhasználóinkat a hatékonyabb munkavégzésben.

3. Riportok és Elemzések: Fontos, hogy könnyen hozzáférhessünk olyan riportokhoz és elemzésekhez, amelyek segítenek a készletgazdálkodás optimalizálásában, az értékesítési trendek felismerésében és a beszerzési stratégia kidolgozásában.

4. Rendszerintegráció: A programnak támogatnia kell a harmadik fél szoftverekkel való integrációt, különösen a pénzügyi és értékesítési rendszerekkel, hogy az információk egységesen kezelhetők legyenek.

5. Skálázhatóság: Várjuk, hogy a raktárkezelő rendszer könnyen skálázható legyen, és alkalmazkodjon a cégünk növekvő igényeihez és volumenéhez.

6. Adatbiztonság: A rendszerünknek biztonságosnak kell lennie, és garantálnia kell az érzékeny adatok védelmét. Csak a megfelelő jogosultságokkal rendelkező személyek férhetnek hozzá a kritikus információkhoz.

A fentiekben vázolt vízió mentén szeretnénk kialakítani és bevezetni egy raktárkezelő programot, amely nem csak megfelel az aktuális igényeinknek, de a jövőbeli kihívásokra is rugalmas választ ad. A programnak hozzá kell járulnia a cégünk hatékonyságához, növekedéséhez és versenyképességéhez a piacon.

## Megrendelői követelmény:

1. Készletnyilvántartás

   1.1. A rendszernek valós idejű készletnyilvántartást kell biztosítania az összes raktárban.

   1.2. Képesnek kell lennie követni az egyes termékek mennyiségét és állapotát.

   1.3. Automatikus riasztásokat kell generálnia alacsony készlet vagy lejáró termék esetén.

2. Árukezelés

   2.1. Egyszerű és intuitív felületen keresztül kezelhető legyen az áruk beérkezése és kimenete.

   2.2. Lehetőség legyen batch-számok, lejárati dátumok és egyéb jellemzők rögzítésére.

   2.3. A rendszernek támogatnia kell a különböző egységállományok kezelését.

3. Riportok és Elemzések

   3.1. Készletriportokkal rendelkezzen, amelyek részletesen mutatják be a készletmozgásokat és változásokat.

   3.2. Lehetőség legyen testreszabott riportok készítésére az értékesítési adatok, beszerzések és egyéb releváns információk alapján.

4. Rendszerintegráció

   4.1. Támogassa a harmadik fél alkalmazásokkal történő integrációt, különösen pénzügyi és értékesítési rendszerekkel.

   4.2. API-kat biztosítson az egyszerű és hatékony adatcseréhez más vállalati rendszerekkel.

5. Biztonság és Jogosultságok

   5.1. Az adatoknak biztonságosan kell tárolódnia, és csak a megfelelő jogosultságokkal rendelkező felhasználók férhetnek hozzá.

   5.2. Az auditálhatóságot és naplózást biztosítson minden készletmozgásról és felhasználói tevékenységről.

6. Felhasználói Képzés és Támogatás

   6.1. Nyújtson részletes felhasználói dokumentációt és képzéseket a rendszer hatékony használatához.
   6.2. Biztosítson könnyen elérhető támogatási csatornákat, amelyeken keresztül a felhasználók segítséget kaphatnak.

7. Skálázhatóság

   7.1. A rendszernek skálázhatónak kell lennie, hogy alkalmazkodni tudjon a vállalatunk növekvő igényeihez és volumenéhez.

8. Teljesítmény

   8.1. A rendszernek gyors és hatékony teljesítményt kell nyújtania a napi tevékenységek során.
   8.2. Minimálisra kell csökkentenie az esetleges leállásokat és rendszerhibákat.

###### Megrendelői igényspecifikáció:

1. Felhasználói Interfész

   1.1. Bejelentkezés és Jogosultságok:
   A rendszernek biztosítania kell biztonságos bejelentkezést, és különböző jogosultságokkal kell rendelkeznie (pl. adminisztrátor, raktárkezelő, munkatárs).

   1.2. Raktárat Megjelenítő Felület:
   Az áruk könnyen áttekinthetők legyenek, és a felhasználók könnyen kereshessenek és rendezhessenek a készletben.

   1.3. Árukezelés:
   Az áruk beérkezésének és kimenetének rögzítése intuitív módon történjen, és legyen lehetőség kiegészítő információk (batch-számok, lejárati dátumok) rögzítésére.

2. Készletnyilvántartás

   2.1. Valós Idejű Készletinformációk:
   A rendszernek valós idejű készletinformációkat kell szolgáltatnia, beleértve az összes raktárat és áru típust.

   2.2. Riasztások:
   Automatikus riasztásokat kell generálnia alacsony készlet, lejáró termék vagy egyéb kritikus események esetén.

3. Riportok és Elemzések

   3.1. Készletriportok:
   Legyen lehetőség a készletriportok testreszabására, és ezek a riportok mutassák be a készletmozgásokat, változásokat és az áruállományt.

   3.2. Eladási Riportok:
   Riportokat kell generálnia az értékesítési adatokról, ügyfelek vásárlási szokásairól és az eladások trendjeiről.

4. Rendszerintegráció

   4.1. API-k:
   A rendszernek támogatnia kell az API-kat más vállalati rendszerekkel (pénzügyi, értékesítési rendszerek) való kommunikáció céljából.

   4.2. Import/Export Funkciók:
   Legyen lehetőség adatok importálására és exportálására más formátumokban.

5. Biztonság és Jogosultságok

   5.1. Adatbiztonság:
   Az adatoknak szigorúan védetteknek kell lenniük, és a rendszernek védenie kell a jogosulatlan hozzáférést és adatvesztést.

   5.2. Jogosultságkezelés:
   A rendszernek részletes jogosultságkezelést kell biztosítania, lehetővé téve, hogy csak az arra jogosult személyek férjenek hozzá bizonyos funkciókhoz.

6. Skálázhatóság

   6.1. Jövőbeli Igényekre Való Felkészülés:
   A rendszernek rugalmasnak kell lennie, és könnyen skálázhatónak, hogy alkalmazkodjon a vállalat növekvő igényeihez és volumenéhez.

7. Felhasználói Képzés és Támogatás

   7.1. Dokumentáció:
   Teljes és érthető felhasználói dokumentációval kell rendelkeznie.

   7.2. Támogatás:
   Az alkalmazásnak biztosítania kell könnyen elérhető támogatási csatornákat (e-mail, telefon), és esetleg egy belső támogatási rendszert.


-------------------------------------------------------------------------------


# Fejlesztői igényspecifikáció:

1. Technológiai Környezet

   1.1. Operációs Rendszer:
   A rendszernek futtathatónak kell lennie legalább a legújabb Windows és Linux operációs rendszereken.

   1.2. Adatbázis:
   Az adatbázisnak támogatnia kell az SQL adatbázisokat (pl. MySQL, PostgreSQL).

   1.3. Programozási Nyelv:
   A fejlesztés során a választott programozási nyelv a python lesz.

   1.4. Webes Technológiák:
   Az alkalmazásnak tartalmaznia kell egy webes felületet, amely támogatja a legújabb HTML, CSS és JavaScript technológiákat.

2. Architektúra

   2.1. MVC Architektúra:
   Az alkalmazásnak követnie kell a Model-View-Controller (MVC) tervezési mintát a könnyű karbantarthatóság és kódújrafelhasználhatóság érdekében.

   2.2. Kliens-szerver Kommunikáció:
   Az alkalmazásnak támogatnia kell a hatékony kliens-szerver kommunikációt, például RESTful API-k segítségével.

3. Adatkezelés

   3.1. Adatbázis Séma:
   A készletnyilvántartásnak és a raktárkezelő funkcióknak megfelelő adatbázis séma szükséges.

   3.2. Adatkezelési Műveletek:
   A rendszernek biztosítania kell az adatok hatékony lekérdezését, beszúrását, módosítását és törlését.

4. Biztonság

   4.1. SSL Támogatás:
   Az alkalmazásnak támogatnia kell az SSL titkosítást a biztonságos adatátvitel érdekében.

   4.2. Jogosultságkezelés:
   A rendszernek részletes jogosultságkezelést kell biztosítania a felhasználók és szerepkörök számára.

5. Teljesítmény

   5.1. Optimalizált Adatbázis-lekérdezések:
   A rendszernek hatékonyan kell kezelnie az adatbázis-lekérdezéseket a gyors és hatékony teljesítmény érdekében.

   5.2. Gyors Felhasználói Interfész:
   A webes felületnek reszponzívnak és gyorsnak kell lennie a felhasználói élmény javítása érdekében.

6. Tesztelés

   6.1. Egységtesztek:
   A fejlesztőknek rendszeresen kell végrehajtaniuk egységteszteket a kód minőségének és funkcionalitásának ellenőrzésére.

   6.2. Rendszertesztek:
   A rendszernek részletes rendszerteszteken kell átesnie, beleértve a funkcionalitást, teljesítményt és biztonságot.

7. Dokumentáció

   7.1. Kód Dokumentáció:
   A fejlesztőknek részletesen dokumentálniuk kell a kódot, beleértve a függvények leírását és a kommenteket.

   7.2. Felhasználói Dokumentáció:
   Készítsenek teljes körű felhasználói dokumentációt a rendszer telepítéséhez és használatához.

8. Verziókezelés

   8.1. Verziókezelő Rendszer:
   Használjanak verziókezelő rendszert a kódbázis kezeléséhez és változások nyomon követéséhez (pl. Git).

9. Skálázhatóság

   9.1. Horizontális Skálázhatóság:
   A rendszernek legyen képes horizontális skálázhatóságra, hogy a növekvő igényeket kezelni tudja.

10. Támogatás

    10.1. Támogatási Rendszer:
    - Kialakítani egy támogatási rendszert, ahol a felhasználók problémáikat jelenthetik és segítséget kérhetnek.


## Fejlesztői vízió (Vágyálom):

Célunk a raktárkezelő program fejlesztése során egy modern és rugalmas szoftvert létrehozni, amely hatékonyan támogatja a raktárkészlet-kezelési folyamatokat. Az alábbiakban felsoroljuk a fejlesztői vágyainkat és céljainkat:

1. Modern Technológiai Alapok:
Vágyunk egy olyan fejlesztési környezetet, amely tartalmazza a legújabb technológiai trendeket és keretrendszereket. Ez magában foglalja a modern programozási nyelvek, keretrendszerek és adatbázis-megoldások használatát.

2. Skálázhatóság és Teljesítmény:
A programnak skálázhatónak és hatékonyan teljesítőképesnek kell lennie a növekvő adatmennyiségek és felhasználói igények kezelése érdekében. Szeretnénk megteremteni a lehetőséget a horizontális és vertikális skálázhatóságra.

3. Modularitás és Kódújrafelhasználhatóság:
A kódbázisnak modulárisnak kell lennie, hogy könnyen bővíthető legyen új funkciók hozzáadásakor. A kódújrafelhasználhatóság segít abban, hogy az ismétlődő kód ne terhelje a fejlesztést.

4. Felhasználóbarát és Reszponzív Felület:
A rendszer grafikus felületének intuitívnak és könnyen kezelhetőnek kell lennie. A reszponzív dizájn biztosítja, hogy a felhasználói élmény minden eszközön optimális legyen.

5. Biztonság és Adatvédelem:
Az adatbiztonság és az adatvédelem kiemelt prioritások. A kritikus adatokat megfelelő módon kell titkosítani, és a jogosultságoknak szigorúnak kell lenniük.

6. Automatizált Tesztelés és CI/CD Folyamatok:
Kiemelt figyelmet fordítunk az automatizált tesztelésre és a folyamatos integráció/állapotellenőrzés (CI/CD) folyamatokra, hogy a kódbázis mindig stabil és működőképes legyen.

7. Rendszerintegrációk:
A programnak támogatnia kell a könnyű integrációt más vállalati rendszerekkel, beleértve pénzügyi és értékesítési szoftvereket.

8. Dokumentáció és Tudásátadás:
Az alapos dokumentáció és a tudásátadás kulcsfontosságú a hosszú távú karbantarthatóság szempontjából. Minden funkció és modul részletes dokumentációját szeretnénk elkészíteni.

9. Folyamatos Verbesserung (Folyamatos Fejlesztés):
Szeretnénk bevezetni egy folyamatos fejlesztési kultúrát a csapatban, amely lehetővé teszi az agilis módszerek alkalmazását és a rendszer folyamatos fejlesztését.

10. Felhasználói Visszajelzések Integrációja:
Fontosnak tartjuk a felhasználói visszajelzések integrációját a fejlesztési folyamatba, hogy a program mindig a felhasználói elvárásoknak megfeleljen.



## Fejlesztői cél: 

1. Funkcionális Teljesítmény:
Cél: Kifejleszteni és implementálni a raktárkezelő program fő funkcióit, beleértve a készletnyilvántartást, árukezelést, riportokat és rendszerintegrációkat.

2. Reszponzív Felhasználói Felület:
Cél: Létrehozni egy reszponzív és felhasználóbarát grafikus felületet, amely lehetővé teszi az intuitív navigációt és a könnyű kezelést minden eszközön.

3. Adatbiztonság és Jogosultságkezelés:
Cél: Implementálni erős adatbiztonsági intézkedéseket és részletes jogosultságkezelést a rendszerben a bizalmas adatok védelméért.

4. Skálázhatóság:
Cél: Kialakítani egy skálázható rendszert, amely képes rugalmasan növekedni és alkalmazkodni a növekvő adatmennyiségekhez és felhasználói igényekhez.

5. Automatizált Tesztelés és CI/CD Folyamatok:
Cél: Bevezetni automatizált tesztelési folyamatokat és folyamatos integrációt/állapotellenőrzést a fejlesztési folyamatok felgyorsítása és a kódbázis stabilan tartása érdekében.

6. Rendszerintegrációk:
Cél: Biztosítani a hatékony rendszerintegrációkat más vállalati rendszerekkel, például pénzügyi és értékesítési szoftverekkel.

7. Dokumentáció és Tudásátadás:
Cél: Elaborált dokumentáció készítése a kódbázisról, az architektúráról és a felhasználói funkciókról a könnyű karbantarthatóság és a tudásátadás érdekében.

8. Teljesítményoptimalizáció:
Cél: Végrehajtani teljesítményoptimalizációt a rendszerben annak érdekében, hogy a felhasználói élményt javítsuk és minimalizáljuk a válaszidőket.

9. Verziókezelés és Verziófrissítések:
Cél: Használni egy hatékony verziókezelő rendszert (pl. Git) és biztosítani folyamatos verziófrissítéseket a programon keresztül az új funkciók és hibajavítások számára.

10. Felhasználói Visszajelzések Integrációja:
Cél: Bevezetni egy rendszert a felhasználói visszajelzések integrációjára a fejlesztési folyamatba annak érdekében, hogy az alkalmazás folyamatosan fejlődjön a felhasználói elvárások alapján.



## Fejlesztői követelmény:

1. Fejlesztési Környezet

   1.1. Operációs Rendszer:
   A fejlesztőknek szükségük van olyan rendszerre, amely támogatja a fejlesztéshez szükséges eszközöket és platformokat. A támogatott operációs rendszerek közé tartozik a Windows, Linux és macOS.

   1.2. Fejlesztői Eszközök:
   Használjuk az X fejlesztői környezetet (IDE), például Visual Studio Code vagy IntelliJ IDEA.

2. Programozási Nyelvek és Keretrendszerek

   2.1. Backend:
   A backend részben a fejlesztés során alkalmazzunk [programozási nyelvet] (például Java, Python, Node.js) és keretrendszereket (Spring Boot, Django, Express).

   2.2. Frontend:
   A frontend rész fejlesztéséhez használjunk [programozási nyelvet] (például JavaScript, TypeScript) és modern keretrendszereket (React, Angular, Vue.js).

3. Adatbázis-kezelés

   3.1. Adatbázis:
   Az adatbázis-kezeléshez használjunk SQL-alapú adatbázist, például MySQL vagy PostgreSQL.

   3.2. ORM:
   Az adatbázis-műveletek könnyebb kezelése érdekében használjunk objektum-relációs leképző (ORM) keretrendszert, például Hibernate vagy Sequelize.

4. Verziókezelés és CI/CD

   4.1. Verziókezelés:
   Használjunk verziókezelő rendszert, például Git-et, a kódbázis verzióinak kezelésére és nyomon követésére.

   4.2. CI/CD Rendszer:
   Állítsunk be egy folyamatos integráció és folyamatos szállítás (CI/CD) rendszert, például Jenkins vagy Travis CI a kódbázis automatizált teszteléséhez és kiszállításához.

5. Biztonság és Tesztelés

   5.1. Tesztelés:
   Fejlesszünk egységteszteket, integrációs teszteket és rendszerteszteket a kód minőségének és stabilitásának biztosítása érdekében.

   5.2. Biztonság:
   Az alkalmazásban alkalmazzunk biztonsági legjobb gyakorlatokat, például megfelelő adatbázis-parametrizálást, token-alapú hitelesítést és SSL-t az adatátvitelhez.

6. Dokumentáció és Kódstílus

   6.1. Kód Dokumentáció:
   Készítsünk részletes kód dokumentációt, amely magában foglalja a funkciók, metódusok és modulok leírását.

   6.2. Kódstílus és Konvenciók:
   Kövessünk egységes kódstílust és kódkonvenciókat a könnyebb karbantarthatóság és olvashatóság érdekében.

7. Rendszerintegráció és API-k
   7.1. API-k:
   Biztosítsunk könnyen használható és dokumentált API-kat az esetleges harmadik fél integrációkhoz.

   7.2. Rendszerintegrációk:
   Készítsünk olyan rendszerintegrációkat, amelyek lehetővé teszik a szoftver harmadik fél rendszerekkel való együttműködését.

8. Felhasználói Visszajelzések Integrációja

   8.1. Visszajelzési Rendszer:
   Implementáljunk egy visszajelzési rendszert a fejlesztési folyamatba, hogy a felhasználók véleménye beépüljön a további fejlesztési lépésekbe.








