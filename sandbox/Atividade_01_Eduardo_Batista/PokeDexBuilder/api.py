from typing import Any
import requests
from json import loads as json_loads

BASE_URL = "https://pokeapi.co/api/v2"
FETCH = "pokemon"


def buscar_pokemon(nome:str):

    response:requests = requests.get(f"{BASE_URL}/{FETCH}/{nome}")

    if response.status_code == 200:
        parsed_content:dict = response.json()
        return parsed_content
    else:
        print(f"Erro ao buscar Pokémon '{nome}': Status {response.status_code}")
        return None
    