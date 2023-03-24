import requests

url = "https://opendomesday.org/api/1.0/county/dby"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    place_ids = [place["id"] for place in data["places_in_county"]]
    print(place_ids)
else:
    print(f"Failed to retrieve data. Error code: {response.status_code}")
