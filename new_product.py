from datetime import datetime

def new_product():
    print("Ön az Új áru felvitele opciót választotta.")
    nev = input("Adja meg az áru nevét: ")
    magassag = input("Adja meg az áru magasságát(cm): ")
    szelesseg = input("Adja meg az áru szélességét(cm): ")
    suly = input("Adja meg az áru súlyát(Kg): ")
    ar = input("Adja meg az áru árát: ")
    forgalmazo = input("Ki a forgalmazója az árunak?")

    # Rögzítés ideje
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    try:
        # Az utolsó ID lekérése a fájlból
        with open("aruk.txt", "r") as f:
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

    # Az adatokat egy szövegfájlba írjuk
    with open("aruk.txt", "a") as f:
        f.write(f"\nID: {new_id}\nNév: {nev}\nMagasság: {magassag} cm\nSzélesség: {szelesseg} cm\nSúly: {suly} g\nForgalmazó: {forgalmazo}\nÁr: {ar} Ft\nRögzítés ideje: {timestamp}\n")
        f.write(f"-------------------------")

    print("Az áru hozzáadva az árlistához. ID:", new_id)

    input("Nyomja meg az entert a menübe való visszatéréshez...")
