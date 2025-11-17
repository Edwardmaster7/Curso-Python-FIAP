# Importe as classes Carro e Concessionaria do seu módulo.
# Ex: from carstorechallenge.models import Carro, Concessionaria
from carstorechallenge import Carro, Concessionaria

dados_api_1:dict = {
    "id": "f7e6e8b5-5a3c-4b0f-8d7a-9c1e0b9b0e4a",  # UUID
    "modelo": "Tesla Model S",
    "marca": "Tesla",
    "ano": 2023,
    "valor_base": 1587865.22,
    "condicao": "Novo",  # Pode ser: Novo, Usado, Recondicionado, Avariado
}

dados_api_2:dict = {
    "id": "a1b2c3d4-e5f6-7890-1234-567890abcdef",
    "modelo": "Lamborghini Revuelto",
    "marca": "Lamborghini",
    "ano": 2025,
    "valor_base": 4867905.37,
    "condicao": "Avariado",
}

dados_api_3:dict = {
    "id": "6a7b8c9d-0e1f-2345-6789-012345fedcba",
    "modelo": "Hyundai Hb20",
    "marca": "Hyundai",
    "ano": 2025,
    "valor_base": 109990.00,
    "condicao": "Usado",
}

dados_api:dict = []

dados_api.append(dados_api_1)
dados_api.append(dados_api_2)
dados_api.append(dados_api_3)

def main():
    """
    Função principal para executar o desafio CarStore.

    Desafio
    -------

    - Crie uma instância da sua classe Concessionaria.

    >>> minha_concessionaria = Concessionaria(nome="Super Car")

    - Defina os dados da "API" como um dicionário.

    - Crie uma instância da classe Carro utilizando os dados do dicionário.

    >>> novo_carro = Carro(**dados_api)

    - Adicione o carro criado à sua concessionária.

    - Adicione o carro criado à sua concessionária.

    >>> minha_concessionaria.adicionar_carro(novo_carro)

    - Gere e imprima o relatório para o carro adicionado.

    >>> relatorio = minha_concessionaria.gerar_relatorio_carro(novo_carro)
    >>> print(relatorio)

    Desafio Extra
    -------------
    Crie outros carros com condições diferentes e adicione-os.

    Depois, chame um método que gera um relatório para todos os carros da concessionária.
    """
    print("Iniciando o Desafio da Concessionária...")

    minha_concessionaria = Concessionaria(nome="Tkar")

    for response in dados_api:
        carro = Carro(**response)
        minha_concessionaria.adicionar_carro(carro)

    minha_concessionaria.gerar_relatorio_geral()

if __name__ == "__main__":
    main()
