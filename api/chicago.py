import requests
# import json


def main():
    print("Search the Art Instetute of Chicago by typing artist name below")
    artist = input("Artist: ")
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", {"q": artist}
        )
        response.raise_for_status()
    except requests.HTTPError:
        print("faild to fetch data from api")
        return
    data = response.json()

    for results in data["data"]:
        print(f"* {results['title']}")

    # print(json.dumps(data, indent=2))


main()
