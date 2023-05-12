import requests
from plotly.graph_objs import Bar
from plotly import offline

# создание вызова API и сохранение ответа
url = 'https://api.github.com/search/repositories?q=language=python&sort=stars'  # url-адрес вызова API сохраняется в переменной
headers = {'Accept': 'application/vnd.github.v3+json'}  # определяются заголовки для вызова API
r = requests.get(url, headers=headers)  # вызов API, get получает url и headers, сохранение объекта ответа
print(f"Status code: {r.status_code}")  # вывод результата запроса

# сохранение ответа API в переменной
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']  # извлечение url-адреса проекта
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"  # генерация ссылки на проект
    repo_links.append(repo_link)
    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']  # в цикле извлекаются автор и описание каждого проекта
    description = repo_dict['description']
    label = f"{owner}<br />{description}"  # br - разрыв строки
    labels.append(label)

# построение визуализации
data = [{  # в список заносятся данные из списков repo_names, stars - репозитории (проекты, х) и их звезды (у)
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}  # у столбцов серая граница толщиной 1.5
    },
    'opacity': 0.6,  # прозрачность
}]
my_layout = {  # определение макета диаграммы
    'title': 'Most-starred Python Projects on Github',
    'titlefont': {'size': 28},  # размер шрифта общего заголовка диаграммы
    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},  # размер меток делений
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
