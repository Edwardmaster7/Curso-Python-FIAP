usuario = {
    "id": 123,
    "nome": "João",
    "email": "joao.silva@gmail.com",
    "senha": "senha123",
    "ativo": True,
    "data_cadastro": "2023-01-01 10:00:00",
    "data_nascimento": "1990-01-01",
    "endereco": {
        "rua": "Rua A",
        "numero": "123",
        "bairro": "Centro",
        "cidade": "São Paulo",
        "estado": "SP",
        "cep": "12345-678"
    }
}

print(usuario.get("endereco").get("rua"))
print(usuario.get("telefone", "Telefone não cadastrado"))

for valor in usuario.values():
    print(valor) 
    
# O(n) - Linear: lento
if "email" in usuario.values():
    print("Email cadastrado")

# O(1) - Constante: rápido
if "email" in usuario:
    print("Email cadastrado")