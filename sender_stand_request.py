import requests
import configuration
import data


# Создание пользователя и получение токена
def get_auth_token():
    responce = requests.post(configuration.URL + configuration.CREATE_USER_PATH, headers=data.headers, json=data.user_body)
    if responce.status_code == 201:
        return responce.json()['authToken']

# Создание набора (позитиваная проверка)
def create_kit_positive_check(token, status, name):
    current_header = data.headers.copy()
    current_header['Authorization'] = f"Bearer {token}"
    current_name_kit_body = data.name_kit.copy()
    current_name_kit_body['name'] = name

    # Получаем ответ
    responce = requests.post(configuration.URL + configuration.CREATE_KIT_PATH, headers=current_header, json=current_name_kit_body)

    # Производим проверку названия набора
    assert responce.json()['name'] == name
    assert responce.status_code == status


# Создание набора (негативная проверка)
def create_kit_negative_check(token, status, name=None):
    current_header = data.headers.copy()
    current_header['Authorization'] = f"Bearer {token}"
    current_name_kit_body = data.name_kit.copy()

    # Если имя набора не передано, то передаем словарь без параметров
    if name is None:
        current_name_kit_body = {}
    else:
        current_name_kit_body['name'] = name

    # Получаем ответ
    responce = requests.post(configuration.URL + configuration.CREATE_KIT_PATH, headers=current_header, json=current_name_kit_body)
    assert responce.status_code == status




