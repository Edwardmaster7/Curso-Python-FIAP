from requests import get
from urllib3.util import connection

URL = 'https://parallelum.com.br/fipe/api/v1/'
def connect(veiculo:str, marca:str = None, modelo:str = None):
    response = get(f"{URL}/carros/marcas")  
    return True if response.status_code == 200 else False

def retrieve(**args):
    veiculo = args.get('veiculo')
    marca = args.get('marca')
    modelo = args.get('modelo')
    ano = args.get('ano')
    
    if not veiculo: return f"[erro: NOT_FOUND]"
    if not marca: connection = f"{URL}/{veiculo}/marcas"
    elif not modelo: connection = f"{URL}/{veiculo}/marcas/{marca}/modelos/{modelo}/anos"
    elif not ano: connection = f"{URL}/{veiculo}/marcas/{marca}/modelos/{modelo}/anos"
    
if __name__ == '__main__':
    connect('carros')