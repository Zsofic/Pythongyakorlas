import requests
import csv

URL = "https://gutendex.com/books/?languages=hu"


def fetch_all_books(max_pages=4):
    url = URL
    page = 1
    all_books = []

    while url and page <= max_pages:
        print(f"Oldal letöltése: {page}")

        response = requests.get(url)
        data = response.json()

        for book in data.get("results", []):
            title = book.get("title", "")

            authors = ", ".join(
                author.get("name", "") for author in book.get("authors", [])
            )

            summaries = "\n".join(book.get("summaries", []))

            all_books.append({
                "title": title,
                "authors": authors,
                "summaries": summaries,
                "page": page
            })

        url = data.get("next")
        page += 1

    return all_books


def save_to_csv(books, filename="talalatok.csv"):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["title", "authors", "summaries", "page"]
        )

        writer.writeheader()
        writer.writerows(books)


if __name__ == "__main__":
    books = fetch_all_books(max_pages=4)
    save_to_csv(books)

    print(f"\nÖsszes rekord: {len(books)}")
    print("Mentve: talalatok.csv")