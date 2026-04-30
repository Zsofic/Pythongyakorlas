#konnyu
try:
    szam = float(input("Adj meg egy számot: "))
    print("A megadott szám:", szam)
except ValueError:
    print("Hiba: Nem számot adtál meg!")


#kozepes
try:
    szam1 = float(input("Add meg az első számot: "))
    szam2 = float(input("Add meg a második számot: "))

    print("Az osztás eredménye:", szam1 / szam2)
except ZeroDivisionError:
    print("Nullával nem lehet osztani!")
except ValueError:
    print("Nem számot adtál meg!")


#kozepes+
try:
    fajl = open("adatok.txt", "r")
    tartalom = fajl.read()
    print(tartalom)

except FileNotFoundError:
    print("Hiba: A fájl nem létezik!")

finally:
    print("Ezért nem lehet megynitni.")


#halado
def atlag(szamok):
    osszeg = 0
    darab = 0

    for szam in szamok:
        try:
            szam = float(szam)
            osszeg += szam
            darab += 1

        except ValueError:
            print("Nem szám, kihagyom:", szam)

    if darab == 0:
        return "Nincs szám a listában!"

    return osszeg / darab


szamok = [13, 20, 49, "cica", 5]
print(atlag(szamok))

#mini projekt
