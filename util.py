class Manga:

    def __init__(self, name, latest_chapter, latest_update, latest_check, url):
        self.name = name
        self.latest_chapter = latest_chapter
        self.latest_update = latest_update
        self.latest_check = latest_check
        self.url = url

    def __str__(self):
        return f"Name: {self.name} ({self.url}), latest chapter: {self.latest_chapter} on {self.latest_update}"