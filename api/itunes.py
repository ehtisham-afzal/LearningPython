import requests
import sys
# import json


if len(sys.argv) < 2:
    sys.exit()

# command "python itunes.py weezer"
# data = requests.get(
#     "https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1]
# )

# print the resonse on json formate and not prettyfied
# print(data.json())

# print the resonse on json formate and prettyfied with python json library
# print(json.dumps(data.json(), indent=2))


# fetch and print the 10 trackName's of artist names weezer from apple itunes api and print them on console

# command "python itunes.py weezer"
response = requests.get(
    "https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1]
)

data = response.json()

for result in data["results"]:
    print(result["trackName"])
