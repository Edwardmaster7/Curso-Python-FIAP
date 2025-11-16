from json import loads

class Main:
    
    def __init__(self) -> None:
        from .utils import return_args
        self.args = return_args()

        try: 
            self.veiculo = self.args.vehicle
        except AttributeError: 
            self.veiculo = None
        
        try: 
            self.modelo = self.args.model
            self.request_id('modelo', self.modelo)
        except AttributeError: 
            self.modelo = None
        
        try: 
            self.marca = self.args.brand
            self.request_id('marca', self.marca)

        except AttributeError: 
            self.marca = None
        
        try: 
            self.ano = self.args.year
        except AttributeError: 
            self.ano = None
        
        self.call_info()
        
    def call_info(self):
        from .api import connect, retrieve
        
        if not connect(veiculo=self.args.vehicle): 
            print("Necssãrio um tipo de veículo.")
            exit()
        
        info = retrieve(veiculo = self.veiculo, marca = self.marca, modelo = self.modelo)
        print(info.content)
    
    def request_id(self, tipo, nome):
        from .api import retrieve
        response = retrieve(veiculo=self.veiculo)
        for item in loads(response):
            if item["nome"].lower() == nome.lower():
                return item["codigo"]
        
class Carro:
    
    def __init__(self):
        pass

class Marca:
    ...