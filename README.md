# Новое русское вино

Сайт магазина авторского вина "Новое русское вино".

## Как установить

Python3 должен быть уже установлен. 
Разверните новое виртуальное окружение проекта, чтобы избежать проблем с ненужными зависимостями.
Затем используйте pip для установки зависимостей:

    pip install -r requirements.txt

## Переменные в окружении
Программа считывает данные для магазина из Эксель файла с каталогом вин. Со следующими колонками: "Категория",	"Название",	"Сорт",	"Цена",	"Картинка",	"Акция". Именно на основе этого каталога и будет построен ассортимент товаров магазина.
При запуске программы вы можете добавитить --product_path Название файла.xlsx и/или просто поставить файл по-умалчанию.

## Запуск

- Запустите сайт командой
    python main.py
- Или командой, если хотите указать другой файл для считывания продуктовой линейки
    python main.py --product_path Название файла.xlsx

## Что должно получиться

Просто пройдите по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000), там должен быть развернут сайт магазина с вином.
Пройдите по страничке и ознакомьтесь с ассортиментом

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
