# list_products.py

def list_products():
    print("Ön az Áruk listázása opciót választotta.")

    # Olvassa be az aruk.txt fájlt és listázza az összes terméket
    try:
        with open("aruk.txt", "r") as f:
            products = f.readlines()

            if not products:
                print("Nincsenek rögzített termékek.")
            else:
                print("Rögzített termékek:")
                for product in products:
                    print(product.strip())


    except FileNotFoundError:
        print("Az 'aruk.txt' fájl nem található.")

    input("Nyomja meg az entert a menübe való visszatéréshez...")
