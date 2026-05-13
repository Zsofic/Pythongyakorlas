import sys
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

async def feldolgoz(szam):
    logging.info(f"Feldolgozás: {szam}")
    await asyncio.sleep(1)
    eredmeny = szam * 2
    return eredmeny

async def main():
    logging.info("A program elindult!")
    szamok = [5,10,20]

    for arg in sys.argv[1:]:
        try:
            szam = int(arg)
            szamok.append(szam)
        except ValueError:
            logging.error(f"Hibás karakter ez nem szám: {arg}")

    feladatok = [feldolgoz(szam) for szam in szamok]
    eredmenyek = await asyncio.gather(*feladatok)
    print("Eredmények:", eredmenyek)

if __name__ == "__main__":
    asyncio.run(main())