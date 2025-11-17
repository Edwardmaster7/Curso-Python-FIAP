# carstorechallenge/models.py


class Carro:
    """
    Representa um carro na concessionária.

    Atributos:
        `id` (str): O identificador único do carro.
        `modelo` (str): O modelo do carro.
        `marca` (str): A marca do carro.
        `ano` (int): O ano de fabricação do carro.
        `valor_base` (float): O valor base do carro.
        `condicao` (str): A condição do carro (Novo, Usado, etc.).
    """

    def __init__(self, id, modelo, marca, ano, valor_base, condicao):
        self.id = id
        self.modelo = modelo
        self.marca = marca
        self.ano = ano
        self.valor_base = valor_base
        self.condicao = condicao

    def __str__(self) -> str:
        return f"Id: {self.id}, Modelo: {self.modelo}, Marca: {self.marca}, Ano: {self.ano}, Valor Base: {self.valor_base}, Condição: {self.condicao}"

    def __repr__(self) -> str:
        return f"Carro(id={self.id}, modelo={self.modelo}, marca={self.marca}, ano={self.ano}, valor_base={self.valor_base}, condicao={self.condicao})"


class Concessionaria:
    """
    Representa a concessionária que gerencia os carros.

    Atributos:
        `nome` (str): O nome da concessionária.
        `carros` (list): A lista de carros (objetos da classe Carro) na concessionária.
    """

    def __init__(self, nome):
        self.nome: str = nome
        self.carros: list[Carro] = []

    def adicionar_carro(self, carro):
        """
        Adiciona um carro à lista da concessionária.
        """
        if isinstance(carro, Carro):
            self.carros.append(carro)
        else:
            raise ValueError("Valor de 'carro' não é uma instância de 'Carro'.")

    def calcular_preco_venda(self, carro):
        """
        Calcula o preço de venda de um carro com base na sua condição.

        Regras:
        - Novo: `valor_base` + 20%
        - Usado: `valor_base` - 30%
        - Recondicionado: `valor_base` - 40%
        - Avariado: `valor_base` - 55%
        """
        if not isinstance(carro, Carro):
            raise ValueError("Valor de 'carro' não é uma instância de 'Carro'.")
        elif carro.valor_base <= 0:
            raise ValueError("'valor_base' deve ser maior que 0.")

        valor: float = carro.valor_base

        match carro.condicao.lower():
            case "novo":
                valor += carro.valor_base * 0.2
            case "usado":
                valor -= carro.valor_base * 0.3
            case "recondicionado":
                valor -= carro.valor_base * 0.4
            case "avariado":
                valor -= carro.valor_base * 0.55

        return valor

    def gerar_relatorio_carro(self, carro):
        """
        Gera uma string formatada com o relatório de um carro específico.

        TODO
        ----
        1. Calcule o preço de venda chamando o método apropriado.
        2. Formate a string como especificado no instructions.md.

        Dica
        ----
        Use f-strings para facilitar a formatação.
        """
        preco_venda = self.calcular_preco_venda(carro)

        response = f"""--- Relatório do Veículo ---
Modelo: {carro.modelo}
Marca: {carro.marca}
Condição: {carro.condicao}
Valor Base: R$ {carro.valor_base}
Preço de Venda: R$ {preco_venda}
--------------------------
"""

        return response

    def gerar_relatorio_geral(self):
        """
        Gera uma string formatada com o relatório geral da concessionária.
        """
        response: str = ""

        for carro in self.carros:
            response += self.gerar_relatorio_carro(carro)

        # if print_output:
        #     print(response)

        return response
