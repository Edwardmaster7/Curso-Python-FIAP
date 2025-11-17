# main.py
import requests

# TODO: Importe suas classes Pokedex e Pokemon, e a função de API.
from pokedexbuilder import Pokedex, Pokemon
from api import buscar_pokemon

def main():
    """
    Função principal para executar o PokeDex Builder.

    Essa função deve conter a possibilidade de criar uma nova pokedex

    Exemplo
    -------
    >>> pokedex = Pokedex(dono='Ash')

    O usuário deve ser capaz de remover ou adicionar pokemons da pokedex

    >>> pokedex.add('pikachu')
    >>> pokedex.remove('magikarp')

    O usuário deve poder listar pokemons

    >>> pokedex.list() ou pokedex.__str__
    """
    print("Iniciando o PokeDex Builder!")

    # Lista de Pokémon para buscar.
    pokemons_para_buscar = ["pikachu", "charizard", "bulbasaur", "mewtwo", "ditto"]

    pokedex:Pokedex = Pokedex("Ash")

    for pokemon in pokemons_para_buscar:
        response = buscar_pokemon(pokemon)
        new_pokemon = Pokemon(response)
        pokedex.adicionar_pokemon(new_pokemon)

    pokedex.listar_pokemons()

if __name__ == "__main__":
    main()
