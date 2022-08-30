import pytest
import requests
from jsonschema import validate


def test_list_breeds(base_url):
    """ Проверка статус кода = 200 и что это объект, который пришел в JSON """
    response = requests.get(f"{base_url}/breeds/list/all")
    assert response.status_code == 200

    schema = {
        "type": "object",
        "properties": {
            "message": {"type": "object"},
            "status": {"type": "string"},
        },
        "required": ["message", "status"]
    }
    validate(instance=response.json(), schema=schema)


def test_param_message_string(base_url, get_image):
    """ Проверить параметр message является string """
    url = f"{base_url}/{get_image}"
    dogs_limit = requests.get(url)
    assert dogs_limit.status_code == 200
    assert isinstance(dogs_limit.json().get("message"), str)


@pytest.mark.parametrize("number", [1, 2, 37, 15, 50])
def test_numbers_image(number, base_url, get_image):
    """ Проверить кол-во запрошенных фото соответствует полученным с сервера """
    url = f"{base_url}/{get_image}/{number}"
    res_dogs = requests.get(url)
    assert res_dogs.status_code == 200
    assert len(res_dogs.json().get("message")) == number


def test_list_all_sub_breeds(base_url):
    """ Проверить список всех подпород == 7"""
    response = requests.get(f"{base_url}/breed/hound/list")
    assert response.status_code == 200
    assert len(response.json().get("message")) == 7


@pytest.mark.parametrize('hound, amount',
                         [('afghan', 239),
                          ('basset', 175),
                          ('blood', 187),
                          ('english', 157),
                          ('ibizan', 188),
                          ('plott', 2),
                          ('walker', 153)])
def test_list_all_sub_breeds_images(base_url, hound, amount):
    """ Проверить список(кол-во) всех изображении подпород"""
    response = requests.get(f"{base_url}/breed/hound/{hound}/images")
    assert response.status_code == 200
    assert len(response.json().get("message")) == amount
