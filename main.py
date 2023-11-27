# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

print('V1')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/


while True:
    # Menü kiíratása
    print("Válasszon egy lehetőséget:")
    print("1. Új áru felvitele 1")
    print("2. Listázás 2")
    print("3. Elem törlése 3")
    print("4. Felviteli részletek  4")
    print("5. Legnehezebb áru 5")
    print("6. Utoljára felvitt 6")
    print("7. Kiszállítási dátum módosítása 7")
    print("8. Futár cég felvitel 8")
    print("9. Fuvarozó hozzárendelése 9")
    print("0. Kilépés 0")

    # Felhasználói input bekérése
    valasztas = input("Kérem, válasszon (0-9): ")

    # Kilépés ellenőrzése
    if valasztas == '0':
        print("Kilépés...")
        break

    # Választás kezelése
    elif valasztas == '1':
        print("Ön választotta az Opció 1-t.")
        # Itt folytathatja az Opció 1-hoz tartozó műveleteket.

    elif valasztas == '2':
        print("Ön választotta az Opció 2-t.")
        # Itt folytathatja az Opció 2-hoz tartozó műveleteket.

    elif valasztas == '3':
        print("Ön választotta az Opció 3-t.")
        # Itt folytathatja az Opció 3-hoz tartozó műveleteket.

    elif valasztas == '4':
        print("Ön választotta az Opció 4-t.")
        # Itt folytathatja az Opció 4-hoz tartozó műveleteket.

    elif valasztas == '5':
        print("Ön választotta az Opció 5-t.")
        # Itt folytathatja az Opció 5-höz tartozó műveleteket.

    elif valasztas == '6':
        print("Ön választotta az Opció 6-t.")
        # Itt folytathatja az Opció 6-hoz tartozó műveleteket.

    elif valasztas == '7':
        print("Ön választotta az Opció 7-t.")
        # Itt folytathatja az Opció 7-hoz tartozó műveleteket.

    elif valasztas == '8':
        print("Ön választotta az Opció 8-t.")
        # Itt folytathatja az Opció 8-hoz tartozó műveleteket.

    elif valasztas == '9':
        print("Ön választotta az Opció 9-t.")
        # Itt folytathatja az Opció 9-hoz tartozó műveleteket.

    else:
        print("Érvénytelen választás. Kérem, válasszon újra.")
