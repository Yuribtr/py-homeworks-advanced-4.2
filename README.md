# Домашнее задание к лекции 4.«Tests»


## Solution
- made pytest for create folder and check folder functions
- before usage pls save your YandexDisk token (https://yandex.ru/dev/disk/poligon/) in file token.txt

### Задача №2 Автотест API Яндекса
Проверим правильность работы Яндекс.Диск REST API. Написать тесты, проверяющий создание папки на Диске.  
Используя библиотеку requests напишите unit-test на верный ответ и возможные отрицательные тесты на ответы с ошибкой

Пример положительных тестов:
* Код ответа соответствует 200.
* Результат создания папки - папка появилась в списке файлов.