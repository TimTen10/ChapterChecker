from manga import Manga


class MangaList:

    def __init__(self, source):
        # creates a new manga list from a source file
        # TODO: we need two constructor methods -> from file and empty list
        self.source = source

    def add_manga_single(self, url):
        # Takes in an URL and adds the corresponding manga to the manga list object.
        pass

    def add_manga_list(self, url_list):
        pass

    def sort_by(self):
        # Manga list should be sortable by latest release, rating, genres, etc.
        pass
