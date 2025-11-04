# Transforme uma lista de pedidos em um dicionário {cliente: total_gasto}, 
# mas apenas para clientes com mais de R$ 100 em compras.
pedidos = [
    {"cliente": "Ana", "valor": 50.00},
    {"cliente": "Bruno", "valor": 150.00},
    {"cliente": "Ana", "valor": 80.00},  # Ana: 130 total
    {"cliente": "Carlos", "valor": 30.00},
    {"cliente": "Bruno", "valor": 50.00},  # Bruno: 200 total
]

# Desafio: Usar dict comprehension + sum()

from collections import defaultdict # cria um dicionário padrão com um tipo de valor específico

totais = defaultdict(float)
for pedido in pedidos:
    totais[pedido["cliente"]] += pedido["valor"] # o default dict vai receber uma chave cliente e um valor 

print(totais)

# Cria um dicionário 'cliente_vip' onde as chaves são os clientes e os valores são os totais gastos,
# apenas para clientes que gastaram mais de 100.
# Itera sobre os itens (pares chave-valor) do dicionário 'totais'.
# Para cada par cliente-total, verifica se o total é maior que 100.
# Se for, adiciona o cliente e o total ao dicionário 'cliente_vip'.
cliente_vip = {cliente: total for cliente, total in totais.items() if total > 100}
print(cliente_vip)