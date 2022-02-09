import fileinput


def clean_up_mangakakalot(manga_url):
    if 'chapter' in manga_url:
        provider, _, ending = manga_url.partition('/chapter/')
        return provider + '/manga/' + ending.split('/')[0] + '\n'
    else:
        return manga_url


def clean_up_manganelo(manga_url):
    if 'chapter' in manga_url:
        provider, _, ending = manga_url.partition('/chapter/')
        return provider + '/manga/' + ending.split('/')[0] + '\n'
    else:
        return manga_url


def clean_up_manganato(manga_url):
    if 'chapter' in manga_url:
        return manga_url.split('/chapter-')[0] + '\n'
    else:
        return manga_url


def clean_up_manga_list_file(manga_list_file):
    # clean up each line in the mangalists file
    cleaned_manga_urls = []
    with open(f'./mangalists/{manga_list_file}.txt', mode='r') as manga_in:
        for manga_url in manga_in:
            if 'mangakakalot' in manga_url:
                cleaned_manga_urls.append(clean_up_mangakakalot(manga_url))
            elif 'manganelo' in manga_url:
                cleaned_manga_urls.append(clean_up_manganelo(manga_url))
            elif 'readmanganato' in manga_url:
                cleaned_manga_urls.append(clean_up_manganato(manga_url))
            else:
                raise ValueError(f'Provider not supported {manga_url}.')

    with open(f'./mangalists/{manga_list_file}_clean.txt', mode='w') as manga_out:
        manga_out.writelines(cleaned_manga_urls)


if __name__ == '__main__':
    print('Nothing to do..')
