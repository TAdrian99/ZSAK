
def futar_termekek_listazasa():
    try:
        # Fuvarozó választása vagy kilépés
        print("Válassza ki a futárcéget a terméklista megtekintéséhez:")
        # Itt lehetne listázni a rendelkezésre álló futárcégeket és kérni a felhasználót, hogy válasszon

        futar_nev = input("Adja meg a futár cég nevét (vagy 0 a kilépéshez): ")
        if futar_nev == '0':
            print("Visszatérés a főmenübe.")
            return

        # Futárcéghez tartozó termékek listázása
        with open("aruk.txt", "r", encoding='utf-8') as aruk_file:
            lines = aruk_file.readlines()

        print(f"{futar_nev} futárcéghez tartozó termékek:")
        found_futar = False
        for line in lines:
            futar_line = line.startswith("Fuvarozo:") and line.split(":")[1].strip() == futar_nev
            termek_nev_line = line.startswith("Nev:")  # Itt lehet bővíteni, ha van egyedi termékazonosító

            if futar_line:
                found_futar = True
            elif found_futar and termek_nev_line:
                print(line.strip())

        if not found_futar:
            print(f"Nincs termék a(z) {futar_nev} futárcéghez rendelve.")

        input("Nyomja meg az entert a főmenübe való visszatéréshez...")

    except Exception as e:
        print(f"Hiba történt: {e}")
