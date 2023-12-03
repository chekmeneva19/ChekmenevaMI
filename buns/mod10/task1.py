import requests
import json
api_url = 'https://swapi.dev/api/starships/10/'
response = json.loads(requests.get(api_url).text)

pilots = []

for pilot in response['pilots']:
    pilot_response = json.loads(requests.get(pilot).text)
    pilot_info = {'имя': pilot_response['name'],
                  'рост': pilot_response['height'],
                  'вес:': pilot_response['mass'],
                  'Родная планета': json.loads(requests.get(pilot_response['homeworld']).text)['name'],
                  'Ссылка на информацию о родной планете': pilot_response['homeworld']}
    pilots.append(pilot_info)

ship_info = {'name': response['name'],
            'max_atmosphering_speed': response['max_atmosphering_speed'],
            'starship_class': response['starship_class'],
            'pilots': pilots}

with open('info_starship.json', 'w') as file:
    json.dump(ship_info, file, indent=4)

print(json.dumps(ship_info, indent=4))