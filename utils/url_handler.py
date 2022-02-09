import fileinput


def clean_up_mangakakalot(manga_url):
    if 'chapter' in manga_url:
        provider, _, ending = manga_url.partition('/chapter/')
        return provider + '/manga/' + ending.split('/')[0]
    else:
        return manga_url.strip()


def clean_up_manganelo(manga_url):
    if 'chapter' in manga_url:
        provider, _, ending = manga_url.partition('/chapter/')
        return provider + '/manga/' + ending.split('/')[0]
    else:
        return manga_url.strip()


def clean_up_manganato(manga_url):
    if 'chapter' in manga_url:
        return manga_url.split('/chapter-')[0]
    else:
        return manga_url.strip()


def clean_up_manga_list_file(manga_list_file):
    # clean up each line in the mangalists file
    with fileinput.input(f'./mangalists/{manga_list_file}.txt', inplace=True) as manga_f:
        for manga_url in manga_f:
            if 'mangakakalot' in manga_url:
                print(clean_up_mangakakalot(manga_url))
            elif 'manganelo' in manga_url:
                print(clean_up_manganelo(manga_url))
            elif 'readmanganato' in manga_url:
                print(clean_up_manganato(manga_url))
            else:
                raise ValueError(f'Provider not supported {manga_url}.')


if __name__ == '__main__':
    print('Nothing to do..')
