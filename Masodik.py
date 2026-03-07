def feldolgozas(kerdes):
    print("Feldolgozas alatt!")

    szamjegyek = dict()
    for betu in kerdes:
        # print(betu)
        if betu in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            if betu in szamjegyek:
                szamjegyek[betu] += 1
            else:
                szamjegyek[betu] = 1

    #1. feladat
    if kerdes[-1] == "?":
        print("Ez bizony egy kérdés")

    #3. feladat
    if len(szamjegyek) == 0:
        print("Ebben egy számjegy sem volt.")

    #4. feladat
    pontszamlalo = kerdes.count(".")
    print("A kérdés", pontszamlalo ,"darab pontot tartalmazott.")

    return szamjegyek

    #return kerdes[::-1]

while True:
    kerdes = input("Kerdes: ")

    if kerdes == "exit":
        print("Viszlát!")
        break

    #2. feladat
    if kerdes == "quit":
        print("Bye!")
        break

    print("Ezt kerdezte: " + kerdes)

    valasz = feldolgozas(kerdes)
    print("Valasz: " + str(valasz))

print("Program vege!")

