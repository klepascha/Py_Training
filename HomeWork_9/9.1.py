# Реализовать две функции: write_to_file(data) и read_file_data().
# Которые соответственно: пишут данные в файл и читают данные из файла.

# Реализовать следующую логику: получать при помощи requests данные сервиса https://jsonplaceholder.typicode.com/
# (сущность можно выбрать любую, например https://jsonplaceholder.typicode.com/comments),
# выводить в консоль все пары заголовки, сохранять полученный json в файл на диск

# Обратиться с странице https://habrahabr.ru/. Получить текст страницы.
# При помощи регулярных выражений нужно получить все ссылки со страницы на другие.

import requests
import json
import re


def write_to_file(file_name, data, mode='w'):
    with open(file_name, mode) as file:
        file.writelines(data)


def read_file_data(file_name):
    with open(file_name) as file:
        return file.read()


def get_headers(url):
    r = requests.get(url)
    headers = dict(r.headers)
    for key, value in headers.items():
        print(key, value)

    write_to_file('site_response.json', json.dumps(headers, sort_keys=True, indent=4))


def habrahabr_re():
    habrahabr_response = requests.get('https://habrahabr.ru/')
    link_pattern = r'<a[^><]*href=[\'"]([^><\'"]*)[\'"][^><]*>'
    print('Links from {} saved in file \'site_links.txt\''.format('https://habrahabr.ru/'))
    write_to_file('site_links.txt', '')
    for link_string in re.findall(link_pattern, habrahabr_response.text):
        write_to_file('site_links.txt', link_string + '\n', mode='a')
        print(link_string)


def main():
    write_to_file('test_write.txt', ['Hello\n', 'We are test file'])
    print(read_file_data('test_write.txt'))
    get_headers('https://jsonplaceholder.typicode.com/comments')
    habrahabr_re()


if __name__ == '__main__':
    main()
