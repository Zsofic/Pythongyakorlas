import csv
  from api_helper import keres_konyveket

  keresett_cim = input("Title of the book:")

  adat = keres_konyveket(keresett_cim)

  if adat:
      talalatok = adat["docs"][:5]

      with open("konyvek.csv", "w", encoding="utf-8", newline="") as f:
          iro = csv.writer(f, delimiter=";")
          iro.writerow(["cim", "szerzo", "elso_kiadas_eve"])

          for konyv in talalatok:
              cim = konyv.get("title", "N/A")
              szerzok = ", ".join(konyv.get("author_name", ["N/A"]))
              ev = konyv.get("first_publish_year", "N/A")

              iro.writerow([cim, szerzok, ev])

      print("A mentés elkészült: konyvek.csv")
  else:
      print("Nem sikerült adatot lekérni.")