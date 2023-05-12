import requests

# создание вызова API и сохранение ответа
url = 'https://api.github.com/search/repositories?q=language=python&sort=stars'  # url-адрес вызова API сохраняется в переменной
headers = {'Accept': 'application/vnd.github.v3+json'}  # определяются заголовки для вызова API
r = requests.get(url, headers=headers)  # вызов API, get получает url и headers, сохранение объекта ответа
print(f"Status code: {r.status_code}")  # вывод результата запроса

# сохранение ответа API в переменной
response_dict = r.json()  # для преобразования json-объекта ответа в словарь Python
print(f"Total repositories: {response_dict['total_count']}")  # общее кол-во репозиториев Python в Github из ответа

# анализ информации о репозиториях
repo_dicts = response_dict['items']  # сохранение списка со словарями (информация о каждом репозитории)
print(f"Repositories returned: {len(repo_dicts)}")

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:  # перебираются все словари
    print(f"Name: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Description: {repo_dict['description']}")

# анализ первого репозитория
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")  # определяется объем допустимой информации
for key in sorted(repo_dict.keys()):
    print(key)  # ключ - какую информацию можно извлечь из проекта

# обработка результатов
# print(response_dict.keys())

# print("\nSelected information about first repository:")
# print(f"Name: {repo_dict['name']}") # имя проекта
# print(f"Owner: {repo_dict['owner']['login']}") # владелец проекта - по словарю owner определяется ключ login
# print(f"Stars: {repo_dict['stargazers_count']}") # общее кол-во звезд проекта
# print(f"Repository: {repo_dict['html_url']}") # url репозитория на Github
# print(f"Created: {repo_dict['created_at']}") # дата создания
# print(f"Updated: {repo_dict['updated_at']}") # дата обновления
# print(f"Description: {repo_dict['description']}") # описание репозитория
