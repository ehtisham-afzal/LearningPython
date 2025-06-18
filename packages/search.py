# from chicago.artworks import get_artworks
from chicago.artist import get_artists


def main():
    # inputQuerry = input("Search querry: ")
    # results = get_artworks(query=inputQuerry, limit=10)
    inputQuerry = input("Search artists: ")
    results = get_artists(query=inputQuerry, limit=5)
    print(results)


main()
