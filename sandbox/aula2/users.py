from functools import cache


cache_users = {}
def obter_usuario(user_id: int):
    if user_id in cache_users:
        print("Usuário encontrado no cache")
        return cache_users[user_id]
    else:
        print("Usuário não encontrado no cache")
    
    # Simulação de busca no banco de dados
    usuario = {"id": user_id, "nome": "Usuário " + str(user_id), "email": "usuario" + str(user_id) + "@exemplo.com"}
    
    cache_users[user_id] = usuario
    return usuario

user1 = obter_usuario(123) # MISS
user2 = obter_usuario(123) # HIT
user3 = obter_usuario(456) # MISS

# Estatísticas do cache
print(f"\nTotal em cache: {len(cache_users)}")
print(f"IDs em cache: {list(cache_users.keys())}")