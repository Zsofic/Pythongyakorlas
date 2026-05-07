#alap
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Ez egy üzenet O.o")


#CLI paraméteres feladat
import sys
import logging

logging.basicConfig(level=logging.DEBUG)

if len(sys.argv) == 1:
    logging.error("Nem adtál meg számokat!")
    sys.exit()

osszeg = 0

for i in sys.argv[1:]:
    try:
        logging.debug("Kovetkező szám:" + i)
        osszeg += int(i)
    except ValueError:
        logging.warning("Nem számot adtál meg: {i}")

print("A megadott számok összege:", osszeg)


#Debugging feladat
def oszt(a, b):
    return a / b

print(oszt(10, 0))
