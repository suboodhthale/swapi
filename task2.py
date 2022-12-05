import requests
from mymodules.fetch_data import fetch_data

def get_all_chars(result):
    char_urls = result.get("characters")
    char_data = fetch_data(char_urls) if char_urls else []
    char_names = [char.get("name") for char in char_data if char_data]  #char.get("name") to access values of key "name"
    return char_data

def get_vehicle_names(result):
    v_urls = result.get("vehicles")
    v_data =  fetch_data(v_urls) if v_urls else []
    v_names = [vehicle.get("name") for vehicle in v_data if v_data]
    return v_names

if __name__ ==  "__main__":
    url = "https://swapi.dev/api/films/1/"
    response = requests.get(url)
    result = response.json()
    char_names = get_all_chars(result)
    vehicles = get_vehicle_names(result)
    print(char_names)
    print("****" * 25)
    print(vehicles)