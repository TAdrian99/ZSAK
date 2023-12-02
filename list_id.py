def list_id():
    try:
        product_id = int(input("Nyomjon 0-át a menübe való visszatéréshez\nAdja meg az áru ID-jét a megjelenítéshez: "))
        if input == 0:
            pass
        with open("aruk.txt", "r") as f:
            lines = f.readlines()

        found = False
        for line in lines:
            if line.startswith("ID:") and int(line.split(":")[1].strip()) == product_id:
                found = True
            elif found and line.startswith("-------------------------"):
                found = False
            elif found:
                print(line.strip())

        if not found:
            print(f"Nincs találat az '{product_id}' ID-vel rendelkező termékre.")

    except ValueError:
        print("Érvénytelen bemenet. Kérlek, adj meg egy számot az áru ID-jéhez.")

    except FileNotFoundError:
        print("Az 'aruk.txt' fájl nem található.")

    input("Nyomja meg az entert a menübe való visszatéréshez...")