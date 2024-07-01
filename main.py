"""Module providing a function counting age."""
import os
import datetime
from datetime import date
import collections
from http.server import HTTPServer, SimpleHTTPRequestHandler
import argparse
import pandas
from incline_numerals import incline
from jinja2 import Environment, FileSystemLoader, select_autoescape


def get_path():
    parser = argparse.ArgumentParser(
        description='Программа позволяет разворачивать сайт по продаже винного магазина, с перечнем товаров из Эксель файла'
        )
    parser.add_argument(
        '--product_path',
        help='Введите --product_path путь к файлу',
        type=str,
        default='wine3.xlsx'
        )
    product_range = parser.parse_args()
    products = product_range.product_path
    return products


def get_products(file_path):
    df_wines = load_wines(file_path)
    wines = collections.defaultdict(list)
    for wine in df_wines:
        wines[wine["Категория"]].append(wine)
    return wines


def load_wines(products):
    """Take a DF from Excel"""
    df = pandas.read_excel(
        products,
        na_values=['N/A', 'NA'],
        keep_default_na=False).to_dict(orient='records')
    return df


def count_age():
    opend_time = datetime.datetime(year=1920, month=12, day=24, hour=11)
    today = date.today()
    age = (today.year - opend_time.year
        - ((today.month, today.day) < (opend_time.month, opend_time.day))
        )   
    return age


if __name__ == "__main__":
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = env.get_template('template.html')
    file_path = get_path()
    wines = get_products(file_path)
    age = count_age()
    inclined = incline(age)
    rendered_page = template.render(
        top_heading="Проверенно временем",
        bottom_header=f"Уже {age} {inclined} с Вами",
        wines=wines
        )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
