import new_product,list_products,delete_product_by_id,list_id, last_product, heaviest_product



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
        new_product.new_product()

    elif valasztas == '2':
        list_products.list_products()

    elif valasztas == '3':
        delete_product_by_id.input_delete_product_by_id()

    elif valasztas == '4':
        list_id.list_id()

    elif valasztas == '5':
        heaviest_product.heaviest_product()

    elif valasztas == '6':
        last_product.last_product()

    elif valasztas == '7':
        # Itt folytathatja az Opció 7-hoz tartozó műveleteket.

    elif valasztas == '8':
        # Itt folytathatja az Opció 8-hoz tartozó műveleteket.

    elif valasztas == '9':
        # Itt folytathatja az Opció 9-hoz tartozó műveleteket.

    else:
        print("Érvénytelen választás. Kérem, válasszon újra.")
