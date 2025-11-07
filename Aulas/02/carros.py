class Carro:
    
    def __init__(self,
                 marca:str,
                 modelo:str,
                 ano:int,
                 preco:float
                 ) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
    
    def __repr__(self) -> str:
        return f'Carro(marca=\'{self.marca}\', modelo=\'{self.modelo}\', ano=\'{self.ano}\', preco=\'{self.preco}\')'

    def __str__(self) -> str:
        return f'({self.marca}) ({self.modelo}) ({self.ano}) → R${self.preco}'
    
    # def __eq__(self, other) -> bool:
    #     if isinstance(other, Carro):
    #         carro_1 = (self.marca, self.modelo, self.ano, self.preco)
    #         carro_2 = (self.marca, self.modelo, self.ano, self.preco)
            
    #         if carro_1 == carro_2:
    #             return True
    #     return False

    def __gt__(self, other):
        if not isinstance(other, Carro):
            return None
        preco_1 = self.preco
        preco_2 = other.preco
        
        if preco_1 > preco_2: 
            return True
        return False
    
if __name__ == '__main__':
    ka = Carro('Ford', 'Ka', 2020, 35000.0)
    ka_2 = Carro('Ford', 'Ka', 2016, 8000.0)
    
    f1_gtr = Carro('Mclaren', 'F1-GTR', 1996, 12000000.0)
    charger = Carro('Dodge', 'Charger', 1970, 230000.0)
    
    list_carros = []
    list_carros.append(ka)
    list_carros.append(f1_gtr)
    list_carros.append(charger)
    
    print(f'User-frendly: {ka}')
    print(f'para devs: {repr(ka)}')
    
    print('----'*20)
    
    print(ka == ka_2) # acessa o __eq__ equivalent
    
    print(ka > ka_2) # acessa o __gt__ greater than