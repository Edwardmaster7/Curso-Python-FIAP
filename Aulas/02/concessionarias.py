from carros import Carro

class Concessionaria:
    
    def __init__(self, nome:str, positions:int, arquivo_carros:str = None, dict_carros:dict = {}):
        self.nome = nome
        self.arquivo = arquivo_carros
        self.positions:int = positions
        self.dict_carros:dict[Carro] = dict_carros
        
        self.empty_positions:list[int] = list[int](range(1, positions+1))
        self.occup_positions:list[int] = []
        
        if not arquivo_carros:
            raise Exception('Nenhum arquivo passado')
        else:
            self.add_cars()
        
    def __repr__(self) -> str:
        return f'Concessionaria(nome="{self.nome}", positions="{self.positions}", arquivo_carros="{self.nome}", dict_carros="{self.dict_carros}")'
    
    def __str__(self) -> str:
        return f'{self.nome} ({self.positions} Posições)'
    
    def __add__(self, other):
        if not isinstance(other, Carro):
            raise Exception('Você tentou adcionar algo que não é um carro!')
        
        if other in self.dict_carros:
            return False
        
        try:
            self.dict_carros[self.empty_positions[0]] = other
            self.occup_positions.append(self.empty_positions[0])
            self.empty_positions.pop(0)
            print(f'{other.modelo} {other.ano} adcionado.')
        except (KeyError, IndexError):
            print(f'A concessionária "{self.nome}" está cheia! Não foi possível adcionar {other.modelo} {other.ano}')
            return None
    
    def __sub__(self, other):
        if not isinstance(other, Carro):
            raise Exception('Você tentou remover algo que não é um carro!')

        deletar = None
        
        for vaga, carro in self.dict_carros.items():
            if other == carro:
                deletar = vaga
                
        if deletar:
            self.occup_positions.remove(deletar)
            self.empty_positions.append(deletar)
            del self.dict_carros[deletar]
            print(f'{other.modelo} {other.ano}removido com sucesso.')

    def add_cars(self):
        from json import loads as json_loads
        
        with open(self.arquivo) as f:
            dict_carros:dict = json_loads(f.read())
        
        for _, carro in dict_carros:
            marca, modelo, ano, preco = carro
            car = Carro(marca, modelo, ano, preco)            
            self + car


    
if __name__ == '__main__':
    # super_car = Concessionaria(nome='Super Car', arquivo_carros='carros.json', positions=30)

    test_car = Concessionaria(nome='Teste', positions=2, arquivo_carros='carros.json')
    # ka = Carro('Ford', 'Ka', 2020, 35000.00)
    # ka_2 = Carro('Ford', 'Ka', 2016, 8000.0)
    # f1_gtr = Carro('Mclaren', 'F1-GTR', 1996, 12000000.0)
    # test_car + ka
    # test_car + ka_2
    # test_car + f1_gtr
    # test_car - ka
    # test_car + f1_gtr