import requests

# Define the API endpoint URL and query parameters
url = 'https://nominatim.openstreetmap.org/search.php'
params = {
    'q': 'Derbyshire',
    'format': 'json',
    'polygon_geojson': 1,
    'addressdetails': 1,
    'limit': 1
}

# Send the API request
response = requests.get(url, params=params)

# Extract the place id from the response
if response.status_code == 200:
    data = response.json()
    if data:
        place_id = data[0]['place_id']
        print(f'Place id for Derbyshire: {place_id}')
    else:
        print('No results found.')
else:
    print(f'Request failed with status code {response.status_code}.')

