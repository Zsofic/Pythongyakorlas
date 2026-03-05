print("Helloka")
# komment nekem

"""
több soros 
komment
"""
x = 10
print(x)
x = 30
print(x)

y = 1.2342
print(y)

nev : str = "ValakiaValami"
print(nev)

print([1,2,3,4,5])
print("helloka" + " belloka")
print("hello" + str(12))
print(f"hello {12} {nev}")

tuple_szamok = {1, 2}
print(f"szamok: {1, 2, 5, 7}")
print("tuple_szamok:" + str(tuple_szamok))

print(range(5))

lista = [1,1,1,1,1,3,3,4]
print(lista)
halmaz = {1,1,1,1,1,3,3,4}
print(halmaz)

szotar = {"név": "Anna", "kor": 20}
print(szotar)

logikai = True
print(logikai)

ertek = None
print(ertek)

nev = "Jancsi"
Nev = "Juliska"
print(nev + " és " + Nev)

PI = 3.14
print(PI)
PI = 1.2
print(PI)

print(12 + 2.4 + 3 -4 / 2.6)
print(12 + 2 + 3 - 4 - 2)

x = 5
y = 3
print("x and y: " + str(x % y))

print("Három az értéke y-nak? " +str(y) == 3)
print("Három az értéke y-nak? " == 3)
print("Három az értéke y-nak? " == "Három az értéke y-nak? 3")

print("Három az értéke y-nak? " + str(y == 3))
print("Nem három az értéke y-nak? " + str(y != 3))
print("Y kisebb, mint 3 három? " + str(y < 3))
print("Y kisebb vagy egyenlő, mint 3 három? " + str(y <= 3))

print("Y kisebb vagy egyenlő, mint 3 három? " + str(y < 3 or y == 3))

if y > 5:
    print("Y nagyobb, mint 5")
    if y % 2 == 0:
        print("Y páros és nagyobb, mint 5")
else:
    print("Y kisebb vagy egyenlő, mint 5")

for i in range(5):
    print(i)

for nev in ["Anna", "Béla", "Cecil"]:
    print(nev)
    if nev == "Anna":
        print("Szia Anna!")

print("vége")

while y < 10:
    print("Y kisebb, mint 10")
    y += 1
    print("Y értéke: " + str(y))

def fuggveny():
        print("Ez egy függvény")

        return "Alma"

print("következő sor")
fuggveny()

eredmeny = fuggveny()

print("A függvény visszaadott egy: " + fuggveny() + "-t")
print("A függvény visszaadott egy: " + eredmeny + "-t")

def osszeadas(a, b):
    osszeg = a + b
    return osszeg

eredmeny = str(osszeadas(1, 2))
print("Összeg:" + str(osszeadas(5, 4)))