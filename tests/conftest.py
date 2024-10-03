import pytest
import requests
from requests import Response

@pytest.fixture(autouse=True)
def api():
    """
    'http://api.zippopotam'
    """
    return "http://api.zippopotam"

@pytest.fixture(scope='session')
def zipper():
    zipper = requests.Session()
    return zipper