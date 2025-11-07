class Tarefas:
    
    def __init__(self):
        raise ErroPersonalizado('Esse é um erro personalizado')
        
    
class ErroPersonalizado(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)