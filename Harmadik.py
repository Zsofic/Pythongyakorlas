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