def adicionar_funcionario(lista: list, funcionario):
    # Adicionar à lista
    lista.append(funcionario)

def listar_por_cargo(lista: list, cargo: str) -> list:
    # Filtrar funcionários por cargo
    lista_filtrada = []
    for f in lista:
        if f.cargo == cargo
            lista_filtrada.append(f)
    
    return lista_filtrada

def calcular_folha_total(lista: list) -> float:
    # Somar salários + bônus
    total = float
    for f in lista:
        total += (f.salario + f.calcular_bonus())
    
    # return sum(f.salario + f.calcular_bonus() for f in lista)

    return total