'''
Para facilitar a importação, podemos expor as classes principais aqui.

Assim, em vez de "from carstorechallenge.models import Carro", o dev poderá usar "from carstorechallenge import Carro".
'''

from .models import Carro, Concessionaria

__all__ = ['Carro', 'Concessionaria']
