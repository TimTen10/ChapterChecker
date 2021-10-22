from bs4 import BeautifulSoup
from datetime import datetime
from manga import Manga

import requests


def parse_mangakakalot(url) -> Manga:
    r = requests.get(url)

    if r.status_code == 200:
        manga_html = BeautifulSoup(r.text, 'html.parser')

        # Info about the latest chapter
        chapter_list = manga_html.find("div", class_="chapter-list")
        latest_chapter = chapter_list.find("div", class_="row")
        chapter = latest_chapter.find("a")

        # Info about the manga
        info_text = manga_html.find("ul", class_="manga-info-text")
        name = info_text.find("h1").text

        # authors
        authors = [info_text.find("a").text]
        additional_authors = info_text.find("a").find_next_siblings("a")
        if additional_authors:
            for additional_author in additional_authors:
                authors.append(additional_author.text)

        # genres
        genres_a_tag_list = info_text.find_all("a")[len(authors):]  # TODO: there has to be a nicer solution
        genres = [tag.text for tag in genres_a_tag_list[:-1]]  # excluding the last one, it is a placeholder a-tag

        return Manga(
            url,
            name,
            authors,
            genres,
            latest_chapter=None,
            latest_chapter_url=None,
            latest_update=None,
            latest_check=datetime.now()
        )


def parse_readmanganato(url) -> Manga:
    r = requests.get(url)


def main():
    test_manga = parse_mangakakalot("")
    print(test_manga.name)
    print(test_manga.genres)
    print(test_manga.url)
    print(test_manga.authors)
    print(test_manga.latest_check)


if __name__ == '__main__':
    main()
