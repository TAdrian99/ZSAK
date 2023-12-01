def last_product():
    try:
        with open("aruk.txt", "r") as f:
            lines = f.readlines()

            if not lines:
                print("Nincsenek rögzített termékek.")
            else:
                last_id = 0
                last_product = ""
                for line in reversed(lines):
                    if line.startswith("ID:"):
                        last_id = int(line.split(":")[1].strip())
                        break

                for line in reversed(lines):
                    if line.startswith(f"ID: {last_id}"):
                        last_product = line.strip()
                        break

                if last_product:
                    print("Az utoljára felvitt áru:")
                    print(last_product)
                else:
                    print("Nincs utoljára felvitt áru.")

    except FileNotFoundError:
        print("Az 'aruk.txt' fájl nem található.")

    input("Nyomja meg az entert a menübe való visszatéréshez...")