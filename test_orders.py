# Коновалова Елена, 12-я когорта — Финальный проект. Инженер по тестированию плюс
import requests
import configuration
import data


# Функция создания нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER, json=body, headers=data.headers)


# Функция получения заказа по номеру трека
def get_order_by_track(track_number):
    # Добаляем в URL GET параметр track
    url = configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK + "?t="+str(track_number)
    return requests.get(url)

# Тест 1. Проверка создания нового заказа и получения его по треку
def test_create_and_get_order():
    # Создаем новый заказ через API
    response_new_order = post_new_order(data.order_body)
    # Из JSON ответа получаем номер трека
    track = response_new_order.json()["track"]
    # По номеру трека получаем из API заказ
    response_order = get_order_by_track(track)
    # Проверяем, что статус ответа == 200
    assert response_order.status_code == 200