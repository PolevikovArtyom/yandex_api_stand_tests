import sender_stand_request
import data_for_user_test

# эта функция меняет значения в параметре firstName
def get_user_body(first_name):
    current_body = data_for_user_test.user_body.copy() # копирование словаря с телом запроса из файла data, чтобы не потерять данные в исходном словаре
    current_body["firstName"] = first_name # изменение значения в поле firstName
    return current_body # возвращается новый словарь с нужным значением firstName


# Тест 1. Успешное создание пользователя
# Параметр fisrtName состоит из 2 символов

def test_create_user_2_letter_in_first_name_get_success_response():
    user_body = get_user_body("Аа") # В переменную user_body сохраняется обновленное тело запроса с именем “Аа”
    user_response = sender_stand_request.post_new_user(user_body) # В переменную user_response сохраняется результат запроса на создание пользователя
    assert user_response.status_code == 201# Проверяется, что код ответа равен 201
    assert user_response.json()["authToken"] != "" # Проверяется, что в ответе есть поле authToken, и оно не пустое
    users_table_response = sender_stand_request.get_users_table() # В переменную users_table_response сохраняется результат запрос на получение данных из таблицы user_model
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"]# Строка, которая должна быть в ответе запроса на получение данных из таблицы users


# Функция для позитивной проверки
def positive_assert(first_name):
    user_body = get_user_body(first_name) # В переменную user_body сохраняется обновленное тело запроса
    user_response = sender_stand_request.post_new_user(user_body) # В переменную user_response сохраняется результат запроса на создание пользователя:
    assert user_response.status_code == 201  # Проверяется, что код ответа равен 201
    assert user_response.json()["authToken"] != "" # Проверяется, что в ответе есть поле authToken, и оно не пустое
    users_table_response = sender_stand_request.get_users_table() # В переменную users_table_response сохраняется результат запроса на получение данных из таблицы user_model
    str_user = user_body["firstName"] + "," + user_body["phone"] + "," \
               + user_body["address"] + ",,," + user_response.json()["authToken"] # Строка, которая должна быть в ответе
    assert users_table_response.text.count(str_user) == 1 # Проверка, что такой пользователь есть, и он единственный

# Тест 1. Успешное создание пользователя
# Параметр fisrtName состоит из 2 символов
def test_create_user_2_letter_in_first_name_get_success_response():
    positive_assert("Aa")