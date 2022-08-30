import pytest


@pytest.fixture()
def base_url():
    return "https://dog.ceo/api"


@pytest.fixture()
def get_image():
    return "breeds/image/random"
