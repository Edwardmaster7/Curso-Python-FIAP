# Exemplo de *args e **kwargs (key,word arguments)
def funcao_completa(obrigatorio, opcional="padrão", *args, **kwargs):
    print(f"Obrigatório: {obrigatorio}")
    print(f"Opcional: {opcional}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")
    
if __name__ == "__main__":
    funcao_completa(1, 2, 3, 4, "teste", nome="joao", idade=25)