import requests

heroes = ['Hulk', 'Captain America', 'Thanos']
def most_int_hero(list):
    response = requests.get('https://akabab.github.io/superhero-api/api/all.json')
    heroes_int_list = {}
    for hero in response.json():
        if hero['name'] in heroes:
            heroes_int_list[hero['name']] = hero['powerstats']['intelligence']
    return (max(heroes_int_list))

print(most_int_hero(heroes))
