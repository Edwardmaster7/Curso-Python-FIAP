import requests 
from json import loads as json_loads

BASE_URL = 'https://api.disneyapi.dev'
FETCH = 'character'

class Disney:
    def __init__(self, id:int):
        self.id:int = id
        info = self.chamar_personagem()
        self.url:str = info.get('url')
        self.name:str = info.get('name')
        self.image_url:str = info.get('imageUrl')
        self.films:list[str] = info.get('films')
        self.short_films:list[str] = info.get('shortFilms')
        self.tv_shows:list[str] = info.get('tvShows')
        self.video_games:list[str] = info.get('videoGames')
        self.park_attractions:list[str] = info.get('parkAttractions')
        self.allies:list[str] = info.get('allies')
        self.enemies:list[str] = info.get('enemies')
        
    def chamar_personagem(self) -> dict:
        response:requests = requests.get(f"{BASE_URL}/{FETCH}/{self.id}")
        
        raw_content:bytes = response.content
        parsed_content:dict = json_loads(raw_content)['data']
        return dict(parsed_content)

if __name__ == '__main__':
    
if __name__ == '__main__':
    try:
        '''
        Nome: {nome}
        Imagem: {imageUrl}
        Filmes:
            {film1}
            {film2}
            {film3}
        Video Games:
            {vg1}
            {vg2}
        '''
        id = '4703'
        char = Disney(id)
        #first_name = char.name.split(' ')[0]
        print(f'Nome: {char.name}')
        print(f'Imagem: {char.image_url}')
        print('Filmes:')
        for filme in char.films:
            print('\t-',filme)
        print('Video Games:')
        for vg in char.video_games:
            print('\t-',vg)
    except KeyboardInterrupt:
        exit()