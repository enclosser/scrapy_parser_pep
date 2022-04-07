# Scrappy_parser_pep

Парсер страницы https://peps.python.org/  который собирает в файл список PEP, 
и в отдельный файл расчитывает и сохраняет количество PEP находящихся в каждом
статусе

## Подготовка и запуск проекта

Склонировать репозиторий на локальную машину:
```
git clone https://github.com/Andrey-oss-ai/scrapy_parser_pep.git
```
Установить и активировать виртуальное окружение
```
python -m venv env
source env/bin/activate         # для MacOS
source env/scripts/activate     # для Windows
```
Установить требуемые зависимости
```
pip install -r requirements.txt
```
Далее запуск скрипта командой
```
scrapy crawl pep
```
## Результат работы скрипта

В ходе работы скрипта в папке results будет создано 2 файла

- pep - куда будет собраны все PEP в виде csv файла в формате <номер,имя,статус>

- status summary - куда будет сгенерирована таблица с количеством PEP находящимся
в каждом статусе

## Технологии
В ходе разработки использованы

- Scrappy
## Автор

andreu-antonov@yandex.ru
