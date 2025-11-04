# lista = [] # mutável
# tupla = () # imutável e usa hashtable (quando precisamos de performance e não precisamos alterar os valores)


# usuarios = ["Ana", "Bruno", "Carla"]
# usuarios.append("Daniel") # add no final
# usuarios.insert(1, "Beatriz") # insere em uma posição específica
# usuarios.remove("Carla") # remove pelo valor
# usuarios.pop(0) # remove pela posição e retorna o ítem nesse índex
# usuarios[usuarios.index("Beatriz")] = "Beata"

# SET
tecnologias = {"Python", "Java", "JavaScript", "Python"}
print(tecnologias)

# Operações de conjuntos
backend_devs = {"Ana", "Bruno", "Carlos"}
frontend_devs = {"Bruno", "Diana", "Elena"}

# Interseção (quem faz ambos?)
fullstack = backend_devs & frontend_devs  # {'Bruno'}

# União (todos os devs)
todos_devs = backend_devs | frontend_devs

# Diferença (só backend)
so_backend = backend_devs - frontend_devs  # {'Ana', 'Carlos'}