import requests  # pip install requests
from bs4 import BeautifulSoup  # pip install beautifulsoup4


def has_no_attrs(tag):
    return not tag.attrs


def count_html_tags():
    hdr = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get("https://greenatom.ru/", headers=hdr)

    soup = BeautifulSoup(response.text, "html.parser")

    all_tags = len(soup.find_all())
    tags_with_attributes = len(soup.find_all(has_no_attrs))

    print(f'Количество всех тегов - {all_tags}')
    print(f'Количество тегов с аттрибутами - {tags_with_attributes}')


if __name__ == "__main__":
    count_html_tags()
