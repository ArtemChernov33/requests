import requests
from pprint import pprint
Heroes = ['Thanos', 'Captain America', 'Hulk']
ids = {}
def test_requests():
    for name in Heroes:
            url = ("https://www.superheroapi.com/api.php/2619421814940190/search/" + name)
            response = requests.get(url)
            list_name = response.json()
            heroes = list_name['results']
            for info in heroes:
                powerstats = info['powerstats']
                intelligence = powerstats['intelligence']
                ids[name] = intelligence
if __name__ == '__main__':
    test_requests()

intelligence = max(ids, key = ids.get)
print(f' Самый умный из героев: {intelligence}')

test_requests()