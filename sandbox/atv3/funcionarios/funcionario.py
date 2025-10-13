# funcionario.py
class Funcionario:
    def __init__(self, nome: str, cargo: str, salario: float):
        # Validações e inicialização
        self.nome = nome
        self.cargo = cargo
        self.__cargos__ = ["Gerente", "Chefe", "Peão"]
        self.salario = float
        pass

    @property
    def nome(self) -> str:
        return self.nome

    @property
    def cargo(self) -> str:
        return self.cargo

    @property
    def salario(self) -> float:
        return self.salario
    
    @nome.setter
    def nome(self, value: str):
        if any(char.isalpha() for char in value):
            raise ValueError("Nome deve conter apenas caracteres alfabéticos")
        self.nome = value
    
    @cargo.setter
    def cargo(self, value: str):
        if value not in self.__cargos__:
            raise ValueError(f"Cargo deve receber um dos seguintes valores: {self.__cargos__}")
        self.cargo = value
    
    def calcular_bonus(self) -> float:
        # Calcular 10% do salário
        return self.salario * 0.1

