Program Dokumentáció
Bevezetés
Ez a program egy egyszerű árulistát kezelő alkalmazás, amely lehetővé teszi új áruk felvételét, meglévő áruk listázását, egyes termékek törlését, valamint egyéb műveletek végrehajtását.

Rendszerkövetelmények
Python 3.x futtató környezet
datetime modul
Telepítés és Futtatás
Klónozd le a repository-t vagy töltsd le a forrásfájlt.
Nyisd meg a terminált vagy parancssort az alkalmazás gyökérkönyvtárában.
Futtasd a programot a következő paranccsal: python program_neve.py (vagy python3 program_neve.py a Python 3 esetén).
Használat
A program indítása után a főmenü jelenik meg.
A felhasználónak lehetősége van választani a rendelkezésre álló opciók közül (0-9).
Az opciók leírása:
1: Új áru felvitele
2: Áruk listázása
3: Áru törlése
4: Felviteli részletek
5: Legnehezebb áru megjelenítése
6: Utoljára felvitt áru megjelenítése
7: Kiszállítási dátum módosítása (még nincs implementálva)
8: Futár cég felvitele (még nincs implementálva)
9: Fuvarozó hozzárendelése (még nincs implementálva)
10: Adott futárcéghez tartozó terméklista megjelenítése (még nincs implementálva)
0: Kilépés a programból
Almodulok
new_product
Ez a modul felelős az új áru felvételéért. A felhasználó megadhatja az áru nevét, magasságát, szélességét, súlyát, árát, és a beszállító nevét.

list_products
Ez a modul listázza az összes rögzített terméket a aruk.txt fájl alapján.

list_id
Ez a modul lehetővé teszi a felhasználónak, hogy megadja egy áru azonosítóját, és azonosító alapján megjelenítse az áru részleteit.

delete_product_by_id
Ez a modul felelős egy áru törléséért az azonosító alapján.

heaviest_product
Ez a modul megjeleníti a legnehezebb súlyú árut a rögzített termékek között.

last_product
Ez a modul megjeleníti az utoljára felvitt árut a rögzített termékek között.

Adatkezelés
Az áru adatait egy szövegfájlban (aruk.txt) tároljuk. Minden termék adatait egyedi azonosítóval ellátott sorok képezik.

Hibakezelés
A program igyekszik kezelni az érvénytelen bemeneteket, és hibaüzenetekkel tájékoztatja a felhasználót az esetleges problémákról.