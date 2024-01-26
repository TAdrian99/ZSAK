Dokumentáció
Általános ismertetés
A fejlesztett rendszer egy kisvállalkozás árlistáját és a hozzá kapcsolódó műveleteket kezeli. A program lehetővé teszi új áruk felvételét, meglévő áruk listázását, áruk törlését ID alapján, felviteli részletek megtekintését, a legnehezebb áru megjelenítését, valamint az utoljára felvitt áru listázását.

Menürendszer
A program egy egyszerű konzolos menürendszerrel rendelkezik, amely a felhasználó számára lehetőséget ad a különböző műveletek elvégzésére. A menüpontokat a felhasználó a konzolon keresztül választhatja ki, és az adott művelet elvégzéséhez kapcsolódó funkciók hívódnak meg.

Funkciók
1. Új áru felvitele
A felhasználó új árut vihet fel a rendszerbe, megadva a termék nevét, magasságát, szélességét, súlyát, árát, valamint a beszállító nevét. Az adatok megadása során a rendszer ellenőrzi a megfelelő formátumot, és a rögzítés idejét automatikusan generálja.

2. Listázás
Az összes rögzített áru listázása a konzolon. Az áruk adatai szépen formázott módon jelennek meg.

3. Elem törlése
Az áruk törlése ID alapján. A felhasználó megadhatja az áru ID-jét, és a rendszer törli az adott ID-hoz tartozó árut az árlistából.

4. Felviteli részletek
A felhasználó megadhat egy áru ID-t, és a rendszer megjeleníti az adott ID-hoz tartozó áru összes részletét.

5. Legnehezebb áru
A rendszer megkeresi és megjeleníti a legnehezebb súlyú árut az árlistában.

6. Utoljára felvitt
Az utoljára felvitt áru részleteinek megjelenítése.

7-10. Opciók
Az 7-10 opciók jelenleg még implementációra várnak, így a felhasználót "pass" kulcsszóval kiszolgálják, amíg ezek a funkciók el nem készülnek.

Adattárolás
Az áruk adatait egy "aruk.txt" nevű szövegfájlban tárolja a rendszer. Az adatokat minden művelet során a fájlból olvassa be, és a módosítások után visszaírja.

Felhasználói input ellenőrzés
A felhasználótól bekért inputokat a rendszer ellenőrzi, hogy megfelelnek-e a várt formátumnak. Hiba esetén a felhasználót értesíti a hibáról és újra bekéri az adatot.

Objektumorientált megközelítés
A Szemely osztály segítségével az alkalmazás használ objektumorientált megközelítést a személyek (általánosságban az áruk) kezelésére. A delete_product_by_id függvény törli az adott ID-hez tartozó árut a szövegfájlból.

Hibakezelés
A rendszer különböző hibákkal szemben ellenálló. Például a felhasználó által megadott ID alapján történő törlés esetén, ha az ID nem található, a rendszer nem ír ki hibaüzenetet, hanem egyszerűen visszatér a főmenübe.

Használati útmutató
A felhasználónak a program elindításakor választania kell a menüpontok közül, majd az adott művelet végrehajtásához követnie kell a program által adott utasításokat. A felhasználó hibás bemenetek esetén tájékoztatást kap, majd újra megadhatja az adatokat. A program végén a felhasználó a "0" opcióval tud kilépni.

Következő lépések
A fejlesztés további lépései közé tartozik az 7-10 opciók funkcionalitásának implementálása, valamint a rendszer bővítése további funkciókkal a felhasználói élmény javítása érdekében. Ezen kívül a kód további optimalizálása és a hibák kezelésének javítása is fontos lépése a fejlesztésnek.