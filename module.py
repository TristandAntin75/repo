import requests
import pandas as pd

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


def place_ids():
    """
    Retrieves a list of all place IDs in Derbyshire.
    """
    url = "https://opendomesday.org/api/1.0/county/dby"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        place_ids = [place["id"] for place in data["places_in_county"]]
        return place_ids
    else:
        print(f"Failed to retrieve data. Error code: {response.status_code}")

def get_all_manor_ids_in_derbyshire():
    """
    Retrieves a list of all manor IDs in all places in Derbyshire.
    """
    all_manor_ids = []
    cpt=0
    # Call place_ids() to retrieve a list of place IDs in Derbyshire
    place_ids_list = place_ids()
    # Iterate through all place IDs in Derbyshire and call get_manor_ids for each place
    for place_id in place_ids_list:
        manor_ids = get_manor_ids(place_id)
        all_manor_ids.extend(manor_ids)
    return all_manor_ids



def get_manor_info(manor_ids):
    manor_info = []
    for manor_id in manor_ids:
        response = requests.get(f"https://opendomesday.org/api/1.0/manor/{manor_id}/")
        if response.status_code == 200:
            data = response.json()
            manor = {
                "id": manor_id,
                "geld": data["geld"],
                "total_ploughs": data["totalploughs"]
            }
            manor_info.append(manor)
    return manor_info


if __name__ == '__main__':
    manor_ids = get_all_manor_ids_in_derbyshire()
    manor_info = get_manor_info(manor_ids)
    df = pd.DataFrame(manor_info)
    print(df)
