import requests
import pytest

url='https://api.pokemonbattle.me:9104'
token='e2009324e57cd032f8e15f9ee78fef2d'

def test_status_code():
    response = requests.get ("https://api.pokemonbattle.me:9104/trainers", params= {'trainer_id':"2460"})
    assert response.status_code == 200


def test_part_of_body():
    response = requests.put(f'{url}/trainers',headers={"trainer_token":token},
                            json={
                                "name":"Kрокодил",
                                "city":"Tokyo"
                            })
    assert response.json()["message"] =="Информация о тренере обновлена"
   