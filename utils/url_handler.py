def clean_up_mangakakalot(manga_url):
    if 'chapter' in manga_url:
        provider, _, ending = manga_url.partition('/chapter/')
        return provider + '/manga/' + ending.split('/')[0] + '\n'
    else:
        return manga_url


def clean_up_manganelo(manga_url):
    if 'chapter' in manga_url:
        return manga_url
    else:
        return manga_url


def clean_up_manganato(manga_url):
    if 'chapter' in manga_url:
        return manga_url
    else:
        return manga_url


def clean_up_manga_list_file(manga_list_file):
    # clean up each line in the mangalists file
    with open(f'./mangalists/{manga_list_file}.txt', 'r+') as ml_file:
        for manga_url in ml_file.readlines():
            if 'mangakakalot' in manga_url:
                manga_url = clean_up_mangakakalot(manga_url)
            elif 'manganelo' in manga_url:
                manga_url = clean_up_manganelo(manga_url)
            elif 'readmanganato' in manga_url:
                manga_url = clean_up_manganato(manga_url)
            else:
                raise ValueError(f'Provider not supported {manga_url}.')


if __name__ == '__main__':
    print('Nothing to do..')
