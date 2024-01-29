
def fuvarozas_hozzarendeles():
    try:
        # Fuvarozó választása vagy kilépés
        print("Válasszon egy futárcéget a hozzárendeléshez:")
        # Itt lehetne listázni a rendelkezésre álló futárcégeket és kérni a felhasználót, hogy válasszon

        futar_nev = input("Adja meg a futár cég nevét (vagy 0 a kilépéshez): ")
        if futar_nev == '0':
            print("Visszatérés a főmenübe.")
            return

        # Áruhoz tartozó fuvarozó nevének beolvasása
        aru_id = int(input("Adja meg az áru ID-jét a fuvarozóhozrendeléshez: "))
        futar_nev = input("Adja meg a futár cég nevét a hozzárendeléshez: ")

        # Fuvarozó nevének hozzárendelése az áruhoz
        with open("aruk.txt", "r", encoding='utf-8') as aruk_file:
            lines = aruk_file.readlines()

        with open("aruk.txt", "w", encoding='utf-8') as aruk_file:
            for line in lines:
                aru_id_line = line.startswith("ID:") and int(line.split(":")[1].strip()) == aru_id
                futar_nev_line = line.startswith("Beszallito:") and line.split(":")[1].strip() == futar_nev

                if aru_id_line:
                    aruk_file.write(line)
                elif futar_nev_line:
                    aruk_file.write(f"Fuvarozo: {futar_nev}\n")
                else:
                    aruk_file.write(line)

        print("Fuvarozó hozzárendelve az áruhoz.")
        input("Nyomja meg az entert a főmenübe való visszatéréshez...")

    except Exception as e:
        print(f"Hiba történt: {e}")
