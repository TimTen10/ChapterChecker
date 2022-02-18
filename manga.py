from datetime import datetime
from typing import List, Dict

from utils.manga_parser import parse_manga_update


class Manga:

    def __init__(self,
                 url: str,
                 name: str,
                 authors: List[str],
                 genres: List[str],
                 latest_chapter: float,
                 latest_chapter_url: str,
                 latest_update: datetime,
                 latest_check: datetime):
        self.url = url
        self.name = name
        self.authors = authors
        self.genres = genres
        self.latest_chapter = latest_chapter
        self.latest_chapter_url = latest_chapter_url
        self.latest_update = latest_update
        self.latest_check = latest_check

        self.rating = -1

    def set_rating(self, value):
        self.rating = value

    def update(self, update_time) -> bool:
        # Checks for updates (new chapters) of the manga
        # And updates the respective attribute(s) -> latest_chapter(_url), latest_update, latest_check
        if (datetime.now() - self.latest_check).seconds // 3600 > update_time:
            new_chapter, new_chapter_url, new_update_time, new_check_time = parse_manga_update(self.url)
            if new_chapter > self.latest_chapter:
                self.latest_chapter = new_chapter
                self.latest_chapter_url = new_chapter_url
                self.latest_update = new_update_time
                self.latest_check = new_check_time
                return True
        return False

    def as_dict(self) -> Dict:
        return {'url': self.url,
                'name': self.name,
                'authors': self.authors,
                'genres': self.genres,
                'latest_chapter': self.latest_chapter,
                'latest_chapter_url': self.latest_chapter_url,
                'latest_update': self.latest_update.strftime("%Y-%m-%d %H:%M:%S"),
                'latest_check': self.latest_check.strftime("%Y-%m-%d %H:%M:%S")}

    def __str__(self):
        return f"Name: {self.name} ({self.url}), latest chapter: {self.latest_chapter} updated {self.latest_update}."