# Коновалова Елена, 12-я когорта — Финальный проект. Инженер по тестированию плюс
import requests
import configuration
import data

# Функция создания нового заказа
def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_NEW_ORDER,
                         json=body,
                         headers=data.headers)


# Функция получения заказа по номеру трека
def get_order_by_track(track_number):
    # Добаляем в URL GET параметр track
    url = configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK + "?t="+str(track_number)
    return requests.get(url)