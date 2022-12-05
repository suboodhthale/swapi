import requests

url = "https://swapi.dev/api/films/1/"

response = requests.request("GET", url)

print(response.text)
