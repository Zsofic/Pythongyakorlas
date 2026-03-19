import csv

with open("teszt.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
        print(row[1])
        print(row[3])

        print("Oszlopok:" str(len(row)))

        for oszlop in row:
            print("O:" + oszlop)

        with open("teszt.csv", "r", encoding="utf-8", newline="") as f:
            olvaso = csv.reader(f)
            for row in reader:
                print(row)

                print("Cím:")

        import csv

        adatok = [
            ["szerzo", "cim", "kiadas"],
            ["George Orwell", "1984", 1949],
            ["Ray Bradbury", "Fahrenheit 451", 1953]
        ]

        with open("uj_konyvek.csv", "w", encoding="utf-8", newline="") as f:
            iro = csv.writer(f)
            iro.writerows(adatok)