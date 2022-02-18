from bs4 import BeautifulSoup
from datetime import datetime, timedelta

import requests


def parse_manga(url):
    return _parse_mangakakalot(url) if 'mangakakalot' in url else _parse_readmanganato(url)


def _parse_mangakakalot(url):
    r = requests.get(url)

    if r.status_code == 200:
        manga_html = BeautifulSoup(r.text, "html.parser")

        # manga got a new url since last update:
        # TODO: might be able to not call function again and handle in some other way
        if manga_html.body.string:
            _, new_url = manga_html.body.string.strip().split(' : ')
            if 'mangakakalot' in new_url:
                return _parse_mangakakalot(new_url)
            else:
                return _parse_readmanganato(new_url)

        # Info about the latest chapter (latest_chapter, latest_chapter_url, latest_update)
        chapter_list = manga_html.find("div", class_="chapter-list")
        latest_chapter_info = chapter_list.find("div", class_="row")
        chapter_info = latest_chapter_info.find("a")
        latest_chapter_url = chapter_info["href"]
        _, latest_chapter = latest_chapter_url.split('chapter_')
        try:
            latest_update = datetime.strptime(latest_chapter_info.contents[-2]["title"], "%b-%d-%Y %H:%M")
        except ValueError:
            latest_update = (datetime.now() - timedelta(days=1)).strftime("%b-%d-%Y %H:%M")

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

        return url, name, authors, genres, latest_chapter, latest_chapter_url, latest_update, datetime.now()


def _parse_readmanganato(url):
    r = requests.get(url)

    if r.status_code == 200:
        manga_html = BeautifulSoup(r.text, "html.parser")

        # Info about the latest chapter (latest_chapter, latest_chapter_url, latest_update)
        chapter_list = manga_html.find("ul", class_="row-content-chapter")
        latest_chapter_info = chapter_list.find("li", class_="a-h")
        chapter_info = latest_chapter_info.find("a")
        latest_chapter_url = chapter_info["href"]
        _, latest_chapter = latest_chapter_url.split('chapter-')
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

        return url, name, authors, genres, latest_chapter, latest_chapter_url, latest_update, datetime.now()


def parse_manga_update(url) -> (int, str, datetime, datetime):
    return _parse_mangakakalot_update(url) if 'mangakakalot' in url else _parse_readmanganato_update(url)


def _parse_mangakakalot_update(url) -> (int, str, datetime, datetime):
    r = requests.get(url)

    if r.status_code == 200:
        manga_html = BeautifulSoup(r.text, "html.parser")

        # manga got a new url since last update:
        # TODO: might be able to not call function again and handle in some other way
        if manga_html.body.string:
            _, new_url = manga_html.body.string.strip().split(' : ')
            if 'mangakakalot' in new_url:
                return _parse_mangakakalot(new_url)
            else:
                return _parse_readmanganato(new_url)

        # Info about the latest chapter (latest_chapter, latest_chapter_url, latest_update)
        chapter_list = manga_html.find("div", class_="chapter-list")
        latest_chapter_info = chapter_list.find("div", class_="row")
        chapter_info = latest_chapter_info.find("a")
        latest_chapter_url = chapter_info["href"]
        _, latest_chapter = latest_chapter_url.split('chapter_')
        try:
            latest_update = datetime.strptime(latest_chapter_info.contents[-2]["title"], "%b-%d-%Y %H:%M")
        except ValueError:
            latest_update = (datetime.now() - timedelta(days=1)).strftime("%b-%d-%Y %H:%M")

        return latest_chapter, latest_chapter_url, latest_update, datetime.now()


def _parse_readmanganato_update(url) -> (int, str, datetime, datetime):
    r = requests.get(url)

    if r.status_code == 200:
        manga_html = BeautifulSoup(r.text, "html.parser")

        # Info about the latest chapter (latest_chapter, latest_chapter_url, latest_update)
        chapter_list = manga_html.find("ul", class_="row-content-chapter")
        latest_chapter_info = chapter_list.find("li", class_="a-h")
        chapter_info = latest_chapter_info.find("a")
        latest_chapter_url = chapter_info["href"]
        _, latest_chapter = latest_chapter_url.split('chapter-')
        latest_update = datetime.strptime(latest_chapter_info.contents[-2]["title"], "%b %d,%Y %H:%M")

        return latest_chapter, latest_chapter_url, latest_update, datetime.now()


def main():
    pass


if __name__ == '__main__':
    main()
