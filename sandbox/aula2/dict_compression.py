quadrados = {i: i**2 for i in range(1, 11)}
print(quadrados)

# Mesclando dicts (Python 3.9+)
dict1 = {"a": 1, "b": 2, "c": 4}
dict2 = {"c": 3, "d": 4}
soma = dict1 | dict2 # união dos dois dicts 
soma2 = {**dict1, **dict2} # união dos dois dicts
# **dict1 e **dict2 desempacotam os dicionários dict1 e dict2, respectivamente, 
# permitindo que seus pares chave-valor sejam incluídos em um novo dicionário soma2. 
# Se houver chaves duplicadas, os valores de dict2 sobrescrevem os de dict1.
print(soma)
print(soma2)


