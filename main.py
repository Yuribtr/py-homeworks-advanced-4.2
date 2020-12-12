import requests


def create_folder(folder_name: str):
    with open('token.txt', 'r', encoding='utf8') as file:
        token = file.readline()
        headers = {'User-Agent': 'Netology', 'Authorization': 'OAuth ' + token}
        params = {'path': '/' + folder_name}
        response = requests.put('https://cloud-api.yandex.net:443/v1/disk/resources', params=params, headers=headers)
    return response


def check_folder_exist(folder_name: str):
    with open('token.txt', 'r', encoding='utf8') as file:
        token = file.readline()
        headers = {'User-Agent': 'Netology', 'Authorization': 'OAuth ' + token}
        params = {'path': '/' + folder_name}
        response = requests.get('https://cloud-api.yandex.net:443/v1/disk/resources', params=params, headers=headers)
    return response


print(create_folder('Test').status_code)
print(check_folder_exist('Test').status_code)
