import argparse

from utils.manga_parser import parse_mangakakalot, parse_readmanganato


def main():
    parser = argparse.ArgumentParser(description='What manga or manga list do you want checked?')
    parser.add_argument('manga_url')
    args = parser.parse_args()
    args_dict = vars(args)
    if 'mangakakalot' in args_dict['manga_url']:
        manga = parse_mangakakalot(args_dict['manga_url'])
    else:
        manga = parse_readmanganato(args_dict['manga_url'])
    print(manga)


if __name__ == "__main__":
    main()
