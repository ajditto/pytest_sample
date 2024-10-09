import pytest
import requests
from requests import Response

# This sets our base URL for all tests.
# Adding it as a fixture allows for easy
# global use
@pytest.fixture
def api():
    return "http://api.zippopotam"

# This is our un-authenticated user session data.
# Adding it as a fixture allows for easy
# global use. 
# "Scope" indicates that any data in this
# fixture is maintained for the indicated segment
# in this case the whole test session
@pytest.fixture(scope='session')
def zipper():
    zipper = requests.Session()
    return zipper