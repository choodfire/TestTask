# Тестовое задание для работы в GreenAtom

---

### 1. Какие шаги ты бы принял, если бы пользователь сказал, что API возвращает ему ошибку 500?
1. Проверил бы логи сервера, чтоб узнать в каком участке кода произошла ошибка
2. Проверил бы логи нагрузки сервера, чтоб узнать нет ли проблем с нагрузкой/недостатком мощности
3. Попробовал бы отправить запрос на этот эндпоинт, чтоб узнать воспроизводится ли ошибка
4. Посмотрел бы в код, может быть ошибка была допущена там

### 2. Ошибки в коде
Проблема в том, что в execute_handlers все лямбда выражения возвращают 5, для исправления следует добавить промежуточную переменную, которая будет получать значение шага на каждой итерации.
Исправленный код в файле task2.py

### 3. HTML
Код в файле task3.py

### 4. IP address
Код в файле task4.py

### 5. Сравнение версий
Код в файле task5.py