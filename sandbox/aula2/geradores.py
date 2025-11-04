# RUIM: Cria lista com 1M de elementos na memória
numeros = [x**2 for x in range (1_000_000)]

# BOM: gera valores sob demanda (expressão geradora)
generator = (x**2 for x in range (1_000_000))
print(type(generator))

# for v in generator:
#     print(v)

# função geradora
def fibonacci(n: int):
    """Gera os primeiros n números de Fibonacci

    Args:
        n (int): _description_
    """
    a, b = 0, 1
    
    for _ in range(n):
        # A palavra-chave 'yield' transforma a função em um gerador.
        # Em vez de retornar um valor e encerrar a função, 'yield' produz um valor
        # e pausa a execução da função. O estado da função é salvo para que possa
        # ser retomada posteriormente. Na próxima vez que o gerador for chamado,
        # a execução continuará a partir do ponto onde 'yield' parou.
        yield a
        a, b = b, a + b
        
for num in fibonacci(10):
    print(num, end=" ")