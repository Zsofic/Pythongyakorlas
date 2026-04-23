#konnyu
gen1 = (i for i in range(1, 6))

for x in gen1:
    print(x)
print("-------")


#kozepes
gen2 = (i for i in range(0, 11) if i % 2 == 0)

for szam in gen2:
    print(szam)
print("-------")


#kozepes+
negyzetre_emeles = lambda x: x * x
print(negyzetre_emeles(50))
print("-------")


#kozepes++
lista = [x * 3 for x in range(1, 11) if x % 2 == 1]
print(lista)
print("-------")


#halado
adott_lista = [10, 15, 20, 25]
print(adott_lista)

haromszoros = list(map(lambda x: x * 3, adott_lista))
print(haromszoros)

husz_feletti = list(filter(lambda x: x > 20, adott_lista))
print(husz_feletti)
print("-------")


#halado+
lista1000 = list(range(1, 1001))
print(lista1000)

gen3 = (i for i in range(1, 1001))
print(type(gen3))
print(list(gen3)[:10])