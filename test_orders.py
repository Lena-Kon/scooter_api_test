import sender_stand_request
import data


# Тест 1. Проверка создания нового заказа и получения его по треку
def test_create_and_get_order():
    # Создаем новый заказ через API
    response_new_order = sender_stand_request.post_new_order(data.order_body)
    # Из JSON ответа получаем номер трека
    track = response_new_order.json()["track"]
    # По номеру трека получаем из API заказ
    response_order = sender_stand_request.get_order_by_track(track)
    # Проверяем, что статус ответа == 200
    assert response_order.status_code == 200