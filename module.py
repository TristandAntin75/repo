import requests

def get_manor_ids(place_id):
    """
    Takes a place ID as a parameter and returns a list of manors associated with that place.
    """
    manor_ids = []
    
    # Send a GET request to the OpenDomesday API to retrieve information about the place
    response = requests.get(f'http://opendomesday.org/api/1.0/place/{place_id}')
    
    # Extract the manor IDs from the response JSON
    if response.status_code == 200:
        place_data = response.json()
        manor_ids = [manor['id'] for manor in place_data['manors']]
    
    return manor_ids
if __name__ == '__main__':
    # Test the get_manor_ids function
    place_id = 20086
    manor_ids = get_manor_ids(place_id)
    print(f"Manor IDs for place {place_id}: {manor_ids}")
