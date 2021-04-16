import sys
import os

print('path: {}'.format(sys.path))
CURR_DIR = os.path.dirname(os.path.realpath(__file__))
print('curdir: {}'.format(CURR_DIR))

import pytest

import requests

from shortener_app.utils import *

@pytest.fixture
def flask_url():
    return 'http://127.0.0.1:5000/'


def test_default_url(flask_url):
    response = requests.get(flask_url)
    assert response.status_code == 200
    assert response.text == 'Good'


def test_version_url(flask_url):
    ver_url = flask_url + 'version'
    response = requests.get(ver_url)
    assert response.status_code == 200
    assert response.text == '0.0.1'


def test_encode_url(flask_url):
    test_url = flask_url + '/url=http://google.com'
    response = requests.post(test_url)
    expected = flask_url + 'AEY3dXZNHm76Sbzu6oENjw'
    assert expected == response.text

def test_encode_url2(flask_url):
    test_url = flask_url + '/url=http://yahoo.com'
    response = requests.post(test_url)
    expected = flask_url + 'UoMypncGznJxe6tWUvUASE'
    assert expected == response.text


def test_decode_url(flask_url):
    test_url = flask_url + 'AEY3dXZNHm76Sbzu6oENjw'
    response = requests.get(test_url)
    print('{}'.format(response.text))
    assert True == False
