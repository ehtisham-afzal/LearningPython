import requests


def get_artworks(query, limit=5):
    try:
        response = requests.get(
            "https://api.artic.edu/api/v1/artworks/search", {"q": query, "limit": limit}
        )
        response.raise_for_status()
    except requests.HTTPError:
        return "faild to fetch data from api"

    data = response.json()
    # titles = []
    titles = ""

    for results in data["data"]:
        # titles.append(results["title"])
        titles += results["title"] + " \n"
    return titles
