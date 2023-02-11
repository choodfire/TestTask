# Тестовое задание для работы в GreenAtom (Часть 1)

---

### 1. Какие шаги ты бы принял, если бы пользователь сказал, что API возвращает ему ошибку 500?
1. Проверил бы логи сервера, чтоб узнать в каком участке кода произошла ошибка
2. Проверил бы логи нагрузки сервера, чтоб узнать нет ли проблем с нагрузкой/недостатком мощности
3. Попробовал бы отправить запрос на этот эндпоинт, чтоб узнать воспроизводится ли ошибка
4. Посмотрел бы в код, может быть ошибка была допущена там

### 2. Ошибки в коде
Проблема в том, что в execute_handlers все лямбда выражения возвращают 5, для исправления следует добавить промежуточную переменную, которая будет получать значение шага на каждой итерации.

```
from typing import Callable, List


def create_handlers(callback: Callable[[int], None]) -> List[Callable[[], None]]:
    handlers = []
    for step in range(5):
        handlers.append(lambda new_step=step: callback(new_step))
    return handlers


def execute_handlers(handlers: List[Callable[[], None]]):
    for handler in handlers:
        handler()
```

Исправленный код в также в файле [task2.py](task2.py)

### 3. HTML

```
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
    count_html_tags()`
```

Код также находится в файле [task3.py](task3.py)

### 4. IP address

```
import requests  # pip install requests


def get_my_public_ip_address():
    response = requests.get("https://ifconfig.me/")

    return response.text.strip()


if __name__ == "__main__":
    get_my_public_ip_address()
```

Код также находится в файле [task4.py](task4.py)

### 5. Сравнение версий

```
def compare_versions(version_a: str, version_b: str) -> int:
    if version_a == version_b:
        return 0

    version_a_nums = version_a.split('.')
    version_b_nums = version_b.split('.')

    for i in range(min(len(version_a_nums), len(version_b_nums))):
        if version_a_nums[i] > version_b_nums[i]:  # Значит А новее, чем B
            return 1
        elif version_a_nums[i] < version_b_nums[i]:
            return -1

    if len(version_a_nums) > len(version_b_nums):  # Значит version A новее
        return 1
    else:
        return -1
```

Код также находится в файле [task5.py](task5.py)
