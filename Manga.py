from datetime import datetime


class Manga:

    def __init__(self,
                 name: str,
                 url: str,
                 provider: str = None,
                 latest_chapter: int = None,
                 latest_update: datetime = None,
                 latest_check: datetime = None):
        self.name = name
        self.url = url
        self.provider = provider
        self.latest_chapter = latest_chapter
        self.latest_update = latest_update
        self.latest_check = latest_check
        self.need_check = True  # On creation a check for update is needed, then after every X amount of time interval.

    def __str__(self):
        return f"Name: {self.name} ({self.url}), latest chapter: {self.latest_chapter} on {self.latest_update}"