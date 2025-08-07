import requests
import urllib3
import timeit

def can_access(url):
    response = requests.head(url, verify=False)  # Disable SSL certificate verification
    return response.status_code == 200

urls = [
    "https://api.open5e.com/v1/manifest/",
    "https://api.open5e.com/v2/spells/",
    "https://api.open5e.com/v1/spelllist/",
    "https://api.open5e.com/v1/monsters/",
    "https://api.open5e.com/v2/documents/",
    "https://api.open5e.com/v2/backgrounds/",
    "https://api.open5e.com/v1/planes/",
    "https://api.open5e.com/v1/sections/",
    "https://api.open5e.com/v2/feats/",
    "https://api.open5e.com/v2/conditions/",
    "https://api.open5e.com/v1/races/",
    "https://api.open5e.com/v1/classes/",
    "https://api.open5e.com/v1/magicitems/",
    "https://api.open5e.com/v2/weapons/",
    "https://api.open5e.com/v2/armor/",
]

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

for url in urls:
    start = timeit.default_timer()
    access = can_access(url)
    elapsed = timeit.default_timer() - start
    print(f"{url}\taccess: {access}\ttime: {elapsed:.4f} seconds")

