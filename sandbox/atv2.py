# Esqueleto inicial:
tempos_resposta = [50, 120, 450, 1200, 80, 950]

# DESAFIO: Use for + if/elif/else para classificar
# Saída esperada:
# 50ms: Excelente
# 120ms: Bom

print("Tempos de resposta da API:")

for tempo in tempos_resposta:
    if tempo <= 50:
        print(f"{tempo}ms: Excelente")
    elif tempo <= 120:
        print(f"{tempo}ms: Bom")
    elif tempo <= 450:
        print(f"{tempo}ms: Ruim")
    else:
        print(f"{tempo}ms: Péssimo")