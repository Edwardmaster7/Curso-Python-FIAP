import os

# Numéricos
inteiro:int = 10
flutuante:float = 10.5

# Texto
texto:str = "Olá, mundo!"
texto_bytes:bytes = b"Ola, mundo!"

os.system("clear")
print((f"O valor da variável inteira é: {inteiro}"))
print(f"O tipo da variável inteira é: {type(inteiro)}")

# Nulo
inteiro:any = None

print((f"O valor da variável inteira é: {inteiro}"))
print(f"O tipo da variável inteira é: {type(inteiro)}")

# Booleano
booleano:bool = True

print((f"O valor da variável booleano é: {booleano}"))
print(f"O tipo da variável booleano é: {type(booleano)}")


# Coleções

# Listas
lista:list = [1, "João", True, 10.5, None, b'Bytestring']

print((f"O valor da variável lista é: {lista}"))
print(f"O tipo da variável lista é: {type(lista)}")

# Tuplas
tupla:tuple = (1, 2, 3, 4, 5)

print((f"O valor da variável tupla é: {tupla}"))
print(f"O tipo da variável tupla é: {type(tupla)}")

# Sets
listinha:set = {'banana', 'maçã', 'uva'}
print((f"O valor da variável listinha é: {listinha}"))
print(f"O tipo da variável listinha é: {type(listinha)}")

listinha.append('banana')

# Dicionários
dicionario:dict = {"nome": "João", "idade": 20}