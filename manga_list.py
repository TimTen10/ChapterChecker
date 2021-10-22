from manga import Manga
from utils import manga_parser


class MangaList:

    def __init__(self, source, update_interval):
        # creates a new manga list from a source file
        # TODO: we need two constructor methods -> from file and empty list
        self.source = source
        self.update_interval = update_interval

    def set_update_interval(self, new_update_interval):
        self.update_interval = new_update_interval

    def add_manga_single(self, url):
        # Takes in an URL and adds the corresponding manga to the manga list object.
        pass

    def add_manga_list(self, url_list):
        pass

    def update_manga_single(self):
        pass

    def update_manga_list(self):
        # This should update every manga where the latest update > update interval
        # Might call update_manga_single inside
        pass

    def sort_by(self):
        # Manga list should be sortable by latest release, rating, genres, etc.
        pass
