def input_delete_product_by_id():
    try:
        product_id_to_delete = int(input("Nyomjon 0-át a menübe való visszatéréshez\nAdja meg az áru ID-jét a törléshez: "))
        delete_product_by_id(product_id_to_delete)
        if input == 0:
            pass


    except ValueError:
        print("Érvénytelen bemenet. Kérlek, adj meg egy számot az áru ID-jéhez.")
        product_id_to_delete = int(input("Adja meg az áru ID-jét a törléshez: "))
        delete_product_by_id(product_id_to_delete)

def delete_product_by_id(product_id):
    try:
        # Beolvassuk a fájl tartalmát
        with open("aruk.txt", "r") as f:
            lines = f.readlines()

        # Megkeressük a törlendő rekordot az ID alapján
        found = False
        new_lines = []
        for line in lines:

            if line.startswith("ID:") and int(line.split(":")[1].strip()) == product_id:
                found = True
            elif found and line.startswith("-------------------------"):
                found = False
                print(f"Az áru (ID: {product_id}) sikeresen törölve.")
                input("Nyomja meg az entert a menübe való visszatéréshez...")
            elif not found:
                new_lines.append(line)
                # Ellenőrizzük, hogy találtunk-e ilyen ID-t


#Probléma, ha nem talál olyan ID-t amit az inputba megadtunk akkor nem ír ki hibaüzenetet

        # Az új tartalmat visszaírjuk a fájlba
        with open("aruk.txt", "w") as f:
            f.writelines(new_lines)




    except FileNotFoundError:
        print("Az 'aruk.txt' fájl nem található.")




