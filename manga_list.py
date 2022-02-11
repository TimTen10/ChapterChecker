import json

from utils.manga_parser import parse_mangakakalot, parse_readmanganato


class MangaList:

    def __init__(self, name, *params, **kwargs):
        # creates a new empty manga list
        self.name = name
        self.mangas = []
        self.update_time = kwargs.get('update_time', 24)
        if len(params) == 1:
            self.add_manga_list(*params)
        elif len(params) > 1:
            raise ValueError('Got too many attributes for creating a new MangaList object.')

    def add_manga_single(self, url):
        # Takes in an URL and adds the corresponding manga to the manga list object.
        if 'mangakakalot' in url:
            self.mangas.append(parse_mangakakalot(url))
        else:
            # TODO: split needed? readmanganato and manganelo
            self.mangas.append(parse_readmanganato(url))

    def add_manga_list(self, url_list):
        for manga_url in url_list:
            self.add_manga_single(manga_url.strip())

    def update_manga_single(self):
        pass

    def update_manga_list(self):
        # This should update every manga where the latest update > update interval
        # Might call update_manga_single inside
        pass

    def sort_by(self):
        # Manga list should be sortable by latest release, rating, genres, etc.
        pass

    def save(self):
        with open(f'./mangalists/{self.name}.json', mode='w', encoding='utf-8') as output_file:
            json.dump({'Name': self.name,
                       'Mangas': str(self.mangas),  # TODO: fix this to be a list of urls in the json file
                       'Update Time (h)': self.update_time},
                      output_file, ensure_ascii=False, indent=4)

    def __str__(self):
        return f'{self.name}\n' + '\n'.join(str(manga) for manga in self.mangas)
