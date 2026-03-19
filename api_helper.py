import requests

  def keres_konyveket(cim):
      url = "https://openlibrary.org/search.json"
      params = {
          "title": cim
      }

      response = requests.get(url, params=params)

      if response.status_code == 200:
          return response.json()
      else:
          print("Hiba történt:", response.status_code)
          return None