from bs4 import BeautifulSoup
from datetime import datetime
from manga import Manga

import requests


def parse_mangakakalot(url) -> Manga:
    r = requests.get(url)

    if r.status_code == 200:
        manga_html = BeautifulSoup(r.text, "html.parser")

        # Info about the latest chapter (latest_chapter_url, latest_update)
        chapter_list = manga_html.find("div", class_="chapter-list")
        latest_chapter_info = chapter_list.find("div", class_="row")
        chapter_info = latest_chapter_info.find("a")
        latest_chapter_url = chapter_info["href"]
        latest_update = datetime.strptime(latest_chapter_info.contents[-2]["title"], "%b-%d-%Y %H:%M")

        # Info about the manga (name)
        info_text = manga_html.find("ul", class_="manga-info-text")
        name = info_text.find("h1").text

        # Info about the authors (authors)
        first_author = info_text.find("a")
        authors = [first_author.text]
        additional_authors = first_author.find_next_siblings("a")
        if additional_authors:
            for additional_author in additional_authors:
                authors.append(additional_author.text)

        # Info about the genres (genres)
        genres_a_tag_list = info_text.find_all("a")[len(authors):]  # TODO: there has to be a nicer solution
        genres = [tag.text for tag in genres_a_tag_list[:-1]]  # excluding the last one, it is a placeholder a-tag

        return Manga(
            url,
            name,
            authors,
            genres,
            -1,  # TODO: Missing chapter number
            latest_chapter_url,
            latest_update,
            latest_check=datetime.now()
        )


def parse_readmanganato(url) -> Manga:
    r = requests.get(url)

    if r.status_code == 200:
        manga_html = BeautifulSoup(r.text, "html.parser")

        # Info about the latest chapter (latest_chapter_url, latest_update)
        chapter_list = manga_html.find("ul", class_="row-content-chapter")
        latest_chapter_info = chapter_list.find("li", class_="a-h")
        chapter_info = latest_chapter_info.find("a")
        latest_chapter_url = chapter_info["href"]
        latest_update = datetime.strptime(latest_chapter_info.contents[-2]["title"], "%b %d,%Y %H:%M")

        # Info about the manga (name)
        info_text = manga_html.find("div", class_="story-info-right")
        name = info_text.find("h1").text

        # Info about the authors (authors)
        first_author = info_text.tbody.tr.next_sibling.next_sibling.find("a")
        authors = [first_author.text]
        additional_authors = first_author.find_next_siblings("a")
        if additional_authors:
            for additional_author in additional_authors:
                authors.append(additional_author.text)

        # Info about the genres (genres)
        genres_td_tag_list =\
            info_text.tbody.tr.next_sibling.next_sibling.\
            next_sibling.next_sibling.next_sibling.next_sibling.find_all("a")
        genres = [tag.text for tag in genres_td_tag_list]

        return Manga(
            url,
            name,
            authors,
            genres,
            -1,  # TODO: Missing chapter number
            latest_chapter_url,
            latest_update,
            latest_check=datetime.now()
        )


def main():
    pass


if __name__ == '__main__':
    main()
