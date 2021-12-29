import requests
from pprint import pprint
#from requests.models import parse_url
#TOKKEN = '2619421814940190'
ids = {}
def test_requests():
    url = "https://www.superheroapi.com/api.php/2619421814940190/search/Thanos"
    response = requests.get(url)
    list_Thanos = response.json()
    Thanos = list_Thanos['results']
    for info in Thanos:
        powerstats = info['powerstats']
        intelligence = powerstats['intelligence']
        ids['Thanos'] = intelligence
if __name__ == '__main__':
    test_requests()

def test_requests():
    url = "https://www.superheroapi.com/api.php/2619421814940190/search/Captain America"
    response = requests.get(url)
    list_CA = response.json()
    CA = list_CA['results']
    for info in CA:
        powerstats = info['powerstats']
        intelligence = powerstats['intelligence']
        ids['Captain America'] = intelligence
if __name__ == '__main__':
    test_requests()

def test_requests():
    url = "https://www.superheroapi.com/api.php/2619421814940190/search/Hulk"
    response = requests.get(url)
    list_Hulk = response.json()
    Hulk = list_Hulk['results']
    for info in Hulk:
        powerstats = info['powerstats']
        intelligence = powerstats['intelligence']
        ids['Hulk'] = intelligence
if __name__ == '__main__':
    test_requests()

intelligence = max(ids, key = ids.get)
print(f' Самый умный из героев: {intelligence}')