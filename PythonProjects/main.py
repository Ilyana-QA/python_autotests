import requests

token="e2009324e57cd032f8e15f9ee78fef2d"
url="https://api.pokemonbattle.me:9104"
'''response = requests.post('https://api.pokemonbattle.me:9104/trainers/reg',
 json={"trainer_token": token,"email": "ml9vu9@sfolkar.com", "password": "Iloveqa1"},
 headers = {"Content-Type":"application/json"})

print(response.text)'''

response_sozdat = requests.post('https://api.pokemonbattle.me:9104/pokemons',json={
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"},
 headers={"Content-Type": "application/json","trainer_token":"e2009324e57cd032f8e15f9ee78fef2d"})

print(response_sozdat.text)

response_name=requests.put('https://api.pokemonbattle.me:9104/pokemons',json=
{
    "pokemon_id": "11857",
    "name": "Крокодил",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
},  headers={"Content-Type": "application/json","trainer_token":"e2009324e57cd032f8e15f9ee78fef2d"})

print(response_name.text)

response_pokebol = requests.post(f'{url}/trainers/add_pokeball', json=
{
    "pokemon_id": "11857"
},
 headers={"Content-Type": "application/json","trainer_token":"e2009324e57cd032f8e15f9ee78fef2d"})

print(response_pokebol.text)

