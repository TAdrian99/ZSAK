from datetime import datetime

def new_product():
    print("Ön az Új áru felvitele opciót választotta.")
    while True:
        try:
            nev = input("Adja meg az áru nevét (vagy 0 a kilépéshez): ")
            if not nev:
                print("Hibás adatbevitel! Kérlek adj meg egy nevet.")
                continue  # Az üres input esetén folytassuk az újbóli bekérést

            if nev == "0":
                print("Visszatérés a főmenübe.")
                break

            magassag = input("Adja meg az áru magasságát (cm) (vagy 0 a kilépéshez): ")
            if not magassag:
                print("Hibás adatbevitel! Kérlek adj meg egy magasságot.")
                continue
            magassag = int(magassag)
            if magassag == 0:
                print("Visszatérés a főmenübe.")
                break

            szelesseg = input("Adja meg az áru szélességét (cm) (vagy 0 a kilépéshez): ")
            if not szelesseg:
                print("Hibás adatbevitel! Kérlek adj meg egy szélességet.")
                continue
            szelesseg = int(szelesseg)
            if szelesseg == 0:
                print("Visszatérés a főmenübe.")
                break

            suly = input("Adja meg az áru súlyát (Kg) (vagy 0 a kilépéshez): ")
            if not suly:
                print("Hibás adatbevitel! Kérlek adj meg egy súlyt.")
                continue
            suly = int(suly)
            if suly == 0:
                print("Visszatérés a főmenübe.")
                break

            ar = input("Adja meg az áru árát (vagy 0 a kilépéshez): ")
            if not ar:
                print("Hibás adatbevitel! Kérlek adj meg egy árat.")
                continue
            ar = int(ar)
            if ar == 0:
                print("Visszatérés a főmenübe.")
                break

            forgalmazo = input("Ki a beszállítója az árunak? (vagy 0 a kilépéshez): ")
            if not forgalmazo:
                print("Hibás adatbevitel! Kérlek adj meg egy beszállítót.")
                continue
            if forgalmazo == '0':
                print("Visszatérés a főmenübe.")
                break

            # Rögzítés ideje
            now = datetime.now()
            timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

            # Itt folytathatod a többi kóddal, pl. adatok feldolgozása, tárolása stb.

        except ValueError:
            print("Hibás adatbevitel! Kérlek csak számokat adj meg a méretekhez, súlyhoz és árhoz.")
            continue  # Érvénytelen input esetén újra bekérjük az adatokat
        except Exception as e:
            print(f"Hiba történt: {e}")
            continue  # Egyéb hiba esetén is újra bekérjük az adatokat

        # Az adatokat egy szövegfájlba írjuk
        try:
            # Az utolsó ID lekérése a fájlból
            with open("aruk.txt", "r", encoding='utf-8') as f:
                lines = f.readlines()
                last_id = 0

                for line in reversed(lines):
                    if line.startswith("ID:"):
                        last_id = int(line.split(":")[1].strip())
                        break

        except FileNotFoundError:
            last_id = 0

        # Új ID generálása
        new_id = last_id + 1

        with open("aruk.txt", "a") as f:
            f.write(f"\nID: {new_id}\nNév: {nev}\nMagasság: {magassag} cm\nSzélesség: {szelesseg} cm\nSúly: {suly} g\nBeszállító: {forgalmazo}\nÁr: {ar} Ft\nRögzítés ideje: {timestamp}\n")
            f.write(f"-------------------------")

        print("Az áru hozzáadva az árlistához. ID:", new_id)
        input("Nyomja meg az entert a menübe való visszatéréshez...")
        return