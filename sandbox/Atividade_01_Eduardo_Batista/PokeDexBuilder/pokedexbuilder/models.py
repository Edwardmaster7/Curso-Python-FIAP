from unicodedata import numeric


class Pokemon:
    """
    Representa um Pokémon com dados extraídos da PokéAPI.

    Atributos:
        `id` (int): O número do Pokémon na Pokédex nacional.
        `nome` (str): O nome do Pokémon.
        `altura` (int): A altura do Pokémon em decímetros.
        `peso` (int): O peso do Pokémon em hectogramas.
        `tipos` (list): Uma lista de strings com os tipos do Pokémon.
        `habilidades` (list): Uma lista de strings com as habilidades do Pokémon.
    """
    def __init__(self, dados_json:dict):
        '''
        TODO
        ----

        Extraia os dados do dicionário `dados_json` e atribua-os aos atributos da classe.

        >>> self.id = dados_json['id']
        
        Dica: Para 'tipos' e 'habilidades', use list comprehension.
        
        >>> self.tipos = [item['type']['name'] for item in dados_json['types']]
        '''
        self.id:int = dados_json.get("id")
        self.nome:str = dados_json.get("name")
        self.altura:float = dados_json.get("height")
        self.peso:float = dados_json.get("weight")
        self.tipos:list[dict] = [item["type"]["name"] for item in dados_json.get("types")]
        # self.habilidades:list[dict] = [item["abilities"]["name"] for item in dados_json.get("abilities")]

    def __str__(self):
        return f"Id: {self.id}, Name: {self.nome}, Height: {self.altura}, Weight: {self.peso}, Types: {self.tipos}"


class Pokedex:
    """
    Representa uma Pokédex que armazena os Pokémon capturados.

    Atributos:
        `dono` (str): O nome do treinador que possui a Pokédex.
        `pokemons` (dict): Um dicionário de Pokémon, onde a chave é o ID
                         e o valor é o objeto Pokemon.
    """

    def __init__(self, dono):
        '''
        TODO
        ----
        Inicialize os atributos 'dono' e 'pokemons' (como um dicionário vazio).
        '''
        self.dono:str = dono
        self.pokemons:dict = {}

    def adicionar_pokemon(self, pokemon:Pokemon):
        """
        TODO
        ----
        Adiciona um objeto Pokemon ao dicionário da Pokédex.

        A chave deve ser o ID do pokemon.
        """
        self.pokemons[pokemon.id] = pokemon

    def listar_pokemons(self):
        """
        TODO
        ----
        
        Itere sobre o dicionário `'self.pokemons'` e imprima os detalhes de cada um.

        >>> #025 - Pikachu | Tipos: ['electric']

        Imprima um resumo de cada Pokémon na Pokédex.
        """
        print(f"Pokédex de {self.dono}:")
        if not self.pokemons:
            print("  Nenhum Pokémon capturado ainda.")
            return
        
        for pokemon in self.pokemons.values():
            print(f"  {pokemon} | Tipos: {pokemon.tipos}")
