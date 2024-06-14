import datetime
import collections
import pandas
from incline_numerals import incline
from datetime import date
from pprint import pprint
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)
template = env.get_template('template.html')
opend_time = datetime.datetime(year=1920, month=12, day=24, hour=11)
today = date.today()
age = today.year - opend_time.year - ((today.month, today.day) < (opend_time.month, opend_time.day))
inclined = incline(age)
load_wines = pandas.read_excel('wine3.xlsx', na_values=['N/A', 'NA'], keep_default_na=False).to_dict(orient='records')
wines_many = collections.defaultdict(list)
[wines_many[wine["Категория"]].append(wine) for wine in load_wines]
rendered_page = template.render(
    text1="Проверенно временем",
    text2=f"Уже {age} {inclined} с Вами",
    wines=wines_many
    )

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
