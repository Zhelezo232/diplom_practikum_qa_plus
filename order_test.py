import requests_function


def test_track_order():
    track_number = requests_function.post_new_order()
    get_response = requests_function.get_order(track_number.json()["track"])
    assert get_response.status_code == 200


# Билетова Анжела, 9-я когорта – Финальный проект. Инженер по тестированию Плюс