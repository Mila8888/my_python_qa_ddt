import pytest
import requests


def test_check_ya(base_url, status_code):
    """Проверка статус кода - запрос выполнен успешно"""
    response = requests.get(url=base_url)
    assert response.status_code == status_code


@pytest.mark.parametrize("id", ["qwewtegfufngig", 23])
def test_negative_yandex(base_url, id, error_status_code):
    """Проверка статус кода - Ошибка 404 или Not Found"""
    url = f"{base_url}/{id}"
    response = requests.get(url=url)
    assert response.status_code == error_status_code
