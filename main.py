import argparse

from manga_list import MangaList, load_manga_list

from utils.manga_parser import parse_manga_update
from utils.url_handler import clean_up_manga_list_file



def handle_parser(**kwargs):
    # TODO: do not allow multiple arguments at once
    # create > add > check
    if kwargs['create_empty']:
        manga_list = MangaList(kwargs['create_empty'])
        manga_list.save()

    if kwargs['create_from']:
        manga_list = MangaList(kwargs['create_from'][0],
                               clean_up_manga_list_file(kwargs['create_from'][1]))
        manga_list.save()

    if kwargs['add_manga']:
        manga_list = load_manga_list(kwargs['add_manga'][0])
        manga_list.add_manga_single(kwargs['add_manga'][1])
        manga_list.save()

    if kwargs['add_manga_list']:
        manga_list = load_manga_list(kwargs['add_manga_list'][0])
        manga_list.add_manga_list(kwargs['add_manga_list'][1])
        manga_list.save()

    if kwargs['check_single']:
        # Checks the manga (by url) for updates in the last "time" hours
        chapter, url, latest_update, _ = parse_manga_update(kwargs['check_single'])
        print(f'Chapter {chapter} got released! -> {url}'
              f' Date: {latest_update.strftime("%H:%M %d.%m.%Y ")}')

    if kwargs['check_list']:
        # Updates / Checks a whole manga list
        manga_list = load_manga_list(kwargs['check_list'])
        manga_list.update_manga_list()
        manga_list.save()

        # TODO: for testing purposes:
        manga_list_test = load_manga_list(kwargs['check_list'])
        manga_list_test.save()

    if kwargs['load_list']:
        print(load_manga_list(kwargs['load_list']))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()  # TODO: (re-)add description

    # argument for creating an empty manga list
    parser.add_argument('--create_empty', '--create_manga_list_empty', '-ce', help='name of the new manga list')

    # argument for creating a manga list from file
    parser.add_argument('--create_from', '--create_manga_list_from', '-cf', nargs=2,
                        help='name of the new manga list followed by manga urls filename')

    # argument for adding a single manga to a manga list
    parser.add_argument('--add_manga', nargs=2, help='manga list name followed by url of the manga you want to add')

    # argument for adding a list of manga to a manga list
    parser.add_argument('--add_manga_list', nargs=2, help='manga list name followed by manga urls filename')

    # argument for checking single manga for most recent update
    parser.add_argument('--check_single', help='url of manga that you want checked followed by time window to check')

    # argument for checking a manga list for most recent updates
    parser.add_argument('--check_list', help='name of the manga list you want checked')

    # TODO: only for testing purposes
    parser.add_argument('--load_list')

    args = parser.parse_args()

    handle_parser(**vars(args))
