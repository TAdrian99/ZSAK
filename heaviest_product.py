def heaviest_product():
    try:
        heaviest_weight = 0
        heaviest_product_name = ""

        with open("aruk.txt", "r") as f:
            lines = f.readlines()

        for i in range(len(lines)):
            line = lines[i].strip()
            if line.startswith("Súly"):
                weight = int(line.split()[1])

                if weight > heaviest_weight:
                    heaviest_weight = weight
                    name_line = lines[i - 3]  # A "Név" rész egy sorral előtte van a "Magasság" előtt
                    heaviest_product_name = name_line.split(":")[1].strip()  # Csak a nevet vesszük figyelembe

        if heaviest_product_name:
            print("A legnehezebb súlyú áru:")
            print(f"Név: {heaviest_product_name}")  # A nevet írja ki
            print(f"Súly: {heaviest_weight} kg")  # A megtalált súly kiírása
        else:
            print("Nincs rögzített áru.")

    except FileNotFoundError:
        print("Az 'aruk.txt' fájl nem található.")

    input("Nyomja meg az entert a menübe való visszatéréshez...")
