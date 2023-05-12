from operator import itemgetter
import requests

# вызов API и сохранение ответа
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'  # создание вызова API
r = requests.get(url)
print(f"Status code: {r.status_code}")

# обработка информации о каждой статье
submissions_ids = r.json()  # преобразование текста ответа в список
submissions_dicts = []
for submission_id in submissions_ids[:30]:  # перебор 30 самых популярных статей
    # создание отдельного вызова API для каждой статьи
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"  # новый вызов API для каждого id
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # построение словаря для каждой статьи
    try:
        submissions_dict = {  # для текущей, обрабатываемой в цикле, статьи
            'title': response_dict['title'],
            'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict['descendants'],
        }
        submissions_dicts.append(submissions_dict)
    except KeyError:
        pass

submissions_dicts = sorted(submissions_dicts, key=itemgetter('comments'), reverse=True)
# itemgetter - сортировка списка со словарями по ключу comments (число комментариев);
# обратный порядок - публикация с большим числом комментариев выводится первой

for submissions_dict in submissions_dicts:  # вывод информации для каждой статьи
    print(f"\nTitle: {submissions_dict['title']}")
    print(f"Discussion link: {submissions_dict['hn_link']}")
    print(f"Comments: {submissions_dict['comments']}")
