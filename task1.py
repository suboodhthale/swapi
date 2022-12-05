"""The Star Wars API lists 82 main characters in the Star Wars saga. For the first task, we w
ould like you to use a random number generator that picks a number between 1-82. Using the
se random numbers you will be pulling 15 characters from the API using Python."""

import requests
from mymodules.random_generator import Random15

start, stop  = 1, 83

def random_chars(obj_):
    charecters = []
    for i in obj_:
        charecters.append(i)
    return charecters


if __name__ == "__main__":
    print(__name__)
    print("current module is exicuting")
    home_url = "https://swapi.dev"
    relative_url = "/api/people/{0}"    #magic string
    print("Producing random 15 charecters")
    obj = Random15(start,stop)
    charecters = random_chars(obj)

    '''import pdb
    pdb.set_trace()'''

    for i in charecters:
        absolute_url = home_url + relative_url.format(i)    #random 15 numbers used in magic string
        print(f"Now fetcting 15 charecters data from {absolute_url}")
        response = requests.get(absolute_url)
        response = response.json()
        print(response)
        print("*******" * 25)




