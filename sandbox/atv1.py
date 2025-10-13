import numbers


def createUser(user_id: int, username: str, email: str, conta_ativa: bool, tags: list = ["admin", "user"]):
    return print(f"""
    Dados cadastrados com sucesso!
    
    user_id = {user_id}
    username = {username}
    email = {email}
    ativo = {"sim" if conta_ativa else "não"}
    tags = {tags}
    """)
    



if __name__ == "__main__":
    print("Bem-vindo a atividade 1!\nInforme os dados do usuário abaixo:")
    
    id = int(input("Insira o ID:"))
    
    name = input("Insira o Nome:")
    
    email = input("Insira o Email:")
    
    ativo = bool(input("O usuário está ativo? (0 - sim, 1 - não):"))
    
    createUser(id, name, email, ativo)
