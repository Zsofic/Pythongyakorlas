import csv

with open("teszt.csv", "r", encoding="utf-8", newline="") as f:
    reader = csv.reader(f)

    for row in reader:
        print(row)

        if len(row) > 1:
            print(row[1])
        if len(row) > 3:
            print(row[3])

        print(f"Oszlopok: {len(row)}")

        for oszlop in row:
            print("O:" + oszlop)


adatok = [
    ["szerzo", "cim", "kiadas"],
    ["George Orwell", "1984", 1949],
    ["Ray Bradbury", "Fahrenheit 451", 1953]
]

with open("uj_konyvek.csv", "w", encoding="utf-8", newline="") as f:
    iro = csv.writer(f)
    iro.writerows(adatok)