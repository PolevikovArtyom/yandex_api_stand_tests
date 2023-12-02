import configuration
import requests
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, headers={"Content-Type": "application/json"}, params={"count":20})

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки
#response = post_new_user(data.user_body); - для ПОСТ запроса в респонс вписываем название файла ДАТА
# в метод респонс пишем функцию, по которой хотим сделать запрос
response = post_new_user(data.user_body);

print(response.status_code)
print(response.headers)
print(response.text)