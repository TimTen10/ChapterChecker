import json
import time

from datetime import datetime

from manga import Manga
from utils.manga_parser import parse_manga


class MangaList:

    def __init__(self,
                 name: str,
                 *params,
                 **kwargs):
        # creates a new empty manga list
        self.name = name
        self.mangas = []
        self.update_time = kwargs.get('update_time', 24)
        self.last_update = kwargs.get('last_update', datetime.now())

        if len(params) == 1:
            self.add_manga_list(*params)
        elif len(params) > 1:
            raise ValueError('Got too many attributes for creating a new MangaList object.')

    def add_manga_single(self, url):
        # Takes in an URL and adds the corresponding manga to the manga list object.
        self.mangas.append(Manga(*parse_manga(url)))

    def add_manga_list(self, url_list):
        for manga_url in url_list:
            self.add_manga_single(manga_url.strip())
            time.sleep(0.1)

    def update_manga_list(self):
        # This should update every manga where the latest update > update interval
        # Might call update_manga_single inside
        for manga in self.mangas:
            # if there is going to be an update_manga_single method in the future - replace from here:
            if manga.update(self.update_time):
                print(f'Chapter {manga.latest_chapter} for {manga.name} got released!'
                      f' -> {manga.latest_chapter_url}')

    def sort_by(self):
        # Manga list should be sortable by latest release, rating, genres, etc.
        pass

    def save(self):
        with open(f'./mangalists/{self.name}.json', mode='w', encoding='utf-8') as output_file:
            json.dump({'name': self.name,
                       'mangas': [manga.as_dict() for manga in self.mangas],
                       'update_time': self.update_time,
                       'last_update': self.last_update.strftime("%Y-%m-%d %H:%M:%S")},
                      output_file, ensure_ascii=False, indent=4)

    def __str__(self):
        return f'{self.name}\n' + '\n'.join(str(manga) for manga in self.mangas)


def load_manga_list(manga_list_name) -> MangaList:
    with open(f'./mangalists/{manga_list_name}.json', mode='r', encoding='utf-8') as input_file:
        manga_list_dict = json.load(input_file)
        loaded_manga_list = MangaList(name=manga_list_dict['name'],
                                      update_time=manga_list_dict['update_time'],
                                      last_update=datetime.strptime(manga_list_dict['last_update'],
                                                                    "%Y-%m-%d %H:%M:%S"))
        loaded_manga_list.mangas = [Manga(latest_update=datetime.strptime(kwargs.pop('latest_update'),
                                                                          "%Y-%m-%d %H:%M:%S"),
                                          latest_check=datetime.strptime(kwargs.pop('latest_check'),
                                                                         "%Y-%m-%d %H:%M:%S"),
                                          **kwargs) for kwargs in manga_list_dict['mangas']]
        return loaded_manga_list
