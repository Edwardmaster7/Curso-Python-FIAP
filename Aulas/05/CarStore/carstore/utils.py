from sys import argv
from argparse import ArgumentParser

def return_args():
    args = ArgumentParser('CarStore', 
                                'carstore.py -t carro -b Lamborghini -m Aventador -y 2020-1', 
                                "Busca carros e seus preços para venda na loja")
    
    args.add_argument('-v', '--vehicle', help='Recebe um tipo de veículo.')
    args.add_argument('-b', '--brand', help='Recebe uma marca de carro.')
    args.add_argument('-m', '--model', help='Recebe um modelo de carro.')
    args.add_argument('-y', '--year', help='Recebe o ano do veículo.')
    
    return args.parse_args()