from datetime import datetime
from typing import List


class Manga:

    def __init__(self,
                 url: str,
                 name: str,
                 authors: List[str],
                 genres: List[int],
                 latest_chapter: int,
                 latest_chapter_url: str,
                 latest_update: datetime,
                 latest_check: datetime,):
        self.url = url
        self.name = name
        self.authors = authors
        self.genres = genres
        self.latest_chapter = latest_chapter
        self.latest_chapter_url = latest_chapter_url
        self.latest_update = latest_update
        self.latest_check = latest_check

        self.rating = -1
        self.need_check = True  # On creation a check for update is needed, then after every X amount of time interval.

    def set_rating(self, value):
        self.rating = value

    def update(self):
        # Checks for updates (new chapters) of the manga
        # Sends message: "New Chapter(s) Nr. X, Y, Z since last update."
        # And updates the respective attribute(s)
        pass

    def __str__(self):
        return f"Name: {self.name} ({self.url}), latest chapter: {self.latest_chapter} on {self.latest_update}"