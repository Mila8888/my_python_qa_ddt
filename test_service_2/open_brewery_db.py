import pytest
import requests
from jsonschema import validate

base_url = 'https://api.openbrewerydb.org/breweries'

schema = {
    'type': ['array', 'object'],
    'properties': {
        'id': {'type': 'string'},
        'name': {'type': 'string'},
        'brewery_type': {'type': 'string'},
        'street': {'type': 'string'},
        'address_2': {'type': ['string', 'null']},
        'address_3': {'type': ['string', 'null']},
        'city': {'type': 'string'},
        'state': {'type': 'string'},
        'county_province': {'type': ['string', 'null']},
        'postal_code': {'type': 'string'},
        'country': {'type': 'string'},
        'longitude': {'type': 'string'},
        'latitude': {'type': 'string'},
        'phone': {'type': 'string'},
        'website_url': {'type': 'string'},
        'updated_at': {'type': 'string'},
        'created_at': {'type': 'string'},
    },
}


def status_code_200(response):
    return response.status_code == 200


def test_schema_brewereis():
    """ Проверка статус кода = 200 и что это объект, который пришел в JSON """
    response = requests.get(f"{base_url}")
    assert status_code_200(response)
    validate(instance=response.json(), schema=schema)


def test_id_breweries():
    """ Проверка статус кода = 200 и что это объект, который пришел в JSON  """
    response = requests.get(f"{base_url}/madtree-brewing-cincinnati")
    assert status_code_200(response)
    validate(instance=response.json(), schema=schema)


@pytest.mark.parametrize('number', [1, 2, 25, 50])
def test_brewery_per_page(number):
    """  """
    response = requests.get(f"{base_url}?per_page={number}/search?query=dog")
    assert status_code_200(response)
    assert len(response.json()) == number


@pytest.mark.parametrize('name', ('Brewing', 'Tapped', 'Company'))
def test_filter_by_name(name):
    response = requests.get(f'{base_url}?by_name={name}')
    assert status_code_200(response)
    assert all((name.lower() in brewery['name'].lower() for brewery in response.json()))
