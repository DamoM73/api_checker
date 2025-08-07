import requests
from pprint import pprint
import timeit

for id in range(732):
    start = timeit.default_timer()
    response = requests.get(f"https://superheroapi.com/api/0f9e3ce4e9b83ce606ac1d993fa55105/{id}")
    elapsed = timeit.default_timer() - start
    if response.json()["response"] == "success":
        print(f"ID: {id}\tTime: {elapsed:.4f} seconds")
        pprint(response.json())
     