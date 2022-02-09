import argparse

from utils.manga_parser import parse_mangakakalot, parse_readmanganato
from utils.url_handler import clean_up_manga_list_file


def main():
    parser = argparse.ArgumentParser(description='What manga or manga list do you want checked?')
    parser.add_argument('--url', '-u')
    parser.add_argument('--manga_list', '-ml')
    args = parser.parse_args()
    if args.manga_list:
        clean_up_manga_list_file(args.manga_list)
    elif args.url and 'mangakakalot' in args.url:
        manga = parse_mangakakalot(args.url)
        print(manga)
    elif args.url:
        manga = parse_readmanganato(args.url)
        print(manga)


if __name__ == "__main__":
    main()
