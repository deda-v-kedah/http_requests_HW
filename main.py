from pprint import pprint
import requests


def smartest_superhero():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    iq = 0
    for i in response.json():
        if i['name'] in ['Hulk', 'Captain America', 'Thanos']:
            if iq < i['powerstats']['intelligence']:
                iq = i['powerstats']['intelligence']
                iq_belongs = i['name']
    print(f"Самый умный: {iq_belongs} со значением: {iq}")


smartest_superhero()
