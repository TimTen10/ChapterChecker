from datetime import datetime


class Manga:

    def __init__(self,
                 name: str,
                 url: str,
                 latest_chapter: int = None,
                 latest_update: datetime = None,
                 latest_check: datetime = None):
        self.name = name
        self.latest_chapter = latest_chapter
        self.latest_update = latest_update
        self.latest_check = latest_check
        self.url = url
        self.need_update = True  # On creation an update is needed, then after each X amount of time.

    def __str__(self):
        return f"Name: {self.name} ({self.url}), latest chapter: {self.latest_chapter} on {self.latest_update}"