import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# изучение структуры данных
filename = 'readable_eq_data.geojson'
with open(filename) as f:
    all_eq_data = json.load(f)  # читает файл json с землетрясениями как словарь

all_eq_dicts = all_eq_data['features']  # собирает данные землетрясений словарями и заносит в список

mags, lons, lats, hover_texts = [], [], [], []  # магнитуды, долготы, широты и подсказки
for eq_dict in all_eq_dicts:  # перебор по словарям eq_dict в списке all_eq_dicts
    mag = eq_dict['properties']['mag']  # секция properties словаря с ключом mag
    lon = eq_dict['geometry']['coordinates'][
        0]  # eq_dict['geometry'] обращается к словарю элемента geometry, coordinates извлекает значения по своему ключу
    lat = eq_dict['geometry']['coordinates'][1]
    title = eq_dict['properties']['title']
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    hover_texts.append(title)

# нанесение данных на карту
data = [{  # запись данных для диаграммы; scattergeo - тип диаграммы для вывода данных
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'text': hover_texts,  # описание магнитуды и местоположения при наведении на маркер
    'marker': {
        'size': [5 * mag for mag in mags],  # размер метки земл-ия в зависимости от магнитуды
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,  # темно-синий цвет для самых разрушительных земл-ий
        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title='Global Earthquakes')

fig = {'data': data, 'layout': my_layout}  # содержит данные для диаграммы и макет
offline.plot(fig, filename='global_earthquakes.html')  # offline для вывода карты мира

print(lats[:6])
print(lons[:6])
