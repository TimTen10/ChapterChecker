from datetime import datetime
from typing import List


class Manga:

    def __init__(self,
                 name: str,
                 url: str,
                 rating: int = None,
                 genres: List[int] = None,
                 provider: str = None,
                 latest_chapter: int = None,
                 latest_update: datetime = None,
                 latest_check: datetime = None):
        self.name = name
        self.url = url
        self.rating = rating
        self.genres = genres
        self.provider = provider
        self.latest_chapter = latest_chapter
        self.latest_update = latest_update
        self.latest_check = latest_check
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