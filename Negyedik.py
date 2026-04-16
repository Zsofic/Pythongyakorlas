#konnyu
class Film:
    def __init__(self, cim, rendezo, ev):
        self.cim = cim
        self.rendezo = rendezo
        self.ev = ev

#kozepes
    def leiras(self):
        return f"{self.rendezo} - {self.cim} - {self.ev}"

    def regi_film(self):
        return self.ev < 2000

f1 = Film("Péntek 13", "Sean S. Cunningham", 1980)
print(f1.leiras())
print("2000 előtti ez a film? " + str(f1.regi_film()))

#kozepes+
class Konyv:
    def __init__(self, cim, szerzo, oldalszam):
        self.cim = cim
        self.szerzo = szerzo
        self.oldalszam = oldalszam

    def leiras(self):
        return f"{self.szerzo} - {self.cim} - {self.oldalszam}"
    def hosszukonyv(self):
        return self.oldalszam > 300

k1 = Konyv("1984", "George Orwell", 328)
print(k1.leiras())
print("300 oldalnál hosszabb a konyv? " + str(k1.hosszukonyv()))


#halado
class Dokumentum:
    def leiras(self):
        return "Ez egy dokumentum osztaly"

class Konyv(Dokumentum):
    def leiras(self):
        return "Ez egy konyv a dokumentum osztalybol"

class Folyoirat(Dokumentum):
    def leiras(self):
        return "Ez egy folyoirat a dokumentum osztalybol"

d = Dokumentum()
print(d.leiras())
k = Konyv()
print(k.leiras())
f = Folyoirat()
print(f.leiras())

#mini projekt
class Konyv1:
    def __init__(self, cim, szerzo):
        self.cim = cim
        self.szerzo = szerzo

class Konyvtar:
    def __init__(self):
        self.konyvek = []

    def hozzaad(self, konyv):
        self.konyvek.append(konyv)

    def lista(self):
        for konyv in self.konyvek:
            print(f"{konyv}")

konyvtar = Konyvtar()
konyvtar.hozzaad(Konyv1("1984", "George Orwell"))
konyvtar.hozzaad(Konyv1("Brave New World", "Aldous Huxley"))
konyvtar.lista()


