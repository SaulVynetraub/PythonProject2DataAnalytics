import json

# изучение структуры данных
filename = 'readable_eq_data.geojson'
with open(filename) as f:
    all_eq_data = json.load(f)  # читает файл json с землетрясениями как словарь

all_eq_dicts = all_eq_data['features']  # собирает данные землетрясений словарями и заносит в список

mags, lons, lats = [], [], []  # магнитуды, долготы, широты
for eq_dict in all_eq_dicts:  # перебор по словарям eq_dict в списке all_eq_dicts
    mag = eq_dict['properties']['mag']  # секция properties словаря с ключом mag
    lon = eq_dict['geometry']['coordinates'][
        0]  # eq_dict['geometry'] обращается к словарю элемента geometry, coordinates извлекает значения по своему ключу
    lat = eq_dict['geometry']['coordinates'][0]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
