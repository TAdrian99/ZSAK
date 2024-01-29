# kisz_datum_mod.py

def kiszallitas_datum_modositasa():
    try:
        product_id_to_modify = int(input("Adja meg az áru ID-jét a módosításhoz: "))
        new_delivery_date = input("Adja meg az új kiszállítási dátumot (YYYY-MM-DD HH:mm:ss): ")

        modify_delivery_date(product_id_to_modify, new_delivery_date)

    except ValueError:
        print("Érvénytelen bemenet. Kérlek, adj meg egy számot az áru ID-jéhez.")
    except Exception as e:
        print(f"Hiba történt: {e}")


def modify_delivery_date(product_id, delivery_date):
    try:
        with open("aruk.txt", "r", encoding='utf-8') as f:
            lines = f.readlines()

        found = False
        new_lines = []
        for i in range(len(lines)):
            if lines[i].startswith("ID:") and int(lines[i].split(":")[1].strip()) == product_id:
                found = True

                # Kiszállítási dátum módosítása
                lines[i + 8] = f"Kiszallitas datuma: {delivery_date}\n"

                print(f"Az áru (ID: {product_id}) kiszállítási dátuma sikeresen módosítva.")

        if not found:
            print(f"Nincs találat az '{product_id}' ID-vel rendelkező termékre.")

        with open("aruk.txt", "w") as f:
            f.writelines(lines)

    except FileNotFoundError:
        print("Az 'aruk.txt' fájl nem található.")

    input("Nyomja meg az entert a menübe való visszatéréshez...")