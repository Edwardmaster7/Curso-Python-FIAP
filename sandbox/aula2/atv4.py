# Você tem uma lista de pedidos. Cada pedido é uma tupla: (id, cliente, valor, status). Extraia: 
#    (1) Pedidos pendentes, (2) Valor total, (3) Cliente com mais pedidos.
pedidos = [
    (1, "Ana", 150.00, "pago"),
    (2, "Bruno", 200.00, "pendente"),
    (3, "Ana", 100.00, "pago"),
    (4, "Carlos", 300.00, "pendente"),
    (5, "Ana", 50.00, "cancelado"),
]

# Desafio: Resolver em 5 minutos!
# Dica: Use compreensão de lista e função sum()

from collections import Counter


pendentes = [p for p in pedidos if p[3] == "pendente"]
clientes = [p[1] for p in pedidos]
cliente_com_mais_pedidos = Counter(clientes).most_common(1)[0][0] # desenpacota o valor da lista e da tupla
total = sum([p[2] for p in pedidos if p[3] != "cancelado"])

print(f"Pedidos pendentes: {pendentes}")
print(f"Cliente com mais pedidos: {cliente_com_mais_pedidos}")
print(f"Valor total: {total}")